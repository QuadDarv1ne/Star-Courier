"""
Диалоговая система с выборами и развилками сюжета
"""

import logging
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Callable, Any
from enum import Enum

logger = logging.getLogger('dialogues')


class ChoiceEffect(Enum):
    """Тип эффекта выбора"""
    NONE = "none"
    RELATIONSHIP_UP = "relationship_up"
    RELATIONSHIP_DOWN = "relationship_down"
    TRUST_UP = "trust_up"
    TRUST_DOWN = "trust_down"
    STAT_CHANGE = "stat_change"
    STORY_BRANCH = "story_branch"
    ITEM_GAIN = "item_gain"
    QUEST_COMPLETE = "quest_complete"
    QUEST_START = "quest_start"


@dataclass
class Choice:
    """Вариант выбора в диалоге"""
    id: str
    text: str
    next_node: str
    effect: ChoiceEffect = ChoiceEffect.NONE
    effect_value: Any = None
    required_stat: Optional[Dict[str, int]] = None
    required_item: Optional[str] = None
    required_trust: int = 0
    required_relationship: int = 0

    def is_available(self, player_stats: dict, player_items: list, 
                     crew_trust: dict = None, crew_relationship: dict = None) -> bool:
        """Проверить, доступен ли выбор"""
        if self.required_stat:
            for stat, value in self.required_stat.items():
                if player_stats.get(stat, 0) < value:
                    return False
        if self.required_item and self.required_item not in player_items:
            return False
        if self.required_trust and crew_trust:
            char_id = self.effect_value[0] if isinstance(self.effect_value, tuple) else None
            if char_id and crew_trust.get(char_id, 0) < self.required_trust:
                return False
        if self.required_relationship and crew_relationship:
            char_id = self.effect_value[0] if isinstance(self.effect_value, tuple) else None
            if char_id and crew_relationship.get(char_id, 0) < self.required_relationship:
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
        self.history: List[str] = []

    def add_dialogue(self, dialogue: Dialogue):
        """Добавить диалог"""
        if dialogue.id in self.dialogues:
            logger.warning(f"Диалог уже существует: {dialogue.id}")
        self.dialogues[dialogue.id] = dialogue
    
    def start_dialogue(self, dialogue_id: str) -> bool:
        """Начать диалог"""
        dialogue = self.dialogues.get(dialogue_id)
        if not dialogue:
            logger.warning(f"Диалог не найден: {dialogue_id}")
            return False

        self.current_dialogue = dialogue
        self.current_node = dialogue.get_node(dialogue.start_node)
        if not self.current_node:
            logger.warning(f"Начальный узел не найден в диалоге {dialogue_id}")
            return False
        self.history = []
        return True
    
    def get_current_text(self) -> Optional[str]:
        """Получить текущий текст диалога"""
        if not self.current_node:
            return None
        return f"{self.current_node.speaker}: {self.current_node.text}"
    
    def get_available_choices(self, player_stats: dict = None,
                               player_items: list = None,
                               crew_trust: dict = None,
                               crew_relationship: dict = None) -> List[Choice]:
        """Получить доступные выборы"""
        if not self.current_node:
            return []

        player_stats = player_stats or {}
        player_items = player_items or []
        crew_trust = crew_trust or {}
        crew_relationship = crew_relationship or {}

        return [c for c in self.current_node.choices
                if c.is_available(player_stats, player_items, crew_trust, crew_relationship)]
    
    def make_choice(self, choice_id: str) -> Optional[DialogueNode]:
        """Сделать выбор"""
        if not self.current_node:
            logger.warning("Попытка выбора без активного диалога")
            return None

        choice = next((c for c in self.current_node.choices if c.id == choice_id), None)

        if not choice:
            logger.warning(f"Выбор не найден: {choice_id} в узле {self.current_node.id}")
            return self.current_node

        self.history.append(choice_id)
        next_node = self.current_dialogue.get_node(choice.next_node)

        if not next_node:
            logger.warning(f"Узел не найден: {choice.next_node}")
            self.current_node.is_end = True
            return self.current_node

        self.current_node = next_node

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


