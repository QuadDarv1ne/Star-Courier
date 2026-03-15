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
            description="Полное слияние с резонансом. Доступ к древним знаниям.",
            level_required=ResonanceLevel.TRANSCENDENT,
            effects={
                "anomaly_immunity": True,
                "entity_bond": True,
                "time_perception": True,
                "psychic_amplification": 50
            },
            unlock_condition="psychic_90_plus"
        )

    def get_level_number(self) -> int:
        """Получить текущий уровень числом"""
        return self.current_level.value

    def check_level_up(self, psychic_level: int, completed_chapters: List[int]):
        """Проверить повышение уровня Резонанса"""
        if 14 in completed_chapters and self.current_level.value < 3:
            self.current_level = ResonanceLevel.MASTERY
            logger.info(f"Resonance: повышен до {self.current_level.name}")
        
        if psychic_level >= 90 and self.current_level.value < 4:
            self.current_level = ResonanceLevel.TRANSCENDENT
            logger.info(f"Resonance: повышен до {self.current_level.name} (трансцендентный)")
        
        return self.current_level

    def get_effects(self) -> Dict:
        """Получить текущие эффекты Резонанса"""
        ability = self.abilities.get(f"resonance_{self.current_level.name.lower()}")
        if ability:
            return ability.effects
        return {}

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
