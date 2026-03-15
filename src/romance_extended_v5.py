# -*- coding: utf-8 -*-
"""
Star Courier - Extended Romance Lines
Расширенные романтические линии для всех персонажей
"""

# === МИЯ — ТАКТИК ===

MIA_ROMANCE_EVENTS = {
    "romance_start_mia": {
        "id": "rom_mia_01",
        "chapter": 3,
        "location": "ship_bridge",
        "trigger": {"mia_relationship": 30, "event": "late_night_shift"},
        "scene": {
            "description": "Поздно ночью вы находите Мию на мостике, изучающей звёздные карты. Она выглядит уставшей, но сосредоточенной.",
            "dialogues": [
                {
                    "speaker": "mia",
                    "text": "Капитан? Я не ожидала вас в этот час. Просто... не могла уснуть. Думала о наших координатах и следующей точке назначения.",
                    "emotion": "surprised"
                },
                {
                    "speaker": "narrator",
                    "text": "Она отводит взгляд, словно смущённая тем, что её застали врасплох."
                }
            ]
        },
        "choices": [
            {
                "text": "Присоединиться к ней и помочь с анализом",
                "effects": {"mia_relationship": 10, "knowledge": 5},
                "next": "rom_mia_01a"
            },
            {
                "text": "Предложить ей отдохнуть — работа подождёт",
                "effects": {"mia_relationship": 15, "empathy": 5},
                "next": "rom_mia_01b"
            },
            {
                "text": "Вернуться в каюту — она знает своё дело",
                "effects": {"mia_relationship": -5},
                "next": "rom_mia_01c"
            }
        ]
    },
    "rom_mia_01b": {
        "id": "rom_mia_01b",
        "scene": {
            "dialogues": [
                {
                    "speaker": "player",
                    "text": "Мия, ты работаешь без отдыха с тех пор, как мы покинули порт. Позволь мне беспокоиться о команде — иди спать."
                },
                {
                    "speaker": "mia",
                    "text": "Я... спасибо, капитан. Вы правы. Иногда я забываю, что не одна несу эту ношу.",
                    "emotion": "grateful"
                },
                {
                    "speaker": "narrator",
                    "text": "Она встаёт, собирая карты, и задерживается на мгновение рядом с вами. Её рука слегка касается вашей."
                },
                {
                    "speaker": "mia",
                    "text": "Знаете, до встречи с вами я думала, что доверие — это слабость. Теперь я понимаю... это сила.",
                    "emotion": "vulnerable"
                }
            ]
        },
        "flags": {"mia_romance_started": True}
    },
    
    "romance_develop_mia": {
        "id": "rom_mia_02",
        "chapter": 7,
        "location": "ship_cargo",
        "trigger": {"mia_relationship": 55, "flag": "mia_romance_started"},
        "scene": {
            "description": "Во время инвентаризации груза вы оказываетесь вдвоём с Мией в тесном подсобном помещении. Неожиданно гаснет свет — авария в системе.",
            "dialogues": [
                {
                    "speaker": "mia",
                    "text": "Датчики показывают перегрузку в секции C. Придётся подождать, пока Сергей починит.",
                    "emotion": "calm"
                },
                {
                    "speaker": "narrator",
                    "text": "В темноте вы чувствуете её дыхание рядом. Она не отодвигается."
                },
                {
                    "speaker": "mia",
                    "text": "Капитан... могу я задать личный вопрос? Почему вы взяли меня на борт? Я была... никем. Просто аналитиком с разрушенной станции."
                }
            ]
        },
        "choices": [
            {
                "text": "Потому что увидел в тебе то, что ты сама не замечала — преданность.",
                "effects": {"mia_relationship": 20},
                "next": "rom_mia_02a"
            },
            {
                "text": "Мне был нужен хороший тактик. Ты оказалась лучшей.",
                "effects": {"mia_relationship": 5},
                "next": "rom_mia_02b"
            },
            {
                "text": "Не знаю. Просто чувствовал, что это правильно.",
                "effects": {"mia_relationship": 15},
                "next": "rom_mia_02c"
            }
        ]
    },
    "rom_mia_02a": {
        "id": "rom_mia_02a",
        "scene": {
            "dialogues": [
                {
                    "speaker": "mia",
                    "text": "Преданность... Да. Наверное, это всё, что у меня осталось после потери семьи. Но теперь... теперь у меня есть кое-что большее.",
                    "emotion": "touched"
                },
                {
                    "speaker": "narrator",
                    "text": "В темноте вы чувствуете, как её пальцы переплетаются с вашими."
                },
                {
                    "speaker": "mia",
                    "text": "Когда всё это закончится... когда мы победим или... неважно. Я хочу, чтобы вы знали — вы не просто мой капитан. Вы — моя семья."
                }
            ]
        },
        "flags": {"mia_romance_developed": True}
    },
    
    "romance_confession_mia": {
        "id": "rom_mia_03",
        "chapter": 12,
        "location": "observation_deck",
        "trigger": {"mia_relationship": 80, "flag": "mia_romance_developed"},
        "scene": {
            "description": "После тяжёлой миссии вы находите Мию на смотровой площадке, наблюдающей за звёздами.",
            "dialogues": [
                {
                    "speaker": "mia",
                    "text": "Знаете, я рассчитала тысячи сценариев. Вероятности, исходы, коэффициенты успеха. Но есть одна переменная, которую я не могу предсказать.",
                    "emotion": "thoughtful"
                },
                {
                    "speaker": "player",
                    "text": "Какая?"
                },
                {
                    "speaker": "mia",
                    "text": "Мои собственные чувства. Ко мне они не применяются никакие формулы. Когда я думаю о риске потерять вас... все расчёты рушатся.",
                    "emotion": "vulnerable"
                },
                {
                    "speaker": "narrator",
                    "text": "Она поворачивается к вам, и в её глазах отражаются далёкие звёзды."
                },
                {
                    "speaker": "mia",
                    "text": "Я люблю вас. Не как капитана, не как командира. Просто... вас. И это пугает меня больше любой аномалии."
                }
            ]
        },
        "choices": [
            {
                "text": "Поцеловать её",
                "effects": {"mia_relationship": 25, "romantic_partner": "mia"},
                "next": "rom_mia_03a"
            },
            {
                "text": "Признаться во взаимности словами",
                "effects": {"mia_relationship": 20, "romantic_partner": "mia"},
                "next": "rom_mia_03b"
            },
            {
                "text": "Сказать, что сейчас не время для романтики",
                "effects": {"mia_relationship": -20},
                "next": "rom_mia_03c"
            }
        ]
    },
    "rom_mia_03a": {
        "id": "rom_mia_03a",
        "scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Вы привлекаете её к себе, и её губы встречают ваши. Поцелуй полон отчаяния и надежды — двух людей, нашедших друг друга посреди хаоса."
                },
                {
                    "speaker": "mia",
                    "text": "Я рассчитала этот момент в тысячах симуляций. Ни одна не сравнится с реальностью.",
                    "emotion": "happy"
                },
                {
                    "speaker": "narrator",
                    "text": "Она кладёт голову вам на плечо, и вы вместе смотрите на звёзды."
                }
            ]
        },
        "flags": {"mia_romantic_partner": True}
    }
}