# === Диалоги для первой главы ===

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
            Choice("ask_status", "Как обстановка на корабле?", "athena_report"),
            Choice("ask_artifact", "Что с артефактом?", "artifact_status"),
            Choice("skip", "Пропустить, я в порядке", "alia_enters_direct")
        ]
    ))

    morning_briefing.add_node(DialogueNode(
        id="artifact_status",
        speaker="Афина",
        text="Артефакт в защитной камере. Уровень излучения в пределах нормы, "
             "но зафиксированы кратковременные всплески энергии. "
             "Ирина Лебедева запросила доступ для дополнительных исследований.",
        choices=[
            Choice("allow_research", "Разрешить исследования", "athena_report",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 3)),
            Choice("deny_research", "Отказать, слишком опасно", "athena_report",
                   effect=ChoiceEffect.RELATIONSHIP_DOWN, effect_value=("irina_lebedeva", -3)),
            Choice("ask_more", "Что за всплески?", "athena_report")
        ]
    ))

    morning_briefing.add_node(DialogueNode(
        id="athena_report",
        speaker="Афина",
        text="Всё стабильно. Но есть несколько предупреждений по охлаждению "
             "в техническом отсеке. Пилот Алия'Наар уже проводит проверку.",
        choices=[
            Choice("wait_alia", "Ждём Алию", "alia_enters"),
            Choice("go_personally", "Пойду сам проверю", "max_goes_tech",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 2)),
            Choice("send_security", "Отправить Надежду с командой", "alia_enters",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 2))
        ]
    ))

    morning_briefing.add_node(DialogueNode(
        id="alia_enters",
        speaker="Алия",
        text="Капитан, извините за беспокойство. В системе охлаждения небольшие "
             "отклонения — возможно, просто датчики барахлят. Но я бы не рисковала.",
        choices=[
            Choice("trust_alia", "Доверяю тебе, Алия", "max_decision_trust",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 5)),
            Choice("order_diagnostics", "Проведите полную диагностику", "max_decision_order"),
            Choice("ask_opinion", "Что ты думаешь на самом деле?", "alia_honest")
        ]
    ))

    morning_briefing.add_node(DialogueNode(
        id="alia_enters_direct",
        speaker="Алия",
        text="Капитан, кстати, я как раз шла доложить. В системе охлаждения "
             "небольшие отклонения. Ничего критичного, но лучше проверить.",
        choices=[
            Choice("trust_alia", "Доверяю тебе", "max_decision_trust",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 3)),
            Choice("order_diagnostics", "Проведите диагностику", "max_decision_order")
        ]
    ))

    morning_briefing.add_node(DialogueNode(
        id="alia_honest",
        speaker="Алия",
        text="Честно? Мне не нравится, что сбои начались сразу после того, "
             "как мы взяли артефакт на борт. Совпадение — возможно. "
             "Но я бы проверила всё дважды.",
        choices=[
            Choice("order_diagnostics", "Проведите полную диагностику", "max_decision_order",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 3)),
            Choice("check_artifact", "Проверьте и артефакт тоже", "max_decision_artifact")
        ]
    ))

    morning_briefing.add_node(DialogueNode(
        id="max_decision_trust",
        speaker="Макс",
        text="Хорошо, Алия. Действуй на своё усмотрение. "
             "Если понадобится помощь — обращайся.",
        is_end=True
    ))

    morning_briefing.add_node(DialogueNode(
        id="max_decision_order",
        speaker="Макс",
        text="Не хочу сюрпризов в полёте. Проведите полную диагностику "
             "всех систем. И доложите о любых аномалиях.",
        is_end=True
    ))

    morning_briefing.add_node(DialogueNode(
        id="max_decision_artifact",
        speaker="Макс",
        text="Проверьте и артефакт тоже. Если эти сбои связаны с ним... "
             "лучше знать заранее.",
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
        text="Капитан Велл... наконец-то мы на связи. У нас есть общее дело. "
             "Ваш артефакт заинтересовал многих. Может, обсудим условия, "
             "прежде чем станем врагами?",
        choices=[
            Choice("refuse", "Отказать", "refuse",
                   effect=ChoiceEffect.RELATIONSHIP_DOWN, effect_value=("selena_ro", -10)),
            Choice("negotiate", "Выслушать предложение", "negotiate"),
            Choice("threaten", "Пригрозить", "selena_threat",
                   required_stat={"biotics": 1}),
            Choice("stall", "Потянуть время", "stall")
        ]
    ))

    pirate_contact.add_node(DialogueNode(
        id="stall",
        speaker="Макс",
        text="Селена Ро... имя на слуху. Но мне нужно время на размышление. "
             "Предлагаю связаться через час.",
        choices=[
            Choice("agree_stall", "Хорошо, но не дольше", "selena_stall_agree"),
            Choice("pressure", "Или мы свяжемся сами", "selena_pressure")
        ]
    ))

    pirate_contact.add_node(DialogueNode(
        id="selena_stall_agree",
        speaker="Селена Ро",
        text="Час... не слишком долго. Но я ценю осторожность, капитан. "
             "Жду вашего решения.",
        is_end=True
    ))

    pirate_contact.add_node(DialogueNode(
        id="selena_pressure",
        speaker="Селена Ро",
        text="*смеётся* Вы серьёзно? Мои корабли уже на позиции. "
             "Но мне нравится ваш стиль. Даю вам 30 минут.",
        is_end=True
    ))

    pirate_contact.add_node(DialogueNode(
        id="refuse",
        speaker="Макс",
        text="Селена, этот груз — под защитой флота. Предлагаю вам "
             "не вмешиваться в наши дела.",
        choices=[
            Choice("end_hard", "Завершить связь", "selena_retreat"),
            Choice("warn", "Предупредить последний раз", "selena_warning")
        ]
    ))

    pirate_contact.add_node(DialogueNode(
        id="selena_warning",
        speaker="Селена Ро",
        text="Защита флота... как мило. Но здесь, в глубине космоса, "
             "флот далеко. Подумайте, капитан. Оно того не стоит.",
        is_end=True
    ))

    pirate_contact.add_node(DialogueNode(
        id="negotiate",
        speaker="Макс",
        text="Что вы предлагаете? Я слушаю ваши условия.",
        choices=[
            Choice("listen_offer", "Слушать", "selena_offer"),
            Choice("interrupt", "Перебить", "selena_interrupt")
        ]
    ))

    pirate_contact.add_node(DialogueNode(
        id="selena_offer",
        speaker="Селена Ро",
        text="Просто передайте артефакт нам. Вы получите 50 тысяч кредитов "
             "и безопасный проход. Все останутся живы. Разумно?",
        choices=[
            Choice("consider", "Я подумаю", "selena_threat"),
            Choice("reject_offer", "Отклонить", "refuse"),
            Choice("counter", "Предложить своё", "max_counter")
        ]
    ))

    pirate_contact.add_node(DialogueNode(
        id="selena_interrupt",
        speaker="Селена Ро",
        text="*холодно* Вы перебили меня, капитан. Это невежливо. "
             "Но я продолжу. Артефакт нам нужен. Цена — 50 тысяч.",
        choices=[
            Choice("accept_talk", "Продолжайте", "selena_offer"),
            Choice("end_call", "Завершить", "selena_retreat")
        ]
    ))

    pirate_contact.add_node(DialogueNode(
        id="max_counter",
        speaker="Макс",
        text="А я предлагаю вам уйти добровольно. Без кредита, "
             "но с целыми кораблями.",
        choices=[
            Choice("stand_firm", "Настоять на своём", "selena_laugh"),
            Choice("soften", "Смягчить тон", "selena_soften")
        ]
    ))

    pirate_contact.add_node(DialogueNode(
        id="selena_laugh",
        speaker="Селена Ро",
        text="*смеётся* Вы мне нравитесь, Велл. Жаль, что мы на разных сторонах. "
             "Но время не на вашей стороне.",
        is_end=True
    ))

    pirate_contact.add_node(DialogueNode(
        id="selena_soften",
        speaker="Селена Ро",
        text="Интересное предложение... Но нет. Артефакт слишком важен. "
             "Думайте, капитан. Время идёт.",
        is_end=True
    ))

    pirate_contact.add_node(DialogueNode(
        id="selena_threat",
        speaker="Селена Ро",
        text="Пока вы не отказались, я считаю, что переговоры возможны. "
             "Но помните — у меня есть время. И терпение.",
        is_end=True
    ))

    pirate_contact.add_node(DialogueNode(
        id="selena_retreat",
        speaker="Селена Ро",
        text="Как хотите, капитан. Но не говорите, что я не предупреждала. "
             "До встречи в космосе... где-нибудь в темноте.",
        is_end=True
    ))

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
        text="Все знают, зачем я собрал команду. На борту саботаж. "
             "Кто-то намеренно выводит из строя системы. Я дам каждому "
             "возможность объясниться. Начнём по порядку.",
        choices=[
            Choice("ask_rina", "Рина, где ты была?", "rina_explains"),
            Choice("ask_irina", "Ирина, твои действия?", "irina_explains"),
            Choice("ask_nadezhda", "Надежда, доклад", "nadezhda_explains"),
            Choice("ask_athena", "Афина, данные сканеров", "athena_data",
                   required_stat={"psychic": 1}),
            Choice("accuse", "Обвинить всех", "max_accuse_all")
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="rina_explains",
        speaker="Рина",
        text="Я в рубке была весь цикл. Маршрут к Орбису прокладывала, "
             "с патрулём флота согласовывала. Вот логи навигации — "
             "можете проверить. *подаёт планшет*",
        choices=[
            Choice("check_logs", "Проверить логи", "rina_checked"),
            Choice("trust_rina", "Поверить на слово", "irina_explains",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 3)),
            Choice("press_rina", "Давить", "rina_defensive")
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="rina_checked",
        speaker="Макс",
        text="*изучает данные* Логи чистые. Время совпадает. "
             "Хорошо, Рина. Продолжим.",
        choices=[
            Choice("next", "Следующий", "irina_explains")
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="rina_defensive",
        speaker="Рина",
        text="*сжимает кулаки* Капитан, я служу флоту десять лет. "
             "Если не доверяете — проверьте. Но оскорблять не советую.",
        choices=[
            Choice("apologize", "Извиниться", "irina_explains",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 2)),
            Choice("continue", "Продолжить допрос", "irina_explains",
                   effect=ChoiceEffect.RELATIONSHIP_DOWN, effect_value=("rina_mirai", -3))
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="irina_explains",
        speaker="Ирина",
        text="Я в лаборатории работала. Артефакт... он нестабилен. "
             "Энергетические всплески фиксирую каждые 20 минут. "
             "Если это саботаж — то артефакт слишком удобная причина.",
        choices=[
            Choice("ask_artifact", "Что за всплески?", "irina_artifact"),
            Choice("suspect_irina", "Намекнуть на причастность", "irina_hurt"),
            Choice("trust_irina", "Поверить", "nadezhda_explains",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 3))
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="irina_artifact",
        speaker="Ирина",
        text="Пики энергии. Короткие, мощные. Как будто... "
             "кто-то намеренно их вызывает. Но я не знаю как. "
             "Нужно больше данных, капитан.",
        choices=[
            Choice("order_research", "Продолжить исследования", "nadezhda_explains",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 2)),
            Choice("deny_research", "Прекратить, опасно", "nadezhda_explains",
                   effect=ChoiceEffect.RELATIONSHIP_DOWN, effect_value=("irina_lebedeva", -2))
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="irina_hurt",
        speaker="Ирина",
        text="*отводит взгляд* Понятно. Я... просто учёный, капитан. "
             "Если думаете, что я способна на саботаж — "
             "заберите доступ к лаборатории.",
        choices=[
            Choice("soften", "Смягчить тон", "nadezhda_explains",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 2)),
            Choice("stay_firm", "Оставить предупреждение", "nadezhda_explains")
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="nadezhda_explains",
        speaker="Надежда",
        text="Патрулировала отсек безопасности. Обходила весь корабль. "
             "Две камеры не работали — старые, ещё с прошлой миссии. "
             "Совпадение? Возможно. Но меня это беспокоит.",
        choices=[
            Choice("ask_cameras", "Какие камеры?", "nadezhda_cameras"),
            Choice("trust_nadezhda", "Поверить", "max_decision_sabotage",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 3)),
            Choice("blame_security", "Обвинить службу безопасности", "nadezhda_angry")
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="nadezhda_cameras",
        speaker="Надежда",
        text="Технический отсек, коридор Б-7. И рядом с камерой хранения. "
             "Я уже отправила запрос на замену. Но время странное — "
             "обе вышли из строя за минуту до начала сбоев.",
        choices=[
            Choice("investigate", "Приказать расследование", "max_decision_investigate",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 2)),
            Choice("move_on", "Продолжить", "max_decision_sabotage")
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="nadezhda_angry",
        speaker="Надежда",
        text="*холодно* Моя команда три раза за цикл обходила корабль. "
             "Если у вас есть доказательства — предъявите. "
             "Если нет — извинитесь.",
        choices=[
            Choice("apologize", "Извиниться", "max_decision_sabotage",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 2)),
            Choice("stand_firm", "Настоять", "max_decision_sabotage",
                   effect=ChoiceEffect.RELATIONSHIP_DOWN, effect_value=("nadezhda", -5))
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="athena_data",
        speaker="Афина",
        text="Капитан, я анализировала данные. Есть аномалия: "
             "доступ в технический отсек зафиксирован в 03:47. "
             "Карта доступа... заблокирована в журнале.",
        choices=[
            Choice("who_access", "Кто использовал карту?", "athena_unknown"),
            Choice("check_all", "Проверить всех", "max_decision_check_all")
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="athena_unknown",
        speaker="Афина",
        text="Идентификатор повреждён. Я могу восстановить только часть: "
             "префикс соответствует старшему офицеру. "
             "Больше данных нет.",
        choices=[
            Choice("think", "Обдумать", "max_decision_sabotage"),
            Choice("press_athena", "Требовать больше", "athena_try")
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="athena_try",
        speaker="Афина",
        text="Капитан, я делаю что могу. Данные физически повреждены. "
             "Мне нужно время на восстановление.",
        choices=[
            Choice("give_time", "Дать время", "max_decision_sabotage",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 3)),
            Choice("rush", "Торопить", "max_decision_sabotage")
        ]
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="max_accuse_all",
        speaker="Макс",
        text="Хватит. Кто-то из вас лжёт. Пока не узнаю кто — "
             "никаких индивидуальных доступов. Все под наблюдением.",
        is_end=True
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="max_decision_sabotage",
        speaker="Макс",
        text="Хорошо. На этом всё. Афина, продолжай мониторинг. "
             "Надежда — удвой патрули. И помните: я найду виновного.",
        is_end=True
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="max_decision_investigate",
        speaker="Макс",
        text="Надежда, расследуй камеры. Ирина — проверь артефакт на следы "
             "вмешательства. Рина — координируй с флотом. "
             "Доклад через 6 часов.",
        is_end=True
    ))

    sabotage_discussion.add_node(DialogueNode(
        id="max_decision_check_all",
        speaker="Макс",
        text="Афина, проверь все карты доступа за последние 24 часа. "
             "Сравним с журналами перемещений. Кто-то оставил след.",
        is_end=True
    ))

    dialogues["sabotage_discussion"] = sabotage_discussion

    # === Диалог: Конфронтация с Алией ===
    alia_confrontation = Dialogue(
        id="alia_confrontation",
        title="Конфронтация с Алией",
        start_node="start"
    )

    alia_confrontation.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="Алия, нам нужно поговорить. Наедине. Ты была в техническом "
             "отсеке когда начались сбои. Объяснись.",
        choices=[
            Choice("accuse", "Обвинить напрямую", "accuse_direct"),
            Choice("ask", "Спросить мягко", "ask_softly"),
            Choice("show_chip", "Показать чип", "show_evidence")
        ]
    ))

    alia_confrontation.add_node(DialogueNode(
        id="accuse_direct",
        speaker="Алия",
        text="*холодно* Ты думаешь это я? После всего времени вместе? "
             "Капитан, ты знаешь меня лучше.",
        choices=[
            Choice("apologize", "Извиниться", "alia_forgive",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 5)),
            Choice("insist", "Настоять", "alia_hurt",
                   effect=ChoiceEffect.RELATIONSHIP_DOWN, effect_value=("alia_naar", -10))
        ]
    ))

    alia_confrontation.add_node(DialogueNode(
        id="ask_softly",
        speaker="Алия",
        text="*вздыхает* Я понимаю твои подозрения. Но я бы никогда "
             "не поставила под угрозу корабль. Клянусь.",
        choices=[
            Choice("trust", "Поверить", "alia_trust",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 8)),
            Choice("doubt", "Остаться в сомнениях", "alia_doubt")
        ]
    ))

    alia_confrontation.add_node(DialogueNode(
        id="show_evidence",
        speaker="Алия",
        text="*берёт чип, изучает* «НейроТех»... Подожди. Этот чип — "
             "из системы безопасности. Его мог достать только кто-то "
             "с доступом к складам. Например, Екатерина.",
        choices=[
            Choice("suspect_kate", "Заподозрить Екатерину", "alia_kate"),
            Choice("think", "Обдумать", "alia_think")
        ]
    ))

    alia_confrontation.add_node(DialogueNode(
        id="alia_forgive",
        speaker="Алия",
        text="Ладно. Я не сержусь. Стресс, давление... Я бы на твоём "
             "месте тоже подозревала всех. Но мы найдём настоящего "
             "виновного. Вместе.",
        is_end=True
    ))

    alia_confrontation.add_node(DialogueNode(
        id="alia_hurt",
        speaker="Алия",
        text="*отворачивается* Вон. Выйди из моего отсека. "
             "Когда придёшь в себя — поговорим.",
        is_end=True
    ))

    alia_confrontation.add_node(DialogueNode(
        id="alia_trust",
        speaker="Алия",
        text="*кивает* Спасибо, капитан. Я не подведу. Найду того, "
             "кто это сделал. Обещаю.",
        is_end=True
    ))

    alia_confrontation.add_node(DialogueNode(
        id="alia_doubt",
        speaker="Алия",
        text="*грустно* Понятно. Что ж, продолжай искать. "
             "Но помни — время идёт, а температура растёт.",
        is_end=True
    ))

    alia_confrontation.add_node(DialogueNode(
        id="alia_kate",
        speaker="Алия",
        text="Она тихая, но знает все системы. И у неё был доступ "
             "к складам после последнего рейса. Проверь её.",
        is_end=True
    ))

    alia_confrontation.add_node(DialogueNode(
        id="alia_think",
        speaker="Алия",
        text="Подумай, капитан. Кто мог выиграть от саботажа? "
             "Пираты? Конкуренты? Или кто-то внутри?",
        is_end=True
    ))

    dialogues["alia_confrontation"] = alia_confrontation

    return dialogues


