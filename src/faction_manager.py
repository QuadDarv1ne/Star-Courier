# -*- coding: utf-8 -*-
"""
Star Courier - Faction Reputation Manager
Менеджер репутации фракций для интеграции с GameState
"""

from typing import Dict, Any, Optional, Tuple, List
from dataclasses import dataclass, field

try:
    from .factions_v5 import (
        FACTIONS, REPUTATION_ACTIONS, FACTION_RELATIONS,
        get_faction, get_reputation_tier, get_faction_bonuses,
        get_faction_penalties, can_access_faction_content,
        get_all_faction_standings, get_faction_quest_givers
    )
except ImportError:
    from factions_v5 import (
        FACTIONS, REPUTATION_ACTIONS, FACTION_RELATIONS,
        get_faction, get_reputation_tier, get_faction_bonuses,
        get_faction_penalties, can_access_faction_content,
        get_all_faction_standings, get_faction_quest_givers
    )


@dataclass
class FactionState:
    """Состояние репутации фракции"""
    reputation: int = 0
    tier: str = "neutral"
    unlocked_bonuses: List[str] = field(default_factory=list)
    active_penalties: List[str] = field(default_factory=list)


class FactionManager:
    """Менеджер репутации фракций"""

    def __init__(self):
        self.factions: Dict[str, FactionState] = {
            faction_id: FactionState()
            for faction_id in FACTIONS.keys()
        }
        self.hunted_by: List[str] = []  # Фракции, охотящиеся на игрока
        self.unlocked_factions: List[str] = []  # Открытые фракции

    def get_reputation(self, faction_id: str) -> int:
        """Получить текущую репутацию с фракцией"""
        if faction_id not in self.factions:
            return 0
        return self.factions[faction_id].reputation

    def set_reputation(self, faction_id: str, value: int) -> bool:
        """Установить репутацию фракции"""
        if faction_id not in self.factions:
            return False

        faction = get_faction(faction_id)
        if not faction:
            return False

        min_rep, max_rep = faction["reputation_range"]
        new_value = max(min_rep, min(max_rep, value))

        old_state = self.factions[faction_id]
        old_tier = old_state.tier

        old_state.reputation = new_value

        # Обновить уровень репутации
        tier_data = get_reputation_tier(faction_id, new_value)
        old_state.tier = tier_data["tier_id"]

        # Обновить бонусы и штрафы
        old_state.unlocked_bonuses = list(get_faction_bonuses(faction_id, new_value).keys())
        old_state.active_penalties = list(get_faction_penalties(faction_id, new_value).keys())

        # Проверка на охоту
        if old_state.tier == "hostile" and faction_id not in self.hunted_by:
            self.hunted_by.append(faction_id)
        elif old_state.tier != "hostile" and faction_id in self.hunted_by:
            self.hunted_by.remove(faction_id)

        # Проверка отношений с другими фракциями
        self._update_faction_relations(faction_id, new_value - old_state.reputation)

        return True

    def change_reputation(self, faction_id: str, change: int, reason: str = "") -> Tuple[bool, int]:
        """
        Изменить репутацию фракции.
        Возвращает (успех, новое значение)
        """
        if faction_id not in self.factions:
            return False, 0

        old_value = self.factions[faction_id].reputation
        if self.set_reputation(faction_id, old_value + change):
            new_value = self.factions[faction_id].reputation
            return True, new_value
        return False, old_value

    def apply_reputation_action(self, action_id: str) -> Tuple[bool, Dict[str, int]]:
        """
        Применить действие, влияющее на репутацию.
        Возвращает (успех, изменения репутации по фракциям)
        """
        if action_id not in REPUTATION_ACTIONS:
            return False, {}

        action = REPUTATION_ACTIONS[action_id]
        faction_id = action["faction"]
        change = action["value"]

        changes = {}

        success, new_value = self.change_reputation(faction_id, change)
        if success:
            changes[faction_id] = new_value

            # Применить эффекты к связанным фракциям
            for relation_id, relation_data in FACTION_RELATIONS.items():
                if faction_id in relation_data["factions"]:
                    other_faction = [f for f in relation_data["factions"] if f != faction_id][0]

                    if relation_data["relation"] == "hostile" and change > 0:
                        other_change = -change // 2
                        _, other_new = self.change_reputation(other_faction, other_change)
                        changes[other_faction] = other_new
                    elif relation_data["relation"] == "allied" and change > 0:
                        other_change = change // 3
                        _, other_new = self.change_reputation(other_faction, other_change)
                        changes[other_faction] = other_new

        return success, changes

    def get_tier(self, faction_id: str) -> Optional[Dict[str, Any]]:
        """Получить текущий уровень репутации"""
        if faction_id not in self.factions:
            return None

        reputation = self.factions[faction_id].reputation
        return get_reputation_tier(faction_id, reputation)

    def get_bonuses(self, faction_id: str) -> Dict[str, Any]:
        """Получить активные бонусы фракции"""
        if faction_id not in self.factions:
            return {}

        reputation = self.factions[faction_id].reputation
        return get_faction_bonuses(faction_id, reputation)

    def get_penalties(self, faction_id: str) -> Dict[str, Any]:
        """Получить активные штрафы фракции"""
        if faction_id not in self.factions:
            return {}

        reputation = self.factions[faction_id].reputation
        return get_faction_penalties(faction_id, reputation)

    def can_access(self, faction_id: str, content_type: str, game_state: Dict[str, Any]) -> Tuple[bool, str]:
        """Проверить доступ к контенту фракции"""
        return can_access_faction_content(faction_id, content_type, game_state)

    def get_quest_givers(self, faction_id: str) -> List[str]:
        """Получить квестодателей фракции"""
        return get_faction_quest_givers(faction_id)

    def get_all_standings(self) -> Dict[str, Dict[str, Any]]:
        """Получить все отношения с фракциями"""
        standings = {}

        for faction_id, faction_state in self.factions.items():
            faction_data = get_faction(faction_id)
            tier_data = get_reputation_tier(faction_id, faction_state.reputation)

            standings[faction_id] = {
                "name": faction_data["name"] if faction_data else faction_id,
                "reputation": faction_state.reputation,
                "tier": tier_data,
                "bonuses": self.get_bonuses(faction_id),
                "penalties": self.get_penalties(faction_id),
                "hunted": faction_id in self.hunted_by
            }

        return standings

    def get_shop_discount(self, faction_id: str) -> int:
        """Получить скидку в магазине фракции"""
        bonuses = self.get_bonuses(faction_id)
        return bonuses.get("shop_discount", 0)

    def is_hunted(self) -> bool:
        """Проверить, охотятся ли на игрока"""
        return len(self.hunted_by) > 0

    def get_hunters(self) -> List[str]:
        """Получить список охотящихся фракций"""
        return self.hunted_by.copy()

    def _update_faction_relations(self, faction_id: str, change: int):
        """Обновить отношения с связанными фракциями"""
        if change <= 0:
            return

        for relation_id, relation_data in FACTION_RELATIONS.items():
            if faction_id not in relation_data["factions"]:
                continue

            other_faction = [f for f in relation_data["factions"] if f != faction_id][0]
            relation_type = relation_data["relation"]

            if relation_type == "hostile":
                # Повышение с враждебной фракцией понижает с другой
                self.change_reputation(other_faction, -change // 2)
            elif relation_type == "allied":
                # Повышение с союзной фракцией повышает с другой
                self.change_reputation(other_faction, change // 3)

    def to_dict(self) -> Dict[str, Any]:
        """Сериализовать в словарь"""
        return {
            "factions": {
                faction_id: {
                    "reputation": state.reputation,
                    "tier": state.tier,
                    "bonuses": state.unlocked_bonuses,
                    "penalties": state.active_penalties
                }
                for faction_id, state in self.factions.items()
            },
            "hunted_by": self.hunted_by,
            "unlocked_factions": self.unlocked_factions
        }

    def from_dict(self, data: Dict[str, Any]):
        """Десериализовать из словаря"""
        if "factions" in data:
            for faction_id, faction_data in data["factions"].items():
                if faction_id in self.factions:
                    self.factions[faction_id].reputation = faction_data.get("reputation", 0)
                    self.factions[faction_id].tier = faction_data.get("tier", "neutral")
                    self.factions[faction_id].unlocked_bonuses = faction_data.get("bonuses", [])
                    self.factions[faction_id].active_penalties = faction_data.get("penalties", [])

        self.hunted_by = data.get("hunted_by", [])
        self.unlocked_factions = data.get("unlocked_factions", [])
