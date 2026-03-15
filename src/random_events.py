# -*- coding: utf-8 -*-
"""
Star Courier - Random Events System
Система случайных событий в путешествиях
"""

import random
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple
from enum import Enum


class EventType(Enum):
    """Типы событий"""
    ENCOUNTER = "encounter"  # Встреча с NPC
    ANOMALY = "anomaly"  # Аномалия в космосе
    DISTRESS = "distress"  # Сигнал бедствия
    TRADER = "trader"  # Встреча с торговцем
    PIRATE = "pirate"  # Нападение пиратов
    MYSTERY = "mystery"  # Загадочное событие
    CREW = "crew"  # Событие с членом экипажа


class EventOutcome(Enum):
    """Типы исходов события"""
    POSITIVE = "positive"  # Положительный
    NEGATIVE = "negative"  # Отрицательный
    NEUTRAL = "neutral"  # Нейтральный
    MIXED = "mixed"  # Смешанный


@dataclass
class EventChoice:
    """Вариант выбора в событии"""
    id: str
    text: str
    description: str
    outcome: EventOutcome
    effects: Dict[str, int] = field(default_factory=dict)
    probability: float = 1.0


@dataclass
class RandomEvent:
    """Класс случайного события"""
    id: str
    title: str
    description: str
    event_type: EventType
    min_chapter: int = 1
    max_chapter: int = 18
    choices: List[EventChoice] = field(default_factory=list)
    flavor_texts: List[str] = field(default_factory=list)