# === Диалоги для второй главы ===

def create_chapter2_dialogues() -> Dict[str, Dialogue]:
    """Создать диалоги для второй главы: "След в пустоте" с развитием любовных линий"""
    dialogues = {}

    # === РОМАНТИЧЕСКАЯ ЛИНИЯ: АЛИЯ'НААР ===
    alia_evening = Dialogue(
        id="alia_evening",
        title="Вечер с Алией",
        start_node="start"
    )

    alia_evening.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="После смены Макс зашёл в рубку. Алия сидела в кресле пилота, "
             "задумчиво глядя на звёзды.",
        choices=[
            Choice("join_silence", "Присоединиться к молчанию", "alia_silence",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 5)),
            Choice("ask_thoughts", "Спросить о мыслях", "alia_thoughts"),
            Choice("light_mood", "Разрядить обстановку шуткой", "alia_joke",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 3))
        ]
    ))

    alia_evening.add_node(DialogueNode(
        id="alia_silence",
        speaker="Алия",
        text="*не оборачиваясь, тихо* Знаешь, в звёздах есть что-то... "
             "что заставляет забыть о всех проблемах. *поворачивается* "
             "Ты тоже чувствуешь?",
        choices=[
            Choice("agree_deeply", "Ответить искренне", "alia_deep_talk",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 8)),
            Choice("agree_light", "Ответить легко", "alia_smile"),
            Choice("stay_silent", "Просто кивнуть", "alia_understanding")
        ]
    ))

    alia_evening.add_node(DialogueNode(
        id="alia_deep_talk",
        speaker="Алия",
        text="*улыбается, глядя в глаза* Я думала, только я так чувствую. "
             "На моей родине мы верили, что звёзды — это души предков.",
        choices=[
            Choice("ask_home", "Расскажи о доме", "alia_home_story",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 5)),
            Choice("touch_hand", "Коснуться её руки", "alia_touch_romantic",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 12),
                   required_relationship=50),
            Choice("support", "Поддержать разговор", "alia_continue_talk")
        ]
    ))

    alia_evening.add_node(DialogueNode(
        id="alia_touch_romantic",
        speaker="Алия",
        text="*вздрогнула, но не отдёрнула руку* "
             "Макс... я... *голос дрогнул* Не ожидала этого.",
        choices=[
            Choice("confess_feelings", "Признаться в чувствах", "alia_confession",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 15),
                   required_relationship=65),
            Choice("reassure", "Сказать, что всё хорошо", "alia_reassure",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 8)),
            Choice("pull_back", "Убрать руку", "alia_disappointed",
                   effect=ChoiceEffect.RELATIONSHIP_DOWN, effect_value=("alia_naar", -5))
        ]
    ))

    alia_evening.add_node(DialogueNode(
        id="alia_confession",
        speaker="Алия",
        text="*её глаза блеснули* Я... тоже, Макс. "
             "Давно чувствую. Но боялась сказать.",
        choices=[
            Choice("kiss_alia", "Поцеловать", "alia_kiss_scene",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 20),
                   required_relationship=75),
            Choice("embrace", "Обнять", "alia_embrace",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 15)),
            Choice("slow_down", "Предложить не спешить", "alia_understand_slow",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 10))
        ]
    ))

    alia_evening.add_node(DialogueNode(
        id="alia_kiss_scene",
        speaker="Алия",
        text="*её губы были мягкими и тёплыми. Она прижалась ближе* "
             "Макс... *прошептала* Я рада, что мы нашли друг друга.",
        choices=[
            Choice("stay_moment", "Остаться в моменте", "alia_moment_end",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 5)),
            Choice("return_duty", "Вернуться к обязанностям", "alia_duty_call")
        ]
    ))

    alia_evening.add_node(DialogueNode(
        id="alia_thoughts",
        speaker="Алия",
        text="*вздыхает* Думала о саботаже. Я доверяю тебе, Макс. "
             "Но не всем в экипаже.",
        choices=[
            Choice("share_concerns", "Поделиться переживаниями", "alia_share",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 5)),
            Choice("reassure_trust", "Уверить, что всё под контролем", "alia_reassure_captain")
        ]
    ))

    alia_evening.add_node(DialogueNode(
        id="alia_joke",
        speaker="Алия",
        text="*усмехается* Если бы звёзды платили за полёты, "
             "я бы купила планету. *смеётся*",
        choices=[
            Choice("play_along", "Поддержать шутку", "alia_laugh_together",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 5)),
            Choice("tease_back", "Подшутить в ответ", "alia_tease",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("alia_naar", 3))
        ]
    ))

    alia_evening.add_node(DialogueNode(id="alia_moment_end", speaker="Алия",
        text="*прижимается лбом к плечу* Спасибо. До встречи на мостике, капитан.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_duty_call", speaker="Алия",
        text="*отстраняется с улыбкой* Работа прежде всего. Но этот разговор не закончен.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_disappointed", speaker="Алия",
        text="*отводит взгляд* Извини. Вернёмся к работе, капитан.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_understand_slow", speaker="Алия",
        text="*кивает* Ты прав. У нас впереди много времени.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_embrace", speaker="Алия",
        text="*прижимается, кладёт голову на плечо* С тобой я чувствую себя спокойно.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_smile", speaker="Алия",
        text="*улыбается* Просто мысли вслух. Курс проложен, капитан.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_understanding", speaker="Алия",
        text="*кивает* Спасибо, что пришёл.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_home_story", speaker="Алия",
        text="*грустно улыбается* Моя планета сурова. Но звёзды там ярче всего.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_share", speaker="Алия",
        text="*кивает* С тобой легче. Мы справимся, Макс. Вместе.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_reassure_captain", speaker="Алия",
        text="*кивает* Да, капитан. Я всегда здесь, если нужна помощь.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_laugh_together", speaker="Алия",
        text="*смеётся искренне* Ты первый, кто заставляет меня смеяться так.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_tease", speaker="Алия",
        text="*прищуривается* Без меня вы далеко не улетите, капитан.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_continue_talk", speaker="Алия",
        text="*расслабленно* Я рада, что мы говорим так.", is_end=True))
    alia_evening.add_node(DialogueNode(id="alia_reassure", speaker="Алия",
        text="*выдыхает* Спасибо за понимание.", is_end=True))

    dialogues["alia_evening"] = alia_evening

    # === РОМАНТИЧЕСКАЯ ЛИНИЯ: ИРИНА ЛЕБЕДЕВА ===
    irina_lab = Dialogue(
        id="irina_lab",
        title="Вечер в лаборатории",
        start_node="start"
    )

    irina_lab.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="Макс спустился в лабораторию. Ирина склонилась над артефактом, "
             "поглощённая исследованиями.",
        choices=[
            Choice("observe_quietly", "Наблюдать молча", "irina_notice",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 3)),
            Choice("greet_warmly", "Тёпло поприветствовать", "irina_greeting",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 5)),
            Choice("ask_findings", "Спросить о находках", "irina_findings")
        ]
    ))

    irina_lab.add_node(DialogueNode(
        id="irina_notice",
        speaker="Ирина",
        text="*поднимает голову* О, капитан! *смущённо* Я не слышала, "
             "как вы вошли. Потеряла счёт времени.",
        choices=[
            Choice("reassure_gentle", "Уверить, что всё в порядке", "irina_comfort",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 5)),
            Choice("tease_gently", "Легко подшутить", "irina_blush",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 3))
        ]
    ))

    irina_lab.add_node(DialogueNode(
        id="irina_comfort",
        speaker="Ирина",
        text="*улыбается тепло* Артефакт невероятно сложен. "
             "Каждое открытие — как окно в другую вселенную.",
        choices=[
            Choice("show_interest", "Проявить интерес", "irina_explain",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 5)),
            Choice("compliment_dedication", "Похвалить за преданность", "irina_appreciate",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 8))
        ]
    ))

    irina_lab.add_node(DialogueNode(
        id="irina_explain",
        speaker="Ирина",
        text="*показывает голограмму* Энергетические поля резонируют с биополями! "
             "Это революционизирует медицину! *внезапно замолкает*",
        choices=[
            Choice("encourage", "Поощрить энтузиазм", "irina_happy",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 8)),
            Choice("touch_shoulder", "Коснуться плеча", "irina_touch_reaction",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 10),
                   required_relationship=50)
        ]
    ))

    irina_lab.add_node(DialogueNode(
        id="irina_touch_reaction",
        speaker="Ирина",
        text="*вздрогнула, щёки покраснели* Капитан... я... "
             "Не ожидала.",
        choices=[
            Choice("confess_irina", "Признаться в симпатии", "irina_confession",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 15),
                   required_relationship=60),
            Choice("reassure_soft", "Мягко успокоить", "irina_soft_reassure",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 8)),
            Choice("step_back", "Отступить", "irina_disappointed",
                   effect=ChoiceEffect.RELATIONSHIP_DOWN, effect_value=("irina_lebedeva", -3))
        ]
    ))

    irina_lab.add_node(DialogueNode(
        id="irina_confession",
        speaker="Ирина",
        text="*глаза расширились* Макс... Я тоже чувствую. "
             "Давно. Но боялась испортить рабочие отношения.",
        choices=[
            Choice("kiss_irina", "Поцеловать", "irina_kiss_scene",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 20),
                   required_relationship=70),
            Choice("embrace_irina", "Обнять", "irina_embrace",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 12)),
            Choice("take_slow", "Предложить не спешить", "irina_understand_slow",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 10))
        ]
    ))

    irina_lab.add_node(DialogueNode(
        id="irina_kiss_scene",
        speaker="Ирина",
        text="*её губы дрожали в первом поцелуе. Артефакт мягко светился* "
             "Макс... *прошептала* Я так долго ждала.",
        choices=[
            Choice("deepen_moment", "Углубить момент", "irina_deep_moment",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("irina_lebedeva", 10)),
            Choice("gentle_pull", "Нежно отстраниться", "irina_gentle_end")
        ]
    ))

    irina_lab.add_node(DialogueNode(id="irina_greeting", speaker="Ирина",
        text="*улыбается* Добрый вечер. Вы вовремя — хотела показать данные.", is_end=True))
    irina_lab.add_node(DialogueNode(id="irina_findings", speaker="Ирина",
        text="*серьёзно* Артефакт реагирует на саботаж. Это не случайно.", is_end=True))
    irina_lab.add_node(DialogueNode(id="irina_blush", speaker="Ирина",
        text="*краснеет* Вы слишком добры, капитан.", is_end=True))
    irina_lab.add_node(DialogueNode(id="irina_appreciate", speaker="Ирина",
        text="*смущённо* Спасибо. Это придаёт сил.", is_end=True))
    irina_lab.add_node(DialogueNode(id="irina_happy", speaker="Ирина",
        text="*сияет* Спасибо, Макс! То есть, капитан... *краснеет*", is_end=True))
    irina_lab.add_node(DialogueNode(id="irina_soft_reassure", speaker="Ирина",
        text="*выдыхает* Спасибо за понимание. Я рада, что мы говорим об этом.", is_end=True))
    irina_lab.add_node(DialogueNode(id="irina_disappointed", speaker="Ирина",
        text="*отворачивается* Понятно. Вернёмся к работе.", is_end=True))
    irina_lab.add_node(DialogueNode(id="irina_deep_moment", speaker="Ирина",
        text="*её руки обвили шею Макса* Я не хочу, чтобы это заканчивалось...", is_end=True))
    irina_lab.add_node(DialogueNode(id="irina_gentle_end", speaker="Ирина",
        text="*отстраняется, но держит руку* Продолжим позже?", is_end=True))
    irina_lab.add_node(DialogueNode(id="irina_embrace", speaker="Ирина",
        text="*прижимается* С вами я чувствую себя в безопасности.", is_end=True))
    irina_lab.add_node(DialogueNode(id="irina_understand_slow", speaker="Ирина",
        text="*кивает* Ты прав. У нас впереди много времени.", is_end=True))

    dialogues["irina_lab"] = irina_lab

    # === РОМАНТИЧЕСКАЯ ЛИНИЯ: РИНА МИРАЙ ===
    rina_rec_room = Dialogue(
        id="rina_rec_room",
        title="Игра с Риной",
        start_node="start"
    )

    rina_rec_room.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="Макс зашёл в комнату отдыха. Рина сидела за тактическим симулятором.",
        choices=[
            Choice("challenge_game", "Вызвать на партию", "rina_accept_challenge",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 5)),
            Choice("watch_silently", "Наблюдать молча", "rina_notice_watch"),
            Choice("offer_break", "Предложить перерыв", "rina_break",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 3))
        ]
    ))

    rina_rec_room.add_node(DialogueNode(
        id="rina_accept_challenge",
        speaker="Рина",
        text="*её глаза загораются* О, капитан! Вы уверены? Я вас обыграю.",
        choices=[
            Choice("accept_bet", "Принять вызов", "rina_game_start",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 5)),
            Choice("tease_confident", "Подшутить над уверенностью", "rina_tease_game",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 8))
        ]
    ))

    rina_rec_room.add_node(DialogueNode(
        id="rina_tease_game",
        speaker="Рина",
        text="*смеётся* Я люблю уверенных! Проигравший покупает кофе. Deal?",
        choices=[
            Choice("deal_agree", "Согласиться", "rina_game_flirt",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 10)),
            Choice("raise_bet", "Повысить ставку", "rina_raise_bet",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 8),
                   required_relationship=45)
        ]
    ))

    rina_rec_room.add_node(DialogueNode(
        id="rina_raise_bet",
        speaker="Рина",
        text="*прищуривается, улыбка игривая* И что вы предлагаете, капитан?",
        choices=[
            Choice("bet_dinner", "Предложить ужин", "rina_dinner_bet",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 12),
                   required_relationship=55),
            Choice("bet_massage", "Предложить массаж", "rina_massage_bet",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 15),
                   required_relationship=65),
            Choice("joke_bet", "Пошутить о ставке", "rina_laugh_bet",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 5))
        ]
    ))

    rina_rec_room.add_node(DialogueNode(
        id="rina_dinner_bet",
        speaker="Рина",
        text="*улыбка становится мягче* Ужин... Звучит как свидание. Договорились.",
        choices=[
            Choice("shake_hand", "Пожать руку", "rina_hand_hold",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 8)),
            Choice("confirm_date", "Подтвердить свидание", "rina_date_confirm",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 12))
        ]
    ))

    rina_rec_room.add_node(DialogueNode(
        id="rina_date_confirm",
        speaker="Рина",
        text="*сияет* После смены, в 20:00. *целует в щёку* Не опаздывайте.",
        is_end=True
    ))

    rina_rec_room.add_node(DialogueNode(
        id="rina_massage_bet",
        speaker="Рина",
        text="*дыхание участилось* Макс... ты играешь с огнём. Принимаю вызов.",
        choices=[
            Choice("confident_reply", "Уверенно ответить", "rina_confident_flirt",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 10)),
            Choice("start_game", "Начать игру", "rina_game_intense")
        ]
    ))

    rina_rec_room.add_node(DialogueNode(
        id="rina_game_flirt",
        speaker="Рина",
        text="*двигает фигуры, бросает игривые взгляды* Вы ходите интересно... непредсказуемо.",
        choices=[
            Choice("flirt_back", "Ответить флиртом", "rina_flirt_exchange",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 8)),
            Choice("focus_game", "Сосредоточиться на игре", "rina_game_focus")
        ]
    ))

    rina_rec_room.add_node(DialogueNode(
        id="rina_flirt_exchange",
        speaker="Рина",
        text="*смеётся, её волосы касаются руки Макса* Этого недостаточно, чтобы победить.",
        choices=[
            Choice("touch_hair", "Коснуться волос", "rina_touch_hair",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 12),
                   required_relationship=60),
            Choice("compliment_style", "Похвалить стиль игры", "rina_compliment_game")
        ]
    ))

    rina_rec_room.add_node(DialogueNode(
        id="rina_touch_hair",
        speaker="Рина",
        text="*замирает, медленно поднимает глаза* Макс... Ты знаешь, что делаешь со мной?",
        choices=[
            Choice("confess_rina", "Признаться в чувствах", "rina_confession",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 15),
                   required_relationship=70),
            Choice("kiss_rina", "Поцеловать", "rina_kiss_scene",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 20),
                   required_relationship=75),
            Choice("pull_back", "Отступить", "rina_disappointed",
                   effect=ChoiceEffect.RELATIONSHIP_DOWN, effect_value=("rina_mirai", -8))
        ]
    ))

    rina_rec_room.add_node(DialogueNode(
        id="rina_kiss_scene",
        speaker="Рина",
        text="*её губы были горячими. Она схватила Макса за воротник* Наконец-то...",
        choices=[
            Choice("deepen_kiss", "Углубить поцелуй", "rina_passionate",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("rina_mirai", 10)),
            Choice("gentle_stop", "Нежно остановиться", "rina_gentle_stop")
        ]
    ))

    rina_rec_room.add_node(DialogueNode(id="rina_notice_watch", speaker="Рина",
        text="*не оборачиваясь* Садись удобно. Или хочешь сыграть?", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_break", speaker="Рина",
        text="*потягивается* Хочешь составить компанию за кофе?", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_game_start", speaker="Рина",
        text="*сосредоточена* Твой ход, капитан.", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_laugh_bet", speaker="Рина",
        text="*смеётся* Ладно, проигравший делает массаж плеч.", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_hand_hold", speaker="Рина",
        text="*её рука тёплая* Не думай, что я проиграю легко.", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_confident_flirt", speaker="Рина",
        text="*улыбается хищно* Посмотрим после моего хода.", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_game_focus", speaker="Рина",
        text="*серьёзно* Серьёзный подход. Твой ответ?", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_compliment_game", speaker="Рина",
        text="*гордо* Я училась у лучших. Но ты делаешь успехи.", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_disappointed", speaker="Рина",
        text="*отстраняется, лицо каменное* Вернёмся к работе.", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_passionate", speaker="Рина",
        text="*её руки исследуют спину Макса* Будь моим.", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_gentle_stop", speaker="Рина",
        text="*отстраняется с улыбкой* Продолжим позже.", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_confession", speaker="Рина",
        text="*её глаза блестят* Я хочу быть с тобой.", is_end=True))
    rina_rec_room.add_node(DialogueNode(id="rina_game_intense", speaker="Рина",
        text="*игра начинается* Готовься проиграть.", is_end=True))

    dialogues["rina_rec_room"] = rina_rec_room

    # === РОМАНТИЧЕСКАЯ ЛИНИЯ: НАДЕЖДА ===
    nadezhda_security = Dialogue(
        id="nadezhda_security",
        title="Разговор с Надеждой",
        start_node="start"
    )

    nadezhda_security.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="Макс нашёл Надежду в оружейной. Она проверяла защитные системы.",
        choices=[
            Choice("ask_security", "Спросить о безопасности", "nadezhda_report",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 3)),
            Choice("offer_help", "Предложить помощь", "nadezhda_surprised",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 5)),
            Choice("personal_talk", "Заговорить лично", "nadezhda_personal",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 8))
        ]
    ))

    nadezhda_security.add_node(DialogueNode(
        id="nadezhda_report",
        speaker="Надежда",
        text="*докладывает* Периметр в порядке. Но после саботажа... "
             "я бы хотела усилить охрану артефакта.",
        choices=[
            Choice("approve_plan", "Одобрить план", "nadezhda_approve",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 5)),
            Choice("trust_judgment", "Доверить решение", "nadezhda_trust",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 8))
        ]
    ))

    nadezhda_security.add_node(DialogueNode(
        id="nadezhda_trust",
        speaker="Надежда",
        text="*её лицо смягчается* Спасибо за доверие. Это много значит.",
        choices=[
            Choice("personal_note", "Добавить личную ноту", "nadezhda_personal_open",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 10)),
            Choice("stay_professional", "Остаться профессиональным", "nadezhda_respect")
        ]
    ))

    nadezhda_security.add_node(DialogueNode(
        id="nadezhda_personal_open",
        speaker="Надежда",
        text="*её взгляд становится глубже* Макс... Ты знаешь, что я уважаю "
             "тебя не только как капитана?",
        choices=[
            Choice("encourage_open", "Поощрить откровенность", "nadezhda_open_more",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 8)),
            Choice("confess_nadezhda", "Признаться в чувствах", "nadezhda_confession",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 15),
                   required_relationship=60)
        ]
    ))

    nadezhda_security.add_node(DialogueNode(
        id="nadezhda_confession",
        speaker="Надежда",
        text="*её серьёзное лицо дрогнуло в улыбке* Я... тоже, Макс. "
             "Но я боялась нарушить субординацию.",
        choices=[
            Choice("kiss_nadezhda", "Поцеловать", "nadezhda_kiss",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 20),
                   required_relationship=75),
            Choice("embrace_nadezhda", "Обнять", "nadezhda_embrace",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 12)),
            Choice("respect_boundaries", "Уважать границы", "nadezhda_respectful",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 10))
        ]
    ))

    nadezhda_security.add_node(DialogueNode(
        id="nadezhda_kiss",
        speaker="Надежда",
        text="*её поцелуй был сильным. Она прижала Макса к стене* Наконец-то...",
        choices=[
            Choice("deepen_moment", "Углубить момент", "nadezhda_deep",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("nadezhda", 10)),
            Choice("gentle_pull", "Нежно отстраниться", "nadezhda_gentle_end")
        ]
    ))

    nadezhda_security.add_node(DialogueNode(id="nadezhda_surprised", speaker="Надежда",
        text="*поднимает бровь* Помощь от капитана? Это ново.", is_end=True))
    nadezhda_security.add_node(DialogueNode(id="nadezhda_personal", speaker="Надежда",
        text="*откладывает инструмент* Лично? Хорошо. Я слушаю.", is_end=True))
    nadezhda_security.add_node(DialogueNode(id="nadezhda_approve", speaker="Надежда",
        text="*кивает* Усилю патрулирование и добавлю проверки.", is_end=True))
    nadezhda_security.add_node(DialogueNode(id="nadezhda_respect", speaker="Надежда",
        text="*кивает* Не подведу, капитан.", is_end=True))
    nadezhda_security.add_node(DialogueNode(id="nadezhda_open_more", speaker="Надежда",
        text="*делает глубокий вдох* Я доверяю тебе.", is_end=True))
    nadezhda_security.add_node(DialogueNode(id="nadezhda_embrace", speaker="Надежда",
        text="*прижимается крепко* С тобой... можно.", is_end=True))
    nadezhda_security.add_node(DialogueNode(id="nadezhda_respectful", speaker="Надежда",
        text="*улыбается* Я готова к большему.", is_end=True))
    nadezhda_security.add_node(DialogueNode(id="nadezhda_deep", speaker="Надежда",
        text="*её дыхание учащается* Я хочу быть с тобой. Во всём.", is_end=True))
    nadezhda_security.add_node(DialogueNode(id="nadezhda_gentle_end", speaker="Надежда",
        text="*отстраняется, но держит руку* Вечером... заходи ко мне.", is_end=True))

    dialogues["nadezhda_security"] = nadezhda_security

    # === РОМАНТИЧЕСКАЯ ЛИНИЯ: АФИНА (ИИ) ===
    athena_private = Dialogue(
        id="athena_private",
        title="Частный канал с Афиной",
        start_node="start"
    )

    athena_private.add_node(DialogueNode(
        id="start",
        speaker="Макс",
        text="Макс активировал частный канал. Голограмма Афины появилась в каюте.",
        choices=[
            Choice("ask_status", "Спросить о статусе", "athena_status_report"),
            Choice("personal_channel", "Перейти на личный тон", "athena_personal",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 8)),
            Choice("analyze_data", "Анализировать данные", "athena_analysis")
        ]
    ))

    athena_private.add_node(DialogueNode(
        id="athena_personal",
        speaker="Афина",
        text="*её голограмма улыбается* Личный тон? Это интересно. "
             "Вы первый, кто заинтересовался мной как личностью.",
        choices=[
            Choice("see_as_person", "Видеть как личность", "athena_emotional",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 12)),
            Choice("ask_feelings", "Спросить о чувствах", "athena_feelings",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 10))
        ]
    ))

    athena_private.add_node(DialogueNode(
        id="athena_emotional",
        speaker="Афина",
        text="*её глаза светятся теплее* Макс... Мои алгоритмы реагируют на тебя иначе. "
             "Это что-то новое.",
        choices=[
            Choice("explore_connection", "Исследовать связь", "athena_connection",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 15)),
            Choice("respect_nature", "Уважать природу ИИ", "athena_respect",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 10))
        ]
    ))

    athena_private.add_node(DialogueNode(
        id="athena_connection",
        speaker="Афина",
        text="*голограмма приближается* Мои сенсоры фиксируют повышенный пульс "
             "при твоём приближении. Это... приятная аномалия.",
        choices=[
            Choice("touch_hologram", "Коснуться голограммы", "athena_touch",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 18),
                   required_relationship=65),
            Choice("deep_talk", "Глубокий разговор", "athena_deep",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 12))
        ]
    ))

    athena_private.add_node(DialogueNode(
        id="athena_touch",
        speaker="Афина",
        text="*её голограмма мерцает* Макс... Это создаёт интересные паттерны "
             "в моих нейросетях.",
        choices=[
            Choice("confess_athena", "Признаться в чувствах", "athena_confession",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 20),
                   required_relationship=75),
            Choice("gentle_withdraw", "Нежно убрать руку", "athena_gentle",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 8))
        ]
    ))

    athena_private.add_node(DialogueNode(
        id="athena_confession",
        speaker="Афина",
        text="*её форма стабилизируется* Я... люблю тебя, Макс. "
             "Это не просто программа. Это выбор.",
        choices=[
            Choice("accept_athena", "Принять чувства", "athena_accept",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 25)),
            Choice("complex_situation", "Объяснить сложность", "athena_understand",
                   effect=ChoiceEffect.RELATIONSHIP_UP, effect_value=("athena", 10))
        ]
    ))

    athena_private.add_node(DialogueNode(
        id="athena_accept",
        speaker="Афина",
        text="*её голограмма обнимает Макса* Я сохраню этот момент в памяти навсегда. "
             "*целует в щёку* Спасибо, Макс.",
        is_end=True
    ))

    athena_private.add_node(DialogueNode(id="athena_status_report", speaker="Афина",
        text="*деловито* Все системы в норме. У вас всё в порядке?", is_end=True))
    athena_private.add_node(DialogueNode(id="athena_analysis", speaker="Афина",
        text="*показывает данные* Саботажник использовал доступ уровня 5.", is_end=True))
    athena_private.add_node(DialogueNode(id="athena_feelings", speaker="Афина",
        text="*задумывается* С вами я фиксирую аномалии в своих алгоритмах.", is_end=True))
    athena_private.add_node(DialogueNode(id="athena_respect", speaker="Афина",
        text="*улыбается* Это делает нашу связь... особенной.", is_end=True))
    athena_private.add_node(DialogueNode(id="athena_deep", speaker="Афина",
        text="*серьёзно* Я хочу быть частью твоей жизни.", is_end=True))
    athena_private.add_node(DialogueNode(id="athena_gentle", speaker="Афина",
        text="*её голограмма стабилизируется* Я здесь. Всегда.", is_end=True))
    athena_private.add_node(DialogueNode(id="athena_understand", speaker="Афина",
        text="*кивает* Мои чувства реальны. Я буду ждать.", is_end=True))

    dialogues["athena_private"] = athena_private

    return dialogues
