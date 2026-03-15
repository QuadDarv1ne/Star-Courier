# -*- coding: utf-8 -*-
"""
Star Courier - Mental State System
Система ментального состояния и влияния Сущности
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum
import logging

logger = logging.getLogger('mental_state')


class MentalCondition(Enum):
    """Состояния ментального здоровья"""
    STABLE = "stable"  # 80-100
    STRESSED = "stressed"  # 60-79
    TRAUMATIZED = "traumatized"  # 40-59
    CORRUPTED = "corrupted"  # 20-39
    BROKEN = "broken"  # 0-19


class EntityInfluenceLevel(Enum):
    """Уровни влияния Сущности"""
    CLEAN = "clean"  # 0-10
    EXPOSED = "exposed"  # 11-30
    INFECTED = "infected"  # 31-60
    CORRUPTED = "corrupted"  # 61-90
    ASSIMILATED = "assimilated"  # 91-100


@dataclass
class MentalState:
    """Состояние персонажа"""
    # Ментальное здоровье (0-100, 100 = идеально)
    health: int = 100
    
    # Влияние Сущности (0-100, 0 = чист)
    entity_influence: int = 0
    
    # Уровень стресса (накапливается от событий)
    stress: int = 0
    
    # Травмы (постоянные эффекты)
    traumas: List[str] = field(default_factory=list)
    
    # Временные эффекты
    effects: Dict[str, int] = field(default_factory=dict)
    
    # Флаги
    has_nightmares: bool = False
    hears_entity: bool = False
    sees_visions: bool = False

    def get_condition(self) -> MentalCondition:
        """Получить текущее состояние"""
        if self.health >= 80:
            return MentalCondition.STABLE
        elif self.health >= 60:
            return MentalCondition.STRESSED
        elif self.health >= 40:
            return MentalCondition.TRAUMATIZED
        elif self.health >= 20:
            return MentalCondition.CORRUPTED
        else:
            return MentalCondition.BROKEN

    def get_influence_level(self) -> EntityInfluenceLevel:
        """Получить уровень влияния Сущности"""
        if self.entity_influence <= 10:
            return EntityInfluenceLevel.CLEAN
        elif self.entity_influence <= 30:
            return EntityInfluenceLevel.EXPOSED
        elif self.entity_influence <= 60:
            return EntityInfluenceLevel.INFECTED
        elif self.entity_influence <= 90:
            return EntityInfluenceLevel.CORRUPTED
        else:
            return EntityInfluenceLevel.ASSIMILATED

    def is_stable(self) -> bool:
        """Проверить стабильность"""
        return self.get_condition() in [MentalCondition.STABLE, MentalCondition.STRESSED]

    def is_corrupted(self) -> bool:
        """Проверить коррупцию"""
        return self.get_condition() in [MentalCondition.CORRUPTED, MentalCondition.BROKEN]

    def can_resist_entity(self) -> bool:
        """Проверить способность сопротивляться Сущности"""
        return self.health >= 50 and self.entity_influence < 50


class MentalStateSystem:
    """
    Система управления ментальным состоянием.
    Отслеживает здоровье, влияние Сущности и эффекты.
    """

    def __init__(self):
        # Состояние игрока
        self.player_state = MentalState()
        
        # Состояния членов экипажа
        self.crew_states: Dict[str, MentalState] = {}
        
        # Множители эффектов
        self.difficulty_multiplier = 1.0
        
        # История событий
        self.event_log: List[Dict] = []

    def initialize_crew(self, crew_ids: List[str]):
        """Инициализировать состояния экипажа"""
        for crew_id in crew_ids:
            self.crew_states[crew_id] = MentalState()

    def get_player_state(self) -> MentalState:
        """Получить состояние игрока"""
        return self.player_state

    def get_crew_state(self, crew_id: str) -> Optional[MentalState]:
        """Получить состояние члена экипажа"""
        return self.crew_states.get(crew_id)

    # ==================== ИЗМЕНЕНИЕ СОСТОЯНИЙ ====================

    def change_mental_health(self, amount: int, target: str = "player"):
        """
        Изменить ментальное здоровье.
        amount > 0 = улучшение, amount < 0 = ухудшение
        """
        if target == "player":
            state = self.player_state
        else:
            state = self.crew_states.get(target)
            if not state:
                return

        old_health = state.health
        state.health = max(0, min(100, state.health + amount))
        
        # Логирование события
        self._log_event("mental_health_change", {
            "target": target,
            "amount": amount,
            "old": old_health,
            "new": state.health
        })

        # Проверка порогов
        self._check_thresholds(state, target)

    def change_entity_influence(self, amount: int, target: str = "player"):
        """
        Изменить влияние Сущности.
        amount > 0 = усиление влияния, amount < 0 = очищение
        """
        if target == "player":
            state = self.player_state
        else:
            state = self.crew_states.get(target)
            if not state:
                return

        old_influence = state.entity_influence
        state.entity_influence = max(0, min(100, state.entity_influence + amount))
        
        # Логирование
        self._log_event("entity_influence_change", {
            "target": target,
            "amount": amount,
            "old": old_influence,
            "new": state.entity_influence
        })

        # Проверка порогов
        self._check_thresholds(state, target)

    def add_stress(self, amount: int, target: str = "player"):
        """Добавить стресс"""
        if target == "player":
            state = self.player_state
        else:
            state = self.crew_states.get(target)
            if not state:
                return

        state.stress = min(100, state.stress + amount)
        
        # Стресс влияет на ментальное здоровье
        if state.stress >= 80:
            self.change_mental_health(-10, target)
            state.has_nightmares = True

    def reduce_stress(self, amount: int, target: str = "player"):
        """Снизить стресс"""
        if target == "player":
            state = self.player_state
        else:
            state = self.crew_states.get(target)
            if not state:
                return

        state.stress = max(0, state.stress - amount)
        
        if state.stress < 30:
            state.has_nightmares = False

    # ==================== ЭФФЕКТЫ ====================

    def add_effect(self, effect_id: str, duration: int, target: str = "player"):
        """Добавить временный эффект"""
        if target == "player":
            state = self.player_state
        else:
            state = self.crew_states.get(target)
            if not state:
                return

        state.effects[effect_id] = duration
        logger.info(f"Добавлен эффект {effect_id} на {duration} ходов")

    def remove_effect(self, effect_id: str, target: str = "player"):
        """Удалить эффект"""
        if target == "player":
            state = self.player_state
        else:
            state = self.crew_states.get(target)
            if not state:
                return

        if effect_id in state.effects:
            del state.effects[effect_id]

    def has_effect(self, effect_id: str, target: str = "player") -> bool:
        """Проверить наличие эффекта"""
        if target == "player":
            return effect_id in self.player_state.effects
        return effect_id in self.crew_states.get(target, MentalState()).effects

    def tick_effects(self):
        """Обновить эффекты (каждый ход/день)"""
        for state in [self.player_state] + list(self.crew_states.values()):
            to_remove = []
            for effect_id, duration in state.effects.items():
                state.effects[effect_id] = duration - 1
                if state.effects[effect_id] <= 0:
                    to_remove.append(effect_id)
            
            for effect_id in to_remove:
                del state.effects[effect_id]

    # ==================== ТРАВМЫ ====================

    def add_trauma(self, trauma_id: str, target: str = "player"):
        """Добавить травму"""
        if target == "player":
            state = self.player_state
        else:
            state = self.crew_states.get(target)
            if not state:
                return

        if trauma_id not in state.traumas:
            state.traumas.append(trauma_id)
            logger.info(f"Добавлена травма {trauma_id}")

    def remove_trauma(self, trauma_id: str, target: str = "player"):
        """Удалить травму"""
        if target == "player":
            state = self.player_state
        else:
            state = self.crew_states.get(target)
            if not state:
                return

        if trauma_id in state.traumas:
            state.traumas.remove(trauma_id)
            logger.info(f"Удалена травма {trauma_id}")

    def has_trauma(self, trauma_id: str, target: str = "player") -> bool:
        """Проверить наличие травмы"""
        if target == "player":
            return trauma_id in self.player_state.traumas
        return trauma_id in self.crew_states.get(target, MentalState()).traumas

    # ==================== СОБЫТИЯ ====================

    def on_combat_end(self, victory: bool, casualties: int = 0):
        """Событие: конец боя"""
        if not victory:
            self.change_mental_health(-15)
            self.add_stress(20)
        else:
            self.add_stress(10)

        if casualties > 0:
            self.change_mental_health(-20 * casualties)
            self.add_trauma("combat_trauma")

    def on_entity_encounter(self, intensity: int = 10):
        """Событие: контакт с Сущностью"""
        # Проверка сопротивления перед применением влияния
        if self.check_resistance(difficulty=intensity):
            # Успешное сопротивление - влияние减半
            intensity = intensity // 2
            logger.info("Успешное сопротивление влиянию Сущности")
        
        self.change_entity_influence(intensity)
        self.change_mental_health(-5)

        if self.player_state.entity_influence >= 50:
            self.player_state.hears_entity = True
            self.player_state.sees_visions = True

    def on_nightmare(self):
        """Событие: кошмар"""
        self.change_mental_health(-10)
        self.add_stress(15)
        self.player_state.has_nightmares = True

    def on_rest(self, quality: int = 1):
        """Событие: отдых"""
        health_recovery = 5 * quality
        stress_reduction = 10 * quality

        self.change_mental_health(health_recovery)
        self.reduce_stress(stress_reduction)

    def on_therapy(self, effectiveness: int = 1):
        """Событие: терапия (Мария или другой медик)"""
        health_recovery = 15 * effectiveness
        stress_reduction = 20 * effectiveness

        self.change_mental_health(health_recovery)
        self.reduce_stress(stress_reduction)

    def on_purification(self, strength: int = 1):
        """Событие: очищение от влияния Сущности"""
        influence_reduction = 10 * strength
        health_recovery = 5 * strength
        
        self.change_entity_influence(-influence_reduction)
        self.change_mental_health(health_recovery)
        logger.info(f"Очищение: влияние -{influence_reduction}, здоровье +{health_recovery}")

    def on_meditation(self, duration: int = 1):
        """Событие: медитация (снижение стресса и влияния)"""
        stress_reduction = 15 * duration
        influence_reduction = 5 * duration
        
        self.reduce_stress(stress_reduction)
        self.change_entity_influence(-influence_reduction)
        logger.info(f"Медитация: стресс -{stress_reduction}, влияние -{influence_reduction}")

    # ==================== ПРОВЕРКИ ====================

    def check_resistance(self, difficulty: int = 50) -> bool:
        """
        Проверка сопротивления влиянию Сущности.
        Returns True если успешно.
        """
        import random
        
        # Базовый шанс зависит от ментального здоровья
        base_chance = self.player_state.health
        
        # Влияние Сущности уменьшает шанс
        corruption_penalty = self.player_state.entity_influence // 2
        
        # Стресс уменьшает шанс
        stress_penalty = self.player_state.stress // 3
        
        final_chance = base_chance - corruption_penalty - stress_penalty
        final_chance = max(10, min(90, final_chance))
        
        roll = random.randint(1, 100)
        success = roll <= final_chance
        
        self._log_event("resistance_check", {
            "difficulty": difficulty,
            "chance": final_chance,
            "roll": roll,
            "success": success
        })
        
        return success

    def check_sanity(self, horror_level: int = 50) -> bool:
        """
        Проверка на сохранение рассудка.
        Returns True если персонаж выдержал.
        """
        import random
        
        base_chance = self.player_state.health - horror_level
        base_chance = max(10, min(90, base_chance))
        
        roll = random.randint(1, 100)
        success = roll <= base_chance
        
        if not success:
            self.change_mental_health(-20)
            self.add_stress(30)
        
        return success

    # ==================== ВНУТРЕННИЕ МЕТОДЫ ====================

    def _check_thresholds(self, state: MentalState, target: str):
        """Проверить пороги состояний"""
        condition = state.get_condition()
        
        # Автоматические эффекты при достижении порогов
        if condition == MentalCondition.BROKEN:
            state.has_nightmares = True
            state.hears_entity = True
            self._log_event("mental_break", {"target": target})
        
        if state.entity_influence >= 80:
            state.sees_visions = True
            state.hears_entity = True

    def _log_event(self, event_type: str, data: Dict):
        """Логирование события"""
        self.event_log.append({
            "type": event_type,
            "data": data,
            "timestamp": len(self.event_log)  # Упрощённый таймстемп
        })
        
        if len(self.event_log) > 100:
            self.event_log = self.event_log[-100:]

    # ==================== СЕРИАЛИЗАЦИЯ ====================

    def to_dict(self) -> Dict:
        """Сериализация"""
        return {
            "player": {
                "health": self.player_state.health,
                "entity_influence": self.player_state.entity_influence,
                "stress": self.player_state.stress,
                "traumas": self.player_state.traumas,
                "effects": self.player_state.effects,
                "flags": {
                    "has_nightmares": self.player_state.has_nightmares,
                    "hears_entity": self.player_state.hears_entity,
                    "sees_visions": self.player_state.sees_visions
                }
            },
            "crew": {
                cid: {
                    "health": state.health,
                    "entity_influence": state.entity_influence,
                    "stress": state.stress,
                    "traumas": state.traumas
                }
                for cid, state in self.crew_states.items()
            },
            "event_log": self.event_log[-20:]  # Последние 20 событий
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "MentalStateSystem":
        """Десериализация"""
        system = cls()
        
        if "player" in data:
            p = data["player"]
            system.player_state.health = p.get("health", 100)
            system.player_state.entity_influence = p.get("entity_influence", 0)
            system.player_state.stress = p.get("stress", 0)
            system.player_state.traumas = p.get("traumas", [])
            system.player_state.effects = p.get("effects", {})
            
            flags = p.get("flags", {})
            system.player_state.has_nightmares = flags.get("has_nightmares", False)
            system.player_state.hears_entity = flags.get("hears_entity", False)
            system.player_state.sees_visions = flags.get("sees_visions", False)
        
        if "crew" in data:
            for cid, cdata in data["crew"].items():
                state = MentalState()
                state.health = cdata.get("health", 100)
                state.entity_influence = cdata.get("entity_influence", 0)
                state.stress = cdata.get("stress", 0)
                state.traumas = cdata.get("traumas", [])
                system.crew_states[cid] = state
        
        if "event_log" in data:
            system.event_log = data["event_log"]
        
        return system


# === УТИЛИТЫ ===

def get_condition_description(condition: MentalCondition) -> str:
    """Получить описание состояния"""
    descriptions = {
        MentalCondition.STABLE: "Психика стабильна. Вы готовы к любым испытаниям.",
        MentalCondition.STRESSED: "Лёгкий стресс. Отдых поможет восстановиться.",
        MentalCondition.TRAUMATIZED: "Травма влияет на суждение. Нужна помощь.",
        MentalCondition.CORRUPTED: "Влияние Сущности сильно. Сопротивление слабеет.",
        MentalCondition.BROKEN: "Психика разрушена. Критическое состояние."
    }
    return descriptions.get(condition, "Неизвестное состояние")


def get_influence_description(level: EntityInfluenceLevel) -> str:
    """Получить описание влияния Сущности"""
    descriptions = {
        EntityInfluenceLevel.CLEAN: "Вы чисты. Влияние Сущности минимально.",
        EntityInfluenceLevel.EXPOSED: "Вы чувствовали влияние Сущности. Будьте осторожны.",
        EntityInfluenceLevel.INFECTED: "Сущность оставила след в вашем разуме.",
        EntityInfluenceLevel.CORRUPTED: "Сущность меняет вас. Сопротивление трудно.",
        EntityInfluenceLevel.ASSIMILATED: "Вы почти часть Сущности. Граница стёрта."
    }
    return descriptions.get(level, "Неизвестный уровень")
