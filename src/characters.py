"""
Модуль персонажей и системы отношений
"""

import logging
from dataclasses import dataclass, field
from typing import Dict, Optional
from enum import Enum

logger = logging.getLogger('characters')

try:
    from .config import MAX_RELATIONSHIP, MIN_RELATIONSHIP
except ImportError:
    from config import MAX_RELATIONSHIP, MIN_RELATIONSHIP


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
    MERCHANT = "Торговец"
    MERCENARY = "Наёмник"
    INFORMANT = "Информатор"
    KNIGHT = "Рыцарь Ордена"
    CAPTAIN_NPC = "Капитан"
    SCIENTIST_NPC = "Учёный"


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

    # Доверие в критических ситуациях (0-100)
    trust: int = 50

    # Статус в экипаже
    is_recruited: bool = True
    is_alive: bool = True

    # Личный квест
    personal_quest_id: Optional[str] = None
    personal_quest_completed: bool = False

    # === НОВЫЕ МЕХАНИКИ для глав 11-18 ===
    # Уровень Резонанса (1-4)
    resonance_level: int = 1
    
    # Выбранный путь: "alliance", "observer", "independence", None
    path: Optional[str] = None
    
    # Ментальное состояние (0-100, 100 = идеально)
    mental_health: int = 100
    
    # Влияние Сущности (0-100, 0 = чист)
    entity_influence: int = 0
    
    # Доступные концовки
    ending_available: list = field(default_factory=lambda: ["exile"])
    
    # Навыки для глав 6-18
    alchemy_level: int = 0
    biotics_level: int = 0
    psychic_level: int = 0
    hacking_level: int = 0
    empathy_level: int = 0
    determination_level: int = 0
    knowledge_level: int = 0
    
    def change_relationship(self, amount: int) -> int:
        """Изменить отношение на amount (может быть положительным или отрицательным)"""
        self.relationship = min(MAX_RELATIONSHIP, max(MIN_RELATIONSHIP, self.relationship + amount))
        return self.relationship
    
    def change_trust(self, amount: int) -> int:
        """Изменить доверие на amount"""
        self.trust = min(MAX_RELATIONSHIP, max(MIN_RELATIONSHIP, self.trust + amount))
        return self.trust
    
    def is_loyal(self) -> bool:
        """Проверить лояльность (доверие + отношения)"""
        return (self.relationship + self.trust) >= 100
    
    def can_betray(self) -> bool:
        """Проверить возможность предательства"""
        return self.trust < 30 and self.relationship < 40
    
    def start_personal_quest(self, quest_id: str):
        """Начать личный квест"""
        self.personal_quest_id = quest_id
        self.personal_quest_completed = False
    
    def complete_personal_quest(self):
        """Завершить личный квест"""
        self.personal_quest_completed = True
        self.change_trust(20)
        self.change_relationship(15)
    
    def get_relationship_status(self) -> str:
        """Получить статус отношений"""
        thresholds = [(80, "Близкие"), (60, "Дружеские"), (40, "Профессиональные"), (20, "Знакомые")]
        for threshold, status in thresholds:
            if self.relationship >= threshold:
                return status
        return "Холодные"
    
    def get_trust_level(self) -> str:
        """Получить уровень доверия"""
        if self.trust >= 80:
            return "Абсолютное"
        elif self.trust >= 60:
            return "Высокое"
        elif self.trust >= 40:
            return "Среднее"
        elif self.trust >= 20:
            return "Низкое"
        return "Отсутствует"
    
    def get_summary(self) -> str:
        """Получить краткую сводку о персонаже"""
        return f"{self.name} ({self.role.value}): {self.get_relationship_status()}, доверие: {self.get_trust_level()}"


