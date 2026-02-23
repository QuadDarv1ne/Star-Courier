"""
Система квестов и заданий
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Callable
from enum import Enum
from datetime import datetime


class QuestType(Enum):
    """Типы квестов"""
    MAIN = "main"          # Основной сюжет
    SIDE = "side"          # Побочный
    COMMISSION = "commission"  # Заказ
    EXPLORATION = "exploration"  # Исследование
    COMBAT = "combat"      # Боевое задание
    DELIVERY = "delivery"  # Доставка
    RESEARCH = "research"  # Исследование


class QuestState(Enum):
    """Состояния квеста"""
    AVAILABLE = "available"    # Доступен для взятия
    ACTIVE = "active"          # Выполняется
    COMPLETED = "completed"    # Выполнен
    FAILED = "failed"          # Провален
    EXPIRED = "expired"        # Истёк срок


class ObjectiveType(Enum):
    """Типы целей"""
    KILL = "kill"              # Убить
    COLLECT = "collect"        # Собрать
    DELIVER = "deliver"        # Доставить
    TALK = "talk"              # Поговорить
    EXPLORE = "explore"        # Исследовать
    USE_ITEM = "use_item"      # Использовать предмет
    REACH_LEVEL = "reach_level"  # Достичь уровня
    MAKE_CHOICE = "make_choice"  # Сделать выбор


@dataclass
class Objective:
    """Цель квеста"""
    id: str
    type: ObjectiveType
    description: str
    target_id: str = ""       # ID цели (NPC, предмет, локация)
    required: int = 1         # Требуемое количество
    current: int = 0          # Текущий прогресс
    is_completed: bool = False
    is_optional: bool = False  # Необязательная цель
    
    def update(self, amount: int = 1):
        """Обновить прогресс"""
        self.current += amount
        if self.current >= self.required:
            self.is_completed = True
    
    def get_progress_percent(self) -> float:
        """Получить прогресс в процентах"""
        if self.required <= 0:
            return 100.0
        return min(100.0, (self.current / self.required) * 100)
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "type": self.type.value,
            "description": self.description,
            "target_id": self.target_id,
            "required": self.required,
            "current": self.current,
            "is_completed": self.is_completed,
            "is_optional": self.is_optional,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Objective":
        return cls(**data)


@dataclass
class QuestReward:
    """Награда за квест"""
    credits: int = 0
    experience: int = 0
    items: List[Dict[str, int]] = field(default_factory=list)  # [{item_id: quantity}]
    relationship_changes: Dict[str, int] = field(default_factory=dict)  # {char_id: amount}
    unlocks: List[str] = field(default_factory=list)  # Разблокировки
    achievements: List[str] = field(default_factory=list)  # Достижения


@dataclass
class Quest:
    """Квест"""
    id: str
    title: str
    description: str
    quest_type: QuestType
    state: QuestState = QuestState.AVAILABLE
    
    # Контент
    giver: str = ""           # Кто выдаёт
    objectives: List[Objective] = field(default_factory=list)
    reward: QuestReward = field(default_factory=QuestReward)
    
    # Мета
    level_requirement: int = 0
    time_limit: int = 0       # В секундах (0 = без лимита)
    prerequisites: List[str] = field(default_factory=list)  # Требуемые квесты
    
    # Текст
    journal_entry: str = ""   # Запись в журнале
    completion_text: str = "" # Текст при завершении
    
    # Даты
    date_accepted: Optional[str] = None
    date_completed: Optional[str] = None
    
    def add_objective(self, objective: Objective):
        """Добавить цель"""
        self.objectives.append(objective)
    
    def is_available(self, completed_quests: List[str], player_level: int = 0) -> bool:
        """Проверить доступность квеста"""
        if self.state != QuestState.AVAILABLE:
            return False
        if player_level < self.level_requirement:
            return False
        for prereq in self.prerequisites:
            if prereq not in completed_quests:
                return False
        return True
    
    def can_complete(self) -> bool:
        """Проверить, можно ли завершить квест"""
        if self.state != QuestState.ACTIVE:
            return False
        # Все обязательные цели выполнены
        required_objectives = [o for o in self.objectives if not o.is_optional]
        return all(o.is_completed for o in required_objectives)
    
    def update_objective(self, objective_id: str, amount: int = 1):
        """Обновить цель"""
        for obj in self.objectives:
            if obj.id == objective_id and not obj.is_completed:
                obj.update(amount)
    
    def get_progress(self) -> tuple:
        """Получить прогресс (выполнено, всего)"""
        total = len([o for o in self.objectives if not o.is_optional])
        completed = len([o for o in self.objectives 
                        if (not o.is_optional and o.is_completed)])
        return completed, total
    
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "quest_type": self.quest_type.value,
            "state": self.state.value,
            "giver": self.giver,
            "objectives": [o.to_dict() for o in self.objectives],
            "reward": {
                "credits": self.reward.credits,
                "experience": self.reward.experience,
                "items": self.reward.items,
                "relationship_changes": self.reward.relationship_changes,
                "unlocks": self.reward.unlocks,
                "achievements": self.reward.achievements,
            },
            "level_requirement": self.level_requirement,
            "time_limit": self.time_limit,
            "prerequisites": self.prerequisites,
            "journal_entry": self.journal_entry,
            "completion_text": self.completion_text,
            "date_accepted": self.date_accepted,
            "date_completed": self.date_completed,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Quest":
        quest = cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            quest_type=QuestType(data["quest_type"]),
            state=QuestState(data["state"]),
            giver=data.get("giver", ""),
            level_requirement=data.get("level_requirement", 0),
            time_limit=data.get("time_limit", 0),
            prerequisites=data.get("prerequisites", []),
            journal_entry=data.get("journal_entry", ""),
            completion_text=data.get("completion_text", ""),
            date_accepted=data.get("date_accepted"),
            date_completed=data.get("date_completed"),
        )
        
        # Цели
        for obj_data in data.get("objectives", []):
            quest.objectives.append(Objective.from_dict(obj_data))
        
        # Награда
        reward_data = data.get("reward", {})
        quest.reward = QuestReward(
            credits=reward_data.get("credits", 0),
            experience=reward_data.get("experience", 0),
            items=reward_data.get("items", []),
            relationship_changes=reward_data.get("relationship_changes", {}),
            unlocks=reward_data.get("unlocks", []),
            achievements=reward_data.get("achievements", []),
        )
        
        return quest


class QuestManager:
    """Менеджер квестов"""
    
    def __init__(self):
        self.quests: Dict[str, Quest] = {}
        self.active_quests: Dict[str, Quest] = {}
        self.completed_quests: List[str] = []
        self.failed_quests: List[str] = []
        self._init_default_quests()
    
    def _init_default_quests(self):
        """Инициализировать базовые квесты"""
        
        # === ГЛАВНЫЙ КВЕСТ ===
        main_quest = Quest(
            id="main_001",
            title="Доставка артефакта",
            description="Доставить загадочный артефакт на станцию Орбис-9.",
            quest_type=QuestType.MAIN,
            state=QuestState.ACTIVE,
            giver="Командование флота",
            journal_entry="Артефакт неизвестного происхождения должен быть "
                         "доставлен на исследовательскую станцию Орбис-9.",
            completion_text="Артефакт успешно доставлен. Командование довольно."
        )
        
        main_quest.add_objective(Objective(
            id="obj_deliver",
            type=ObjectiveType.DELIVER,
            description="Доставить артефакт на Орбис-9",
            target_id="main_artifact",
            required=1,
            is_completed=False
        ))
        
        main_quest.reward = QuestReward(
            credits=5000,
            experience=1000,
            unlocks=["chapter_2"],
            achievements=["first_delivery"]
        )
        
        self.quests["main_001"] = main_quest
        self.active_quests["main_001"] = main_quest
        
        # === ПОБОЧНЫЙ: Саботаж ===
        sabotage_quest = Quest(
            id="side_001",
            title="Внутренний враг",
            description="Выяснить, кто саботирует системы корабля.",
            quest_type=QuestType.SIDE,
            state=QuestState.ACTIVE,
            giver="Алия'Наар",
            journal_entry="Кто-то на корабле намеренно выводит из строя системы. "
                         "Нужно найти предателя до того, как станет слишком поздно.",
        )
        
        sabotage_quest.add_objective(Objective(
            id="obj_investigate",
            type=ObjectiveType.EXPLORE,
            description="Исследовать технический отсек",
            target_id="engineering_bay",
            required=1,
            is_completed=False
        ))
        
        sabotage_quest.add_objective(Objective(
            id="obj_evidence",
            type=ObjectiveType.COLLECT,
            description="Собрать улики",
            required=3,
            current=0,
            is_completed=False
        ))
        
        sabotage_quest.add_objective(Objective(
            id="obj_confront",
            type=ObjectiveType.TALK,
            description="Обличить предателя",
            target_id="traitor",
            required=1,
            is_completed=False,
            is_optional=True  # Необязательно для сюжета
        ))
        
        sabotage_quest.reward = QuestReward(
            credits=1000,
            experience=300,
            relationship_changes={"alia_naar": 15, "nadezhda": 10},
            items=[{"energy_cell": 5}]
        )
        
        self.quests["side_001"] = sabotage_quest
        self.active_quests["side_001"] = sabotage_quest
        
        # === ПОБОЧНЫЙ: Пиратские переговоры ===
        pirate_quest = Quest(
            id="side_002",
            title="Непростой союз",
            description="Решить, как поступить с предложением пиратов.",
            quest_type=QuestType.SIDE,
            state=QuestState.AVAILABLE,
            giver="Селена Ро",
            prerequisites=["main_001"],  # Доступен после начала главного
            journal_entry="Пиратский капитан Селена Ро предложила союз. "
                         "Можно принять, отвергнуть или найти третий путь.",
        )
        
        pirate_quest.add_objective(Objective(
            id="obj_decide",
            type=ObjectiveType.MAKE_CHOICE,
            description="Принять решение по предложению пиратов",
            required=1,
            is_completed=False
        ))
        
        pirate_quest.reward = QuestReward(
            credits=500,
            experience=100,
            relationship_changes={"selena_ro": 20},
        )
        
        self.quests["side_002"] = pirate_quest
        
        # === ИССЛЕДОВАНИЕ: Артефакт ===
        research_quest = Quest(
            id="research_001",
            title="Тайны артефакта",
            description="Помочь Ирине изучить свойства артефакта.",
            quest_type=QuestType.RESEARCH,
            state=QuestState.AVAILABLE,
            giver="Ирина Лебедева",
            journal_entry="Артефакт излучает неизвестную энергию. "
                         "Ирина просит помочь со сборами данных.",
        )
        
        research_quest.add_objective(Objective(
            id="obj_scan",
            type=ObjectiveType.USE_ITEM,
            description="Провести сканирование артефакта",
            target_id="main_artifact",
            required=5,
            current=0,
            is_completed=False
        ))
        
        research_quest.add_objective(Objective(
            id="obj_analyze",
            type=ObjectiveType.COLLECT,
            description="Собрать образцы энергии",
            required=3,
            current=0,
            is_completed=False
        ))
        
        research_quest.reward = QuestReward(
            credits=800,
            experience=250,
            relationship_changes={"irina_lebedeva": 20},
            items=[{"psychic_amplifier": 2}],
            unlocks=["psychic_ability_basic"]
        )
        
        self.quests["research_001"] = research_quest
        
        # === БОЕВОЙ: Защита корабля ===
        defense_quest = Quest(
            id="combat_001",
            title="Отражение атаки",
            description="Защитить корабль от абордажной команды.",
            quest_type=QuestType.COMBAT,
            state=QuestState.AVAILABLE,
            giver="Надежда",
            journal_entry="Пираты пытаются захватить корабль. "
                         "Нужно отразить атаку любой ценой.",
        )
        
        defense_quest.add_objective(Objective(
            id="obj_defend",
            type=ObjectiveType.KILL,
            description="Отразить атакующих",
            required=5,
            current=0,
            is_completed=False
        ))
        
        defense_quest.add_objective(Objective(
            id="obj_secure",
            type=ObjectiveType.EXPLORE,
            description="Обеспечить безопасность мостика",
            required=1,
            is_completed=False
        ))
        
        defense_quest.reward = QuestReward(
            credits=1500,
            experience=500,
            relationship_changes={"nadezhda": 15},
            items=[{"plasma_pistol": 1}],
            achievements=["ship_defender"]
        )
        
        self.quests["combat_001"] = defense_quest
    
    def add_quest(self, quest: Quest):
        """Добавить квест"""
        self.quests[quest.id] = quest
    
    def get_quest(self, quest_id: str) -> Optional[Quest]:
        """Получить квест по ID"""
        return self.quests.get(quest_id)
    
    def accept_quest(self, quest_id: str) -> bool:
        """Принять квест"""
        quest = self.get_quest(quest_id)
        if not quest:
            return False
        
        if not quest.is_available(self.completed_quests):
            return False
        
        quest.state = QuestState.ACTIVE
        quest.date_accepted = datetime.now().isoformat()
        self.active_quests[quest_id] = quest
        
        return True
    
    def complete_quest(self, quest_id: str) -> Optional[QuestReward]:
        """
        Завершить квест.
        Возвращает награду если успешно.
        """
        quest = self.active_quests.get(quest_id)
        if not quest:
            return None
        
        if not quest.can_complete():
            return None
        
        quest.state = QuestState.COMPLETED
        quest.date_completed = datetime.now().isoformat()
        
        reward = quest.reward
        self.completed_quests.append(quest_id)
        del self.active_quests[quest_id]
        
        return reward
    
    def fail_quest(self, quest_id: str):
        """Провалить квест"""
        quest = self.active_quests.get(quest_id)
        if quest:
            quest.state = QuestState.FAILED
            self.failed_quests.append(quest_id)
            del self.active_quests[quest_id]
    
    def update_objective(self, quest_id: str, objective_id: str, amount: int = 1):
        """Обновить цель квеста"""
        quest = self.active_quests.get(quest_id)
        if quest:
            quest.update_objective(objective_id, amount)
    
    def get_active_quests(self) -> List[Quest]:
        """Получить активные квесты"""
        return list(self.active_quests.values())
    
    def get_available_quests(self, player_level: int = 0) -> List[Quest]:
        """Получить доступные квесты для принятия"""
        available = []
        for quest in self.quests.values():
            if quest.is_available(self.completed_quests, player_level):
                available.append(quest)
        return available
    
    def get_completed_quests(self) -> List[str]:
        """Получить список завершённых квестов"""
        return self.completed_quests.copy()
    
    def has_completed(self, quest_id: str) -> bool:
        """Проверить, завершён ли квест"""
        return quest_id in self.completed_quests
    
    def get_quest_progress(self, quest_id: str) -> Optional[str]:
        """Получить строку прогресса квеста"""
        quest = self.active_quests.get(quest_id)
        if not quest:
            return None
        
        completed, total = quest.get_progress()
        return f"{completed}/{total}"
    
    def to_dict(self) -> dict:
        """Сериализация"""
        return {
            "quests": {k: v.to_dict() for k, v in self.quests.items()},
            "active": list(self.active_quests.keys()),
            "completed": self.completed_quests,
            "failed": self.failed_quests,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "QuestManager":
        """Десериализация"""
        manager = cls()
        
        # Очищаем дефолтные квесты
        manager.quests = {}
        manager.active_quests = {}
        
        # Загружаем квесты
        for quest_id, quest_data in data.get("quests", {}).items():
            quest = Quest.from_dict(quest_data)
            manager.quests[quest_id] = quest
            
            if quest.state == QuestState.ACTIVE:
                manager.active_quests[quest_id] = quest
        
        manager.completed_quests = data.get("completed", [])
        manager.failed_quests = data.get("failed", [])
        
        return manager
