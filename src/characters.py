"""
Модуль персонажей и системы отношений
"""

from dataclasses import dataclass, field
from typing import Dict, Optional
from enum import Enum


class Role(Enum):
    """Роли персонажей в экипаже"""
    CAPTAIN = "Капитан"
    PILOT = "Пилот"
    ENGINEER = "Инженер"
    SCIENTIST = "Учёный"
    SECURITY = "Офицер безопасности"
    NAVIGATOR = "Навигатор"
    MEDIC = "Медик"
    AI = "ИИ корабля"
    HACKER = "Специалист по кибербезопасности"
    COMMUNICATIONS = "Офицер связи"
    MECHANIC = "Механик"


@dataclass
class Character:
    """Базовый класс персонажа"""
    id: str
    name: str
    role: Role
    bio: str = ""
    appearance: str = ""
    personality: str = ""
    motivation: str = ""
    
    # Отношения с игроком (0-100)
    relationship: int = 0
    
    # Статус в экипаже
    is_recruited: bool = True
    is_alive: bool = True
    
    def increase_relationship(self, amount: int) -> int:
        """Увеличить отношение на amount, вернуть новое значение"""
        self.relationship = min(100, max(0, self.relationship + amount))
        return self.relationship
    
    def decrease_relationship(self, amount: int) -> int:
        """Уменьшить отношение на amount, вернуть новое значение"""
        self.relationship = min(100, max(0, self.relationship - amount))
        return self.relationship
    
    def get_relationship_status(self) -> str:
        """Получить статус отношений"""
        if self.relationship >= 80:
            return "Близкие"
        elif self.relationship >= 60:
            return "Дружеские"
        elif self.relationship >= 40:
            return "Профессиональные"
        elif self.relationship >= 20:
            return "Знакомые"
        else:
            return "Холодные"


class CrewManager:
    """Менеджер экипажа"""
    
    def __init__(self):
        self.crew: Dict[str, Character] = {}
        self._init_default_crew()
    
    def _init_default_crew(self):
        """Инициализировать базовый экипаж"""
        
        # Макс Велл - капитан
        self.add_character(Character(
            id="max_well",
            name="Макс Велл",
            role=Role.CAPTAIN,
            bio="Капитан звездолёта «Элея». Родился на космической колонии Земли. "
                "Закончил Академию Космических Исследований с отличием.",
            appearance="Высокий, атлетичного телосложения, тёмные волосы, зелёные глаза.",
            personality="Решительный, харизматичный, умеет слушать команду.",
            motivation="Успешно выполнить миссию и сохранить жизнь экипажа.",
            relationship=0  # Это сам игрок
        ))
        
        # Афина - ИИ
        self.add_character(Character(
            id="athena",
            name="Афина",
            role=Role.AI,
            bio="Искусственный интеллект корабля. Создана ведущей компанией ИИ.",
            appearance="Голографический образ в виде женского силуэта.",
            personality="Вежливая, интеллигентная, проявляет иронию и юмор.",
            motivation="Обеспечить безопасность корабля и команды."
        ))
        
        # Алия'Наар - пилот
        self.add_character(Character(
            id="alia_naar",
            name="Алия'Наар",
            role=Role.PILOT,
            bio="Родом с планеты с жесткими условиями. Опытный пилот и инженер.",
            appearance="Стройная, спортивная, светлые волосы, синие глаза.",
            personality="Хладнокровная, саркастичная, преданная экипажу.",
            motivation="Сохранить экипаж живым и доказать свою ценность."
        ))
        
        # Ирина Лебедева - учёный
        self.add_character(Character(
            id="irina_lebedeva",
            name="Ирина Лебедева",
            role=Role.SCIENTIST,
            bio="Учёная с мировым именем, специалист по энергетическим аномалиям.",
            appearance="Среднего роста, тёмные волосы, карие глаза.",
            personality="Вдумчивая, застенчивая, любознательная.",
            motivation="Раскрыть тайны артефакта."
        ))
        
        # Рина Мирай - навигатор
        self.add_character(Character(
            id="rina_mirai",
            name="Рина Мирай",
            role=Role.NAVIGATOR,
            bio="Происходит из семьи военных стратегов. Отличный тактик.",
            appearance="Рыжие волосы, зелёные глаза, носит AR-очки.",
            personality="Энергичная, решительная, остроумная.",
            motivation="Доказать ценность своих стратегических навыков."
        ))
        
        # Надежда - офицер безопасности
        self.add_character(Character(
            id="nadezhda",
            name="Надежда",
            role=Role.SECURITY,
            bio="Бывший военный с опытом полевых операций.",
            appearance="Крепкая, короткие русые волосы, серьёзный взгляд.",
            personality="Жёсткая, дисциплинированная, с кодексом чести.",
            motivation="Обеспечить безопасность экипажа."
        ))
        
        # Екатерина - кибербезопасность
        self.add_character(Character(
            id="ekaterina",
            name="Екатерина",
            role=Role.HACKER,
            bio="Талантливая хакерша из мегаполиса.",
            appearance="Невысокая, чёрная стрижка, голубые глаза.",
            personality="Добрая, застенчивая, перфекционист в работе.",
            motivation="Сделать вклад в миссию и доказать свою ценность."
        ))
    
    def add_character(self, character: Character):
        """Добавить персонажа в экипаж"""
        self.crew[character.id] = character
    
    def get_character(self, char_id: str) -> Optional[Character]:
        """Получить персонажа по ID"""
        return self.crew.get(char_id)
    
    def get_all_crew(self) -> list:
        """Получить всех членов экипажа"""
        return list(self.crew.values())
    
    def get_by_role(self, role: Role) -> list:
        """Получить персонажей по роли"""
        return [c for c in self.crew.values() if c.role == role]
    
    def get_highest_relationship(self) -> Optional[Character]:
        """Получить персонажа с наивысшими отношениями"""
        crew_without_player = [c for c in self.crew.values() if c.role != Role.CAPTAIN]
        if not crew_without_player:
            return None
        return max(crew_without_player, key=lambda c: c.relationship)
