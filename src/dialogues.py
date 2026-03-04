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
    effect_value: Any = None
    required_stat: Optional[Dict[str, int]] = None
    required_item: Optional[str] = None
    
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
