# -*- coding: utf-8 -*-
"""
Star Courier - Resonance System
Система Резонанса для взаимодействия с аномалиями и Сущностью
"""

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional

logger = logging.getLogger('resonance')


class ResonanceLevel(Enum):
    """Уровни Резонанса"""
    BASIC = 1           # Основы (Глава 6)
    AMPLIFICATION = 2   # Усиление (Глава 10)
    MASTERY = 3         # Мастерство (Глава 14)
    TRANSCENDENT = 4    # Трансцендентный (Psychic 90+)


@dataclass
class ResonanceAbility:
    """Способность Резонанса"""
    id: str
    name: str
    description: str
    level_required: ResonanceLevel
    effects: Dict[str, any] = field(default_factory=dict)
    unlock_condition: str = ""


class ResonanceSystem:
    """Система Резонанса"""

    def __init__(self):
        self.current_level: ResonanceLevel = ResonanceLevel.BASIC
        self.experience: int = 0
        self.abilities: Dict[str, ResonanceAbility] = {}
        self._init_abilities()

    def _init_abilities(self):
        """Инициализировать способности Резонанса"""
        
        self.abilities["resonance_basics"] = ResonanceAbility(
            id="res_1",
            name="Основы Резонанса",
            description="Базовая способность чувствовать присутствие аномалий и Сущности.",
            level_required=ResonanceLevel.BASIC,
            effects={
                "anomaly_detection_range": 100,
                "entity_presence_warning": True
            },
            unlock_condition="chapter_6_complete"
        )

        self.abilities["resonance_amplification"] = ResonanceAbility(
            id="res_2",
            name="Усиление Резонанса",
            description="Улучшенное чувствование и частичное сопротивление аномалиям.",
            level_required=ResonanceLevel.AMPLIFICATION,
            effects={
                "anomaly_detection_range": 500,
                "entity_weakness_perception": True,
                "mental_resistance": 20
            },
            unlock_condition="chapter_10_complete"
        )

        self.abilities["resonance_mastery"] = ResonanceAbility(
            id="res_3",
            name="Мастерство Резонанса",
            description="Полный контроль над резонансом с пространством.",
            level_required=ResonanceLevel.MASTERY,
            effects={
                "anomaly_navigation": True,
                "entity_communication": True,
                "future_fragments": True
            },
            unlock_condition="chapter_14_complete"
        )

        self.abilities["resonance_transcendent"] = ResonanceAbility(
            id="res_4",
            name="Трансцендентный Резонанс",
            description="Единение с тканью реальности. Требуется для финала Слияния.",
            level_required=ResonanceLevel.TRANSCENDENT,
            effects={
                "reality_manipulation": True,
                "entity_integration_safe": True,
                "merge_ending_unlock": True
            },
            unlock_condition="psychic_90_or_entity_communion"
        )

    def get_level(self) -> ResonanceLevel:
        """Получить текущий уровень"""
        return self.current_level

    def get_level_number(self) -> int:
        """Получить номер уровня"""
        return self.current_level.value

    def add_experience(self, amount: int):
        """Добавить опыт Резонанса"""
        self.experience += amount
        logger.info(f"Получен опыт Резонанса: {amount} (всего: {self.experience})")

    def check_level_up(self, psychic_stat: int, completed_chapters: List[int]) -> bool:
        """Проверить возможность повышения уровня"""
        if self.current_level == ResonanceLevel.TRANSCENDENT:
            return False

        next_level = ResonanceLevel(self.current_level.value + 1)
        ability = self._get_ability_for_level(next_level)

        if not ability:
            return False

        # Проверка условия разблокировки
        if self._check_unlock_condition(ability, psychic_stat, completed_chapters):
            self.current_level = next_level
            logger.info(f"Уровень Резонанса повышен: {self.current_level.name}")
            return True

        return False

    def _get_ability_for_level(self, level: ResonanceLevel) -> Optional[ResonanceAbility]:
        """Получить способность для уровня"""
        for ability in self.abilities.values():
            if ability.level_required == level:
                return ability
        return None

    def _check_unlock_condition(self, ability: ResonanceAbility, 
                                 psychic_stat: int, 
                                 completed_chapters: List[int]) -> bool:
        """Проверить условие разблокировки"""
        condition = ability.unlock_condition

        if "chapter_6" in condition and 6 in completed_chapters:
            return True
        if "chapter_10" in condition and 10 in completed_chapters:
            return True
        if "chapter_14" in condition and 14 in completed_chapters:
            return True
        if "psychic_90" in condition and psychic_stat >= 90:
            return True
        if "entity_communion" in condition:
            # Проверяется через флаг игры
            return True

        return False

    def get_active_effects(self) -> Dict[str, any]:
        """Получить активные эффекты"""
        effects = {}
        for ability in self.abilities.values():
            if ability.level_required.value <= self.current_level.value:
                effects.update(ability.effects)
        return effects

    def has_effect(self, effect_name: str) -> bool:
        """Проверить наличие эффекта"""
        effects = self.get_active_effects()
        return effect_name in effects and effects[effect_name]

    def get_effect_value(self, effect_name: str, default=0):
        """Получить значение эффекта"""
        effects = self.get_active_effects()
        return effects.get(effect_name, default)

    def to_dict(self) -> dict:
        """Сериализация в словарь"""
        return {
            "level": self.current_level.value,
            "experience": self.experience,
            "abilities": list(self.abilities.keys())
        }

    def from_dict(self, data: dict):
        """Десериализация из словаря"""
        if "level" in data:
            self.current_level = ResonanceLevel(data["level"])
        if "experience" in data:
            self.experience = data["experience"]

    def get_status_display(self) -> str:
        """Получить отображение статуса"""
        level_names = {
            1: "Основы",
            2: "Усиление",
            3: "Мастерство",
            4: "Трансцендентный"
        }
        level_name = level_names.get(self.current_level.value, "Неизвестно")
        return f"Резонанс: {level_name} (Уровень {self.current_level.value})"
