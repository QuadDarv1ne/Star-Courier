# -*- coding: utf-8 -*-
"""
Star Courier - Relationship System Enhancements
Улучшения системы отношений: подарки, совместные миссии, события
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum
import random


class GiftType(Enum):
    """Типы подарков"""
    FLOWER = "flower"  # Цветы
    JEWELRY = "jewelry"  # Украшения
    BOOK = "book"  # Книги
    ARTIFACT = "artifact"  # Артефакты
    FOOD = "food"  # Еда/Напитки
    TECHNOLOGY = "technology"  # Технологии
    MEMORY = "memory"  # Воспоминания
    CRAFT = "craft"  # Рукоделие


class RelationshipLevel(Enum):
    """Уровни отношений"""
    STRANGER = "stranger"  # 0-19: Незнакомец
    ACQUAINTANCE = "acquaintance"  # 20-39: Знакомый
    FRIEND = "friend"  # 40-59: Друг
    CLOSE_FRIEND = "close_friend"  # 60-79: Близкий друг
    ROMANTIC = "romantic"  # 80-99: Романтика
    PARTNER = "partner"  # 100: Партнёр


@dataclass
class Gift:
    """Класс подарка"""
    id: str
    name: str
    description: str
    gift_type: GiftType
    value: int  # Стоимость в кредитах
    relationship_effect: int  # Эффект на отношения
    preferred_by: List[str] = field(default_factory=list)  # Кто любит
    disliked_by: List[str] = field(default_factory=list)  # Кто не любит
    flavor_text: str = ""


@dataclass
class JointMission:
    """Совместная миссия с членом экипажа"""
    id: str
    title: str
    description: str
    required_character: str
    min_relationship: int
    duration: int  # В ходах/часах
    rewards: Dict[str, int] = field(default_factory=dict)
    relationship_reward: int = 0
    trust_reward: int = 0
    choices: List[Dict] = field(default_factory=list)
    completed: bool = False


@dataclass
class RelationshipEvent:
    """Событие в отношениях"""
    id: str
    character_id: str
    title: str
    description: str
    min_relationship: int
    trigger_conditions: Dict[str, any] = field(default_factory=dict)
    event_text: str = ""
    choices: List[Dict] = field(default_factory=list)
    effects: Dict[str, int] = field(default_factory=dict)


class RelationshipEnhancementManager:
    """Менеджер улучшений отношений"""

    def __init__(self):
        self.gifts: Dict[str, Gift] = {}
        self.missions: Dict[str, JointMission] = {}
        self.events: Dict[str, RelationshipEvent] = {}
        self.character_preferences: Dict[str, Dict] = {}
        self._init_gifts()
        self._init_missions()
        self._init_events()
        self._init_preferences()

    def _init_gifts(self):
        """Инициализировать подарки"""
        # === ЦВЕТЫ ===
        self.gifts["orchid"] = Gift(
            id="orchid",
            name="Космическая орхидея",
            description="Редкий цветок, выращенный в нулевой гравитации.",
            gift_type=GiftType.FLOWER,
            value=150,
            relationship_effect=15,
            preferred_by=["irina_lebedeva", "maria", "anna"],
            disliked_by=["nadezhda", "zara"],
            flavor_text="Нежный лепесток светится в темноте."
        )

        self.gifts["nebula_rose"] = Gift(
            id="nebula_rose",
            name="Туманная роза",
            description="Роза с лепестками цвета далёкой туманности.",
            gift_type=GiftType.FLOWER,
            value=200,
            relationship_effect=20,
            preferred_by=["irina_lebedeva", "maria", "rina_mirai"],
            disliked_by=["zara", "veronika"],
            flavor_text="Её аромат напоминает о далёких мирах."
        )

        # === УКРАШЕНИЯ ===
        self.gifts["quantum_necklace"] = Gift(
            id="quantum_necklace",
            name="Квантовое ожерелье",
            description="Ожерелье с квантовым кристаллом, меняющим цвет.",
            gift_type=GiftType.JEWELRY,
            value=500,
            relationship_effect=30,
            preferred_by=["irina_lebedeva", "rina_mirai", "mia"],
            disliked_by=["nadezhda"],
            flavor_text="Кристалл пульсирует в такт сердцу."
        )

        self.gifts["star_bracelet"] = Gift(
            id="star_bracelet",
            name="Звёздный браслет",
            description="Браслет с миниатюрной проекцией звёздного неба.",
            gift_type=GiftType.JEWELRY,
            value=400,
            relationship_effect=25,
            preferred_by=["anna", "maria", "kira"],
            disliked_by=["zara"],
            flavor_text="Звёзды на браслете движутся в реальном времени."
        )

        # === КНИГИ ===
        self.gifts["ancient_archive"] = Gift(
            id="ancient_archive",
            name="Древний архив",
            description="Цифровая копия утраченных знаний Древних.",
            gift_type=GiftType.BOOK,
            value=600,
            relationship_effect=25,
            preferred_by=["irina_lebedeva", "athena", "vera"],
            flavor_text="Страницы мерцают голографическим светом."
        )

        self.gifts["poetry_collection"] = Gift(
            id="poetry_collection",
            name="Сборник поэзии",
            description="Классическая поэзия Земли в кожаном переплёте.",
            gift_type=GiftType.BOOK,
            value=100,
            relationship_effect=15,
            preferred_by=["maria", "anna", "rina_mirai"],
            flavor_text="Стихи о любви и звёздах."
        )

        # === АРТЕФАКТЫ ===
        self.gifts["resonance_crystal"] = Gift(
            id="resonance_crystal",
            name="Резонирующий кристалл",
            description="Кристалл, вибрирующий в унисон с энергией носителя.",
            gift_type=GiftType.ARTIFACT,
            value=800,
            relationship_effect=35,
            preferred_by=["irina_lebedeva", "athena", "echo"],
            flavor_text="Кристалл поёт на неслышимой частоте."
        )

        self.gifts["memory_sphere"] = Gift(
            id="memory_sphere",
            name="Сфера воспоминаний",
            description="Устройство, хранящее записи прошлого.",
            gift_type=GiftType.ARTIFACT,
            value=700,
            relationship_effect=30,
            preferred_by=["athena", "echo", "veronika"],
            flavor_text="Внутри сферы кружатся воспоминания."
        )

        # === ЕДА/НАПИТКИ ===
        self.gifts["synthetic_wine"] = Gift(
            id="synthetic_wine",
            name="Синтетическое вино",
            description="Элитное вино, созданное молекулярной гастрономией.",
            gift_type=GiftType.FOOD,
            value=250,
            relationship_effect=20,
            preferred_by=["irina_lebedeva", "marcus_ride", "volkov"],
            flavor_text="Вкус напоминает о виноградниках Прованса."
        )

        self.gifts["space_chocolate"] = Gift(
            id="space_chocolate",
            name="Космический шоколад",
            description="Шоколад с невесомости — тает по-особенному.",
            gift_type=GiftType.FOOD,
            value=80,
            relationship_effect=12,
            preferred_by=["maria", "anna", "kira", "mia"],
            flavor_text="Шоколад левитирует над тарелкой."
        )

        # === ТЕХНОЛОГИИ ===
        self.gifts["neural_interface"] = Gift(
            id="neural_interface",
            name="Нейроинтерфейс",
            description="Персональный интерфейс для прямого подключения к кораблю.",
            gift_type=GiftType.TECHNOLOGY,
            value=900,
            relationship_effect=28,
            preferred_by=["athena", "ekaterina", "sergey"],
            flavor_text="Интерфейс мягко касается висков."
        )

        self.gifts["multi_tool"] = Gift(
            id="multi_tool",
            name="Мультиинструмент инженера",
            description="Профессиональный инструмент с ИИ-помощником.",
            gift_type=GiftType.TECHNOLOGY,
            value=350,
            relationship_effect=18,
            preferred_by=["sergey", "dmitry", "nadezhda"],
            flavor_text="Инструмент сам подстраивается под задачу."
        )

        # === ВОСПОМИНАНИЯ ===
        self.gifts["holo_photo"] = Gift(
            id="holo_photo",
            name="Голографическое фото",
            description="Снимок важного момента в виде голограммы.",
            gift_type=GiftType.MEMORY,
            value=50,
            relationship_effect=25,
            preferred_by=["maria", "anna", "rina_mirai", "mia"],
            flavor_text="На фото вы вместе смеётесь."
        )

        self.gifts["memory_chip"] = Gift(
            id="memory_chip",
            name="Чип памяти",
            description="Запись совместного приключения.",
            gift_type=GiftType.MEMORY,
            value=100,
            relationship_effect=20,
            preferred_by=["athena", "veronika", "kira"],
            flavor_text="Воспоминания проигрываются как сон."
        )

        # === РУКОДЕЛИЕ ===
        self.gifts["handmade_scarf"] = Gift(
            id="handmade_scarf",
            name="Шарф ручной работы",
            description="Тёплый шарф, связанный вручную.",
            gift_type=GiftType.CRAFT,
            value=120,
            relationship_effect=22,
            preferred_by=["maria", "anna"],
            flavor_text="Каждая петля сделана с заботой."
        )

        self.gifts["engraved_dogtag"] = Gift(
            id="engraved_dogtag",
            name="Гравированный жетон",
            description="Военный жетон с личной гравировкой.",
            gift_type=GiftType.CRAFT,
            value=150,
            relationship_effect=20,
            preferred_by=["nadezhda", "zara", "marcus_ride"],
            flavor_text="На жетоне выгравировано: «Всегда с тобой»."
        )

    def _init_missions(self):
        """Инициализировать совместные миссии"""
        # === МИССИЯ: Ирина ===
        self.missions["irina_lab"] = JointMission(
            id="irina_lab",
            title="Лабораторный эксперимент",
            description="Ирина просит помощи в опасном эксперименте с артефактом.",
            required_character="irina_lebedeva",
            min_relationship=50,
            duration=3,
            rewards={"credits": 300, "experience": 200, "knowledge": 50},
            relationship_reward=15,
            trust_reward=10,
            choices=[
                {
                    "text": "Помочь с настройкой оборудования",
                    "effect": {"success_chance": 80, "bonus": 10},
                    "outcome": "Эксперимент прошёл успешно!"
                },
                {
                    "text": "Наблюдать со стороны",
                    "effect": {"success_chance": 60, "bonus": 0},
                    "outcome": "Ирина справилась сама, но ценит вашу поддержку."
                }
            ]
        )

        # === МИССИЯ: Алия ===
        self.missions["alia_flight"] = JointMission(
            id="alia_flight",
            title="Пилотаж через аномалию",
            description="Алия предлагает вместе пройти через опасную аномалию.",
            required_character="alia_naar",
            min_relationship=45,
            duration=2,
            rewards={"credits": 400, "experience": 250, "fuel": 50},
            relationship_reward=12,
            trust_reward=15,
            choices=[
                {
                    "text": "Довериться пилоту",
                    "effect": {"success_chance": 90},
                    "outcome": "Алия провела корабль как по маслу!"
                },
                {
                    "text": "Взять управление на себя",
                    "effect": {"success_chance": 70},
                    "outcome": "Вы справились, но Алия немного обижена."
                }
            ]
        )

        # === МИССИЯ: Рина ===
        self.missions["rina_navigation"] = JointMission(
            id="rina_navigation",
            title="Прокладка нового маршрута",
            description="Рина нашла короткий путь через неизведанный сектор.",
            required_character="rina_mirai",
            min_relationship=40,
            duration=4,
            rewards={"credits": 500, "experience": 300, "time_saved": 10},
            relationship_reward=18,
            trust_reward=12,
            choices=[
                {
                    "text": "Поддержать решение Рины",
                    "effect": {"success_chance": 85},
                    "outcome": "Маршрут оказался безопасным и быстрым!"
                },
                {
                    "text": "Предложить альтернативу",
                    "effect": {"success_chance": 65},
                    "outcome": "Ваш путь длиннее, но Рина оценила участие."
                }
            ]
        )

        # === МИССИЯ: Мария ===
        self.missions["maria_medical"] = JointMission(
            id="maria_medical",
            title="Медицинская эвакуация",
            description="Мария требует срочной доставки медикаментов на станцию.",
            required_character="maria",
            min_relationship=35,
            duration=3,
            rewards={"credits": 350, "experience": 200, "reputation": 20},
            relationship_reward=15,
            trust_reward=10,
            choices=[
                {
                    "text": "Срочно доставить груз",
                    "effect": {"success_chance": 95, "fuel_cost": 30},
                    "outcome": "Вы спасли жизни! Мария благодарна."
                },
                {
                    "text": "Сначала завершить текущие дела",
                    "effect": {"success_chance": 70, "relationship_penalty": -5},
                    "outcome": "Груз доставлен, но с опозданием."
                }
            ]
        )

        # === МИССИЯ: Мия ===
        self.missions["mia_tactics"] = JointMission(
            id="mia_tactics",
            title="Тактическая симуляция",
            description="Мия предлагает тренировочный бой для улучшения координации.",
            required_character="mia",
            min_relationship=40,
            duration=2,
            rewards={"credits": 200, "experience": 300, "combat_bonus": 10},
            relationship_reward=12,
            trust_reward=8,
            choices=[
                {
                    "text": "Принять вызов",
                    "effect": {"success_chance": 75, "combat_xp": 50},
                    "outcome": "Отличная тренировка! Мия впечатлена."
                },
                {
                    "text": "Наблюдать за симуляцией",
                    "effect": {"success_chance": 100, "knowledge": 20},
                    "outcome": "Вы изучили тактику Мии."
                }
            ]
        )

        # === МИССИЯ: Анна ===
        self.missions["anna_intuition"] = JointMission(
            id="anna_intuition",
            title="Интуитивный путь",
            description="Анна чувствует безопасный путь через опасную зону.",
            required_character="anna",
            min_relationship=50,
            duration=3,
            rewards={"credits": 400, "experience": 250, "discovery": 1},
            relationship_reward=20,
            trust_reward=15,
            choices=[
                {
                    "text": "Довериться интуиции Анны",
                    "effect": {"success_chance": 80},
                    "outcome": "Анна привела вас к красивому секретному месту!"
                },
                {
                    "text": "Настаивать на стандартном маршруте",
                    "effect": {"success_chance": 90, "relationship_penalty": -3},
                    "outcome": "Путь безопасен, но Анна расстроена."
                }
            ]
        )

        # === МИССИЯ: Надежда ===
        self.missions["nadezhda_security"] = JointMission(
            id="nadezhda_security",
            title="Проверка безопасности",
            description="Надежда хочет проверить все системы безопасности корабля.",
            required_character="nadezhda",
            min_relationship=30,
            duration=2,
            rewards={"credits": 250, "experience": 150, "security_boost": 15},
            relationship_reward=10,
            trust_reward=12,
            choices=[
                {
                    "text": "Помочь в проверке",
                    "effect": {"success_chance": 95},
                    "outcome": "Системы в идеальном состоянии!"
                },
                {
                    "text": "Разрешить работать самостоятельно",
                    "effect": {"success_chance": 85},
                    "outcome": "Надежда справилась отлично."
                }
            ]
        )

        # === МИССИЯ: Вероника ===
        self.missions["veronika_info"] = JointMission(
            id="veronika_info",
            title="Тайная встреча",
            description="Вероника организует встречу с информатором в баре на станции.",
            required_character="veronika",
            min_relationship=45,
            duration=3,
            rewards={"credits": 600, "experience": 300, "intel": 50},
            relationship_reward=18,
            trust_reward=10,
            choices=[
                {
                    "text": "Идти вместе с Вероникой",
                    "effect": {"success_chance": 85},
                    "outcome": "Информация получена! Вероника довольна."
                },
                {
                    "text": "Подождать снаружи",
                    "effect": {"success_chance": 70, "relationship_penalty": -5},
                    "outcome": "Вероника справилась, но хотела вашей поддержки."
                }
            ]
        )

        # === МИССИЯ: Зара ===
        self.missions["zara_combat"] = JointMission(
            id="zara_combat",
            title="Боевая тренировка",
            description="Зара предлагает спарринг для улучшения боевых навыков.",
            required_character="zara",
            min_relationship=40,
            duration=2,
            rewards={"credits": 200, "experience": 350, "combat_bonus": 15},
            relationship_reward=12,
            trust_reward=10,
            choices=[
                {
                    "text": "Принять вызов",
                    "effect": {"success_chance": 60, "combat_xp": 80},
                    "outcome": "Жёсткий бой! Зара уважает вас."
                },
                {
                    "text": "Отказаться от боя",
                    "effect": {"success_chance": 100, "relationship_penalty": -8},
                    "outcome": "Зара разочарована, но понимает."
                }
            ]
        )

        # === МИССИЯ: Кира ===
        self.missions["kira_delivery"] = JointMission(
            id="kira_delivery",
            title="Срочная доставка",
            description="Кира просит помочь с доставкой важного груза.",
            required_character="kira",
            min_relationship=35,
            duration=3,
            rewards={"credits": 500, "experience": 250, "reputation": 15},
            relationship_reward=15,
            trust_reward=10,
            choices=[
                {
                    "text": "Помочь с доставкой",
                    "effect": {"success_chance": 90},
                    "outcome": "Груз доставлен вовремя! Кира рада."
                },
                {
                    "text": "Предложить альтернативный маршрут",
                    "effect": {"success_chance": 75, "time_saved": 5},
                    "outcome": "Вы сэкономили время! Кира впечатлена."
                }
            ]
        )

    def _init_events(self):
        """Инициализировать события отношений"""
        # Событие: Ужин при свечах
        self.events["dinner_date"] = RelationshipEvent(
            id="dinner_date",
            character_id="irina_lebedeva",
            title="Ужин в лаборатории",
            description="Ирина приглашает вас на ужин после работы.",
            min_relationship=60,
            trigger_conditions={"location": "lab", "time": "evening"},
            event_text="""
  Лаборатория преображена. На столе — простая еда,
  свечи, приглушённый свет. Ирина нервничает.

  — Я подумала... мы так много работаем. Нужно иногда отдыхать.
            """,
            choices=[
                {
                    "text": "«Это прекрасно, Ирина»",
                    "effects": {"relationship": 20, "romance_progress": 15}
                },
                {
                    "text": "«Спасибо за заботу»",
                    "effects": {"relationship": 12, "trust": 8}
                }
            ]
        )

        # Событие: Прогулка по кораблю
        self.events["ship_walk"] = RelationshipEvent(
            id="ship_walk",
            character_id="maria",
            title="Ночная прогулка",
            description="Мария не спит и предлагает прогуляться по кораблю.",
            min_relationship=50,
            trigger_conditions={"time": "night"},
            event_text="""
  Коридоры пусты. Мария идёт рядом, её шаги тихие.

  — Знаете, в космосе нет настоящих звёзд внутри корабля.
    Только огни других судов...
            """,
            choices=[
                {
                    "text": "«Но у нас есть звёзды в иллюминаторах»",
                    "effects": {"relationship": 18, "romance_progress": 12}
                },
                {
                    "text": "«Вы любите звёзды?»",
                    "effects": {"relationship": 10, "knowledge": 5}
                }
            ]
        )

        # Событие: Танцы в невесомости
        self.events["zero_g_dance"] = RelationshipEvent(
            id="zero_g_dance",
            character_id="rina_mirai",
            title="Танец в невесомости",
            description="Рина предлагает попробовать танец в нулевой гравитации.",
            min_relationship=65,
            trigger_conditions={"location": "gravity_chamber"},
            event_text="""
  Гравитация отключена. Рина парит в воздухе, улыбаясь.

  — Попробуйте... это как полёт, только ближе.
            """,
            choices=[
                {
                    "text": "Протянуть руку и принять приглашение",
                    "effects": {"relationship": 25, "romance_progress": 20}
                },
                {
                    "text": "Наблюдать со стороны",
                    "effects": {"relationship": 8, "trust": 5}
                }
            ]
        )

    def _init_preferences(self):
        """Инициализировать предпочтения персонажей"""
        self.character_preferences = {
            "irina_lebedeva": {
                "favorite_gifts": ["orchid", "nebula_rose", "quantum_necklace", "ancient_archive"],
                "favorite_mission": "irina_lab",
                "personality_traits": ["intellectual", "caring", "shy"],
                "conversation_topics": ["science", "art", "future"]
            },
            "maria": {
                "favorite_gifts": ["orchid", "poetry_collection", "space_chocolate", "handmade_scarf"],
                "favorite_mission": "maria_medical",
                "personality_traits": ["nurturing", "gentle", "empathetic"],
                "conversation_topics": ["medicine", "nature", "dreams"]
            },
            "anna": {
                "favorite_gifts": ["star_bracelet", "poetry_collection", "holo_photo"],
                "favorite_mission": "anna_intuition",
                "personality_traits": ["dreamy", "intuitive", "calm"],
                "conversation_topics": ["space", "mysticism", "beauty"]
            },
            "rina_mirai": {
                "favorite_gifts": ["nebula_rose", "quantum_necklace", "holo_photo"],
                "favorite_mission": "rina_navigation",
                "personality_traits": ["confident", "playful", "skilled"],
                "conversation_topics": ["flying", "adventure", "competition"]
            },
            "mia": {
                "favorite_gifts": ["quantum_necklace", "multi_tool", "holo_photo"],
                "favorite_mission": "mia_tactics",
                "personality_traits": ["analytical", "disciplined", "loyal"],
                "conversation_topics": ["tactics", "strategy", "duty"]
            },
            "nadezhda": {
                "favorite_gifts": ["multi_tool", "engraved_dogtag"],
                "favorite_mission": "nadezhda_security",
                "personality_traits": ["serious", "protective", "honest"],
                "conversation_topics": ["security", "training", "honor"]
            },
            "veronika": {
                "favorite_gifts": ["memory_sphere", "memory_chip", "ancient_archive"],
                "favorite_mission": "veronika_info",
                "personality_traits": ["mysterious", "independent", "clever"],
                "conversation_topics": ["secrets", "politics", "freedom"]
            },
            "zara": {
                "favorite_gifts": ["engraved_dogtag", "resonance_crystal"],
                "favorite_mission": "zara_combat",
                "personality_traits": ["tough", "direct", "honorable"],
                "conversation_topics": ["combat", "honor", "past"]
            },
            "kira": {
                "favorite_gifts": ["star_bracelet", "space_chocolate", "memory_chip"],
                "favorite_mission": "kira_delivery",
                "personality_traits": ["energetic", "optimistic", "free"],
                "conversation_topics": ["travel", "adventure", "freedom"]
            }
        }

    def get_character_preference(self, character_id: str) -> Dict:
        """Получить предпочтения персонажа"""
        return self.character_preferences.get(character_id, {})

    def calculate_gift_effect(self, gift_id: str, character_id: str) -> int:
        """Рассчитать эффект подарка для персонажа"""
        gift = self.gifts.get(gift_id)
        if not gift:
            return 0

        prefs = self.get_character_preference(character_id)
        favorite_gifts = prefs.get("favorite_gifts", [])

        base_effect = gift.relationship_effect

        # Любимый подарок
        if gift_id in favorite_gifts:
            base_effect = int(base_effect * 1.5)

        # Персонаж любит этот тип
        if character_id in gift.preferred_by:
            base_effect += 10

        # Персонаж не любит этот тип
        if character_id in gift.disliked_by:
            base_effect = int(base_effect * 0.5)

        return base_effect

    def get_available_missions(self, character_id: str, relationship: int) -> List[JointMission]:
        """Получить доступные миссии для персонажа"""
        available = []
        for mission in self.missions.values():
            if (mission.required_character == character_id and
                    mission.min_relationship <= relationship and
                    not mission.completed):
                available.append(mission)
        return available

    def complete_mission(self, mission_id: str, choice_index: int = 0) -> Dict:
        """Завершить миссию с выбором"""
        mission = self.missions.get(mission_id)
        if not mission:
            return {"success": False, "error": "Миссия не найдена"}

        if choice_index < 0 or choice_index >= len(mission.choices):
            return {"success": False, "error": "Неверный выбор"}

        choice = mission.choices[choice_index]
        mission.completed = True

        # Проверка успеха
        success_chance = choice["effect"].get("success_chance", 50)
        success = random.randint(1, 100) <= success_chance

        return {
            "success": success,
            "mission": mission,
            "choice": choice,
            "outcome": choice.get("outcome", ""),
            "rewards": mission.rewards if success else {},
            "relationship_reward": mission.relationship_reward if success else 5,
            "trust_reward": mission.trust_reward if success else 3
        }

    def get_available_events(self, character_id: str, relationship: int,
                             location: str = None, time: str = None) -> List[RelationshipEvent]:
        """Получить доступные события отношений"""
        available = []
        for event in self.events.values():
            if event.character_id != character_id:
                continue
            if event.min_relationship > relationship:
                continue

            # Проверка условий
            conditions = event.trigger_conditions
            if conditions.get("location") and location != conditions["location"]:
                continue
            if conditions.get("time") and time != conditions["time"]:
                continue

            available.append(event)

        return available


# Глобальный менеджер
relationship_manager = RelationshipEnhancementManager()


def get_gift(gift_id: str) -> Optional[Gift]:
    """Получить подарок по ID"""
    return relationship_manager.gifts.get(gift_id)


def get_mission(mission_id: str) -> Optional[JointMission]:
    """Получить миссию по ID"""
    return relationship_manager.missions.get(mission_id)


def calculate_gift_effect(gift_id: str, character_id: str) -> int:
    """Рассчитать эффект подарка"""
    return relationship_manager.calculate_gift_effect(gift_id, character_id)
