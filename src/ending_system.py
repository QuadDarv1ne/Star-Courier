# -*- coding: utf-8 -*-
"""
Star Courier - Ending System
Система Финалов: Изгнание, Договор, Слияние
"""

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional

logger = logging.getLogger('ending_system')


class EndingType(Enum):
    """Типы Финалов"""
    EXILE = "exile"           # Изгнание - уничтожение якоря
    TREATY = "treaty"         # Договор - Хранительство Границы
    MERGE = "merge"           # Слияние - трансцендентная эволюция


@dataclass
class EndingRequirement:
    """Требования для Финала"""
    psychic_min: int = 0
    empathy_min: int = 0
    resonance_level: int = 0
    required_abilities: List[str] = field(default_factory=list)
    required_path: Optional[str] = None
    required_quests: List[str] = field(default_factory=list)


@dataclass
class Ending:
    """Финал"""
    ending_type: EndingType
    name: str
    description: str
    requirements: EndingRequirement
    unlocked: bool = False
    seen: bool = False


class EndingSystem:
    """Система Финалов"""

    def __init__(self):
        self.endings: Dict[EndingType, Ending] = {}
        self.active_ending: Optional[EndingType] = None
        self._init_endings()

    def _init_endings(self):
        """Инициализировать Финалы"""

        # === ФИНАЛ: ИЗГНАНИЕ ===
        exile_ending = Ending(
            ending_type=EndingType.EXILE,
            name="Изгнание",
            description="Уничтожение якоря Сущности ценой жертвы. Галактика спасена, но цена высока.",
            requirements=EndingRequirement(
                psychic_min=0,
                empathy_min=0,
                resonance_level=0,
                required_abilities=["sacrifice_strike"],
                required_quests=["q17_03"]
            )
        )
        self.endings[EndingType.EXILE] = exile_ending

        # === ФИНАЛ: ДОГОВОР ===
        treaty_ending = Ending(
            ending_type=EndingType.TREATY,
            name="Договор",
            description="Перенастройка станции для соглашения с Сущностью. Вечное Хранительство Границы.",
            requirements=EndingRequirement(
                psychic_min=70,
                empathy_min=80,  # Или Psychic
                resonance_level=2,
                required_abilities=["diplomatic_communion"],
                required_quests=["q16_01", "q17_02"]
            )
        )
        self.endings[EndingType.TREATY] = treaty_ending

        # === ФИНАЛ: СЛИЯНИЕ ===
        merge_ending = Ending(
            ending_type=EndingType.MERGE,
            name="Слияние",
            description="Интеграция Сущности в сознание. Трансцендентная эволюция с потерей части человечности.",
            requirements=EndingRequirement(
                psychic_min=90,
                empathy_min=0,
                resonance_level=4,
                required_abilities=["entity_absorption", "transcendence"],
                required_quests=["q17_02", "q17_03"]
            )
        )
        self.endings[EndingType.MERGE] = merge_ending

    def check_unlock(self, ending_type: EndingType, 
                     psychic: int, empathy: int, 
                     resonance_level: int,
                     abilities: List[str],
                     completed_quests: List[str]) -> bool:
        """Проверить разблокировку Финала"""
        ending = self.endings.get(ending_type)
        if not ending:
            return False

        req = ending.requirements

        # Проверка Psychic
        if psychic < req.psychic_min:
            return False

        # Проверка Empathy (или Psychic для некоторых финалов)
        if empathy < req.empathy_min and psychic < req.empathy_min:
            if ending_type == EndingType.TREATY:
                return False

        # Проверка Резонанса
        if resonance_level < req.resonance_level:
            return False

        # Проверка способностей
        for ability in req.required_abilities:
            if ability not in abilities:
                return False

        # Проверка квестов
        for quest in req.required_quests:
            if quest not in completed_quests:
                return False

        # Разблокировано
        ending.unlocked = True
        logger.info(f"Финал разблокирован: {ending.name}")
        return True

    def unlock_ending(self, ending_type: EndingType) -> bool:
        """Принудительно разблокировать Финал"""
        ending = self.endings.get(ending_type)
        if not ending:
            return False
        ending.unlocked = True
        return True

    def set_active_ending(self, ending_type: EndingType) -> bool:
        """Установить активный Финал"""
        ending = self.endings.get(ending_type)
        if not ending or not ending.unlocked:
            logger.warning(f"Финал недоступен: {ending_type}")
            return False

        self.active_ending = ending_type
        logger.info(f"Выбран финал: {ending.name}")
        return True

    def get_available_endings(self) -> List[EndingType]:
        """Получить доступные Финалы"""
        return [e for e in self.endings.values() if e.unlocked].copy()

    def get_ending(self, ending_type: EndingType) -> Optional[Ending]:
        """Получить Финал по типу"""
        return self.endings.get(ending_type)

    def get_active_ending(self) -> Optional[Ending]:
        """Получить активный Финал"""
        if not self.active_ending:
            return None
        return self.endings.get(self.active_ending)

    def mark_ending_seen(self, ending_type: EndingType):
        """Отметить Финал как просмотренный"""
        ending = self.endings.get(ending_type)
        if ending:
            ending.seen = True

    def get_ending_requirements(self, ending_type: EndingType) -> Optional[EndingRequirement]:
        """Получить требования Финала"""
        ending = self.endings.get(ending_type)
        return ending.requirements if ending else None

    def check_all_requirements(self, psychic: int, empathy: int, 
                                resonance_level: int,
                                abilities: List[str],
                                completed_quests: List[str]) -> Dict[EndingType, bool]:
        """Проверить все Финалы"""
        results = {}
        for ending_type in self.endings:
            results[ending_type] = self.check_unlock(
                ending_type, psychic, empathy, resonance_level, 
                abilities, completed_quests
            )
        return results

    def get_ending_description(self, ending_type: EndingType) -> str:
        """Получить описание Финала"""
        ending = self.endings.get(ending_type)
        return ending.description if ending else ""

    def get_ending_name(self, ending_type: EndingType) -> str:
        """Получить название Финала"""
        ending = self.endings.get(ending_type)
        return ending.name if ending else ""

    def to_dict(self) -> dict:
        """Сериализация в словарь"""
        return {
            "endings": {
                e_type.value: {"unlocked": e.unlocked, "seen": e.seen}
                for e_type, e in self.endings.items()
            },
            "active_ending": self.active_ending.value if self.active_ending else None
        }

    def from_dict(self, data: dict):
        """Десериализация из словаря"""
        if "endings" in data:
            for ending_type_str, ending_data in data["endings"].items():
                ending_type = EndingType(ending_type_str)
                ending = self.endings.get(ending_type)
                if ending:
                    ending.unlocked = ending_data.get("unlocked", False)
                    ending.seen = ending_data.get("seen", False)
        
        if "active_ending" in data and data["active_ending"]:
            self.active_ending = EndingType(data["active_ending"])

    def get_status_display(self) -> str:
        """Получить отображение статуса"""
        if not self.active_ending:
            available = self.get_available_endings()
            if available:
                return f"Доступные финалы: {', '.join(e.name for e in available)}"
            return "Финал не выбран"
        
        return f"Активный финал: {self.get_ending_name(self.active_ending)}"


