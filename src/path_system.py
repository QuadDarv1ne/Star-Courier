# -*- coding: utf-8 -*-
"""
Star Courier - Path System
Система Путей: Альянс, Наблюдатель, Независимость
"""

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional

logger = logging.getLogger('path_system')


class PathType(Enum):
    """Типы Путей"""
    ALLIANCE = "alliance"       # Альянс - официальная поддержка
    OBSERVER = "observer"       # Наблюдатель - древние знания
    INDEPENDENCE = "independence"  # Независимость - свобода действий


@dataclass
class PathBonus:
    """Бонус Пути"""
    id: str
    name: str
    description: str
    effects: Dict[str, any] = field(default_factory=dict)
    unlock_chapter: int = 0


@dataclass
class Path:
    """Путь развития"""
    path_type: PathType
    name: str
    description: str
    bonuses: List[PathBonus] = field(default_factory=list)
    chosen: bool = False
    chapter_chosen: int = 0


class PathSystem:
    """Система Путей"""

    def __init__(self):
        self.current_path: Optional[Path] = None
        self.paths: Dict[PathType, Path] = {}
        self._init_paths()

    def _init_paths(self):
        """Инициализировать Пути"""

        # === ПУТЬ АЛЬЯНСА ===
        alliance_path = Path(
            path_type=PathType.ALLIANCE,
            name="Альянс",
            description="Официальная поддержка Объединённых Миров. Доступ к флоту, ресурсам и технологиям."
        )
        
        alliance_path.bonuses = [
            PathBonus(
                id="alliance_fleet",
                name="Поддержка Флота",
                description="Доступ к военным кораблям Альянса",
                effects={"fleet_support": True, "combat_advantage": 30},
                unlock_chapter=13
            ),
            PathBonus(
                id="alliance_resources",
                name="Ресурсы Альянса",
                description="Финансовая поддержка и оборудование",
                effects={"credit_bonus": 5000, "equipment_discount": 40},
                unlock_chapter=14
            ),
            PathBonus(
                id="alliance_united_front",
                name="Единый Фронт",
                description="Финальная поддержка в битве с Сущностью",
                effects={"final_battle_allies": "alliance_fleet", "exile_ending_boost": True},
                unlock_chapter=16
            )
        ]
        self.paths[PathType.ALLIANCE] = alliance_path

        # === ПУТЬ НАБЛЮДАТЕЛЯ ===
        observer_path = Path(
            path_type=PathType.OBSERVER,
            name="Наблюдатель",
            description="Древние знания Ордена. Усиление Psychic и доступ к тайнам Хранителей."
        )
        
        observer_path.bonuses = [
            PathBonus(
                id="observer_knowledge",
                name="Древние Знания",
                description="Доступ к архивам Ордена Наблюдателей",
                effects={"lore_unlock": True, "psychic_boost": 20},
                unlock_chapter=13
            ),
            PathBonus(
                id="observer_resonance",
                name="Обучение Резонансу",
                description="Ускоренное развитие резонанса",
                effects={"resonance_level_boost": 2, "anomaly_mastery": True},
                unlock_chapter=14
            ),
            PathBonus(
                id="order_blessing",
                name="Благословение Ордена",
                description="Финальная поддержка рыцарей Ордена",
                effects={"final_battle_allies": "knights_of_order", "treaty_ending_knowledge": True},
                unlock_chapter=16
            )
        ]
        self.paths[PathType.OBSERVER] = observer_path

        # === ПУТЬ НЕЗАВИСИМОСТИ ===
        independence_path = Path(
            path_type=PathType.INDEPENDENCE,
            name="Независимость",
            description="Свобода действий. Сеть независимых агентов и наёмников."
        )
        
        independence_path.bonuses = [
            PathBonus(
                id="independence_network",
                name="Сеть Независимых",
                description="Доступ к сети агентов Волкова",
                effects={"intel_bonus": True, "smuggler_routes": True},
                unlock_chapter=13
            ),
            PathBonus(
                id="freedom_fighters",
                name="Бойцы Свободы",
                description="Привлечение наёмников и независимых капитанов",
                effects={"mercenary_discount": 50, "unique_contracts": True},
                unlock_chapter=14
            ),
            PathBonus(
                id="independent_fleet",
                name="Независимый Флот",
                description="Собственная флотилия независимых кораблей",
                effects={"final_battle_allies": "independent_squadron", "freedom_ending": True},
                unlock_chapter=16
            )
        ]
        self.paths[PathType.INDEPENDENCE] = independence_path

    def choose_path(self, path_type: PathType, chapter: int = 13) -> bool:
        """Выбрать Путь"""
        if self.current_path and self.current_path.chosen:
            logger.warning("Путь уже выбран!")
            return False

        path = self.paths.get(path_type)
        if not path:
            logger.error(f"Путь не найден: {path_type}")
            return False

        self.current_path = path
        path.chosen = True
        path.chapter_chosen = chapter
        
        logger.info(f"Выбран Путь: {path.name}")
        return True

    def get_current_path(self) -> Optional[Path]:
        """Получить текущий Путь"""
        return self.current_path

    def get_path_type(self) -> Optional[PathType]:
        """Получить тип текущего Пути"""
        return self.current_path.path_type if self.current_path else None

    def get_active_bonuses(self, current_chapter: int) -> List[PathBonus]:
        """Получить активные бонусы"""
        if not self.current_path:
            return []

        return [b for b in self.current_path.bonuses if b.unlock_chapter <= current_chapter]

    def has_bonus(self, bonus_id: str) -> bool:
        """Проверить наличие бонуса"""
        if not self.current_path:
            return False

        return any(b.id == bonus_id for b in self.current_path.bonuses)

    def get_effect_value(self, effect_name: str, default=0):
        """Получить значение эффекта от активных бонусов"""
        if not self.current_path:
            return default

        for bonus in self.get_active_bonuses(99):  # 99 = все главы
            if effect_name in bonus.effects:
                return bonus.effects[effect_name]
        
        return default

    def get_path_bonuses_dict(self) -> Dict[str, any]:
        """Получить все бонусы как словарь"""
        if not self.current_path:
            return {}

        result = {}
        for bonus in self.get_active_bonuses(99):
            result.update(bonus.effects)
        
        return result

    def can_choose_path(self) -> bool:
        """Можно ли выбрать Путь"""
        return not (self.current_path and self.current_path.chosen)

    def get_available_paths(self) -> List[PathType]:
        """Получить доступные Пути"""
        return list(self.paths.keys())

    def get_path_description(self, path_type: PathType) -> str:
        """Получить описание Пути"""
        path = self.paths.get(path_type)
        return path.description if path else ""

    def to_dict(self) -> dict:
        """Сериализация в словарь"""
        return {
            "current_path": self.current_path.path_type.value if self.current_path else None,
            "chosen": self.current_path.chosen if self.current_path else False,
            "chapter_chosen": self.current_path.chapter_chosen if self.current_path else 0
        }

    def from_dict(self, data: dict):
        """Десериализация из словаря"""
        if "current_path" in data and data["current_path"]:
            path_type = PathType(data["current_path"])
            self.current_path = self.paths.get(path_type)
        if "chosen" in data:
            if self.current_path:
                self.current_path.chosen = data["chosen"]
        if "chapter_chosen" in data:
            if self.current_path:
                self.current_path.chapter_chosen = data["chapter_chosen"]

    def get_status_display(self) -> str:
        """Получить отображение статуса"""
        if not self.current_path or not self.current_path.chosen:
            return "Путь не выбран"
        return f"Путь: {self.current_path.name}"