# === МАРИЯ — МЕДИК ===

MARIA_ROMANCE_EVENTS = {
    "romance_start_maría": {
        "id": "rom_mar_01",
        "chapter": 4,
        "location": "medbay",
        "trigger": {"maria_relationship": 30, "event": "injury_treatment"},
        "scene": {
            "description": "После стычки с пиратами вы получаете ранение. Мария обрабатывает вашу рану с особой заботой.",
            "dialogues": [
                {
                    "speaker": "maria",
                    "text": "Держите спокойно. Будет немного больно, но я постараюсь быть нежной.",
                    "emotion": "focused"
                },
                {
                    "speaker": "narrator",
                    "text": "Её руки тёплые и уверенные. Она работает близко, и вы чувствуете её дыхание."
                },
                {
                    "speaker": "maria",
                    "text": "Вы рискуете собой каждый день. Знаете, как тяжело мне видеть вас на этом столе? Даже когда это просто царапина?",
                    "emotion": "concerned"
                }
            ]
        },
        "choices": [
            {
                "text": "Это моя работа — защищать команду. Включая тебя.",
                "effects": {"maria_relationship": 10},
                "next": "rom_mar_01a"
            },
            {
                "text": "Надеюсь, ты всегда будешь рядом, чтобы меня чинить.",
                "effects": {"maria_relationship": 15},
                "next": "rom_mar_01b"
            },
            {
                "text": "Просто делай свою работу, Мария.",
                "effects": {"maria_relationship": -10},
                "next": "rom_mar_01c"
            }
        ]
    },
    "rom_mar_01b": {
        "id": "rom_mar_01b",
        "scene": {
            "dialogues": [
                {
                    "speaker": "maria",
                    "text": "Я всегда буду рядом. Пока вы... пока мы вместе. Это обещание врача — и не только.",
                    "emotion": "blushing"
                },
                {
                    "speaker": "narrator",
                    "text": "Она заканчивает перевязку, но не отходит сразу. Её пальцы задерживаются на вашей руке."
                },
                {
                    "speaker": "maria",
                    "text": "Вы знаете, на моей родной планете был обычай. Когда кто-то спасает тебе жизнь, ты становишься связанным с ним навечно. Может, это глупо, но...",
                    "emotion": "shy"
                }
            ]
        },
        "flags": {"maria_romance_started": True}
    },
    
    "romance_develop_maría": {
        "id": "rom_mar_02",
        "chapter": 8,
        "location": "planet_surface",
        "trigger": {"maria_relationship": 55, "flag": "maria_romance_started"},
        "scene": {
            "description": "Во время высадки на планету вы и Мария отрезаны от команды аномалией. Вы вынуждены ждать эвакуации в небольшой пещере.",
            "dialogues": [
                {
                    "speaker": "maria",
                    "text": "Сканеры показывают, что шторм продлится несколько часов. У нас есть время поговорить.",
                    "emotion": "calm"
                },
                {
                    "speaker": "narrator",
                    "text": "Она садится рядом с вами у небольшого костра, который вы развели."
                },
                {
                    "speaker": "maria",
                    "text": "Я никогда не спрашивала... у вас есть кто-то дома? Кто-то, кто ждёт?",
                    "emotion": "curious"
                }
            ]
        },
        "choices": [
            {
                "text": "Нет. Мой дом — этот корабль и его команда.",
                "effects": {"maria_relationship": 15},
                "next": "rom_mar_02a"
            },
            {
                "text": "Был(а). Но это в прошлом.",
                "effects": {"maria_relationship": 10},
                "next": "rom_mar_02b"
            },
            {
                "text": "А почему ты спрашиваешь?",
                "effects": {"maria_relationship": 20},
                "next": "rom_mar_02c"
            }
        ]
    },
    "rom_mar_02c": {
        "id": "rom_mar_02c",
        "scene": {
            "dialogues": [
                {
                    "speaker": "maria",
                    "text": "Потому что... потому что я хочу знать, есть ли у меня шанс. Шанс быть больше, чем просто вашим медиком.",
                    "emotion": "embarrassed"
                },
                {
                    "speaker": "narrator",
                    "text": "Она смотрит на огонь, не смея встретиться с вами взглядом."
                },
                {
                    "speaker": "maria",
                    "text": "Я видела многое. Смерть, болезнь, отчаяние. Но когда я с вами... я чувствую надежду. И это пугает меня больше любой эпидемии."
                }
            ]
        },
        "flags": {"maria_romance_developed": True}
    },
    
    "romance_confession_maría": {
        "id": "rom_mar_03",
        "chapter": 14,
        "location": "ship_quarters",
        "trigger": {"maria_relationship": 80, "flag": "maria_romance_developed"},
        "scene": {
            "description": "Мария приходит к вам в каюту после тяжёлого дня. Она приносит чай — её способ заботы.",
            "dialogues": [
                {
                    "speaker": "maria",
                    "text": "Я принесла вам травяной чай. Помогает от стресса. И... мне нужно сказать кое-что.",
                    "emotion": "nervous"
                },
                {
                    "speaker": "player",
                    "text": "Что случилось?"
                },
                {
                    "speaker": "maria",
                    "text": "Я не могу больше притворяться. Каждый раз, когда вы уходите на задание, моё сердце замирает. Не от страха за пациента — от страха потерять вас.",
                    "emotion": "emotional"
                },
                {
                    "speaker": "narrator",
                    "text": "Она ставит чашку и берёт вас за руки."
                },
                {
                    "speaker": "maria",
                    "text": "Я люблю вас. Люблю так, что это мешает мне быть профессионалом. И я не знаю, что с этим делать."
                }
            ]
        },
        "choices": [
            {
                "text": "Обнять её и пообещать всегда возвращаться",
                "effects": {"maria_relationship": 25, "romantic_partner": "maria"},
                "next": "rom_mar_03a"
            },
            {
                "text": "Признаться, что чувства взаимны",
                "effects": {"maria_relationship": 20, "romantic_partner": "maria"},
                "next": "rom_mar_03b"
            },
            {
                "text": "Отклонить — корабль не место для романов",
                "effects": {"maria_relationship": -25},
                "next": "rom_mar_03c"
            }
        ]
    }
}