# === ROMANCE ENDINGS ===

class RomanceEndingType(Enum):
    """Типы Романтических Концовок"""
    MIA = "mia"
    MARIA = "maria"
    ANNA = "anna"
    VERONIKA = "veronika"
    ZARA = "zara"
    KIRA = "kira"
    SOLO = "solo"  # Без романтики


@dataclass
class RomanceEnding:
    """Романтическая Концовка"""
    character_id: str
    character_name: str
    description: str
    relationship_required: int = 80
    unlocked: bool = False


class RomanceEndingSystem:
    """Система Романтических Концовок"""

    def __init__(self):
        self.endings: Dict[str, RomanceEnding] = {}
        self.active_romance: Optional[str] = None
        self._init_endings()

    def _init_endings(self):
        """Инициализировать Романтические Концовки"""
        
        self.endings["mia"] = RomanceEnding(
            character_id="mia",
            character_name="Мия",
            description="Мия становится вашим партнёром в новой жизни после событий игры.",
            relationship_required=80
        )

        self.endings["maria"] = RomanceEnding(
            character_id="maria",
            character_name="Мария",
            description="Мария остаётся с вами, поддерживая в новой роли.",
            relationship_required=80
        )

        self.endings["anna"] = RomanceEnding(
            character_id="anna",
            character_name="Анна",
            description="Анна разделяет вашу судьбу, какой бы она ни была.",
            relationship_required=80
        )

        self.endings["veronika"] = RomanceEnding(
            character_id="veronika",
            character_name="Вероника",
            description="Вероника становится вашим ближайшим советником.",
            relationship_required=80
        )

        self.endings["zara"] = RomanceEnding(
            character_id="zara",
            character_name="Зара",
            description="Зара основывает новую школу вместе с вами.",
            relationship_required=80
        )

        self.endings["kira"] = RomanceEnding(
            character_id="kira",
            character_name="Кира",
            description="Кира сопровождает вас в новых приключениях.",
            relationship_required=80
        )

    def check_unlock(self, character_id: str, relationship: int) -> bool:
        """Проверить разблокировку Романтической Концовки"""
        ending = self.endings.get(character_id)
        if not ending:
            return False

        if relationship >= ending.relationship_required:
            ending.unlocked = True
            logger.info(f"Романтическая концовка разблокирована: {ending.character_name}")
            return True
        
        return False

    def set_active_romance(self, character_id: str) -> bool:
        """Установить активную Романтическую Концовку"""
        ending = self.endings.get(character_id)
        if not ending or not ending.unlocked:
            return False

        self.active_romance = character_id
        return True

    def get_available_romances(self) -> List[RomanceEnding]:
        """Получить доступные Романтические Концовки"""
        return [e for e in self.endings.values() if e.unlocked]

    def to_dict(self) -> dict:
        """Сериализация в словарь"""
        return {
            "endings": {
                cid: {"unlocked": e.unlocked}
                for cid, e in self.endings.items()
            },
            "active_romance": self.active_romance
        }

    def from_dict(self, data: dict):
        """Десериализация из словаря"""
        if "endings" in data:
            for char_id, ending_data in data["endings"].items():
                ending = self.endings.get(char_id)
                if ending:
                    ending.unlocked = ending_data.get("unlocked", False)
        
        if "active_romance" in data and data["active_romance"]:
            self.active_romance = data["active_romance"]
