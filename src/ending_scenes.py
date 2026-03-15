# -*- coding: utf-8 -*-
"""
Star Courier - Ending Scenes System
Система финальных сцен и 3 концовок
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum


class EndingType(Enum):
    """Типы концовок"""
    EXILE = "exile"  # Изгнание Сущности
    TREATY = "treaty"  # Договор с Сущностью
    MERGE = "merge"  # Слияние с Сущностью


class EndingVariation(Enum):
    """Вариации внутри концовок"""
    SOLO = "solo"  # Герой в одиночку
    TOGETHER = "together"  # С романтическим партнёром
    SACRIFICE = "sacrifice"  # Жертва героя
    TEAM = "team"  # С помощью команды


@dataclass
class EndingProgress:
    """Прогресс финальных сцен"""
    ending_chosen: bool = False
    ending_type: Optional[str] = None
    variation_unlocked: Dict[str, bool] = field(default_factory=dict)
    requirements_met: Dict[str, bool] = field(default_factory=dict)

    def to_dict(self) -> Dict:
        """Сериализация"""
        return {
            "ending_chosen": self.ending_chosen,
            "ending_type": self.ending_type,
            "variation_unlocked": self.variation_unlocked,
            "requirements_met": self.requirements_met
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "EndingProgress":
        """Десериализация"""
        return cls(
            ending_chosen=data.get("ending_chosen", False),
            ending_type=data.get("ending_type"),
            variation_unlocked=data.get("variation_unlocked", {}),
            requirements_met=data.get("requirements_met", {})
        )


@dataclass
class EndingScene:
    """Класс финальной сцены"""
    id: str
    ending_type: EndingType
    variation: EndingVariation
    title: str
    description: str
    requirements: Dict
    scene_text: str
    epilogue_text: str
    crew_fate: Dict[str, str]
    galaxy_fate: str

    def to_dict(self) -> Dict:
        """Сериализация в словарь"""
        return {
            "id": self.id,
            "ending_type": self.ending_type.value,
            "variation": self.variation.value,
            "title": self.title,
            "description": self.description,
            "requirements": self.requirements,
            "scene_text": self.scene_text,
            "epilogue_text": self.epilogue_text,
            "crew_fate": self.crew_fate,
            "galaxy_fate": self.galaxy_fate
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "EndingScene":
        """Десериализация из словаря"""
        return cls(
            id=data.get("id", ""),
            ending_type=EndingType(data.get("ending_type", "exile")),
            variation=EndingVariation(data.get("variation", "solo")),
            title=data.get("title", ""),
            description=data.get("description", ""),
            requirements=data.get("requirements", {}),
            scene_text=data.get("scene_text", ""),
            epilogue_text=data.get("epilogue_text", ""),
            crew_fate=data.get("crew_fate", {}),
            galaxy_fate=data.get("galaxy_fate", "")
        )


def create_ending_scenes() -> Dict[str, EndingScene]:
    """Создать все финальные сцены"""
    scenes = {}

    # ============================================
    # КОНЦОВКА 1: ИЗГНАНИЕ
    # ============================================

    # Вариант 1.1: Героическая жертва (одиночка)
    scenes["exile_sacrifice_solo"] = EndingScene(
        id="exile_sacrifice_solo",
        ending_type=EndingType.EXILE,
        variation=EndingVariation.SACRIFICE,
        title="Изгнание: Цена свободы",
        description="Вы жертвуете собой, чтобы изгнать Сущность",
        requirements={
            "ending_choice": "exile",
            "romantic_partner": None,
            "team_loyalty": "any"
        },
        scene_text="""
  Ядро станции пульсирует ослепительным светом. Сущность
  сопротивляется, её тьма заполняет пространство.

  — Чтобы изгнать меня, нужна вечная стража, — говорит Страж.
    — Кто-то должен остаться у якоря. Навсегда.

  Вы смотрите на команду. На друзей, которые прошли с вами
  через всё. И делаете шаг вперёд.

  — Я останусь.

  Афина: «Капитан, нет! Должен быть другой способ!»
  Мия: «Это... это самоубийство.»
  Ирина: «Макс... пожалуйста...»

  Но вы уже касаетесь якоря. Энергия пронзает вас, и вы
  чувствуете, как ваше сознание расширяется, сливаясь с
  системами станции.

  Сущность кричит — звук, который не слышен ушами, но
  ощущается каждой клеткой. Она отступает, изгоняемая из
  этой реальности.

  — Вы победили, — говорит Страж. — Но цена... Вы станете
    частью станции. Вечным стражем.

  Последнее, что вы видите — лица команды. Они плачут.
  Но они живы. Галактика спасена.
        """,
        epilogue_text="""
  ЭПИЛОГ: Вечный Страж

  Прошли годы. Галактика восстановилась после войны с Сущностью.
  «Элея» стала легендой — кораблём, который спас все миры.

  А в Зоне Тишины, на заброшенной станции, кто-то наблюдает.
  Иногда пилоты клянутся, что видели свет в иллюминаторах.
  Иногда они получают странные сообщения — предупреждения об
  опасности.

  Вы не умерли. Вы стали чем-то большим. Вы — страж границы
  между мирами. И иногда, в тишине космоса, вы чувствуете
  благодарность тех, кого спасли.

  Вы пожертвовали всем. Но галактика жива.
        """,
        crew_fate={
            "athena": "Стала капитаном «Элеи», продолжает миссии",
            "mia": "Вернулась в Альянс, стала командиром",
            "irina_lebedeva": "Продолжила исследования артефактов",
            "rina_mirai": "Стала главным навигатором флота",
            "maria": "Открыла медицинскую станцию",
            "alia_naar": "Пилот Альянса, легенда",
            "nadezhda": "Глава безопасности «Элеи»",
            "ekaterina": "Работает на разведку Альянса"
        },
        galaxy_fate="Галактика спасена, но потеряла героя. Миры восстанавливаются."
    )

    # Вариант 1.2: Вместе с романтическим партнёром
    scenes["exile_together"] = EndingScene(
        id="exile_together",
        ending_type=EndingType.EXILE,
        variation=EndingVariation.TOGETHER,
        title="Изгнание: Вдвоём в вечности",
        description="Вы и ваш романтический партнёр разделяете участь якоря",
        requirements={
            "ending_choice": "exile",
            "romantic_partner": "any",
            "romantic_relationship": 80,
            "team_loyalty": "high"
        },
        scene_text="""
  Ядро станции. Сущность отступает, но якорь требует стража.

  — Один не справится, — говорит Страж. — Нужны двое. Связанные.

  Вы смотрите на команду, но прежде чем вы успеваете говорить,
  ОНА/ОН делает шаг вперёд.

  — Я останусь с ним/ней.

  Это ваш романтический партнёр. В его/её глазах нет страха —
  только решимость.

  — Мы вместе начинали, — говорит он/она. — Вместе и закончим.

  Вы касаетесь якоря вдвоём. Энергия обвивает вас, связывая
  навсегда. Боль сменяется странным покоем.

  Сущность изгнана. А вы... вы стали частью чего-то большего.
  Вдвоём. Навсегда.
        """,
        epilogue_text="""
  ЭПИЛОГ: Вечная связь

  Галактика празднует победу. Но две фигуры в Зоне Тишины
  не могут присоединиться к празднику.

  Вы и ваш партнёр стали стражами. Ваше сознание слилось с
  станцией, но вы вместе. Вы делите каждое мгновение, каждую
  мысль, каждое воспоминание.

  Иногда к вам прилетают старые друзья. Афина приводит «Элею»
  на орбиту, и вы можете на мгновение почувствовать их
  присутствие.

  Вы потеряли свободу. Но обрели друг друга. И в бесконечной
  темноте космоса это — всё, что имеет значение.
        """,
        crew_fate={
            "athena": "Хранит память о капитане, передаёт историю",
            "mia": "Командует флотом Альянса",
            "irina_lebedeva": "Изучает природу якоря, пытается найти способ освободить вас",
            "rina_mirai": "Разработала новую навигационную систему",
            "maria": "Посвятила жизнь помощи ветеранам",
            "alia_naar": "Легендарный пилот",
            "romantic_partner": "Остался с героем как страж якоря"
        },
        galaxy_fate="Галактика спасена. История любви стала легендой."
    )

    # Вариант 1.3: Командная жертва
    scenes["exile_team"] = EndingScene(
        id="exile_team",
        ending_type=EndingType.EXILE,
        variation=EndingVariation.TEAM,
        title="Изгнание: Жертва экипажа",
        description="Команда помогает изгнать Сущность без жертв",
        requirements={
            "ending_choice": "exile",
            "team_loyalty": 90,
            "crew_alive": "all"
        },
        scene_text="""
  Ядро станции. Сущность сопротивляется.

  — Один не справится, — говорит Страж. — Но если команда
    объединит волю...

  Вы смотрите на экипаж. Они кивают.

  — Мы с вами, капитан, — говорит Мия. — До конца.

  Вы берётесь за руки. Все. Весь экипаж «Элеи». И касаетесь
  якоря вместе.

  Энергия проходит через каждого. Больно. Невыносимо. Но вы
  держитесь. Вместе.

  Сущность кричит и отступает. Изгнанная общей волей тех,
  кто отказался сдаться.
        """,
        epilogue_text="""
  ЭПИЛОГ: Единство

  Галактика узнала о подвиге экипажа «Элеи». Команда, которая
  вместе победила непобедимое.

  Вы выжили. Все. Но изменились. Связь, возникшая в ядре,
  осталась. Вы чувствуете друг друга на расстоянии.

  «Элея» продолжает миссии. Но теперь это больше чем корабль.
  Это символ того, что вместе можно преодолеть всё.

  А в Зоне Тишины якорь молчит. Сущность изгнана. И страж
  больше не нужен.
        """,
        crew_fate={
            "all": "Весь экипаж выжил и остался вместе",
            "athena": "Получила новую форму существования",
            "crew": "Стали героями галактики"
        },
        galaxy_fate="Галактика спасена благодаря единству. Новая эра сотрудничества."
    )

    # ============================================
    # КОНЦОВКА 2: ДОГОВОР
    # ============================================

    # Вариант 2.1: Хранитель договора (одиночка)
    scenes["treaty_guardian_solo"] = EndingScene(
        id="treaty_guardian_solo",
        ending_type=EndingType.TREATY,
        variation=EndingVariation.SOLO,
        title="Договор: Хранитель границы",
        description="Вы становитесь вечным хранителем договора с Сущностью",
        requirements={
            "ending_choice": "treaty",
            "romantic_partner": None,
            "diplomacy": "high"
        },
        scene_text="""
  Ядро станции. Сущность перед вами — не как враг, но как
  равная сторона переговоров.

  — Договор возможен, — говорит Страж. — Но кто-то должен
    следить за его исполнением.

  Вы делаете шаг вперёд.

  — Я буду Хранителем.

  Сущность кивает. — Разумно. Ты видел обе стороны. Ты
    понимаешь цену баланса.

  Станция перестраивается вокруг вас. Вы чувствуете, как
  ваше сознание расширяется, сливаясь с системами.

  — Ты станешь частью станции, — говорит Сущность. —
    Вечным арбитром между нашими мирами.

  Вы соглашаетесь. Галактика будет жить. Но вы... вы
  больше не принадлежите себе.
        """,
        epilogue_text="""
  ЭПИЛОГ: Арбитр

  Прошли десятилетия. Галактика изменилась.

  Миры, которые когда-то воевали, теперь торгуют. Сущность
  получает энергию умирающих звёзд — по договору. Взамен
  она не трогает населённые миры.

  А вы... вы наблюдаете. Из станции в Зоне Тишины. Вы —
  живой договор. Живое напоминание о цене мира.

  Иногда к вам прилетают. Афина, теперь уже старая,
  приносит новости. Мия присылает отчёты. Ирина пытается
  найти способ освободить вас.

  Но вы знаете: это ваша судьба. Быть хранителем. Быть
  гарантом. Быть тем, кто стоит между светом и тьмой.

  И в этом есть своя красота.
        """,
        crew_fate={
            "athena": "Стала послом Альянса",
            "mia": "Командует флотом",
            "irina_lebedeva": "Пытается найти способ освободить Хранителя",
            "rina_mirai": "Разработала торговые маршруты",
            "maria": "Основала медицинскую сеть",
            "alia_naar": "Пилот-легенда"
        },
        galaxy_fate="Хрупкий мир. Сущность и галактика сосуществуют по договору."
    )

    # Вариант 2.2: Договор с романтическим партнёром
    scenes["treaty_together"] = EndingScene(
        id="treaty_together",
        ending_type=EndingType.TREATY,
        variation=EndingVariation.TOGETHER,
        title="Договор: Вдвоём на границе",
        description="Вы и партнёр становитесь хранителями договора",
        requirements={
            "ending_choice": "treaty",
            "romantic_partner": "any",
            "romantic_relationship": 75
        },
        scene_text="""
  — Договор требует двух хранителей, — говорит Страж.

  Вы смотрите на команду. Но прежде чем вы успеваете
  говорить, ОН/ОНА делает шаг вперёд.

  — Я буду с ним/ней.

  Ваш романтический партнёр. Без колебаний. Без страха.

  — Мы вместе начинали, — говорит он/она. — Вместе и
    продолжим.

  Вы касаетесь якоря вдвоём. Станция принимает вас.
  Сущность отступает, соблюдая договор.

  Вы больше не люди. Вы — институт. Живой договор.
  Но вы вместе. И этого достаточно.
        """,
        epilogue_text="""
  ЭПИЛОГ: Вечные хранители

  Галактика процветает. Договор работает.

  А вы... вы и ваш партнёр стали легендой. Два хранителя
  на границе миров. Вы делите каждое мгновение, каждую
  мысль.

  Иногда старые друзья прилетают. Приносят новости.
  Напоминания о жизни, которую вы оставили.

  Но вы не жалеете. Вы выбрали друг друга. И службу
  галактике.

  И в бесконечной тишине космоса вы нашли свой покой.
  Вместе.
        """,
        crew_fate={
            "athena": "Хранит связь с хранителями",
            "crew": "Продолжают службу на «Элее»",
            "romantic_partner": "Стал хранителем вместе с героем"
        },
        galaxy_fate="Мир через договор. Сущность и галактика в равновесии."
    )

    # ============================================
    # КОНЦОВКА 3: СЛИЯНИЕ
    # ============================================

    # Вариант 3.1: Эволюция (одиночка)
    scenes["merge_evolution"] = EndingScene(
        id="merge_evolution",
        ending_type=EndingType.MERGE,
        variation=EndingVariation.SOLO,
        title="Слияние: Новая эволюция",
        description="Вы сливаетесь с Сущностью, становясь чем-то большим",
        requirements={
            "ending_choice": "merge",
            "psychic": 90,
            "romantic_partner": None
        },
        scene_text="""
  — Ты готов? — спрашивает Сущность.

  Вы киваете. Это не поражение. Это... эволюция.

  Вы делаете шаг вперёд. Сущность обвивает вас, не как
  враг, но как часть вас самих.

  Боль? Нет. Освобождение.

  Ваше сознание расширяется за пределы тела. Вы видите
  всё. Каждую звезду. Каждый мир. Каждую жизнь.

  Вы больше не Макс Велл. Вы — нечто большее.

  Галактика замирает. Что-то изменилось. Что-то древнее
  проснулось.

  Вы — Сущность. И вы — человек. И вы — оба.
        """,
        epilogue_text="""
  ЭПИЛОГ: Божество

  Галактика изменилась. Никто не может объяснить как.

  Иногда пилоты видят странные огни. Иногда целые флоты
  исчезают без следа. Иногда миры спасаются от неминуемой
  гибели.

  Вы везде. Вы — всё.

  Но иногда, в тишине между звёздами, вы вспоминаете.
  Корабль. Друзей. Любовь.

  Вы пожертвовали человечностью. Но обрели вселенную.

  И в бесконечном сознании вы храните память о том, кем
  были. О капитане Максе Велле.

  Потому что даже божества нуждаются в памяти о человечности.
        """,
        crew_fate={
            "athena": "Чувствует изменение, но не понимает",
            "mia": "Продолжает службу, хранит память",
            "irina_lebedeva": "Изучает феномен Сущности",
            "crew": "Разошлись, но помнят капитана"
        },
        galaxy_fate="Галактика изменилась навсегда. Новая эра эволюции."
    )

    # Вариант 3.2: Слияние с возвратом
    scenes["merge_return"] = EndingScene(
        id="merge_return",
        ending_type=EndingType.MERGE,
        variation=EndingVariation.TEAM,
        title="Слияние: Возвращение",
        description="Вы сливаетесь с Сущностью, но сохраняете связь с командой",
        requirements={
            "ending_choice": "merge",
            "psychic": 90,
            "team_loyalty": 95,
            "romantic_partner": "any"
        },
        scene_text="""
  — Слияние изменит тебя, — предупреждает Сущность.

  — Я знаю, — отвечаете вы. — Но я не потеряю себя.

  Вы смотрите на команду. На того, кого любите.

  — Я вернусь, — обещаете вы. — Не таким, как был. Но
    вернусь.

  Слияние. Расширение. Осознание.

  Вы — всё. Но вы помните. И эта память — ваш якорь.

  Сущность удивлена. Она ожила поглотить. Но вы...
  вы сохранили себя.

  Вы — мост. Между человеком и божеством.
        """,
        epilogue_text="""
  ЭПИЛОГ: Мост

  Галактика не знает, что спаслась.

  Вы — Сущность. Но вы — и Макс Велл.

  Иногда вы приходите к ним. В снах. В видениях.

  Афина чувствует вас. Мия видит в звёздах. А ваш
  романтический партнёр... он/она знает.

  Вы не можете вернуться полностью. Но вы можете
  наблюдать. Защищать. Любить.

  Вы стали легендой при жизни. И продолжаете жить
  в каждой звезде, в каждом мире.

  Вы — Курьер. И ваша миссия никогда не закончится.
        """,
        crew_fate={
            "athena": "Чувствует присутствие капитана",
            "romantic_partner": "Посвятил жизнь изучению связи",
            "crew": "Разошлись, но хранят веру"
        },
        galaxy_fate="Галактика под скрытой защитой. Эра скрытых хранителей."
    )

    return scenes


# === ФУНКЦИИ ДЛЯ ПОЛУЧЕНИЯ КОНЦОВОК ===

def get_ending_scene(scene_id: str) -> Optional[EndingScene]:
    """Получить финальную сцену по ID"""
    scenes = create_ending_scenes()
    return scenes.get(scene_id)


def get_available_endings(game_state: Dict) -> List[EndingScene]:
    """Получить доступные концовки на основе состояния игры"""
    scenes = create_ending_scenes()
    available = []

    for scene in scenes.values():
        # Проверка выбора концовки
        if game_state.get("ending_choice") != scene.ending_type.value:
            continue

        # Проверка романтического партнёра
        req_partner = scene.requirements.get("romantic_partner")
        if req_partner == "any" and not game_state.get("romantic_partner"):
            continue
        if req_partner is None and game_state.get("romantic_partner"):
            continue

        # Проверка отношений
        req_relationship = scene.requirements.get("romantic_relationship", 0)
        if req_relationship > 0:
            partner_id = game_state.get("romantic_partner")
            partner_rel = game_state.get("relationships", {}).get(partner_id, 0)
            if partner_rel < req_relationship:
                continue

        # Проверка лояльности команды
        req_loyalty = scene.requirements.get("team_loyalty")
        if req_loyalty == "high" and game_state.get("team_loyalty", 0) < 80:
            continue
        if req_loyalty == "any":
            pass

        # Проверка психики
        req_psychic = scene.requirements.get("psychic", 0)
        if game_state.get("psychic", 0) < req_psychic:
            continue

        available.append(scene)

    return available


def get_ending_by_type(ending_type: EndingType, variation: EndingVariation) -> Optional[EndingScene]:
    """Получить концовку по типу и вариации"""
    scenes = create_ending_scenes()
    for scene in scenes.values():
        if scene.ending_type == ending_type and scene.variation == variation:
            return scene
    return None


def get_all_ending_types() -> List[EndingType]:
    """Получить все типы концовок"""
    return [EndingType.EXILE, EndingType.TREATY, EndingType.MERGE]


# === МЕНЕДЖЕР ПРОГРЕССА ФИНАЛЬНЫХ СЦЕН ===

class EndingSceneManager:
    """Менеджер прогресса финальных сцен"""

    def __init__(self):
        self.scenes: Dict[str, EndingScene] = {}
        self.progress = EndingProgress()

    def initialize(self, scenes: Dict[str, EndingScene]):
        """Инициализация сцен"""
        self.scenes = scenes

    def choose_ending(self, ending_type: EndingType):
        """Выбрать тип концовки"""
        self.progress.ending_chosen = True
        self.progress.ending_type = ending_type.value

    def unlock_variation(self, variation_id: str):
        """Разблокировать вариацию"""
        self.progress.variation_unlocked[variation_id] = True

    def check_requirement(self, req_id: str, met: bool):
        """Отметить выполнение требования"""
        self.progress.requirements_met[req_id] = met

    def to_dict(self) -> Dict:
        """Сериализация"""
        return {
            "progress": self.progress.to_dict()
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "EndingSceneManager":
        """Десериализация"""
        manager = cls()
        if "progress" in data:
            manager.progress = EndingProgress.from_dict(data["progress"])
        return manager