# === АННА — НАВИГАТОР ===

ANNA_ROMANCE_EVENTS = {
    "romance_start_anna": {
        "id": "rom_ann_01",
        "chapter": 5,
        "location": "navigation_room",
        "trigger": {"anna_relationship": 30, "event": "chart_review"},
        "scene": {
            "description": "Вы находите Анну за работой над навигационными картами. Она настолько увлечена, что не замечает вашего присутствия.",
            "dialogues": [
                {
                    "speaker": "anna",
                    "text": "...и если мы пойдём через туманность, то сократим время на три дня. Хотя риск... а, капитан! Как давно вы там стоите?",
                    "emotion": "startled"
                },
                {
                    "speaker": "narrator",
                    "text": "Она быстро закрывает голограмму, которую изучала. Вы успеваете заметить схему маршрута с пометкой «личное»."
                }
            ]
        },
        "choices": [
            {
                "text": "Что это было за «личное»?",
                "effects": {"anna_relationship": 10},
                "next": "rom_ann_01a"
            },
            {
                "text": "Просто admiring вашей работе",
                "effects": {"anna_relationship": 15},
                "next": "rom_ann_01b"
            },
            {
                "text": "Мне нужны результаты, не секреты",
                "effects": {"anna_relationship": -10},
                "next": "rom_ann_01c"
            }
        ]
    },
    "rom_ann_01b": {
        "id": "rom_ann_01b",
        "scene": {
            "dialogues": [
                {
                    "speaker": "anna",
                    "text": "Admiring? Моей работе? Большинство людей считают навигацию скучной. Просто цифры и координаты.",
                    "emotion": "surprised"
                },
                {
                    "speaker": "player",
                    "text": "Цифры и координаты — это карта вселенной. Ты находишь путь там, где другие видят только пустоту."
                },
                {
                    "speaker": "anna",
                    "text": "Вы... вы действительно так думаете? Знаете, я мечтала найти кого-то, кто понимает. Кто видит звёзды так же, как я.",
                    "emotion": "touched"
                },
                {
                    "speaker": "narrator",
                    "text": "Она показывает вам скрытую голограмму — карту особых мест галактики, которые она хотела посетить «с кем-то особенным»."
                }
            ]
        },
        "flags": {"anna_romance_started": True}
    },
    
    "romance_confession_anna": {
        "id": "rom_ann_03",
        "chapter": 13,
        "location": "observation_deck",
        "trigger": {"anna_relationship": 80, "flag": "anna_romance_developed"},
        "scene": {
            "description": "После выбора пути вы находите Анну на смотровой площадке, наблюдающей за звёздами.",
            "dialogues": [
                {
                    "speaker": "anna",
                    "text": "Знаете, я составила карту всех известных миров. Тысячи систем, миллионы звёзд. Но есть одна точка, которую я не могу найти ни на одной карте.",
                    "emotion": "thoughtful"
                },
                {
                    "speaker": "player",
                    "text": "Какая?"
                },
                {
                    "speaker": "anna",
                    "text": "Моё место. Где я принадлежу. Я думала, что это космос, что навигация — мой путь. Но оказывается, путь — это не место. Это человек.",
                    "emotion": "vulnerable"
                },
                {
                    "speaker": "narrator",
                    "text": "Она поворачивается к вам, и в её глазах блестят звёзды."
                },
                {
                    "speaker": "anna",
                    "text": "Я люблю вас. Вы — мой дом в этой бесконечной пустоте. И куда бы ни вели наши координаты, я хочу быть там с вами."
                }
            ]
        },
        "choices": [
            {
                "text": "Поцеловать её под звёздами",
                "effects": {"anna_relationship": 25, "romantic_partner": "anna"},
                "next": "rom_ann_03a"
            },
            {
                "text": "Сказать, что она — твой дом тоже",
                "effects": {"anna_relationship": 20, "romantic_partner": "anna"},
                "next": "rom_ann_03b"
            }
        ]
    }
}

