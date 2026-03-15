# -*- coding: utf-8 -*-
"""
Star Courier - Romance Scenes System
Система романтических сцен для 6 персонажей
"""

from typing import Dict, List, Optional, Set
from dataclasses import dataclass, field

try:
    from .config import MAX_RELATIONSHIP
except ImportError:
    from config import MAX_RELATIONSHIP


@dataclass
class RomanceProgress:
    """Прогресс романтической линии персонажа"""
    character_id: str
    scenes_completed: Set[str] = field(default_factory=set)
    confession_accepted: bool = False
    romance_unlocked: bool = False
    relationship_level: int = 0

    def to_dict(self) -> Dict:
        """Сериализация"""
        return {
            "character_id": self.character_id,
            "scenes_completed": list(self.scenes_completed),
            "confession_accepted": self.confession_accepted,
            "romance_unlocked": self.romance_unlocked,
            "relationship_level": self.relationship_level
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "RomanceProgress":
        """Десериализация"""
        return cls(
            character_id=data.get("character_id", ""),
            scenes_completed=set(data.get("scenes_completed", [])),
            confession_accepted=data.get("confession_accepted", False),
            romance_unlocked=data.get("romance_unlocked", False),
            relationship_level=data.get("relationship_level", 0)
        )


@dataclass
class RomanceScene:
    """Класс романтической сцены"""
    id: str
    character_id: str
    character_name: str
    title: str
    description: str
    min_relationship: int
    scene_text: str
    choices: List[Dict]
    is_confession: bool = False
    is_intimate: bool = False
    unlocks_next: bool = False

    def to_dict(self) -> Dict:
        """Сериализация в словарь"""
        return {
            "id": self.id,
            "character_id": self.character_id,
            "character_name": self.character_name,
            "title": self.title,
            "description": self.description,
            "min_relationship": self.min_relationship,
            "scene_text": self.scene_text,
            "choices": self.choices,
            "is_confession": self.is_confession,
            "is_intimate": self.is_intimate,
            "unlocks_next": self.unlocks_next
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "RomanceScene":
        """Десериализация из словаря"""
        return cls(
            id=data.get("id", ""),
            character_id=data.get("character_id", ""),
            character_name=data.get("character_name", ""),
            title=data.get("title", ""),
            description=data.get("description", ""),
            min_relationship=data.get("min_relationship", 60),
            scene_text=data.get("scene_text", ""),
            choices=data.get("choices", []),
            is_confession=data.get("is_confession", False),
            is_intimate=data.get("is_intimate", False),
            unlocks_next=data.get("unlocks_next", False)
        )


# === РОМАНТИЧЕСКИЕ СЦЕНЫ ДЛЯ КАЖДОГО ПЕРСОНАЖА ===

def create_romance_scenes() -> Dict[str, RomanceScene]:
    """Создать все романтические сцены"""
    scenes = {}

    # ============================================
    # ИРИНА ЛЕБЕДЕВА (Учёный)
    # ============================================
    scenes["irina_confession"] = RomanceScene(
        id="irina_confession",
        character_id="irina_lebedeva",
        character_name="Ирина",
        title="Признание в лаборатории",
        description="Ирина наконец решается признаться в своих чувствах",
        min_relationship=60,
        is_confession=True,
        scene_text="""
  Лаборатория погружена в мягкий свет мониторов. Ирина стоит у стола,
  рассеянно проводя пальцем по голографической проекции артефакта.

  — Капитан... — она не оборачивается, но голос дрожит. — Я хотела
    поговорить с вами. Лично.

  Она наконец поворачивается, щёки слегка розовеют.

  — Все эти исследования, экспедиции... Но главное открытие я сделала
    не здесь. — Она прижимает руку к груди. — Я поняла, что... что вы
    стали для меня больше, чем просто капитаном.

  Ирина делает шаг ближе, глаза блестят.

  — Я знаю, это непрофессионально. Но я не могу больше молчать.
        """,
        choices=[
            {
                "text": "«Ирина, я тоже что-то испытываю к тебе»",
                "effect": {"relationship": 20, "trust": 15, "romance_unlock": "irina_intimate"},
                "next_scene": "irina_accepted"
            },
            {
                "text": "«Мне нужно время подумать»",
                "effect": {"relationship": 5, "trust": 5},
                "next_scene": "irina_wait"
            },
            {
                "text": "«Давай останемся коллегами»",
                "effect": {"relationship": -10, "trust": -5},
                "next_scene": "irina_rejected"
            }
        ]
    )

    scenes["irina_intimate"] = RomanceScene(
        id="irina_intimate",
        character_id="irina_lebedeva",
        character_name="Ирина",
        title="Звёздная ночь в лаборатории",
        description="Интимный момент с Ириной под звёздами",
        min_relationship=80,
        is_intimate=True,
        scene_text="""
  После смены Ирина приглашает вас в лабораторию. На главном экране
  не данные, а проекция звёздного неба — редкое зрелище в космосе.

  — Я настроила проекцию на вашу любимую часть галактики, — тихо
    говорит она, подходя ближе.

  Её пальцы находят ваши. Она смотрит вверх, лицо освещено
  мерцанием далёких звёзд.

  — Знаете, я всегда чувствовала себя более комфортно среди данных,
    чем среди людей. Но с вами... с вами я чувствую себя дома.

  Она поворачивается, и её губы почти касаются ваших.
        """,
        choices=[
            {
                "text": "Поцеловать её",
                "effect": {"relationship": 20, "trust": 20, "romance_confirmed": True},
                "next_scene": "irina_kiss"
            },
            {
                "text": "Обнять и прижать к себе",
                "effect": {"relationship": 15, "trust": 25},
                "next_scene": "irina_embrace"
            }
        ]
    )

    # ============================================
    # АЛИЯ'НААР (Пилот)
    # ============================================
    scenes["alia_moment"] = RomanceScene(
        id="alia_moment",
        character_id="alia_naar",
        character_name="Алия",
        title="Разговор в кокпите",
        description="Алия открывается после сложного манёвра",
        min_relationship=55,
        is_confession=True,
        scene_text="""
  Кокпит погружён в тишину после успешного прохождения аномалии.
  Алия откидывается в кресле пилота, снимает шлем и проводит рукой
  по мокрым волосам.

  — Знаешь, капитан... — она не смотрит на вас. — На моей планете
    есть обычай. Если кто-то спасает тебе жизнь, ты становишься
    частью его стаи. Навсегда.

  Она наконец поворачивается, и в её глазах что-то новое.

  — Ты спас меня не раз. И экипаж тоже. Вы... моя стая теперь.
    Но с тобой... — она запинается, что редко бывает. — С тобой
    я хочу быть больше, чем просто пилотом.
        """,
        choices=[
            {
                "text": "«Ты — лучший пилот и важный член экипажа»",
                "effect": {"relationship": 10, "trust": 15},
                "next_scene": "alia_friendzone"
            },
            {
                "text": "«Я тоже хочу чего-то большего»",
                "effect": {"relationship": 20, "trust": 20, "romance_unlock": "alia_intimate"},
                "next_scene": "alia_accepted"
            },
            {
                "text": "«Давай сосредоточимся на миссии»",
                "effect": {"relationship": -5, "trust": 5},
                "next_scene": "alia_professional"
            }
        ]
    )

    scenes["alia_intimate"] = RomanceScene(
        id="alia_intimate",
        character_id="alia_naar",
        character_name="Алия",
        title="Под звёздами родного мира",
        description="Алия показывает вам голограмму своей планеты",
        min_relationship=75,
        is_intimate=True,
        scene_text="""
  Алия приглашает вас в свою каюту. На стене — голограмма
  пустынной планеты с двумя лунами.

  — Это мой дом, — говорит она тихо. — Суровое место. Но там
    я научилась ценить тепло. Тепло другого существа рядом.

  Она берёт вашу руку, прижимает к своей щеке.

  — Здесь, на корабле, ты — мой дом, Макс. Где бы мы ни были.
        """,
        choices=[
            {
                "text": "Прижать её к себе",
                "effect": {"relationship": 20, "trust": 20},
                "next_scene": "alia_embrace"
            },
            {
                "text": "Поцеловать",
                "effect": {"relationship": 25, "trust": 15, "romance_confirmed": True},
                "next_scene": "alia_kiss"
            }
        ]
    )

    # ============================================
    # РИНА МИРАЙ (Навигатор)
    # ============================================
    scenes["rina_confession"] = RomanceScene(
        id="rina_confession",
        character_id="rina_mirai",
        character_name="Рина",
        title="Стратегия сердца",
        description="Рина признаётся после тактического брифинга",
        min_relationship=60,
        is_confession=True,
        scene_text="""
  После долгого брифинга Рина задерживается на мостике. Она
  крутится в кресле, затем внезапно говорит:

  — Капитан, я проанализировала все возможные сценарии нашей
    миссии. Просчитала риски, вероятности, альтернативы.

  Она встаёт, подходит ближе, улыбаясь.

  — И знаете что? Во всех сценариях, где мы с вами... где мы
    вместе, вероятность успеха на 23% выше.

  Рина кладёт руку вам на плечо.

  — Это не просто статистика. Это... я хочу быть с вами.
    Не только как навигатор.
        """,
        choices=[
            {
                "text": "«Твоя статистика убедительна»",
                "effect": {"relationship": 20, "trust": 15, "romance_unlock": "rina_intimate"},
                "next_scene": "rina_accepted"
            },
            {
                "text": "«Давай не смешивать работу и личное»",
                "effect": {"relationship": -5, "trust": 5},
                "next_scene": "rina_professional"
            },
            {
                "text": "«Мне тоже нелегко с тобой»",
                "effect": {"relationship": 15, "trust": 10},
                "next_scene": "rina_hopeful"
            }
        ]
    )

    scenes["rina_intimate"] = RomanceScene(
        id="rina_intimate",
        character_id="rina_mirai",
        character_name="Рина",
        title="Навигация к тебе",
        description="Рина показывает свои чувства через навигационную метафору",
        min_relationship=80,
        is_intimate=True,
        scene_text="""
  Рина приглашает вас в навигационный отсек. На экране —
  проложенный маршрут через звёздную систему.

  — Видишь эту траекторию? — она показывает на изогнутую линию.
    — Это путь к самой красивой туманности в секторе. Я хотела
    показать тебе... показать вам.

  Она выключает экраны, и вы остаётесь в полумраке.

  — Знаешь, я могу проложить курс куда угодно. Но единственный
    путь, который я хочу исследовать... это путь к твоему сердцу.
        """,
        choices=[
            {
                "text": "«Ты уже нашла путь»",
                "effect": {"relationship": 25, "trust": 15, "romance_confirmed": True},
                "next_scene": "rina_romantic"
            },
            {
                "text": "Обнять её",
                "effect": {"relationship": 20, "trust": 20},
                "next_scene": "rina_embrace"
            }
        ]
    )

    # ============================================
    # МИЯ (Тактик)
    # ============================================
    scenes["mia_confession"] = RomanceScene(
        id="mia_confession",
        character_id="mia",
        character_name="Мия",
        title="Тактика чувств",
        description="Мия признаётся после успешной операции",
        min_relationship=65,
        is_confession=True,
        scene_text="""
  После успешной миссии Мия находит вас в кают-компании. Она
  выглядит необычно взволнованной.

  — Капитан, я должна доложить... — она запинается, что совсем
    на неё не похоже. — Нет, не доложить. Сказать.

  Мия глубоко вдыхает.

  — Я всегда полагалась на логику. На расчёты. Но есть переменная,
    которую я не могу вычислить. — Она смотрит прямо на вас. —
    Мои чувства к вам. Они не вписываются ни в одну модель.
        """,
        choices=[
            {
                "text": "«Иногда чувства важнее расчётов»",
                "effect": {"relationship": 20, "trust": 20, "romance_unlock": "mia_intimate"},
                "next_scene": "mia_accepted"
            },
            {
                "text": "«Давай обсудим это позже»",
                "effect": {"relationship": 5, "trust": 5},
                "next_scene": "mia_wait"
            },
            {
                "text": "«Ты ценный член команды»",
                "effect": {"relationship": -5, "trust": 10},
                "next_scene": "mia_friendzone"
            }
        ]
    )

    scenes["mia_intimate"] = RomanceScene(
        id="mia_intimate",
        character_id="mia",
        character_name="Мия",
        title="Стратегия близости",
        description="Мия позволяет себе быть уязвимой",
        min_relationship=85,
        is_intimate=True,
        scene_text="""
  Мия ждёт вас в тактическом отсеке. Все экраны выключены.

  — Я отключила системы, — говорит она тихо. — Иногда нужно
    просто быть. Без данных. Без планов.

  Она подходит ближе, и вы видите, как дрожат её руки.

  — С тобой я чувствую... спокойствие. Как будто все битвы
    окончены. И это пугает меня больше любой войны.
        """,
        choices=[
            {
                "text": "Взять её за руки",
                "effect": {"relationship": 20, "trust": 25},
                "next_scene": "mia_hands"
            },
            {
                "text": "Поцеловать",
                "effect": {"relationship": 25, "trust": 20, "romance_confirmed": True},
                "next_scene": "mia_kiss"
            }
        ]
    )

    # ============================================
    # МАРИЯ (Медик)
    # ============================================
    scenes["maria_confession"] = RomanceScene(
        id="maria_confession",
        character_id="maria",
        character_name="Мария",
        title="Исцеление сердца",
        description="Мария признаётся во время медицинской проверки",
        min_relationship=60,
        is_confession=True,
        scene_text="""
  Медотсек. Мария проводитroutine проверку после миссии. Её
  пальцы мягко касаются вашей руки, проверяя пульс.

  — Сердцебиение в норме, — говорит она, но не отпускает руку.
    — Хотя... моё сейчас точно не в норме.

  Она поднимает глаза, и в них такая нежность, что становится
  трудно дышать.

  — Я лечу раны экипажа. Но есть рана, которую можете исцелить
    только вы. — Мария делает паузу. — Моё сердце. Оно... оно
    принадлежит вам, капитан.
        """,
        choices=[
            {
                "text": "«Мария, ты исцелила моё давно»",
                "effect": {"relationship": 25, "trust": 20, "romance_unlock": "maria_intimate"},
                "next_scene": "maria_accepted"
            },
            {
                "text": "«Ты замечательный медик и друг»",
                "effect": {"relationship": -5, "trust": 10},
                "next_scene": "maria_friendzone"
            },
            {
                "text": "«Мне нужно время»",
                "effect": {"relationship": 5, "trust": 5},
                "next_scene": "maria_wait"
            }
        ]
    )

    scenes["maria_intimate"] = RomanceScene(
        id="maria_intimate",
        character_id="maria",
        character_name="Мария",
        title="Прикосновение исцеления",
        description="Мария показывает свою страсть",
        min_relationship=80,
        is_intimate=True,
        scene_text="""
  Мария приглашает вас в медотсек после смены. Мягкий свет,
  запах лекарственных трав.

  — Знаешь, — говорит она, подходя ближе, — я изучила все
    способы исцеления. Но есть одно лекарство, которое нельзя
    купить в аптеке.

  Её пальцы касаются вашей щеки.

  — Любовь. Это единственное, что真正 исцеляет душу.
        """,
        choices=[
            {
                "text": "Поцеловать её",
                "effect": {"relationship": 25, "trust": 20, "romance_confirmed": True},
                "next_scene": "maria_kiss"
            },
            {
                "text": "Обнять",
                "effect": {"relationship": 20, "trust": 25},
                "next_scene": "maria_embrace"
            }
        ]
    )

    # ============================================
    # АННА (Навигатор)
    # ============================================
    scenes["anna_confession"] = RomanceScene(
        id="anna_confession",
        character_id="anna",
        character_name="Анна",
        title="Голос сердца",
        description="Анна признаётся через свою интуицию",
        min_relationship=55,
        is_confession=True,
        scene_text="""
  Анна стоит у обзорного окна, глядя на звёзды. Она поворачивается
  к вам, и её глаза сияют.

  — Капитан, я... я чувствую вещи. Интуитивно. И моё сердце
    говорит мне, что вы — тот, с кем я должна быть.

  Она краснеет, но продолжает.

  — Я знаю, это звучит странно. Но когда вы рядом, я чувствую...
    целостность. Как будто все звёзды выстроились в правильный
    узор.
        """,
        choices=[
            {
                "text": "«Я тоже что-то чувствую»",
                "effect": {"relationship": 20, "trust": 15, "romance_unlock": "anna_intimate"},
                "next_scene": "anna_accepted"
            },
            {
                "text": "«Твоя интуиция редко ошибается»",
                "effect": {"relationship": 15, "trust": 10},
                "next_scene": "anna_hopeful"
            },
            {
                "text": "«Давай останемся друзьями»",
                "effect": {"relationship": -5, "trust": 5},
                "next_scene": "anna_friendzone"
            }
        ]
    )

    scenes["anna_intimate"] = RomanceScene(
        id="anna_intimate",
        character_id="anna",
        character_name="Анна",
        title="Звёздная связь",
        description="Анна делится своим видением будущего",
        min_relationship=75,
        is_intimate=True,
        scene_text="""
  Анна приводит вас в наблюдательную рубку. Звёзды заполняют
  всё пространство вокруг.

  — Я видела нас... в будущем, — шепчет она. — Вместе. Среди
    этих звёзд.

  Она берёт вашу руку, прижимает к своей груди.

  — Чувствуешь? Наши сердца бьются в унисон. Это не случайность.
    Это... предназначение.
        """,
        choices=[
            {
                "text": "«Я верю твоему видению»",
                "effect": {"relationship": 25, "trust": 20, "romance_confirmed": True},
                "next_scene": "anna_vision"
            },
            {
                "text": "Обнять её",
                "effect": {"relationship": 20, "trust": 20},
                "next_scene": "anna_embrace"
            }
        ]
    )

    return scenes


# === ФУНКЦИИ ДЛЯ ЗАПУСКА СЦЕН ===

def get_romance_scene(scene_id: str) -> Optional[RomanceScene]:
    """Получить романтическую сцену по ID"""
    scenes = create_romance_scenes()
    return scenes.get(scene_id)


def get_available_romance_scenes(character_id: str, relationship: int) -> List[RomanceScene]:
    """Получить доступные сцены для персонажа"""
    scenes = create_romance_scenes()
    available = []
    for scene in scenes.values():
        if scene.character_id == character_id and relationship >= scene.min_relationship:
            available.append(scene)
    return available


def get_romance_characters() -> List[str]:
    """Получить список персонажей с романтическими сценами"""
    return ["irina_lebedeva", "alia_naar", "rina_mirai", "mia", "maria", "anna"]


# === МЕНЕДЖЕР ПРОГРЕССА РОМАНТИЧЕСКИХ СЦЕН ===

class RomanceSceneManager:
    """Менеджер прогресса романтических сцен"""

    def __init__(self):
        self.scenes: Dict[str, RomanceScene] = {}
        self.progress: Dict[str, RomanceProgress] = {}

    def initialize(self, scenes: Dict[str, RomanceScene]):
        """Инициализация сцен"""
        self.scenes = scenes

    def get_scene(self, scene_id: str) -> Optional[RomanceScene]:
        """Получить сцену по ID"""
        return self.scenes.get(scene_id)

    def complete_scene(self, scene_id: str, character_id: str):
        """Отметить сцену как завершённую"""
        if character_id not in self.progress:
            self.progress[character_id] = RomanceProgress(character_id=character_id)

        self.progress[character_id].scenes_completed.add(scene_id)

    def set_confession_accepted(self, character_id: str, accepted: bool = True):
        """Установить флаг принятия признания"""
        if character_id not in self.progress:
            self.progress[character_id] = RomanceProgress(character_id=character_id)
        self.progress[character_id].confession_accepted = accepted

    def unlock_romance(self, character_id: str):
        """Разблокировать романтическую линию"""
        if character_id not in self.progress:
            self.progress[character_id] = RomanceProgress(character_id=character_id)
        self.progress[character_id].romance_unlocked = True

    def get_progress(self, character_id: str) -> Optional[RomanceProgress]:
        """Получить прогресс персонажа"""
        return self.progress.get(character_id)

    def to_dict(self) -> Dict:
        """Сериализация всего прогресса"""
        return {
            "progress": {
                cid: prog.to_dict() for cid, prog in self.progress.items()
            }
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "RomanceSceneManager":
        """Десериализация"""
        manager = cls()
        progress_data = data.get("progress", {})
        for cid, pdata in progress_data.items():
            manager.progress[cid] = RomanceProgress.from_dict(pdata)
        return manager