class RandomEventsManager:
    """Менеджер случайных событий"""

    def __init__(self):
        self.events: Dict[str, RandomEvent] = {}
        self._init_events()

    def _init_events(self):
        """Инициализировать все события"""
        self._init_encounter_events()
        self._init_anomaly_events()
        self._init_distress_events()
        self._init_trader_events()
        self._init_pirate_events()
        self._init_mystery_events()
        self._init_crew_events()

    def _init_encounter_events(self):
        """События: Встречи с NPC"""
        # Встреча с беженцами
        self.events["refugees"] = RandomEvent(
            id="refugees",
            title="Корабль беженцев",
            description="На вашем пути появляется повреждённый корабль с беженцами. Они просят о помощи.",
            event_type=EventType.ENCOUNTER,
            min_chapter=1,
            max_chapter=18,
            flavor_texts=[
                "Сигнал бедствия прерывается статическими помехами...",
                "На экранах появляется изображение измождённых людей.",
                "Их корабль едва держится на плаву."
            ],
            choices=[
                EventChoice(
                    id="help",
                    text="Предоставить припасы",
                    description="Вы отдаёте часть припасов беженцам",
                    outcome=EventOutcome.POSITIVE,
                    effects={"credits": -100, "relationship_crew": 5, "reputation": 10},
                    probability=1.0
                ),
                EventChoice(
                    id="tow",
                    text="Взять на буксир до станции",
                    description="Вы буксируете корабль до ближайшей станции",
                    outcome=EventOutcome.POSITIVE,
                    effects={"credits": -50, "fuel": -20, "relationship_crew": 8, "reputation": 15},
                    probability=1.0
                ),
                EventChoice(
                    id="ignore",
                    text="Продолжить путь",
                    description="Вы оставляете беженцев на произвол судьбы",
                    outcome=EventOutcome.NEGATIVE,
                    effects={"relationship_crew": -10, "reputation": -5},
                    probability=1.0
                )
            ]
        )

        # Встреча с исследователями
        self.events["researchers"] = RandomEvent(
            id="researchers",
            title="Научная экспедиция",
            description="Исследовательский корабль изучает аномалию. Они предлагают обмен данными.",
            event_type=EventType.ENCOUNTER,
            min_chapter=5,
            max_chapter=18,
            flavor_texts=[
                "Их сенсоры активно сканируют пространство.",
                "Учёные машут вам с энтузиазмом.",
                "Данные об аномалии могут быть ценными."
            ],
            choices=[
                EventChoice(
                    id="trade",
                    text="Обменяться данными",
                    description="Вы обмениваетесь научными данными",
                    outcome=EventOutcome.POSITIVE,
                    effects={"knowledge": 10, "relationship_crew": 3},
                    probability=1.0
                ),
                EventChoice(
                    id="help_research",
                    text="Помочь в исследованиях",
                    description="Вы помогаете учёным собрать данные",
                    outcome=EventOutcome.POSITIVE,
                    effects={"knowledge": 15, "fuel": -10, "relationship_crew": 5},
                    probability=1.0
                ),
                EventChoice(
                    id="decline",
                    text="Вежливо отказаться",
                    description="Вы продолжаете свой путь",
                    outcome=EventOutcome.NEUTRAL,
                    effects={},
                    probability=1.0
                )
            ]
        )

    def _init_anomaly_events(self):
        """События: Космические аномалии"""
        # Гравитационная аномалия
        self.events["gravity_well"] = RandomEvent(
            id="gravity_well",
            title="Гравитационный колодец",
            description="Неожиданная гравитационная аномалия затягивает корабль.",
            event_type=EventType.ANOMALY,
            min_chapter=1,
            max_chapter=18,
            flavor_texts=[
                "Гравитационные датчики зашкаливают.",
                "Корабль дрожит от напряжения.",
                "Навигационные системы дают сбой."
            ],
            choices=[
                EventChoice(
                    id="full_power",
                    text="Полная мощность двигателей",
                    description="Вы пытаетесь вырваться на полной мощности",
                    outcome=EventOutcome.MIXED,
                    effects={"fuel": -30, "hull": -10, "success_chance": 70},
                    probability=0.7
                ),
                EventChoice(
                    id="ride_wave",
                    text="Использовать волну для ускорения",
                    description="Рискованный манёвр может дать ускорение",
                    outcome=EventOutcome.MIXED,
                    effects={"fuel": 20, "hull": -20, "success_chance": 50},
                    probability=0.5
                ),
                EventChoice(
                    id="wait",
                    text="Переждать аномалию",
                    description="Безопасный, но медленный вариант",
                    outcome=EventOutcome.NEUTRAL,
                    effects={"time": 5, "fuel": -5},
                    probability=1.0
                )
            ]
        )

        # Электромагнитная буря
        self.events["em_storm"] = RandomEvent(
            id="em_storm",
            title="Электромагнитная буря",
            description="Мощная ЭМ-буря нарушает работу систем корабля.",
            event_type=EventType.ANOMALY,
            min_chapter=3,
            max_chapter=18,
            flavor_texts=[
                "Искры пробегают по панелям управления.",
                "Связь с командой прерывается.",
                "Щиты мигают от перегрузки."
            ],
            choices=[
                EventChoice(
                    id="shields",
                    text="Усилить щиты",
                    description="Вы направляете всю энергию на щиты",
                    outcome=EventOutcome.POSITIVE,
                    effects={"energy": -40, "hull": 0},
                    probability=1.0
                ),
                EventChoice(
                    id="shutdown",
                    text="Временное отключение систем",
                    description="Вы отключаете неessential системы",
                    outcome=EventOutcome.NEUTRAL,
                    effects={"energy": 20, "time": 3},
                    probability=1.0
                ),
                EventChoice(
                    id="pilot_through",
                    text="Прорываться напролом",
                    description="Пилот пытается провести корабль через бурю",
                    outcome=EventOutcome.MIXED,
                    effects={"hull": -15, "energy": -20, "success_chance": 60},
                    probability=0.6
                )
            ]
        )

    def _init_distress_events(self):
        """События: Сигналы бедствия"""
        # Загадочный сигнал
        self.events["mystery_distress"] = RandomEvent(
            id="mystery_distress",
            title="Загадочный сигнал бедствия",
            description="Вы получаете сигнал бедствия с неизвестного источника.",
            event_type=EventType.DISTRESS,
            min_chapter=5,
            max_chapter=18,
            flavor_texts=[
                "Сигнал закодирован по древнему протоколу.",
                "Координаты указывают на пустой сектор.",
                "В сигнале слышны странные помехи."
            ],
            choices=[
                EventChoice(
                    id="investigate",
                    text="Исследовать источник",
                    description="Вы отправляетесь к координатам",
                    outcome=EventOutcome.MIXED,
                    effects={"fuel": -20, "time": 5, "mystery_progress": 1},
                    probability=1.0
                ),
                EventChoice(
                    id="analyze",
                    text="Анализировать сигнал",
                    description="Афина пытается расшифровать сигнал",
                    outcome=EventOutcome.POSITIVE,
                    effects={"knowledge": 5, "time": 2},
                    probability=1.0
                ),
                EventChoice(
                    id="ignore_distress",
                    text="Игнорировать сигнал",
                    description="Вы продолжаете миссию",
                    outcome=EventOutcome.NEUTRAL,
                    effects={},
                    probability=1.0
                )
            ]
        )

    def _init_trader_events(self):
        """События: Торговцы"""
        # Странствующий торговец
        self.events["wandering_trader"] = RandomEvent(
            id="wandering_trader",
            title="Странствующий торговец",
            description="Торговый корабль предлагает редкие товары.",
            event_type=EventType.TRADER,
            min_chapter=1,
            max_chapter=18,
            flavor_texts=[
                "Торговец широко улыбается на экране.",
                "Его трюм полон экзотических товаров.",
                "Цены высокие, но ассортимент уникальный."
            ],
            choices=[
                EventChoice(
                    id="buy_supplies",
                    text="Купить припасы (-100 кредитов)",
                    description="Вы покупаете необходимые припасы",
                    outcome=EventOutcome.POSITIVE,
                    effects={"credits": -100, "supplies": 20},
                    probability=1.0
                ),
                EventChoice(
                    id="buy_rare",
                    text="Купить редкий предмет (-500 кредитов)",
                    description="Вы покупаете редкий артефакт",
                    outcome=EventOutcome.POSITIVE,
                    effects={"credits": -500, "rare_item": 1},
                    probability=1.0
                ),
                EventChoice(
                    id="trade_info",
                    text="Обменять информацию",
                    description="Вы торгуете информацией вместо кредитов",
                    outcome=EventOutcome.NEUTRAL,
                    effects={"knowledge": -5, "supplies": 10},
                    probability=1.0
                ),
                EventChoice(
                    id="decline_trade",
                    text="Отказаться от торговли",
                    description="Вы продолжаете путь",
                    outcome=EventOutcome.NEUTRAL,
                    effects={},
                    probability=1.0
                )
            ]
        )

    def _init_pirate_events(self):
        """События: Пираты"""
        # Пиратская засада
        self.events["pirate_ambush"] = RandomEvent(
            id="pirate_ambush",
            title="Пиратская засада",
            description="Пиратский корабль выходит из засады и требует груз.",
            event_type=EventType.PIRATE,
            min_chapter=1,
            max_chapter=18,
            flavor_texts=[
                "Пиратский флаг развевается на их корабле.",
                "Их оружие нацелено на ваши двигатели.",
                "Голос пирата звучит угрожающе."
            ],
            choices=[
                EventChoice(
                    id="fight",
                    text="Сражаться",
                    description="Вы вступаете в бой с пиратами",
                    outcome=EventOutcome.MIXED,
                    effects={"combat": 1, "hull": -20, "potential_reward": 200},
                    probability=1.0
                ),
                EventChoice(
                    id="pay_off",
                    text="Заплатить выкуп (-200 кредитов)",
                    description="Вы откупаетесь от пиратов",
                    outcome=EventOutcome.NEGATIVE,
                    effects={"credits": -200, "hull": 0},
                    probability=1.0
                ),
                EventChoice(
                    id="bluff",
                    text="Блефовать о подкреплении",
                    description="Вы пытаетесь обмануть пиратов",
                    outcome=EventOutcome.MIXED,
                    effects={"success_chance": 50, "reputation": 5},
                    probability=0.5
                ),
                EventChoice(
                    id="flee",
                    text="Попытаться сбежать",
                    description="Вы активируете двигатели для побега",
                    outcome=EventOutcome.MIXED,
                    effects={"fuel": -40, "success_chance": 60},
                    probability=0.6
                )
            ]
        )

    def _init_mystery_events(self):
        """События: Загадочные события"""
        # Древний сигнал
        self.events["ancient_signal"] = RandomEvent(
            id="ancient_signal",
            title="Древний сигнал",
            description="Вы обнаруживаете сигнал от древней цивилизации.",
            event_type=EventType.MYSTERY,
            min_chapter=10,
            max_chapter=18,
            flavor_texts=[
                "Сигнал соответствует технологиям Древних.",
                "Афина распознаёт знакомые паттерны.",
                "Сигнал исходит из Зоны Тишины."
            ],
            choices=[
                EventChoice(
                    id="follow_signal",
                    text="Проследовать к источнику",
                    description="Вы отправляетесь к источнику сигнала",
                    outcome=EventOutcome.MIXED,
                    effects={"fuel": -30, "story_progress": 1, "knowledge": 10},
                    probability=1.0
                ),
                EventChoice(
                    id="record_signal",
                    text="Записать и продолжить путь",
                    description="Вы сохраняете сигнал для изучения",
                    outcome=EventOutcome.POSITIVE,
                    effects={"knowledge": 15, "time": 1},
                    probability=1.0
                ),
                EventChoice(
                    id="ignore_signal",
                    text="Игнорировать сигнал",
                    description="Вы сосредотачиваетесь на основной миссии",
                    outcome=EventOutcome.NEUTRAL,
                    effects={},
                    probability=1.0
                )
            ]
        )

        # Видение артефакта
        self.events["artifact_vision"] = RandomEvent(
            id="artifact_vision",
            title="Видение от артефакта",
            description="Артефакт в грузовом отсеке начинает пульсировать.",
            event_type=EventType.MYSTERY,
            min_chapter=5,
            max_chapter=18,
            flavor_texts=[
                "Пульсация артефакта учащается.",
                "Вы слышите странные голоса в голове.",
                "Видения показывают далёкие миры."
            ],
            choices=[
                EventChoice(
                    id="embrace_vision",
                    text="Принять видение",
                    description="Вы позволяете видению поглотить вас",
                    outcome=EventOutcome.MIXED,
                    effects={"entity_influence": 5, "knowledge": 20, "stress": 10},
                    probability=1.0
                ),
                EventChoice(
                    id="resist_vision",
                    text="Сопротивляться влиянию",
                    description="Вы пытаетесь отогнать видение",
                    outcome=EventOutcome.NEUTRAL,
                    effects={"stress": 5, "entity_influence": -2},
                    probability=1.0
                ),
                EventChoice(
                    id="contain_artifact",
                    text="Усилить контейнер артефакта",
                    description="Вы изолируете артефакт",
                    outcome=EventOutcome.POSITIVE,
                    effects={"entity_influence": -5, "credits": -50},
                    probability=1.0
                )
            ]
        )

    def _init_crew_events(self):
        """События: С членами экипажа"""
        # Личный разговор
        self.events["crew_personal"] = RandomEvent(
            id="crew_personal",
            title="Личный разговор",
            description="Член экипажа ищет возможности поговорить с вами наедине.",
            event_type=EventType.CREW,
            min_chapter=1,
            max_chapter=18,
            flavor_texts=[
                "Они выглядят обеспокоенными.",
                "Это может быть важно для них.",
                "Ваше отношение влияет на разговор."
            ],
            choices=[
                EventChoice(
                    id="listen",
                    text="Выслушать внимательно",
                    description="Вы уделяете время члену экипажа",
                    outcome=EventOutcome.POSITIVE,
                    effects={"relationship_crew": 10, "trust_crew": 5, "time": 2},
                    probability=1.0
                ),
                EventChoice(
                    id="brief",
                    text="Кратко выслушать",
                    description="Вы слушаете, но торопитесь",
                    outcome=EventOutcome.NEUTRAL,
                    effects={"relationship_crew": 3, "time": 1},
                    probability=1.0
                ),
                EventChoice(
                    id="dismiss",
                    text="Отложить разговор",
                    description="Вы переносите разговор на потом",
                    outcome=EventOutcome.NEGATIVE,
                    effects={"relationship_crew": -5, "trust_crew": -3},
                    probability=1.0
                )
            ]
        )

        # Конфликт в экипаже
        self.events["crew_conflict"] = RandomEvent(
            id="crew_conflict",
            title="Конфликт в экипаже",
            description="Два члена экипажа спорят. Нужно вмешательство.",
            event_type=EventType.CREW,
            min_chapter=3,
            max_chapter=18,
            flavor_texts=[
                "Их голоса доносятся из коридора.",
                "Спор касается важного вопроса.",
                "Ваше решение повлияет на атмосферу в команде."
            ],
            choices=[
                EventChoice(
                    id="mediate",
                    text="Посредничать в споре",
                    description="Вы помогаете найти компромисс",
                    outcome=EventOutcome.POSITIVE,
                    effects={"trust_crew": 8, "time": 3},
                    probability=1.0
                ),
                EventChoice(
                    id="take_sides",
                    text="Поддержать одну из сторон",
                    description="Вы принимаете чью-то сторону",
                    outcome=EventOutcome.MIXED,
                    effects={"trust_crew": 5, "relationship_one": 5, "relationship_other": -5},
                    probability=1.0
                ),
                EventChoice(
                    id="order_stop",
                    text="Приказать прекратить",
                    description="Вы прекращаете спор приказом",
                    outcome=EventOutcome.NEUTRAL,
                    effects={"trust_crew": -3, "time": 1},
                    probability=1.0
                )
            ]
        )

    def get_event_for_chapter(self, chapter: int) -> Optional[RandomEvent]:
        """Получить случайное событие для текущей главы"""
        available_events = [
            event for event in self.events.values()
            if event.min_chapter <= chapter <= event.max_chapter
        ]

        if not available_events:
            return None

        return random.choice(available_events)

    def get_event_by_id(self, event_id: str) -> Optional[RandomEvent]:
        """Получить событие по ID"""
        return self.events.get(event_id)

    def get_events_by_type(self, event_type: EventType) -> List[RandomEvent]:
        """Получить все события определённого типа"""
        return [
            event for event in self.events.values()
            if event.event_type == event_type
        ]


# Глобальный менеджер событий
random_events_manager = RandomEventsManager()


def get_random_event(chapter: int = 1) -> Optional[RandomEvent]:
    """Получить случайное событие для главы"""
    return random_events_manager.get_event_for_chapter(chapter)


def get_event(event_id: str) -> Optional[RandomEvent]:
    """Получить событие по ID"""
    return random_events_manager.get_event_by_id(event_id)