# === ВЕРОНИКА — ИНФОРМАТОР ===

VERONICA_ROMANCE_EVENTS = {
    "romance_start_veronica": {
        "id": "rom_ver_01",
        "chapter": 6,
        "location": "underground_bar",
        "trigger": {"veronica_relationship": 30, "event": "intel_meeting"},
        "scene": {
            "description": "Встреча с Вероникой в подпольном баре для обмена информацией. Она выглядит более расслабленной, чем обычно.",
            "dialogues": [
                {
                    "speaker": "veronica",
                    "text": "Выпьете со мной? Информация подождёт пять минут. Иногда даже шпионам нужен отдых.",
                    "emotion": "relaxed"
                },
                {
                    "speaker": "narrator",
                    "text": "Она подвигает к вам бокал. В тусклом свете бара она выглядит загадочной и притягательной."
                },
                {
                    "speaker": "veronica",
                    "text": "Знаете, я продаю секреты по всей галактике. Но есть один секрет, который я не продам никому. Хотите узнать какой?",
                    "emotion": "mysterious"
                }
            ]
        },
        "choices": [
            {
                "text": "Расскажи",
                "effects": {"veronica_relationship": 15},
                "next": "rom_ver_01a"
            },
            {
                "text": "Я предпочитаю добыть информацию сам",
                "effects": {"veronica_relationship": 20},
                "next": "rom_ver_01b"
            },
            {
                "text": "У меня нет времени на игры",
                "effects": {"veronica_relationship": -10},
                "next": "rom_ver_01c"
            }
        ]
    },
    "rom_ver_01b": {
        "id": "rom_ver_01b",
        "scene": {
            "dialogues": [
                {
                    "speaker": "veronica",
                    "text": "Ooh, мне нравится этот подход. Не каждый готов сам рисковать ради истины.",
                    "emotion": "impressed"
                },
                {
                    "speaker": "narrator",
                    "text": "Она наклоняется ближе через стол."
                },
                {
                    "speaker": "veronica",
                    "text": "Секрет в том... что я устала быть одной. Устала доверять только себе. И в вас я вижу кого-то, кому... кому я могла бы довериться. По-настоящему.",
                    "emotion": "vulnerable"
                }
            ]
        },
        "flags": {"veronica_romance_started": True}
    },
    
    "romance_confession_veronica": {
        "id": "rom_ver_03",
        "chapter": 15,
        "location": "safe_house",
        "trigger": {"veronica_relationship": 80, "flag": "veronica_romance_developed"},
        "scene": {
            "description": "После раскрытия предательства Вероника приходит к вам в укрытие.",
            "dialogues": [
                {
                    "speaker": "veronica",
                    "text": "Я проверила все контакты. Все источники. Вы — единственный, кто не предал. Единственный, на кого я могу положиться.",
                    "emotion": "serious"
                },
                {
                    "speaker": "narrator",
                    "text": "Она снимает свою обычную маску цинизма, и вы видите её настоящую — уставшую, но полную надежды."
                },
                {
                    "speaker": "veronica",
                    "text": "Я всю жизнь пряталась за ложью. Но с вами... я хочу быть честной. Я люблю вас. И это единственная правда, которая имеет значение."
                }
            ]
        },
        "choices": [
            {
                "text": "Обнять её — она больше не одна",
                "effects": {"veronica_relationship": 25, "romantic_partner": "veronica"},
                "next": "rom_ver_03a"
            },
            {
                "text": "Признаться во взаимности",
                "effects": {"veronica_relationship": 20, "romantic_partner": "veronica"},
                "next": "rom_ver_03b"
            }
        ]
    }
}

