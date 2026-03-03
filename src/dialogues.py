"""
Диалоговая система с выборами и развилками сюжета
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Callable
from enum import Enum


class ChoiceEffect(Enum):
    """Тип эффекта выбора"""
    NONE = "none"
    RELATIONSHIP_UP = "relationship_up"
    RELATIONSHIP_DOWN = "relationship_down"
    STAT_CHANGE = "stat_change"
    STORY_BRANCH = "story_branch"
    ITEM_GAIN = "item_gain"
    QUEST_COMPLETE = "quest_complete"


@dataclass
class Choice:
    """Вариант выбора в диалоге"""
    id: str
    text: str
    next_node: str
    effect: ChoiceEffect = ChoiceEffect.NONE
    effect_value: any = None
    required_stat: Optional[Dict[str, int]] = None  # Требуемые статы
    required_item: Optional[str] = None  # Требуемый предмет
    
    def is_available(self, player_stats: dict, player_items: list) -> bool:
        """Проверить, доступен ли выбор"""
        if self.required_stat:
            for stat, value in self.required_stat.items():
                if player_stats.get(stat, 0) < value:
                    return False
        if self.required_item and self.required_item not in player_items:
            return False
        return True


@dataclass
class DialogueNode:
    """Узел диалога"""
    id: str
    speaker: str
    text: str
    choices: List[Choice] = field(default_factory=list)
    is_end: bool = False
    
    # Эффекты при входе в узел
    on_enter: Optional[Callable] = None


@dataclass
class Dialogue:
    """Диалог — коллекция узлов"""
    id: str
    title: str
    nodes: Dict[str, DialogueNode] = field(default_factory=dict)
    start_node: str = "start"
    
    def add_node(self, node: DialogueNode):
        """Добавить узел диалога"""
        self.nodes[node.id] = node
    
    def get_node(self, node_id: str) -> Optional[DialogueNode]:
        """Получить узел по ID"""
        return self.nodes.get(node_id)


class DialogueManager:
    """Менеджер диалогов"""
    
    def __init__(self):
        self.dialogues: Dict[str, Dialogue] = {}
        self.current_dialogue: Optional[Dialogue] = None
        self.current_node: Optional[DialogueNode] = None
        self.history: List[str] = []  # История выборов
    
    def add_dialogue(self, dialogue: Dialogue):
        """Добавить диалог"""
        self.dialogues[dialogue.id] = dialogue
    
    def start_dialogue(self, dialogue_id: str) -> bool:
        """Начать диалог"""
        dialogue = self.dialogues.get(dialogue_id)
        if not dialogue:
            return False
        
        self.current_dialogue = dialogue
        self.current_node = dialogue.get_node(dialogue.start_node)
        self.history = []
        return True
    
    def get_current_text(self) -> Optional[str]:
        """Получить текущий текст диалога"""
        if not self.current_node:
            return None
        return f"{self.current_node.speaker}: {self.current_node.text}"
    
    def get_available_choices(self, player_stats: dict = None, 
                               player_items: list = None) -> List[Choice]:
        """Получить доступные выборы"""
        if not self.current_node:
            return []
        
        player_stats = player_stats or {}
        player_items = player_items or []
        
        return [c for c in self.current_node.choices 
                if c.is_available(player_stats, player_items)]
    
    def make_choice(self, choice_id: str) -> Optional[DialogueNode]:
        """Сделать выбор"""
        if not self.current_node:
            return None
        
        choice = next((c for c in self.current_node.choices if c.id == choice_id), None)
        
        if not choice:
            return None
        
        self.history.append(choice_id)
        self.current_node = self.current_dialogue.get_node(choice.next_node)
        
        # Выполнить эффект при входе
        if self.current_node and self.current_node.on_enter:
            self.current_node.on_enter()
        
        return self.current_node
    
    def is_finished(self) -> bool:
        """Закончен ли диалог"""
        if not self.current_node:
            return True
        return self.current_node.is_end
    
    def get_history(self) -> List[str]:
        """Получить историю выборов"""
        return self.history.copy()


# === Примеры диалогов для первой главы ===

def create_chapter1_dialogues() -> Dict[str, Dialogue]:
    """Создать диалоги для первой главы"""
    dialogues = {}

    # === Диалог: Утренний брифинг ===
    morning_briefing = Dialogue(
        id="morning_briefing",
        title="Утренний брифинг",
        start_node="start"
    )

    morning_briefing.add_node(DialogueNode(
        id="start",
        speaker="Афина",
        text="Доброе утро, капитан. Погода в каюте — комфортная. "
             "Время 06:30 по звездному времени. Сегодня предстоит важный день.",
        choices=[
            Choice("ask", "Как обстановка?", "ask_status")
        ]
    ))

    morning_briefing.add_node(DialogueNode(
        id="ask_status",
        speaker="Макс",
        text="Спасибо, Афина. Как обстановка на корабле?",
        choices=[
            Choice("listen", "Слушаю", "athena_report")
        ]
    ))

    morning_briefing.add_node(DialogueNode(
        id="athena_report",
        speaker="Афина",
        text="Всё стабильно. Показатели систем в норме, но несколько "
             "предупреждений по охлаждению в техническом отсеке. "
             "Пилот Алия'Наар проводит профилактическую проверку.",
        choices=[
            Choice("wait", "Ждём Алию", "alia_enters")
        ]
    ))

    morning_briefing.add_node(DialogueNode(
        id="alia_enters",
        speaker="Алия",
        text="Доброе утро, капитан. Всё под контролем. Да, есть небольшие "
             "отклонения в системе охлаждения — ничего критичного, "
             "но нужно уделить внимание.",
        choices=[
            Choice("order", "Приказать диагностику", "max_decision"),
            Choice("trust", "Довериться Алие", "max_decision",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 5))
        ]
    ))

    morning_briefing.add_node(DialogueNode(
        id="max_decision",
        speaker="Макс",
        text="Хорошо, пусть инженеры проведут полную диагностику. "
             "Не хочу сюрпризов в полёте.",
        is_end=True
    ))

    dialogues["morning_briefing"] = morning_briefing
    
    # === Диалог: Первый контакт с пиратами ===
    pirate_contact = Dialogue(
        id="pirate_contact",
        title="Первый контакт с пиратами",
        start_node="start"
    )
    
    pirate_contact.add_node(DialogueNode(
        id="start",
        speaker="Селена Ро",
        text="Капитан Велл, у нас есть общее дело. Ваш артефакт "
             "заинтересовал многих. Может, обсудим условия, прежде чем станем врагами?"
    ))
    
    pirate_contact.add_node(DialogueNode(
        id="refuse",
        speaker="Макс",
        text="Селена, этот груз — под защитой флота. Предлагаю вам "
             "не вмешиваться в наши дела."
    ))
    
    pirate_contact.add_node(DialogueNode(
        id="negotiate",
        speaker="Макс",
        text="Что вы предлагаете? Я слушаю ваши условия."
    ))
    
    pirate_contact.add_node(DialogueNode(
        id="selena_threat",
        speaker="Селена Ро",
        text="Пока вы не отказались, я считаю, что переговоры возможны. "
             "Но помните — время не на вашей стороне.",
        is_end=True
    ))
    
    pirate_contact.add_node(DialogueNode(
        id="selena_retreat",
        speaker="Селена Ро",
        text="Как хотите, капитан. Но не говорите, что я не предупреждала. "
             "До встречи в космосе.",
        is_end=True
    ))
    
    pirate_contact.nodes["start"].choices = [
        Choice("refuse", "Отказать", "refuse", 
               effect=ChoiceEffect.RELATIONSHIP_DOWN, effect_value=("selena_ro", -10)),
        Choice("negotiate", "Выслушать предложение", "negotiate"),
        Choice("threaten", "Пригрозить", "selena_threat",
               required_stat={"biotics": 1})
    ]
    pirate_contact.nodes["refuse"].choices = [
        Choice("end", "Завершить связь", "selena_retreat")
    ]
    pirate_contact.nodes["negotiate"].choices = [
        Choice("listen", "Слушать", "selena_threat")
    ]
    
    dialogues["pirate_contact"] = pirate_contact
    
    # === Диалог: Обсуждение саботажа ===
    sabotage_discussion = Dialogue(
        id="sabotage_discussion",
        title="Обсуждение саботажа",
        start_node="start"
    )
    
    sabotage_discussion.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="Все знают, что на борту серьёзные проблемы. Саботаж. "
             "Пока без конкретных подозреваемых. Я хочу, чтобы каждый сказал, "
             "где был последние 12 часов."
    ))
    
    sabotage_discussion.add_node(DialogueNode(
        id="rina_explains",
        speaker="Рина",
        text="Я была в рубке, анализировала разведданные и планировала маршрут. "
             "У меня чистая совесть."
    ))
    
    sabotage_discussion.add_node(DialogueNode(
        id="irina_explains",
        speaker="Ирина",
        text="Я была в лаборатории, изучала артефакт. Доступа к техническим "
             "системам у меня не было."
    ))
    
    sabotage_discussion.add_node(DialogueNode(
        id="nadezhda_explains",
        speaker="Надежда",
        text="Я патрулировала отсек безопасности, всё было нормально. "
             "Если кто-то и виноват, то умело скрывается."
    ))
    
    sabotage_discussion.add_node(DialogueNode(
        id="max_decision_sabotage",
        speaker="Макс",
        text="Хорошо. Афина, проверь биометрические данные и видеозаписи.",
        is_end=True
    ))
    
    sabotage_discussion.nodes["start"].choices = [
        Choice("ask_rina", "Рина, где ты была?", "rina_explains"),
        Choice("ask_irina", "Ирина, твои действия?", "irina_explains"),
        Choice("ask_nadezhda", "Надежда, доклад", "nadezhda_explains"),
        Choice("ask_athena", "Афина, данные", "max_decision_sabotage",
               required_stat={"psychic": 1})
    ]
    sabotage_discussion.nodes["rina_explains"].choices = [
        Choice("next", "Следующий", "irina_explains")
    ]
    sabotage_discussion.nodes["irina_explains"].choices = [
        Choice("next", "Следующий", "nadezhda_explains")
    ]
    sabotage_discussion.nodes["nadezhda_explains"].choices = [
        Choice("end", "Приказать Афине проверить", "max_decision_sabotage")
    ]
    
    dialogues["sabotage_discussion"] = sabotage_discussion
    
    return dialogues