class CrewManager:
    """Менеджер экипажа"""

    def __init__(self):
        self.crew: Dict[str, Character] = {}
        self._init_default_crew()

    def _add_crew(self, id: str, name: str, role: Role, bio: str = "",
                  appearance: str = "", personality: str = "", motivation: str = "",
                  relationship: int = 0, path: Optional[str] = None):
        """Вспомогательный метод для добавления персонажа"""
        self.crew[id] = Character(
            id=id, name=name, role=role, bio=bio, appearance=appearance,
            personality=personality, motivation=motivation, relationship=relationship,
            path=path
        )

    def _init_default_crew(self):
        """Инициализировать базовый экипаж"""
        self._add_crew(
            id="max_well", name="Макс Велл", role=Role.CAPTAIN,
            bio="Капитан звездолёта «Элея». Родился на космической колонии Земли. "
                "Закончил Академию Космических Исследований с отличием.",
            appearance="Высокий, атлетичного телосложения, тёмные волосы, зелёные глаза.",
            personality="Решительный, харизматичный, умеет слушать команду.",
            motivation="Успешно выполнить миссию и сохранить жизнь экипажа."
        )
        self._add_crew(
            id="athena", name="Афина", role=Role.AI,
            bio="Искусственный интеллект корабля. Создана ведущей компанией ИИ.",
            appearance="Голографический образ в виде женского силуэта.",
            personality="Вежливая, интеллигентная, проявляет иронию и юмор.",
            motivation="Обеспечить безопасность корабля и команды."
        )
        self._add_crew(
            id="alia_naar", name="Алия'Наар", role=Role.PILOT,
            bio="Родом с планеты с жесткими условиями. Опытный пилот и инженер.",
            appearance="Стройная, спортивная, светлые волосы, синие глаза.",
            personality="Хладнокровная, саркастичная, преданная экипажу.",
            motivation="Сохранить экипаж живым и доказать свою ценность."
        )
        self._add_crew(
            id="irina_lebedeva", name="Ирина Лебедева", role=Role.SCIENTIST,
            bio="Учёная с мировым именем, специалист по энергетическим аномалиям.",
            appearance="Среднего роста, тёмные волосы, карие глаза.",
            personality="Вдумчивая, застенчивая, любознательная.",
            motivation="Раскрыть тайны артефакта."
        )
        self._add_crew(
            id="rina_mirai", name="Рина Мирай", role=Role.NAVIGATOR,
            bio="Происходит из семьи военных стратегов. Отличный тактик.",
            appearance="Рыжие волосы, зелёные глаза, носит AR-очки.",
            personality="Энергичная, решительная, остроумная.",
            motivation="Доказать ценность своих стратегических навыков."
        )
        self._add_crew(
            id="nadezhda", name="Надежда", role=Role.SECURITY,
            bio="Бывший военный с опытом полевых операций.",
            appearance="Крепкая, короткие русые волосы, серьёзный взгляд.",
            personality="Жёсткая, дисциплинированная, с кодексом чести.",
            motivation="Обеспечить безопасность экипажа."
        )
        self._add_crew(
            id="ekaterina", name="Екатерина", role=Role.HACKER,
            bio="Талантливая хакерша из мегаполиса.",
            appearance="Невысокая, чёрная стрижка, голубые глаза.",
            personality="Добрая, застенчивая, перфекционист в работе.",
            motivation="Сделать вклад в миссию и доказать свою ценность."
        )

        # === НОВЫЕ ПЕРСОНАЖИ: Основной экипаж (романтические интересы) ===
        self._add_crew(
            id="mia", name="Мия", role=Role.SECURITY,
            bio="Тактик с исключительными аналитическими способностями. "
                "Специализируется на стратегическом планировании и разведке.",
            appearance="Стройная, короткие тёмные волосы, проницательный взгляд.",
            personality="Аналитичная, сдержанная, преданная делу.",
            motivation="Защитить экипаж через стратегическое превосходство.",
            relationship=25
        )
        self._add_crew(
            id="maria", name="Мария", role=Role.MEDIC,
            bio="Главный медик корабля. Специалист по ксенобиологии и экстренной медицине.",
            appearance="Среднего роста, длинные каштановые волосы, тёплые карие глаза.",
            personality="Заботливая, терпеливая, эмпатичная.",
            motivation="Сохранить жизнь каждому члену экипажа.",
            relationship=30
        )
        self._add_crew(
            id="anna", name="Анна", role=Role.NAVIGATOR,
            bio="Навигатор второго класса. Специализируется на аномальных зонах.",
            appearance="Высокая, светлые волосы до плеч, голубые глаза.",
            personality="Спокойная, интуитивная, мечтательная.",
            motivation="Найти безопасные пути через опасные регионы.",
            relationship=25
        )
        self._add_crew(
            id="sergey", name="Сергей", role=Role.ENGINEER,
            bio="Старший инженер. Эксперт по двигательным системам.",
            appearance="Крепкий, короткая стрижка, борода.",
            personality="Практичный, надёжный, немногословный.",
            motivation="Поддержать корабль в идеальном состоянии."
        )
        self._add_crew(
            id="dmitry", name="Дмитрий", role=Role.PILOT,
            bio="Второй пилот. Специализируется на экстремальных манёврах.",
            appearance="Среднего роста, тёмные волосы, спортивное телосложение.",
            personality="Азартный, уверенный, лояльный.",
            motivation="Доказать мастерство пилотирования."
        )

        # === КЛЮЧЕВЫЕ NPC (романтические интересы + пути) ===
        self._add_crew(
            id="veronika", name="Вероника", role=Role.INFORMANT,
            bio="Информатор из теневой сети. Знает секреты галактики.",
            appearance="Элегантная, чёрные волосы, пронзительные зелёные глаза.",
            personality="Хитрая, независимая, загадочная.",
            motivation="Выжить в опасном мире через информацию.",
            relationship=20,
            path="independence"
        )
        self._add_crew(
            id="zara", name="Зара", role=Role.MERCENARY,
            bio="Наёмник с тёмным прошлым. Боевой специалист.",
            appearance="Атлетичная, короткая стрижка, шрам на щеке.",
            personality="Жёсткая, прямая, с кодексом чести.",
            motivation="Найти искупление через службу.",
            relationship=15,
            path="observer"
        )
        self._add_crew(
            id="kira", name="Кира", role=Role.MERCENARY,
            bio="Курьер-наёмник. Специализируется на доставке артефактов.",
            appearance="Стройная, рыжие волосы, веснушки.",
            personality="Энергичная, оптимистичная, независимая.",
            motivation="Свобода путешествий по галактике.",
            relationship=20,
            path="independence"
        )

        # === КЛЮЧЕВЫЕ NPC (сюжетные) ===
        self._add_crew(
            id="rainer", name="Райнер", role=Role.MERCENARY,
            bio="Наёмник-ветеран. Работает на того, кто платит.",
            appearance="Массивный, лысый, бородатый.",
            personality="Циничный, профессиональный, надёжный в сделке.",
            motivation="Кредиты и выживание."
        )
        self._add_crew(
            id="volkov", name="Волков", role=Role.CAPTAIN_NPC,
            bio="Капитан торгового судна. Связи в криминальном мире.",
            appearance="Среднего возраста, усы, дорогая одежда.",
            personality="Хитрый, харизматичный, непредсказуемый.",
            motivation="Прибыль и влияние.",
            path="independence"
        )
        self._add_crew(
            id="marcus_ride", name="Маркус Рид", role=Role.MERCENARY,
            bio="Командир Альянса. Стратег с безупречной репутацией.",
            appearance="Высокий, седые виски, военная форма.",
            personality="Дисциплинированный, справедливый, патриот.",
            motivation="Служение Альянсу.",
            path="alliance"
        )
        self._add_crew(
            id="vera", name="Вера", role=Role.SCIENTIST_NPC,
            bio="Учёный-исследователь. Изучает Древние Цивилизации.",
            appearance="Пожилая, седые волосы, умные глаза.",
            personality="Мудрая, терпеливая, любопытная.",
            motivation="Понимание тайн вселенной."
        )
        self._add_crew(
            id="echo", name="Эхо", role=Role.AI,
            bio="Древний ИИ погибшей цивилизации. Голос в кристалле.",
            appearance="Голос без формы, иногда проявляется как свет.",
            personality="Загадочная, меланхоличная, всезнающая.",
            motivation="Передать знания выжившим."
        )
        self._add_crew(
            id="guardian", name="Страж Ядра", role=Role.KNIGHT,
            bio="Последний из Древних. Хранитель Ядра Реальности.",
            appearance="Светящаяся фигура, непостижимый облик.",
            personality="Беспристрастный, древний, мудрый.",
            motivation="Защитить Ядро от недостойных."
        )
    
    def add_character(self, character: Character):
        """Добавить персонажа в экипаж"""
        if character.id in self.crew:
            logger.warning(f"Персонаж уже существует: {character.id}")
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
        return max(
            (c for c in self.crew.values() if c.role != Role.CAPTAIN),
            key=lambda c: c.relationship,
            default=None
        )
    
    def get_most_loyal(self) -> Optional[Character]:
        """Получить самого лояльного персонажа"""
        crew_without_captain = [c for c in self.crew.values() if c.role != Role.CAPTAIN]
        if not crew_without_captain:
            return None
        return max(crew_without_captain, key=lambda c: c.relationship + c.trust)
    
    def get_potential_traitors(self) -> list:
        """Получить персонажей, которые могут предать"""
        return [c for c in self.crew.values() if c.can_betray()]