# === ЗАРА — РЫЦАРЬ ОРДЕНА ===

ZARA_ROMANCE_EVENTS = {
    "romance_start_zara": {
        "id": "rom_zar_01",
        "chapter": 8,
        "location": "ancient_temple",
        "trigger": {"zara_relationship": 30, "event": "temple_exploration"},
        "scene": {
            "description": "Во время исследования древнего храма вы и Зара обнаруживаете скрытую комнату с древними фресками.",
            "dialogues": [
                {
                    "speaker": "zara",
                    "text": "Эти изображения... они рассказывают историю первых Наблюдателей. Видите эту фигуру? Это Основательница. Она тоже была... одна.",
                    "emotion": "contemplative"
                },
                {
                    "speaker": "narrator",
                    "text": "Она проводит рукой по фреске, и вы видите печаль в её глазах."
                },
                {
                    "speaker": "zara",
                    "text": "Орден учит, что привязанность — отвлечение. Но иногда я задаюсь вопросом... стоит ли вечность того, чтобы прожить её в одиночестве?",
                    "emotion": "vulnerable"
                }
            ]
        },
        "choices": [
            {
                "text": "Вечность не важна без того, кого любишь",
                "effects": {"zara_relationship": 20},
                "next": "rom_zar_01a"
            },
            {
                "text": "Цель Ордена превыше личного",
                "effects": {"zara_relationship": -5},
                "next": "rom_zar_01b"
            },
            {
                "text": "Может, ты нашла того, с кем разделить путь",
                "effects": {"zara_relationship": 25},
                "next": "rom_zar_01c"
            }
        ]
    },
    "rom_zar_01c": {
        "id": "rom_zar_01c",
        "scene": {
            "dialogues": [
                {
                    "speaker": "zara",
                    "text": "Вы... смелый человек. Говорить такие вещи рыцарю Ордена. Но... может, вы правы. Может, моя судьба — не только служение.",
                    "emotion": "touched"
                },
                {
                    "speaker": "narrator",
                    "text": "Её рука касается вашей в полумраке древнего храма."
                },
                {
                    "speaker": "zara",
                    "text": "Я чувствую вашу душу. Она... светлая. Чистая. Таких людей я встречала редко. И никогда не думала, что буду дорожить одним из них.",
                    "emotion": "soft"
                }
            ]
        },
        "flags": {"zara_romance_started": True}
    },
    
    "romance_confession_zara": {
        "id": "rom_zar_03",
        "chapter": 14,
        "location": "order_sanctuary",
        "trigger": {"zara_relationship": 80, "flag": "zara_romance_developed"},
        "scene": {
            "description": "После ритуала инициации Зара приходит к вам в святилище Ордена.",
            "dialogues": [
                {
                    "speaker": "zara",
                    "text": "Я видела ваше будущее во время ритуала. Видела множество путей. Но во всех них... вы были рядом со мной.",
                    "emotion": "certain"
                },
                {
                    "speaker": "narrator",
                    "text": "Она снимает ceremonial плащ, открывая простую тунику."
                },
                {
                    "speaker": "zara",
                    "text": "Орден запрещает привязанности. Но я выбираю вас. Не как рыцарь, а как женщина. Я люблю вас — и это самый важный выбор в моей вечности."
                }
            ]
        },
        "choices": [
            {
                "text": "Выбрать её — вопреки всему",
                "effects": {"zara_relationship": 25, "romantic_partner": "zara"},
                "next": "rom_zar_03a"
            },
            {
                "text": "Сказать, что она — твой свет во тьме",
                "effects": {"zara_relationship": 20, "romantic_partner": "zara"},
                "next": "rom_zar_03b"
            }
        ]
    }
}

