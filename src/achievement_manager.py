# -*- coding: utf-8 -*-
"""
Star Courier - Achievement Manager
Менеджер достижений: трекинг, разблокировка, награды и сохранение
"""

import logging
from typing import Dict, Any, List, Optional, Tuple

from .achievements_v5 import (
    ALL_ACHIEVEMENTS, get_all_achievements,
    get_achievement_progress, get_visible_achievements
)

logger = logging.getLogger('achievements')


class AchievementManager:
    """Менеджер достижений игрока"""

    def __init__(self):
        self.unlocked: List[str] = []
        self.stats: Dict[str, Any] = {
            "enemies_defeated": 0,
            "locations_visited": set(),
            "completed_dialogues": [],
            "romance_rejections": 0,
            "dialogues_count": 0,
        }
        self.credits_earned_total: int = 0

    def unlock(self, achievement_id: str, game_state) -> Optional[Dict[str, Any]]:
        """Попытаться разблокировать достижение"""
        if achievement_id in self.unlocked:
            return None

        achievement = get_all_achievements().get(achievement_id)
        if not achievement:
            return None

        if not self._check_condition(achievement, game_state):
            return None

        self.unlocked.append(achievement_id)
        self._apply_rewards(achievement, game_state)
        logger.info(f"Достижение разблокировано: {achievement['name']}")
        return achievement

    def check_all(self, game_state) -> List[Dict[str, Any]]:
        """Проверить все достижения и разблокировать подходящие"""
        newly_unlocked = []
        for achievement_id in get_all_achievements():
            result = self.unlock(achievement_id, game_state)
            if result:
                newly_unlocked.append(result)
        return newly_unlocked

    def _check_condition(self, achievement: Dict[str, Any], game_state) -> bool:
        """Проверить условие разблокировки"""
        condition = achievement.get("unlock_condition", {})
        flags = game_state.save_data.flags if game_state.save_data else {}
        relationships = game_state.save_data.relationships if game_state.save_data else {}
        stats = game_state.save_data.stats if game_state.save_data else {}
        credits = game_state.save_data.credits if game_state.save_data else 0
        chapter = game_state.save_data.chapter if game_state.save_data else 1

        for key, value in condition.items():
            if key == "chapter_complete":
                if chapter < value:
                    return False
            elif key == "dialogue_complete":
                if value not in self.stats["completed_dialogues"]:
                    return False
            elif key == "quest_complete":
                if value not in game_state.quest_manager.completed_quests:
                    return False
            elif key == "ending":
                try:
                    from .ending_system import EndingType
                    ending_type = EndingType(value)
                except ValueError:
                    return False
                ending = game_state.ending_system.get_ending(ending_type)
                if not ending or not ending.unlocked:
                    return False
            elif key == "path":
                path = getattr(game_state.path_system, "current_path", None)
                if not path or getattr(path, "value", "") != value:
                    return False
            elif key == "enemies_defeated":
                if self.stats.get("enemies_defeated", 0) < value:
                    return False
            elif key == "locations_visited":
                if len(self.stats.get("locations_visited", set())) < value:
                    return False
            elif key == "character_relationship":
                for char_id, level in value.items():
                    if relationships.get(char_id, 0) < level:
                        return False
            elif key == "ability_level":
                for branch, level in value.items():
                    if stats.get(branch, 0) < level:
                        return False
            elif key == "resonance_level":
                if game_state.resonance_system.get_level_number() < value:
                    return False
            elif key == "game_complete":
                if not flags.get("game_complete", False):
                    return False
            elif key == "romance_level":
                if max(relationships.values(), default=0) < value:
                    return False
            elif key == "romance_rejections":
                if self.stats.get("romance_rejections", 0) < value:
                    return False
            elif key == "multiple_relationships":
                count = sum(1 for v in relationships.values() if v >= 80)
                if count < value:
                    return False
            elif key == "credits_earned":
                if self.credits_earned_total < value:
                    return False
            elif key == "quests_completed":
                if len(game_state.quest_manager.completed_quests) < value:
                    return False
            elif key == "dialogues_count":
                if self.stats.get("dialogues_count", 0) < value:
                    return False
            elif key == "all_branches_50":
                if not all(stats.get(b, 0) >= 50 for b in ("alchemy", "biotics", "psychic")):
                    return False
            elif key == "all_locations":
                # Проверка на основе количества посещённых локаций
                if len(self.stats.get("locations_visited", set())) < 10:
                    return False
            elif key == "all_paths_complete":
                if not flags.get("all_paths_complete", False):
                    return False
            elif key == "endings_count":
                seen = 0
                endings = getattr(game_state.save_data, "endings", {})
                main = endings.get("main", {}).get("endings", {})
                for data in main.values():
                    if data.get("seen", False):
                        seen += 1
                if seen < value:
                    return False
            elif key == "entity_peaceful_dialogues":
                if self.stats.get("entity_peaceful_dialogues", 0) < value:
                    return False
            elif key == "echo_lore_complete":
                if not flags.get("echo_lore_complete", False):
                    return False
            elif key == "time_paradox_seen":
                if not flags.get("time_paradox_seen", False):
                    return False
            elif key == "survivor_truth_revealed":
                if not flags.get("survivor_truth_revealed", False):
                    return False
            elif key == "perfect_run":
                if not flags.get("perfect_run", False):
                    return False
            elif key == "zone_time":
                if flags.get("zone_time", 0) < value:
                    return False
            elif key == "no_mental_break":
                if not flags.get("no_mental_break", False):
                    return False
            elif key == "chapter_no_kills":
                if not flags.get("chapter_no_kills", False):
                    return False
            elif key == "boss_no_damage":
                if not flags.get("boss_no_damage", False):
                    return False
            elif key == "anomalies_found":
                if self.stats.get("anomalies_found", 0) < value:
                    return False
            elif key == "temple_secrets":
                if not flags.get("temple_secrets", False):
                    return False
            elif key == "entity_spawn_killed":
                if self.stats.get("entity_spawn_killed", 0) < value:
                    return False
            elif key == "secrets_found":
                if flags.get("secrets_found", 0) < (10 if value == "all" else value):
                    return False
            elif key == "item_obtained":
                if not game_state.inventory.has_item(value):
                    return False
            elif key == "event":
                if not flags.get(value, False):
                    return False
            elif key == "location_visited":
                if value not in self.stats.get("locations_visited", set()):
                    return False
            elif key == "playtime_hours":
                if flags.get("playtime_hours", 0) < value:
                    return False

        return True

    def _apply_rewards(self, achievement: Dict[str, Any], game_state):
        """Применить награды за достижение"""
        rewards = achievement.get("rewards", {})
        for reward_type, value in rewards.items():
            if reward_type == "credits":
                game_state.add_credits(value)
                self.credits_earned_total += value
            elif reward_type == "psychic":
                current = game_state.abilities_manager.get_tier(
                    game_state.abilities_manager.AbilityType.PSYCHIC
                ).value if hasattr(game_state.abilities_manager, "AbilityType") else 0
                game_state.set_flag("achievement_psychic_bonus",
                                    game_state.get_flag("achievement_psychic_bonus", 0) + value)
            elif reward_type == "title":
                titles = self.stats.setdefault("titles", [])
                if value not in titles:
                    titles.append(value)
            elif reward_type == "knowledge":
                game_state.set_flag("achievement_knowledge",
                                    game_state.get_flag("achievement_knowledge", 0) + value)

    def register_enemy_defeat(self, count: int = 1):
        """Зарегистрировать победу над врагом"""
        self.stats["enemies_defeated"] = self.stats.get("enemies_defeated", 0) + count

    def register_dialogue(self, dialogue_id: str):
        """Зарегистрировать завершённый диалог"""
        if dialogue_id not in self.stats["completed_dialogues"]:
            self.stats["completed_dialogues"].append(dialogue_id)
        self.stats["dialogues_count"] = self.stats.get("dialogues_count", 0) + 1

    def register_location(self, location_id: str):
        """Зарегистрировать посещённую локацию"""
        if isinstance(self.stats["locations_visited"], set):
            self.stats["locations_visited"].add(location_id)

    def register_rejection(self):
        """Зарегистрировать отказ в романтике"""
        self.stats["romance_rejections"] = self.stats.get("romance_rejections", 0) + 1

    def to_dict(self) -> Dict[str, Any]:
        """Сериализовать в словарь"""
        return {
            "unlocked": self.unlocked,
            "stats": {
                k: (list(v) if isinstance(v, set) else v)
                for k, v in self.stats.items()
            },
            "credits_earned_total": self.credits_earned_total,
        }

    def from_dict(self, data: Dict[str, Any]):
        """Десериализовать из словаря"""
        if not data:
            return
        self.unlocked = data.get("unlocked", [])
        raw_stats = data.get("stats", {})
        self.stats = {
            k: (set(v) if k == "locations_visited" else v)
            for k, v in raw_stats.items()
        }
        self.credits_earned_total = data.get("credits_earned_total", 0)

    def get_progress(self) -> Dict[str, Any]:
        """Получить прогресс по достижениям"""
        return get_achievement_progress({"unlocked_achievements": self.unlocked})

    def get_visible(self) -> Dict[str, Dict[str, Any]]:
        """Получить список видимых достижений"""
        visible = get_visible_achievements({"unlocked_achievements": self.unlocked})
        for category, achievements in ALL_ACHIEVEMENTS.items():
            for ach_id in achievements:
                if ach_id in visible:
                    visible[ach_id]["_category"] = category
        return visible