# === КИРА — КУРЬЕР ===

KIRA_ROMANCE_EVENTS = {
    "romance_start_kira": {
        "id": "rom_kir_01",
        "chapter": 7,
        "location": "spaceport_bar",
        "trigger": {"kira_relationship": 30, "event": "drinks_challenge"},
        "scene": {
            "description": "После успешного контракта Кира приглашает вас выпить в космопорту.",
            "dialogues": [
                {
                    "speaker": "kira",
                    "text": "Давай поспорим! Кто больше выпьет — тот и назначает следующую миссию. И никаких «я капитан, мне нельзя»!",
                    "emotion": "playful"
                },
                {
                    "speaker": "narrator",
                    "text": "Её глаза блестят от азарта и алкоголя. Ряднер хмыкает в углу, делая вид, что не замечает."
                },
                {
                    "speaker": "kira",
                    "text": "А если серьёзно... ты первый человек за долгое время, с кем мне... интересно. Не как с конкурентом. Как с... кем-то особенным.",
                    "emotion": "soft"
                }
            ]
        },
        "choices": [
            {
                "text": "Принять вызов — и выиграть",
                "effects": {"kira_relationship": 15},
                "next": "rom_kir_01a"
            },
            {
                "text": "Проиграть намеренно",
                "effects": {"kira_relationship": 20},
                "next": "rom_kir_01b"
            },
            {
                "text": "Отказаться от пьянства",
                "effects": {"kira_relationship": -5},
                "next": "rom_kir_01c"
            }
        ]
    },
    "rom_kir_01b": {
        "id": "rom_kir_01b",
        "scene": {
            "dialogues": [
                {
                    "speaker": "kira",
                    "text": "Ха! Победа! Хотя... ты специально проиграл, да? Я вижу по твоим глазам.",
                    "emotion": "amused"
                },
                {
                    "speaker": "player",
                    "text": "Может, я просто хотел увидеть твою улыбку."
                },
                {
                    "speaker": "kira",
                    "text": "...Ты опасный человек. Умеешь выбивать меня из колеи. И мне... мне это нравится. Больше, чем должно.",
                    "emotion": "flustered"
                }
            ]
        },
        "flags": {"kira_romance_started": True}
    },
    
    "romance_confession_kira": {
        "id": "rom_kir_03",
        "chapter": 12,
        "location": "ship_cockpit",
        "trigger": {"kira_relationship": 80, "flag": "kira_romance_developed"},
        "scene": {
            "description": "Во время совместного полёта Кира неожиданно отключает автопилот и смотрит на вас.",
            "dialogues": [
                {
                    "speaker": "kira",
                    "text": "Знаешь, я всегда думала, что свобода — это одиночество. Никаких привязанностей, никаких обязательств. Только ты, корабль и звёзды.",
                    "emotion": "thoughtful"
                },
                {
                    "speaker": "narrator",
                    "text": "Она берёт вас за руку, переплетая пальцы."
                },
                {
                    "speaker": "kira",
                    "text": "Но оказывается, настоящая свобода — это найти того, с кем хочешь разделить путь. Я люблю тебя. И для меня это... самый страшный и важный груз, который я когда-либо несла.",
                    "emotion": "vulnerable"
                }
            ]
        },
        "choices": [
            {
                "text": "Поцеловать её — и предложить лететь вместе",
                "effects": {"kira_relationship": 25, "romantic_partner": "kira"},
                "next": "rom_kir_03a"
            },
            {
                "text": "Сказать, что она — тоя свобода",
                "effects": {"kira_relationship": 20, "romantic_partner": "kira"},
                "next": "rom_kir_03b"
            }
        ]
    }
}

# Объединение всех романтических событий
ALL_ROMANCE_EVENTS = {
    "mia": MIA_ROMANCE_EVENTS,
    "maria": MARIA_ROMANCE_EVENTS,
    "anna": ANNA_ROMANCE_EVENTS,
    "veronica": VERONICA_ROMANCE_EVENTS,
    "zara": ZARA_ROMANCE_EVENTS,
    "kira": KIRA_ROMANCE_EVENTS
}

def get_romance_event(character, event_id):
    """Получить романтическое событие"""
    events = ALL_ROMANCE_EVENTS.get(character, {})
    return events.get(event_id)

def check_romance_trigger(event, game_state):
    """Проверить триггер романтического события"""
    trigger = event.get("trigger", {})
    
    for key, value in trigger.items():
        if key == "flag":
            if not game_state.get(value):
                return False
        elif key == "event":
            if game_state.get("last_event") != value:
                return False
        elif key == f"{event['id'].split('_')[1]}_relationship":
            char = event['id'].split('_')[1]
            if game_state.get("relationships", {}).get(char, 0) < value:
                return False
    
    return True

def get_available_romance_events(game_state):
    """Получить доступные романтические события"""
    available = []
    
    for character, events in ALL_ROMANCE_EVENTS.items():
        for event_id, event in events.items():
            if check_romance_trigger(event, game_state):
                if event_id not in game_state.get("seen_romance_events", []):
                    available.append(event)
    
    return available