def format_achievement(achievement: Dict[str, Any], unlocked: bool) -> str:
    """Форматировать достижение для отображения"""
    icon_map = {
        "rocket": "🚀", "crystal": "💎", "crossroad": "🛣️", "footprint": "👣",
        "time_crystal": "⏳", "mask": "🎭", "void": "🌌", "guardian": "🗿",
        "sun": "☀️", "balance": "⚖️", "infinity": "♾️", "trident": "🔱",
        "heart": "❤️", "sword": "⚔️", "medal": "🎖️", "shield": "🛡️",
        "dove": "🕊️", "compass": "🧭", "map": "🗺️", "radar": "📡",
        "temple": "🏛️", "hazard": "⚠️", "potion": "🧪", "force": "🌀",
        "mind": "🧠", "star": "⭐", "wave": "🌊", "alliance": "🤝",
        "observer": "👁️", "independence": "🦅", "triple": "🎯",
        "handshake": "🤝", "memory": "🧬", "clock": "🕐", "truth": "📜",
        "crown": "👑", "coins": "💰", "scroll": "📖", "speech": "💬",
        "hourglass": "⏱️", "key": "🗝️", "broken_heart": "💔", "hearts": "💕",
    }
    icon = icon_map.get(achievement.get("icon", ""), "🏆")
    if unlocked:
        return f"  {icon} {achievement['name']} — {achievement['description']}"
    return f"  {icon} ??? — Скрытое достижение"


def create_default_achievement_manager() -> AchievementManager:
    """Создать менеджер достижений по умолчанию"""
    return AchievementManager()