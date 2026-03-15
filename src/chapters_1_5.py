# -*- coding: utf-8 -*-
"""
Star Courier - Диалоги глав 1-5
Полноценная разветвлённая система диалогов для начала игры

Включает:
- Глава 1: Пробуждение
- Глава 2: Первый контракт
- Глава 3: Столкновение
- Глава 4: Тайны корабля
- Глава 5: Выбор пути

Особенности:
- Множество выборов с последствиями
- Система репутации
- Уникальные ветки диалогов
- Введение всех персонажей
"""

from src.dialogues import Dialogue, DialogueNode, Choice, ChoiceEffect
from typing import Dict, Any

# ============================================================================
# КОНСТАНТЫ И КОНФИГУРАЦИЯ
# ============================================================================

CHAPTER_1_5_CONFIG = {
    "starting_reputation": 50,
    "reputation_change": {
        "minor": 3,
        "moderate": 7,
        "major": 15,
        "critical": 25
    },
    "path_influence": {
        "alliance": 0,
        "observer": 0,
        "independence": 0
    }
}

# ============================================================================
# ГЛАВА 1: ПРОБУЖДЕНИЕ
# ============================================================================

CHAPTER_1_DIALOGUES = {
    # === СЦЕНА: Начало игры ===
    "intro_awakening": {
        "id": "ch1_intro",
        "type": "narration",
        "scene": {
            "location": "cryo_chamber",
            "description": "Темнота. Холод. Потом — свет. Системы корабля оживает вокруг вас.",
            "mood": "mysterious"
        },
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Вы просыпаетесь в криокамере звездолёта «Элея». Голова раскалывается, воспоминания размыты. Сколько вы проспали? Дни? Годы?"
            },
            {
                "speaker": "athena",
                "text": "Капитан Велл? Капитан, вы меня слышите? Это Афина — ИИ корабля. Криосон длился 47 дней. У нас... ситуация.",
                "emotion": "concerned"
            }
        ],
        "choices": [
            {
                "text": "Какая ситуация?",
                "effects": {"path": "alliance", "athena": 5},
                "next": "ch1_situation"
            },
            {
                "text": "Сначала дай мне прийти в себя",
                "effects": {"path": "observer", "athena": -3},
                "next": "ch1_recovery"
            },
            {
                "text": "Кто я? Ничего не помню...",
                "effects": {"path": "independence", "athena": 3},
                "next": "ch1_amnesia"
            }
        ]
    },

    "ch1_situation": {
        "id": "ch1_situation",
        "dialogues": [
            {
                "speaker": "athena",
                "text": "Пиратская эскадра засекла нас три дня назад. Они ждут, когда мы выйдем из стазиса. У нас есть около 30 минут до их атаки. Экипаж всё ещё в криосне — я разбудила только вас.",
                "emotion": "urgent"
            },
            {
                "speaker": "narrator",
                "text": "Красный свет аварийной сигнализации заливает коридор. На экране — схематическое изображение трёх кораблей, окружающих «Элею»."
            }
        ],
        "choices": [
            {
                "text": "Разбуди экипаж немедленно!",
                "effects": {"leadership": 5, "path": "alliance"},
                "next": "ch1_wake_crew"
            },
            {
                "text": "Можем ли мы сбежать?",
                "effects": {"tactical": 5, "path": "independence"},
                "next": "ch1_escape_option"
            },
            {
                "text": "Свяжись с ними — попробуем договориться",
                "effects": {"diplomacy": 5, "path": "observer"},
                "next": "ch1_negotiate"
            }
        ]
    },

    "ch1_recovery": {
        "id": "ch1_recovery",
        "dialogues": [
            {
                "speaker": "athena",
                "text": "Понимаю. Восстановление после криосна требует времени. Но боюсь, у нас его нет. Пираты атакуют через 27 минут. Я вынуждена вывести вас из состояния покоя раньше времени.",
                "emotion": "apologetic"
            },
            {
                "speaker": "narrator",
                "text": "Головокружение медленно отступает. Вы чувствуете себя... странно. Словно что-то изменилось в вас за время сна."
            },
            {
                "speaker": "athena",
                "text": "Капитан, ваши показатели... аномальны. Криокамера зафиксировала всплеск нейронной активности. Как вы себя чувствуете?",
                "emotion": "concerned"
            }
        ],
        "choices": [
            {
                "text": "Чувствую... что-то новое. Словно могу коснуться разума",
                "effects": {"ability_hint": "psionic", "path": "observer"},
                "next": "ch1_psionic_hint"
            },
            {
                "text": "Тело горит огнём — но это нормально после криосна",
                "effects": {"ability_hint": "biotic", "path": "independence"},
                "next": "ch1_biotic_hint"
            },
            {
                "text": "Голова ясная. Что происходит?",
                "effects": {"ability_hint": "alchemy", "path": "alliance"},
                "next": "ch1_situation"
            }
        ]
    },

    "ch1_amnesia": {
        "id": "ch1_amnesia",
        "dialogues": [
            {
                "speaker": "athena",
                "text": "Это... неожиданно. Криосон не должен вызывать амнезию. Капитан, вы — Макс Велл. Владелец и капитан звездолёта «Элея». Мы выполняли транспортный контракт, когда нас перехватили пираты.",
                "emotion": "worried"
            },
            {
                "speaker": "narrator",
                "text": "Имя звучит знакомо, но лицо в отражении экрана — чужое. Или своё? Вы не уверены."
            },
            {
                "speaker": "athena",
                "text": "У меня есть записи ваших предыдущих миссий. Возможно, они помогут восстановить память. Но сейчас — у нас 28 минут до атаки.",
                "emotion": "urgent"
            }
        ],
        "choices": [
            {
                "text": "Покажи записи позже. Что нам делать сейчас?",
                "effects": {"focus": "tactical", "path": "independence"},
                "next": "ch1_situation"
            },
            {
                "text": "Покажи записи — они могут содержать подсказки",
                "effects": {"focus": "knowledge", "path": "observer"},
                "next": "ch1_view_records"
            },
            {
                "text": "Неважно, кто я был. Важно — кто я сейчас",
                "effects": {"focus": "philosophy", "path": "alliance"},
                "next": "ch1_identity_choice"
            }
        ]
    },

    "ch1_wake_crew": {
        "id": "ch1_wake_crew",
        "dialogues": [
            {
                "speaker": "athena",
                "text": "Уже делаю. Процедура экстренного пробуждения запущена для ключевого персонала. Первыми выйдут: Рина — инженер, Надежда — пилот, и Алия — научный сотрудник.",
                "emotion": "efficient"
            },
            {
                "speaker": "narrator",
                "text": "В коридоре раздаётся шипение открывающихся криокамер. Кто-то кашляет. Кто-то ругается."
            },
            {
                "speaker": "rina",
                "text": "*голос из коридора* Какого чёрта?! Экстренное пробуждение? Это стоит два дня головной боли!",
                "emotion": "angry"
            },
            {
                "speaker": "alia",
                "text": "*спокойный голос* Рина, тише. Афина не разбудила бы нас без причины. Капитан?",
                "emotion": "calm"
            }
        ],
        "choices": [
            {
                "text": "Команда, у нас ситуация. Пираты атакуют через 25 минут",
                "effects": {"leadership": 10, "rina": 5, "alia": 5},
                "next": "ch1_crew_briefing"
            },
            {
                "text": "Рина, прости за головную боль. Мне нужна твоя помощь",
                "effects": {"empathy": 5, "rina": 10},
                "next": "ch1_rina_appease"
            },
            {
                "text": "Алия, возьми командование на себя. Мне нужно пару минут",
                "effects": {"delegation": 5, "alia": 10},
                "next": "ch1_delegation"
            }
        ]
    },

    "ch1_crew_briefing": {
        "id": "ch1_crew_briefing",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Экипаж собирается в коридоре криоотсека. Рина — молодая женщина с растрёпанными волосами и пятнами машинного масла на комбинезоне. Алия — высокая азари с кожей голубоватого оттенка и мудрым взглядом. Надежда молча занимает позицию у стены."
            },
            {
                "speaker": "nadezhda",
                "text": "Я уже проверила системы. Двигатели на минимуме, щиты разряжены на 40%. У нас мало шансов в прямом бою.",
                "emotion": "professional"
            },
            {
                "speaker": "rina",
                "text": "Но если я смогу перераспределить энергию со стазис-систем... 15 минут работы, и у нас будет полный щит!",
                "emotion": "determined"
            },
            {
                "speaker": "alia",
                "text": "Или я могу создать биотическое поле. Прикрыть нас на несколько минут. Но это истощит меня.",
                "emotion": "thoughtful"
            }
        ],
        "choices": [
            {
                "text": "Рина, работай над щитами. Алия, сбереги силы для крайнего случая",
                "effects": {"tactical": 10, "rina": 10, "alia": -5},
                "next": "ch1_plan_shields"
            },
            {
                "text": "Алия, готовь поле. Рина, усиливай двигатели — будем убегать",
                "effects": {"tactical": 10, "alia": 10, "rina": -5},
                "next": "ch1_plan_escape"
            },
            {
                "text": "Надежда, твой голос важен. Что ты предлагаешь?",
                "effects": {"leadership": 10, "nadezhda": 15},
                "next": "ch1_ask_nadezhda"
            },
            {
                "text": "Я должен кое-что рассказать вам...",
                "effects": {"honesty": 10},
                "next": "ch1_confession"
            }
        ]
    },

    "ch1_ask_nadezhda": {
        "id": "ch1_ask_nadezhda",
        "dialogues": [
            {
                "speaker": "nadezhda",
                "text": "Вы спрашиваете моё мнение? Интересно. *пауза* Большинство капитанов командуют, не спрашивая. Хорошо. Вот мой анализ.",
                "emotion": "surprised"
            },
            {
                "speaker": "nadezhda",
                "text": "Три корабля — это стандартная пиратская «клешня». Один флагман, два перехватчика. Флагман — старый корвет класса «Гончая». Устаревший, но опасный. Перехватчики быстрее, но слабее бронированы.",
                "emotion": "analytical"
            },
            {
                "speaker": "nadezhda",
                "text": "Если я поведу «Элею» через астероидное поле на севере... перехватчики отстанут. Флагман не сможет маневрировать. Мы потеряем их за 7 минут. Но это требует идеального пилотирования.",
                "emotion": "confident"
            }
        ],
        "choices": [
            {
                "text": "Делай это. Я доверяю твоему пилотированию",
                "effects": {"trust": 15, "nadezhda": 20, "path": "independence"},
                "next": "ch1_asteroid_plan"
            },
            {
                "text": "Слишком рискованно. Есть другой вариант?",
                "effects": {"caution": 5, "nadezhda": -5},
                "next": "ch1_alternative_plans"
            },
            {
                "text": "Команда, голосуем. Кто за план Надежды?",
                "effects": {"democracy": 10, "nadezhda": 10, "alia": 5, "rina": 5},
                "next": "ch1_vote"
            }
        ]
    },

    "ch1_confession": {
        "id": "ch1_confession",
        "dialogues": [
            {
                "speaker": "player",
                "text": "Я... я не помню, кто я. Афина говорит, что я Макс Велл, но это имя ничего не значит для меня."
            },
            {
                "speaker": "rina",
                "text": "Амнезия? Серьёзно?! Отлично, просто отлично! Капитан без памяти посреди пиратской атаки!",
                "emotion": "panicked"
            },
            {
                "speaker": "alia",
                "text": "Тише, Рина. *подходит ближе* Капитан... Макс. Память вернётся. Криосон иногда вызывает временные провалы. Я видела такое раньше.",
                "emotion": "calm"
            },
            {
                "speaker": "alia",
                "text": "Но сейчас неважно, помните ли вы прошлое. Важно — можете ли вы вести нас в настоящем. Я видела, как вы командуете. Это в вашей крови.",
                "emotion": "reassuring"
            }
        ],
        "choices": [
            {
                "text": "Спасибо, Алия. Я постараюсь быть достойным",
                "effects": {"alia": 15, "leadership": 5},
                "next": "ch1_crew_briefing"
            },
            {
                "text": "Но что если я не тот, кем вы меня считаете?",
                "effects": {"alia": 10, "philosophy": 5},
                "next": "ch1_identity_doubt"
            },
            {
                "text": "А что вы знаете обо мне? Расскажите",
                "effects": {"knowledge": 5, "alia": 5},
                "next": "ch1_backstory_reveal"
            }
        ]
    },

    "ch1_identity_doubt": {
        "id": "ch1_identity_doubt",
        "dialogues": [
            {
                "speaker": "alia",
                "text": "Тогда мы узнаем нового вас. Личность — это не только воспоминания. Это выборы, которые мы делаем. Действия. Вы спасли этот экипаж три месяца назад, когда станция взорвалась. Тот, кто это сделал — настоящий. Независимо от памяти.",
                "emotion": "wise"
            },
            {
                "speaker": "rina",
                "text": "Она права. Я... прости за панику. Ты можешь не помнить, но мы помним. Ты хороший капитан. Вот что важно.",
                "emotion": "embarrassed"
            },
            {
                "speaker": "nadezhda",
                "text": "Сентиментальность потом. У нас 22 минуты. Капитан, решение?",
                "emotion": "focused"
            }
        ],
        "choices": [
            {
                "text": "Надежда, веди нас через астероиды. Доверяю тебе",
                "effects": {"nadezhda": 20, "leadership": 10},
                "next": "ch1_asteroid_plan"
            },
            {
                "text": "Рина, щиты — приоритет. Защитимся и прорвёмся",
                "effects": {"rina": 15, "tactical": 10},
                "next": "ch1_plan_shields"
            },
            {
                "text": "Афина, свяжись с пиратами. Попробуем договориться",
                "effects": {"diplomacy": 15, "path": "observer"},
                "next": "ch1_negotiate"
            }
        ]
    },

    "ch1_backstory_reveal": {
        "id": "ch1_backstory_reveal",
        "dialogues": [
            {
                "speaker": "alia",
                "text": "Ты был пилотом Альянса. Одним из лучших. Потом... что-то случилось. Ты не говоришь об этом, но я чувствую шрамы. Не только физические.",
                "emotion": "serious"
            },
            {
                "speaker": "rina",
                "text": "Ты купил «Элею» два года назад. Собрал нас — команду неудачников, изгоев. Дал нам дом. Цель. Большинство капитанов не стали бы брать таких как мы.",
                "emotion": "grateful"
            },
            {
                "speaker": "nadezhda",
                "text": "Я была наёмником. Без команды, без цели. Ты предложил мне не работу — семью. Этого не забывают.",
                "emotion": "rare_softness"
            }
        ],
        "choices": [
            {
                "text": "Звучит как хороший человек. Надеюсь, я смогу им быть",
                "effects": {"all": 5, "path": "alliance"},
                "next": "ch1_crew_briefing"
            },
            {
                "text": "Неудачники? Изгои? Расскажите подробнее...",
                "effects": {"knowledge": 10},
                "next": "ch1_crew_backgrounds"
            },
            {
                "text": "Достаточно разговоров. Время действовать",
                "effects": {"focus": 10, "path": "independence"},
                "next": "ch1_crew_briefing"
            }
        ]
    },

    "ch1_crew_backgrounds": {
        "id": "ch1_crew_backgrounds",
        "dialogues": [
            {
                "speaker": "rina",
                "text": "Я... устроила аварию на станции. Случайно! Ну, почти. Мои эксперименты иногда выходят из-под контроля. Меня хотели арестовать, но ты вмешался.",
                "emotion": "embarrassed"
            },
            {
                "speaker": "alia",
                "text": "Азари живут веками. Я видела многое, но устала от политики своего народа. Я искала... тишины. Понимания. Ты дал мне и то, и другое.",
                "emotion": "peaceful"
            },
            {
                "speaker": "nadezhda",
                "text": "Я убивала за деньги. Потом устала. Но навыки никуда не делись. Ты показал мне другой путь — защищать, а не уничтожать.",
                "emotion": "cold_but_thankful"
            },
            {
                "speaker": "athena",
                "text": "Капитан, у нас 19 минут. Возможно, стоит отложить биографии?",
                "emotion": "urgent"
            }
        ],
        "choices": [
            {
                "text": "Спасибо за откровенность. Теперь к делу!",
                "effects": {"all": 10, "trust": 10},
                "next": "ch1_crew_briefing"
            }
        ]
    },

    # === ПЛАНЫ ДЕЙСТВИЙ ===

    "ch1_plan_shields": {
        "id": "ch1_plan_shields",
        "dialogues": [
            {
                "speaker": "rina",
                "text": "Поняла! Начинаю перераспределение. 15 минут — и у нас будет щит класса «крепость»!",
                "emotion": "determined"
            },
            {
                "speaker": "athena",
                "text": "Капитан, пиратский флагман запрашивает связь. Открыть канал?",
                "emotion": "neutral"
            }
        ],
        "choices": [
            {
                "text": "Открыть канал. Послушаем, что они хотят",
                "effects": {"diplomacy": 5, "path": "observer"},
                "next": "ch1_pirate_contact"
            },
            {
                "text": "Игнорировать. Сосредоточьтесь на подготовке",
                "effects": {"focus": 5, "path": "independence"},
                "next": "ch1_prepare_battle"
            },
            {
                "text": "Открыть, но только аудио. Не показывай им нас",
                "effects": {"tactical": 10, "path": "alliance"},
                "next": "ch1_pirate_audio_only"
            }
        ]
    },

    "ch1_plan_escape": {
        "id": "ch1_plan_escape",
        "dialogues": [
            {
                "speaker": "alia",
                "text": "Поняла. Буду готова. Но, капитан — биотическое поле истощит меня. После этого мне понадобится время на восстановление.",
                "emotion": "serious"
            },
            {
                "speaker": "rina",
                "text": "Двигатели через 12 минут! Ускоряю системы!",
                "emotion": "excited"
            },
            {
                "speaker": "nadezhda",
                "text": "Я рассчитаю маршрут через астероиды. Минимальный риск, максимальная скорость.",
                "emotion": "focused"
            }
        ],
        "choices": [
            {
                "text": "Отлично. Команда, приготовиться к отбытию!",
                "effects": {"leadership": 10, "all": 5},
                "next": "ch1_escape_sequence"
            }
        ]
    },

    "ch1_asteroid_plan": {
        "id": "ch1_asteroid_plan",
        "dialogues": [
            {
                "speaker": "nadezhda",
                "text": "Есть, капитан. *редкая улыбка* Наконец-то интересная работа.",
                "emotion": "pleased"
            },
            {
                "speaker": "narrator",
                "text": "Надежда занимает место пилота. Её руки летают над консолью. «Элея» вздрагивает — двигатели оживают."
            },
            {
                "speaker": "rina",
                "text": "У нас будет 40% щитов и минимальное вооружение. Этого хватит, чтобы пережить пару попаданий, но не больше.",
                "emotion": "worried"
            },
            {
                "speaker": "alia",
                "text": "Я добавлю биотическое прикрытие для манёвра. Это даст нам дополнительные секунды.",
                "emotion": "supportive"
            }
        ],
        "choices": [
            {
                "text": "Команда, это наш шанс. Все по местам!",
                "effects": {"leadership": 10, "morale": 15},
                "next": "ch1_asteroid_sequence"
            }
        ]
    },

    # === КОНТАКТ С ПИРАТАМИ ===

    "ch1_pirate_contact": {
        "id": "ch1_pirate_contact",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Экран мерцает, и появляется лицо — женщина с короткими волосами и шрамом через глаз."
            },
            {
                "speaker": "pirate_captain",
                "text": "Капитан Велл. Наконец-то проснулись. Я — Селена Ро. У меня к вам деловое предложение.",
                "emotion": "confident"
            },
            {
                "speaker": "selena_ro",
                "text": "Груз в вашем трюме принадлежит моему клиенту. Верните его — и вы свободны. Сопротивляйтесь — и я возьму его сама. Вместе с вашим кораблём.",
                "emotion": "threatening"
            }
        ],
        "choices": [
            {
                "text": "Какой груз? О чём вы говорите?",
                "effects": {"knowledge": 5},
                "next": "ch1_ask_about_cargo"
            },
            {
                "text": "У меня нет ничего, что принадлежало бы вам или вашему клиенту",
                "effects": {"defiance": 10, "path": "independence"},
                "next": "ch1_deny_cargo"
            },
            {
                "text": "Предположим, я соглашусь. Как я могу быть уверен, что вы отпустите нас?",
                "effects": {"negotiation": 10, "path": "observer"},
                "next": "ch1_negotiate_terms"
            },
            {
                "text": "[Блеф] Груз уже уничтожен. Вы опоздали.",
                "effects": {"deception": 15, "path": "independence"},
                "next": "ch1_bluff_destroyed"
            }
        ]
    },

    "ch1_ask_about_cargo": {
        "id": "ch1_ask_about_cargo",
        "dialogues": [
            {
                "speaker": "selena_ro",
                "text": "*смеётся* Не притворяйтесь. Аномальный контейнер в трюме 3. Вы знаете, что внутри? Я знаю. И мой клиент готов заплатить очень дорого.",
                "emotion": "amused"
            },
            {
                "speaker": "athena",
                "text": "*шёпот в ухо* Капитан, я обнаружила незарегистрированный контейнер в трюме 3. Он был загружен перед вашим криосном. Без вашего ведома.",
                "emotion": "concerned"
            }
        ],
        "choices": [
            {
                "text": "Я не знал об этом. Дайте мне проверить",
                "effects": {"honesty": 10, "selena": 5},
                "next": "ch1_check_cargo"
            },
            {
                "text": "Неважно, что там. Это мой корабль, и я не отдам его просто так",
                "effects": {"defiance": 10, "path": "independence"},
                "next": "ch1_refuse_demand"
            },
            {
                "text": "Сколько предлагает ваш клиент? Может, у меня есть контрпредложение",
                "effects": {"negotiation": 15, "path": "observer"},
                "next": "ch1_counter_offer"
            }
        ]
    },

    "ch1_negotiate_terms": {
        "id": "ch1_negotiate_terms",
        "dialogues": [
            {
                "speaker": "selena_ro",
                "text": "Разумный вопрос. Хорошо — я даю слово. Груз за вашу жизнь и корабль. Моё слово — закон среди пиратов. Нарушить его — значит потерять репутацию.",
                "emotion": "calculating"
            },
            {
                "speaker": "alia",
                "text": "*шёпот* Капитан, она говорит правду. Пиратский кодекс. Но это не значит, что она не найдёт другой способ причинить нам вред потом.",
                "emotion": "warning"
            }
        ],
        "choices": [
            {
                "text": "Хорошо. Я отдам груз. Но сначала покажите мне, что внутри",
                "effects": {"caution": 10, "selena": -5},
                "next": "ch1_demand_see_cargo"
            },
            {
                "text": "Сделка. Отведите свои корабли, и я передам груз",
                "effects": {"pragmatism": 10, "path": "observer"},
                "next": "ch1_accept_deal"
            },
            {
                "text": "Ваше слово ничего не значит для меня. Мы будем сражаться",
                "effects": {"defiance": 15, "path": "independence"},
                "next": "ch1_refuse_demand"
            }
        ]
    },

    "ch1_bluff_destroyed": {
        "id": "ch1_bluff_destroyed",
        "dialogues": [
            {
                "speaker": "selena_ro",
                "text": "*пауза* Интересно. *склоняет голову* Вы либо очень смелы, либо очень глупы. Уничтожить такой груз... это стоит больше, чем ваш корабль.",
                "emotion": "intrigued"
            },
            {
                "speaker": "selena_ro",
                "text": "Но я не верю вам. Сканеры показивают, что контейнер цел. У вас есть последний шанс сказать правду.",
                "emotion": "cold"
            }
        ],
        "choices": [
            {
                "text": "Ладно, блеф не удался. Давайте обсудим условия",
                "effects": {"honesty": 5, "negotiation": 5},
                "next": "ch1_negotiate_terms"
            },
            {
                "text": "Сканируйте сколько угодно. Груз — мой. И он останется на моём корабле",
                "effects": {"defiance": 20, "path": "independence"},
                "next": "ch1_refuse_demand"
            },
            {
                "text": "[Атака] Афина, отключи связь! Все к боевым постам!",
                "effects": {"surprise": 15, "path": "alliance"},
                "next": "ch1_surprise_attack"
            }
        ]
    },

    # === БОЕВЫЕ ПОСЛЕДОВАТЕЛЬНОСТИ ===

    "ch1_prepare_battle": {
        "id": "ch1_prepare_battle",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Команда работает слаженно. Рина у пульта энергосистем, Алия готовит биотическое поле, Надежда занимает место пилота."
            },
            {
                "speaker": "athena",
                "text": "Пираты обнаружили наши приготовления. Они ускоряются. До контакта — 8 минут.",
                "emotion": "urgent"
            },
            {
                "speaker": "rina",
                "text": "Щиты на 75%! Ещё 5 минут — и будет 100%!",
                "emotion": "excited"
            }
        ],
        "choices": [
            {
                "text": "Держать позицию. Дадим им бой",
                "effects": {"courage": 15, "path": "alliance"},
                "next": "ch1_stand_and_fight"
            },
            {
                "text": "Как только щиты готовы — уходим на прыжок",
                "effects": {"pragmatism": 10, "path": "independence"},
                "next": "ch1_prepare_jump"
            }
        ]
    },

    "ch1_surprise_attack": {
        "id": "ch1_surprise_attack",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Связь обрывается. Селена Ро не успевает отреагировать."
            },
            {
                "speaker": "rina",
                "text": "Что делаем?! Нападаем первыми?!",
                "emotion": "shocked"
            },
            {
                "speaker": "nadezhda",
                "text": "Умный ход. Они не ожидают атаки от торгового судна. У нас есть 30 секунд преимущества.",
                "emotion": "impressed"
            },
            {
                "speaker": "alia",
                "text": "Я готова. Укажите цель.",
                "emotion": "focused"
            }
        ],
        "choices": [
            {
                "text": "Надеюсь на флагман! Раненый зверь опаснее всего",
                "effects": {"tactical": 20, "aggression": 10},
                "next": "ch1_attack_flagship"
            },
            {
                "text": "Перехватчики первыми! Уберём быстрые цели",
                "effects": {"tactical": 15, "caution": 5},
                "next": "ch1_attack_interceptors"
            },
            {
                "text": "Отступаем под прикрытием атаки! Сбить их с толку",
                "effects": {"deception": 15, "path": "independence"},
                "next": "ch1_feint_retreat"
            }
        ]
    },

    # === ФИНАЛ ГЛАВЫ 1 ===

    "ch1_escape_sequence": {
        "id": "ch1_escape_sequence",
        "type": "action",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "«Элея» рвётся вперёд. Астероидное поле надвигается — хаос камня и льда."
            },
            {
                "speaker": "nadezhda",
                "text": "Держитесь! Это будет... тесно.",
                "emotion": "focused"
            },
            {
                "speaker": "narrator",
                "text": "Корабль ныряет между глыбами. Сзади — взрывы. Перехватчики не успевают."
            },
            {
                "speaker": "ria",
                "text": "Попадание в корму! Щит держит... нет, падает! 20%!",
                "emotion": "panicked"
            },
            {
                "speaker": "alia",
                "text": "Биотическое поле активировано! У нас есть 30 секунд!",
                "emotion": "strained"
            }
        ],
        "choices": [
            {
                "text": "Надежда, давай! Выводи нас отсюда!",
                "effects": {"nadezhda": 10, "morale": 10},
                "next": "ch1_escape_success"
            }
        ]
    },

    "ch1_escape_success": {
        "id": "ch1_escape_success",
        "type": "ending",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Астероиды позади. Пираты отстали. «Элея» свободна."
            },
            {
                "speaker": "nadezhda",
                "text": "*выдыхает* Это было... близко. Но мы справились.",
                "emotion": "relieved"
            },
            {
                "speaker": "ria",
                "text": "Щиты на минимуме, но держим. Двигатели целы. Мы живы, капитан!",
                "emotion": "happy"
            },
            {
                "speaker": "alia",
                "text": "*слабеющим голосом* Я... мне нужен отдых. Биотическое поле истощило... упаду...",
                "emotion": "exhausted"
            },
            {
                "speaker": "athena",
                "text": "Капитан, мы вышли из зоны поражения. Но у нас новая проблема — тот контейнер в трюме 3. Он... излучает энергию. И она усиливается.",
                "emotion": "concerned"
            }
        ],
        "choices": [
            {
                "text": "Осмотреть контейнер. Нужно понять, что мы везём",
                "effects": {"curiosity": 10},
                "next": "ch2_start"
            },
            {
                "text": "Сначала позаботиться об Алии. Она спасла нас",
                "effects": {"empathy": 15, "alia": 20},
                "next": "ch2_care_alia"
            },
            {
                "text": "Афина, просканируй контейнер на расстоянии. Безопасность прежде всего",
                "effects": {"caution": 15},
                "next": "ch2_scan_container"
            }
        ],
        "flags": {"chapter_1_complete": True, "pirate_encounter": True, "mysterious_cargo": True}
    },

    "ch1_stand_and_fight": {
        "id": "ch1_stand_and_fight",
        "type": "action",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "«Элея» разворачивается к врагу. Пиратские корабли не ожидают сопротивления."
            },
            {
                "speaker": "ria",
                "text": "Щиты на 100%! Мы готовы!",
                "emotion": "excited"
            },
            {
                "speaker": "nadezhda",
                "text": "Орудия заряжены. Цель — флагман. Жду приказа.",
                "emotion": "cold"
            }
        ],
        "choices": [
            {
                "text": "ОГОНЬ!",
                "effects": {"aggression": 20, "path": "alliance"},
                "next": "ch1_battle_victory"
            }
        ]
    },

    "ch1_battle_victory": {
        "id": "ch1_battle_victory",
        "type": "ending",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Залп «Элеи» точен. Флагман пиратов теряет щиты, затем двигатель. Перехватчики отступают."
            },
            {
                "speaker": "selena_ro",
                "text": "*по связи* Неплохо, Велл. Неплохо. Запомню это. Мы ещё встретимся.",
                "emotion": "angry"
            },
            {
                "speaker": "ria",
                "text": "Мы победили! Мы реально победили пиратскую эскадру!",
                "emotion": "ecstatic"
            },
            {
                "speaker": "athena",
                "text": "Капитан, повреждения минимальны. Но контейнер в трюме 3... он реагирует на бой. Энергия выросла на 300%.",
                "emotion": "worried"
            }
        ],
        "choices": [
            {
                "text": "Осмотреть контейнер немедленно",
                "effects": {"curiosity": 10},
                "next": "ch2_start"
            }
        ],
        "flags": {"chapter_1_complete": True, "pirate_encounter": True, "battle_victory": True, "selena_enemy": True}
    }
}

# ============================================================================
# ГЛАВА 2: ПЕРВЫЙ КОНТРАКТ
# ============================================================================

CHAPTER_2_DIALOGUES = {
    "ch2_start": {
        "id": "ch2_start",
        "scene": {
            "location": "cargo_bay_3",
            "description": "Трюм 3 тёмный, освещённый только аварийными огнями. В центре — контейнер неизвестного происхождения."
        },
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Контейнер выглядит древним — металл покрыт странными символами, которые слабо светятся изнутри."
            },
            {
                "speaker": "ria",
                "text": "Я никогда не видела такую технологию. Это... не современное. И даже не протеанское.",
                "emotion": "fascinated"
            },
            {
                "speaker": "alia",
                "text": "*слабым голосом* Древнее. Очень древнее. Я чувствую... эхо. Голоса. Они шепчут...",
                "emotion": "trance"
            }
        ],
        "choices": [
            {
                "text": "Открыть контейнер",
                "effects": {"curiosity": 15, "risk": 10},
                "next": "ch2_open_container"
            },
            {
                "text": "Не трогать. Сначала изучить",
                "effects": {"caution": 15},
                "next": "ch2_study_container"
            },
            {
                "text": "Связаться с заказчиком. Это его груз",
                "effects": {"professionalism": 10},
                "next": "ch2_contact_client"
            },
            {
                "text": "Алия, что ты чувствуешь? Расскажи подробнее",
                "effects": {"empathy": 10, "alia": 10},
                "next": "ch2_alia_vision"
            }
        ]
    },

    "ch2_open_container": {
        "id": "ch2_open_container",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Крышка контейнера поднимается. Внутри — артефакт. Кристаллическая структура, пульсирующая голубым светом."
            },
            {
                "speaker": "narrator",
                "text": "Внезапно свет ослепляет вас. Вспышка пронзает разум — образы, голоса, видения..."
            },
            {
                "speaker": "???",
                "text": "*[В разуме]* Носитель найден. Протокол инициации активирован. Добро пожаловать, Избранный.",
                "emotion": "ancient"
            },
            {
                "speaker": "narrator",
                "text": "Вы падаете на колени. Видения затапливают сознание — чужие миры, древние существа, битвы в космосе..."
            },
            {
                "speaker": "ria",
                "text": "КАПИТАН! *подбегает* Что произошло?! Вы в порядке?!",
                "emotion": "panicked"
            }
        ],
        "choices": [
            {
                "text": "Я... я видел что-то. Что-то древнее",
                "effects": {"mystery": 10},
                "next": "ch2_artifact_bond"
            },
            {
                "text": "Не знаю. Голова раскалывается...",
                "effects": {"honesty": 5},
                "next": "ch2_aftermath"
            },
            {
                "text": "Этот артефакт... он говорил со мной",
                "effects": {"revelation": 15, "alia": 10},
                "next": "ch2_artifact_communication"
            }
        ]
    },

    "ch2_artifact_bond": {
        "id": "ch2_artifact_bond",
        "dialogues": [
            {
                "speaker": "alia",
                "text": "*подходит, всё ещё слабая* Артефакт выбрал тебя. Это... Ключ. Один из семи. Древняя технология Хранителей.",
                "emotion": "awed"
            },
            {
                "speaker": "ria",
                "text": "Хранители? Те, кто исчез тысячи лет назад? Это их технология?",
                "emotion": "shocked"
            },
            {
                "speaker": "alia",
                "text": "Да. И теперь капитан связан с ним. *смотрит на вас* Ты чувствуешь его? Его мысли?",
                "emotion": "curious"
            }
        ],
        "choices": [
            {
                "text": "Да. Он... он показывает мне карты. Расположение чего-то",
                "effects": {"bond_strength": 20, "knowledge": 10},
                "next": "ch2_map_revelation"
            },
            {
                "text": "Только голоса. Но они неразборчивы",
                "effects": {"bond_strength": 10},
                "next": "ch2_voices_only"
            },
            {
                "text": "Ничего не чувствую. Может, это была просто вспышка?",
                "effects": {"denial": 10, "bond_strength": 5},
                "next": "ch2_denial"
            }
        ]
    },

    "ch2_map_revelation": {
        "id": "ch2_map_revelation",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "В вашем сознании возникает галактическая карта. Семь точек — одна пульсирует ярче других. Это вы."
            },
            {
                "speaker": "athena",
                "text": "Капитан, я засекла нейронную активность в вашем мозгу. Паттерны... нечеловеческие. Вы получаете данные?",
                "emotion": "fascinated"
            },
            {
                "speaker": "player",
                "text": "Да. Семь точек. Одна — мы. Остальные... *пауза* Где-то в галактике."
            },
            {
                "speaker": "alia",
                "text": "Семь Ключей. Семь осколков силы Хранителей. И один теперь — ваш. *серьёзно* Капитан, это меняет всё.",
                "emotion": "grave"
            }
        ],
        "choices": [
            {
                "text": "Мы должны найти остальные Ключи",
                "effects": {"quest_accept": True, "path": "alliance"},
                "next": "ch2_quest_begin"
            },
            {
                "text": "Сначала нужно понять, что это значит. Изучить",
                "effects": {"research_focus": True, "path": "observer"},
                "next": "ch2_research_phase"
            },
            {
                "text": "Это слишком опасно. Нужно избавиться от артефакта",
                "effects": {"rejection": True, "path": "independence"},
                "next": "ch2_reject_artifact"
            }
        ]
    },

    "ch2_quest_begin": {
        "id": "ch2_quest_begin",
        "dialogues": [
            {
                "speaker": "ria",
                "text": "Путешествие по галактике в поисках древних артефактов? Звучит как приключение! Я в!",
                "emotion": "excited"
            },
            {
                "speaker": "nadezhda",
                "text": "Это привлечёт внимание. Селена Ро уже знает о Ключе. Будут другие. Мы готовы к этому?",
                "emotion": "serious"
            },
            {
                "speaker": "alia",
                "text": "Мы должны быть готовы. Но я поддерживаю капитана. Ключи не должны попасть в чужие руки.",
                "emotion": "supportive"
            },
            {
                "speaker": "athena",
                "text": "Капитан, ближайший сигнал Ключа — в системе Орион. Два дня пути. Координаты загружены.",
                "emotion": "efficient"
            }
        ],
        "choices": [
            {
                "text": "Курс на Орион. Начинаем поиск",
                "effects": {"quest_active": True, "morale": 10},
                "next": "ch2_departure"
            },
            {
                "text": "Сначала нужно подготовиться. Запасы, информация, контакты",
                "effects": {"preparation": True, "pragmatism": 10},
                "next": "ch2_preparation"
            }
        ],
        "flags": {"chapter_2_complete": True, "artifact_bonded": True, "quest_keys": True}
    },

    "ch2_care_alia": {
        "id": "ch2_care_alia",
        "scene": {
            "location": "medbay",
            "description": "Медицинский отсек «Элеи». Алия лежит на койке, бледная, но спокойная."
        },
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Вы склоняетесь над Алиёй. Её дыхание ровное, но слабое."
            },
            {
                "speaker": "alia",
                "text": "*открывает глаза* Капитан... ты пришёл(ла). *слабая улыбка* Я думала, ты сразу к контейнеру.",
                "emotion": "touched"
            },
            {
                "speaker": "player",
                "text": "Ты спасла нас. Это важнее любого контейнера."
            },
            {
                "speaker": "alia",
                "text": "*смотрит в глаза* Ты... не помнишь, но мы были близки. До криосна. Не физически — ментально. Азари связываются разумами. Ты позволил мне увидеть тебя настоящего.",
                "emotion": "vulnerable"
            }
        ],
        "choices": [
            {
                "text": "Расскажи. Кто я? Кто мы были друг для друга?",
                "effects": {"alia": 20, "knowledge": 10},
                "next": "ch2_alia_revelation"
            },
            {
                "text": "Неважно прошлое. Важно, что ты в безопасности",
                "effects": {"alia": 15, "empathy": 10},
                "next": "ch2_alia_gratitude"
            },
            {
                "text": "Отдыхай. Нам понадобится твоя сила",
                "effects": {"alia": 10, "professionalism": 5},
                "next": "ch2_alia_rest"
            }
        ]
    },

    "ch2_alia_revelation": {
        "id": "ch2_alia_revelation",
        "dialogues": [
            {
                "speaker": "alia",
                "text": "Ты — человек, который ищет искупления. За что — не знаю, ты не делился. Но я чувствовала боль. И loneliness. Одиночество, которое тянулось годами.",
                "emotion": "gentle"
            },
            {
                "speaker": "alia",
                "text": "Мы... сблизились. Не как любовники — хотя я хотела. Ты держал дистанцию. Но как души. Я видела тебя. Ты видел меня. Это интимнее любого касания.",
                "emotion": "tender"
            },
            {
                "speaker": "alia",
                "text": "А потом — криосон. И ты забыл. *грустная улыбка* Может, это к лучшему. Новое начало.",
                "emotion": "bittersweet"
            }
        ],
        "choices": [
            {
                "text": "Я хочу вспомнить. Помоги мне",
                "effects": {"alia": 25, "bond": 20},
                "next": "ch2_alia_memory_ritual"
            },
            {
                "text": "Может, ты права. Новое начало — это шанс",
                "effects": {"alia": 15, "philosophy": 10},
                "next": "ch2_new_beginning"
            },
            {
                "text": "Спасибо за откровенность. Но сейчас — к делу",
                "effects": {"professionalism": 10},
                "next": "ch2_start"
            }
        ]
    },

    "ch2_alia_memory_ritual": {
        "id": "ch2_alia_memory_ritual",
        "dialogues": [
            {
                "speaker": "alia",
                "text": "Я могу провести ритуал. Азарский обряд обмена памятью. Но это... интимно. Ты увидишь мои воспоминания тоже. Всё.",
                "emotion": "serious"
            },
            {
                "speaker": "narrator",
                "text": "Её глаза серьёзны. Это не просто предложение — это доверие."
            }
        ],
        "choices": [
            {
                "text": "Я доверяю тебе. Проводи ритуал",
                "effects": {"alia": 30, "trust": 20, "memory_restored": True},
                "next": "ch2_memory_ritual_scene"
            },
            {
                "text": "Это слишком личное. Не сейчас",
                "effects": {"caution": 10, "alia": -5},
                "next": "ch2_start"
            }
        ]
    },

    "ch2_memory_ritual_scene": {
        "id": "ch2_memory_ritual_scene",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Алия берёт ваши руки в свои. Её биотическое поле окружает вас обоих..."
            },
            {
                "speaker": "narrator",
                "text": "*Вспышка* Образы хлещут потоком — вы видите себя через её глаза. Первая встреча. Долгие разговоры. Битвы рядом. И... что-то ещё. Чувство. Любовь, которую она скрывала."
            },
            {
                "speaker": "alia",
                "text": "*В разуме* Теперь ты знаешь. Всё. Я люблю тебя, Макс. Люблю уже давно. Если это слишком... прости.",
                "emotion": "vulnerable"
            }
        ],
        "choices": [
            {
                "text": "Я тоже... чувствую это. Теперь, когда вспомнил",
                "effects": {"alia": 40, "romance": True, "alia_romance": True},
                "next": "ch2_romance_alia"
            },
            {
                "text": "Спасибо за честность. Дай мне время разобраться в себе",
                "effects": {"alia": 10, "honesty": 10},
                "next": "ch2_need_time"
            },
            {
                "text": "Твоя дружба бесценна. Но я не могу ответить тем же",
                "effects": {"alia": -15, "friendzone": True},
                "next": "ch2_friendzone_alia"
            }
        ],
        "flags": {"memory_restored": True, "alia_confession": True}
    },

    "ch2_romance_alia": {
        "id": "ch2_romance_alia",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Биотическое поле пульсирует, отражая ваши чувства. Алия улыбается — впервые по-настоящему."
            },
            {
                "speaker": "alia",
                "text": "Я ждала этого. Тысячу лет жизни — и ты — единственный, кого я хотела дождаться.",
                "emotion": "loving"
            },
            {
                "speaker": "narrator",
                "text": "Она притягивает вас ближе. Поцелуй — мягкий, нежный, вековой."
            }
        ],
        "choices": [
            {
                "text": "Продолжить...",
                "effects": {"alia": 30, "romance_progress": True},
                "next": "ch2_after_romance"
            }
        ],
        "flags": {"alia_romantic_partner": True}
    }
}

# ============================================================================
# ГЛАВА 3: СТОЛКНОВЕНИЕ
# ============================================================================

CHAPTER_3_DIALOGUES = {
    "ch3_start": {
        "id": "ch3_start",
        "scene": {
            "location": "space_station_nexus",
            "description": "Космическая станция «Нексус» — торговый хаб на границе освоенного космоса."
        },
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "«Элея» пристыковалась к станции. Здесь можно пополнить запасы, найти информацию о Ключах, и, возможно, новых членов экипажа."
            },
            {
                "speaker": "athena",
                "text": "Капитан, станция предлагает несколько возможностей: рынок для торговли, бар для информации, и верфь для ремонта.",
                "emotion": "informative"
            }
        ],
        "choices": [
            {
                "text": "Идти на рынок — нужен груз и припасы",
                "effects": {"focus": "trade"},
                "next": "ch3_market"
            },
            {
                "text": "Идти в бар — поискать информацию о Ключах",
                "effects": {"focus": "intel"},
                "next": "ch3_bar"
            },
            {
                "text": "Идти на верфь — «Элея» нуждается в ремонте",
                "effects": {"focus": "repair"},
                "next": "ch3_shipyard"
            },
            {
                "text": "Взять команду и осмотреться",
                "effects": {"focus": "explore"},
                "next": "ch3_explore"
            }
        ]
    },

    "ch3_bar": {
        "id": "ch3_bar",
        "scene": {
            "location": "station_bar_shadows",
            "description": "Бар «Тени» — полутёмное заведение с тихими уголками для приватных разговоров."
        },
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Бар полон разношёрстной публики — торговцы, наёмники, контрабандисты. В углу — женщина в тёмном плаще, наблюдающая за входом."
            },
            {
                "speaker": "ria",
                "text": "*шёпот* Капитан, вон тот человек у барной стойки — он следит за нами. Вижу отражение в зеркале.",
                "emotion": "paranoid"
            }
        ],
        "choices": [
            {
                "text": "Подойти к женщине в углу",
                "effects": {"curiosity": 10},
                "next": "ch3_mysterious_woman"
            },
            {
                "text": "Встретиться взглядом со следящим",
                "effects": {"confrontation": 10},
                "next": "ch3_watcher_confront"
            },
            {
                "text": "Игнорировать. Заказать выпивку и послушать разговоры",
                "effects": {"subtlety": 10},
                "next": "ch3_eavesdrop"
            },
            {
                "text": "Выйти — здесь слишком опасно",
                "effects": {"caution": 10},
                "next": "ch3_exit_bar"
            }
        ]
    },

    "ch3_mysterious_woman": {
        "id": "ch3_mysterious_woman",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Женщина замечает ваше приближение. Её лицо скрыто тенью капюшона."
            },
            {
                "speaker": "stranger",
                "text": "Капитан Велл. Я ждала вас. Меня зовут... можно называть Эйзен. У меня есть информация о Ключах.",
                "emotion": "mysterious"
            },
            {
                "speaker": "narrator",
                "text": "Она делает жест — садитесь напротив."
            },
            {
                "speaker": "eisen",
                "text": "Вы держите один Ключ. Селена Ро охотится за другим. И есть третья сторона — организация, о которой мало кто знает. Они называются «Наследие».",
                "emotion": "serious"
            }
        ],
        "choices": [
            {
                "text": "Откуда ты знаешь о Ключе?",
                "effects": {"suspicion": 10},
                "next": "ch3_eisen_source"
            },
            {
                "text": "Что такое «Наследие»?",
                "effects": {"knowledge": 10},
                "next": "ch3_legacy_info"
            },
            {
                "text": "Чего ты хочешь от нас?",
                "effects": {"pragmatism": 10},
                "next": "ch3_eisen_price"
            },
            {
                "text": "Я не доверяю незнакомцам. Докажи, что ты не враг",
                "effects": {"caution": 10},
                "next": "ch3_eisen_proof"
            }
        ]
    },

    "ch3_eisen_price": {
        "id": "ch3_eisen_price",
        "dialogues": [
            {
                "speaker": "eisen",
                "text": "*слабая улыбка* Прямо к делу. Хорошо. Я хочу... присоединиться к вашему экипажу.",
                "emotion": "honest"
            },
            {
                "speaker": "eisen",
                "text": "У меня есть навыки — информация, связи, умение быть невидимой. В обмен — защита и место, где можно... остановиться.",
                "emotion": "vulnerable"
            },
            {
                "speaker": "nadezhda",
                "text": "*шёпот* Капитан, проверить её? Выглядит полезной, но...",
                "emotion": "suspicious"
            }
        ],
        "choices": [
            {
                "text": "Добро пожаловать на борт, Эйзен",
                "effects": {"eisen": 20, "crew_add": "eisen"},
                "next": "ch3_recruit_eisen"
            },
            {
                "text": "Сначала испытательный срок. Докажи себя",
                "effects": {"eisen": 5, "caution": 10},
                "next": "ch3_eisen_probation"
            },
            {
                "text": "Мне нужно больше информации, прежде чем я решу",
                "effects": {"eisen": 0, "knowledge": 5},
                "next": "ch3_eisen_more_info"
            },
            {
                "text": "Извини, мы не берём незнакомцев",
                "effects": {"eisen": -20},
                "next": "ch3_reject_eisen"
            }
        ]
    },

    "ch3_recruit_eisen": {
        "id": "ch3_recruit_eisen",
        "dialogues": [
            {
                "speaker": "eisen",
                "text": "*снимает капюшон* Спасибо. Я... не ожидала такого доверия. *редкая улыбка* Не разочарую.",
                "emotion": "grateful"
            },
            {
                "speaker": "narrator",
                "text": "Под капюшоном — молодая женщина с внимательными глазами, полными секретов."
            },
            {
                "speaker": "eisen",
                "text": "Первая информация бесплатно: Селена Ро направляется к системе Орион. Она знает о втором Ключе. И у неё есть что-то, что поможет его взять — код доступа Хранителей.",
                "emotion": "professional"
            }
        ],
        "choices": [
            {
                "text": "Нам нужно опередить её. Курс на Орион!",
                "effects": {"focus": "race"},
                "next": "ch3_race_to_orion"
            },
            {
                "text": "Как она получила код Хранителей?",
                "effects": {"knowledge": 10},
                "next": "ch3_keeper_code"
            }
        ],
        "flags": {"eisen_recruited": True}
    },

    "ch3_race_to_orion": {
        "id": "ch3_race_to_orion",
        "dialogues": [
            {
                "speaker": "nadezhda",
                "text": "Система Орион — два дня пути на максимальной тяге. Если Селена уже вышла...",
                "emotion": "calculating"
            },
            {
                "speaker": "ria",
                "text": "Двигатели готовы! Я выжму из «Элеи» всё, что можно!",
                "emotion": "determined"
            },
            {
                "speaker": "athena",
                "text": "Капитан, в системе Орион расположен древний храм Хранителей. Археологи Альянса исследуют его уже 50 лет. Они не знают о Ключе.",
                "emotion": "informative"
            }
        ],
        "choices": [
            {
                "text": "Свяжемся с археологами. Может, они помогут",
                "effects": {"path": "alliance", "diplomacy": 10},
                "next": "ch4_temple_approach"
            },
            {
                "text": "Проникнем тайно. Никто не должен знать о нашей цели",
                "effects": {"path": "independence", "stealth": 10},
                "next": "ch4_infiltration"
            },
            {
                "text": "Наблюдаем. Узнаем, что там происходит, потом решим",
                "effects": {"path": "observer", "tactical": 10},
                "next": "ch4_observation"
            }
        ],
        "flags": {"chapter_3_complete": True, "race_begun": True}
    }
}

# ============================================================================
# ГЛАВА 4: ТАЙНЫ КОРАБЛЯ
# ============================================================================

CHAPTER_4_DIALOGUES = {
    "ch4_temple_approach": {
        "id": "ch4_temple_approach",
        "scene": {
            "location": "orion_system",
            "description": "Система Орион. Планета с древним храмом Хранителей на поверхности."
        },
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "«Элея» выходит из гиперпрыжка. Впереди — планета, покрытая джунглями. В центре — пирамидальная структура, видимая даже из космоса."
            },
            {
                "speaker": "athena",
                "text": "Обнаружены два корабля на орбите. Научное судно Альянса «Искатель» и... пиратский корвет. Селена Ро уже здесь.",
                "emotion": "concerned"
            }
        ],
        "choices": [
            {
                "text": "Связаться с «Искателем». Предложить помощь",
                "effects": {"path": "alliance", "diplomacy": 10},
                "next": "ch4_alliance_contact"
            },
            {
                "text": "Скрытно спуститься на планету с другой стороны",
                "effects": {"path": "independence", "stealth": 10},
                "next": "ch4_stealth_landing"
            },
            {
                "text": "Наблюдать за ситуацией из укрытия",
                "effects": {"path": "observer", "tactical": 10},
                "next": "ch4_observe_first"
            }
        ]
    },

    "ch4_alliance_contact": {
        "id": "ch4_alliance_contact",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "На экране появляется женщина в форме Альянса — капитан Елена Соколова."
            },
            {
                "speaker": "elena_sokolova",
                "text": "Говорит капитан Соколова, научное судно «Искатель». Опознайте себя. Мы проводим археологическое исследование под эгидой Альянса.",
                "emotion": "professional"
            },
            {
                "speaker": "narrator",
                "text": "Её глаза задерживаются на вашем лице — она его узнала?"
            },
            {
                "speaker": "elena_sokolova",
                "text": "*тише* Макс Велл? Бывший пилот... Нет, не может быть. Капитан, нам нужно поговорить. Лично.",
                "emotion": "shocked"
            }
        ],
        "choices": [
            {
                "text": "Признать личность. Согласиться на встречу",
                "effects": {"honesty": 10, "elena": 10},
                "next": "ch4_elena_meeting"
            },
            {
                "text": "Отрицать. «Вы меня с кем-то путаете»",
                "effects": {"deception": 10, "elena": -10},
                "next": "ch4_deny_identity"
            },
            {
                "text": "Спросить, откуда она знает",
                "effects": {"knowledge": 10},
                "next": "ch4_how_she_knows"
            }
        ]
    },

    "ch4_elena_meeting": {
        "id": "ch4_elena_meeting",
        "scene": {
            "location": "research_ship_seeker",
            "description": "Каюта капитана на «Искателе»"
        },
        "dialogues": [
            {
                "speaker": "elena_sokolova",
                "text": "*закрывает дверь* Ты не представляешь, как давно я искала тебя. После того, что случилось на станции «Аврора»...",
                "emotion": "emotional"
            },
            {
                "speaker": "narrator",
                "text": "Она достаёт старую фотографию — вы вдвоём, в форме Альянса, моложе. Улыбаетесь."
            },
            {
                "speaker": "elena_sokolova",
                "text": "Мы были партнёрами. Лучшими друзьями. А потом... ты исчез. После взрыва. Все думали, что ты погиб. Я... я траура не переставала искать.",
                "emotion": "vulnerable"
            }
        ],
        "choices": [
            {
                "text": "Я не помню этого. Потерял память в криосне",
                "effects": {"honesty": 15, "elena": 5},
                "next": "ch4_memory_loss_reveal"
            },
            {
                "text": "Почему ты искала меня все эти годы?",
                "effects": {"curiosity": 10, "elena": 10},
                "next": "ch4_why_searched"
            },
            {
                "text": "Это в прошлом. Сейчас важно — храм Хранителей",
                "effects": {"professionalism": 10, "elena": -5},
                "next": "ch4_focus_temple"
            }
        ]
    },

    "ch4_memory_loss_reveal": {
        "id": "ch4_memory_loss_reveal",
        "dialogues": [
            {
                "speaker": "elena_sokolova",
                "text": "*пауза* Память... Потеря памяти? О, Макс... *подходит ближе* Я могу помочь. У меня есть доступ к технологиям восстановления памяти. Но это потребует времени.",
                "emotion": "hopeful"
            },
            {
                "speaker": "narrator",
                "text": "Её глаза полны эмоций — надежды, заботы, чего-то ещё."
            },
            {
                "speaker": "elena_sokolova",
                "text": "Но сначала... *смотрит на дверь* Храм. Там что-то пробудилось. На прошлой неделе наши датчики зафиксировали активность. Потом появились пираты.",
                "emotion": "serious"
            }
        ],
        "choices": [
            {
                "text": "Расскажи о храме. Что вы обнаружили?",
                "effects": {"knowledge": 10},
                "next": "ch4_temple_info"
            },
            {
                "text": "Я хочу, чтобы ты помогла мне вспомнить. После миссии",
                "effects": {"elena": 20, "memory_quest": True},
                "next": "ch4_memory_promise"
            },
            {
                "text": "Что пираты делают здесь? Они знают о Ключе?",
                "effects": {"tactical": 10},
                "next": "ch4_pirates_intel"
            }
        ]
    },

    "ch4_temple_info": {
        "id": "ch4_temple_info",
        "dialogues": [
            {
                "speaker": "elena_sokolova",
                "text": "Храм — это не просто здание. Это... устройство. Мы не понимаем его назначение, но структура напоминает... замок. Который ждёт ключ.",
                "emotion": "fascinated"
            },
            {
                "speaker": "elena_sokolova",
                "text": "На прошлой неделе внутренняя камера начала излучать энергию. Как будто что-то проснулось. И почти сразу появились пираты. Слишком быстро для совпадения.",
                "emotion": "suspicious"
            },
            {
                "speaker": "eisen",
                "text": "*по коммуникатору* Капитан, я засекла утечку информации. Кто-то на «Искателе» передаёт данные пиратам. У вас есть предатель.",
                "emotion": "urgent"
            }
        ],
        "choices": [
            {
                "text": "Рассказать Елене о предателе",
                "effects": {"honesty": 10, "elena": 5, "trust": 10},
                "next": "ch4_reveal_traitor"
            },
            {
                "text": "Расследовать самостоятельно, не предупреждая",
                "effects": {"stealth": 10, "elena": -5},
                "next": "ch4_investigate_traitor"
            },
            {
                "text": "Игнорировать — сейчас важнее храм",
                "effects": {"focus": 10},
                "next": "ch4_ignore_traitor"
            }
        ]
    },

    "ch4_reveal_traitor": {
        "id": "ch4_reveal_traitor",
        "dialogues": [
            {
                "speaker": "player",
                "text": "Елена, у тебя утечка. Мой офицер засекла передачу данных пиратам с этого корабля."
            },
            {
                "speaker": "elena_sokolova",
                "text": "*бледнеет* Что? Невозможно... Мой экипаж проверен... *пауза* Хотя... доктор Марков. Он был против экспедиции. И у него доступ к коммуникациям.",
                "emotion": "shocked"
            },
            {
                "speaker": "narrator",
                "text": "Тревога! В храме зафиксирован взрыв! Пираты начали штурм!"
            },
            {
                "speaker": "elena_sokolova",
                "text": "Чёрт! Они нас опередили! Макс, нам нужно спускаться. Вместе. Храм... он реагирует на Ключ. Только ты можешь его открыть.",
                "emotion": "urgent"
            }
        ],
        "choices": [
            {
                "text": "Идём вместе. Покажи мне храм",
                "effects": {"elena": 15, "alliance": 10},
                "next": "ch5_temple_entrance"
            },
            {
                "text": "Я пойду один. Твой экипаж скомпрометирован",
                "effects": {"caution": 10, "elena": -10},
                "next": "ch5_solo_entry"
            }
        ],
        "flags": {"chapter_4_complete": True, "traitor_revealed": True, "elena_alliance": True}
    }
}

# ============================================================================
# ГЛАВА 5: ВЫБОР ПУТИ
# ============================================================================

CHAPTER_5_DIALOGUES = {
    "ch5_temple_entrance": {
        "id": "ch5_temple_entrance",
        "scene": {
            "location": "keeper_temple_interior",
            "description": "Внутри храма Хранителей — древние стены покрывают светящиеся символы."
        },
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Храм пробуждается при вашем приближении. Символы светятся ярче, пологие коридоры ведут вглубь."
            },
            {
                "speaker": "alia",
                "text": "*по коммуникатору* Капитан, я чувствую... это место было построено для кого-то вроде вас. Носителей Ключей. Оно... приветствует вас.",
                "emotion": "awed"
            },
            {
                "speaker": "elena_sokolova",
                "text": "Невероятно. Мы пытались пройти дальше этой точки годами. Стены не открывались. А сейчас... *смотрит на вас* Ты — ключ буквально.",
                "emotion": "amazed"
            }
        ],
        "choices": [
            {
                "text": "Идём дальше. К центральной камере",
                "effects": {"progress": 10},
                "next": "ch5_inner_temple"
            },
            {
                "text": "Осторожно. Это может быть ловушка",
                "effects": {"caution": 10},
                "next": "ch5_trap_check"
            },
            {
                "text": "Елена, что вы знаете о центральной камере?",
                "effects": {"knowledge": 10},
                "next": "ch5_central_chamber_info"
            }
        ]
    },

    "ch5_inner_temple": {
        "id": "ch5_inner_temple",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Центральная камера открывается. В центре — пьедестал с углублением, идеально подходящим для Ключа. Вокруг — голограммы семи точек в галактике."
            },
            {
                "speaker": "narrator",
                "text": "Сзади раздаётся голос:"
            },
            {
                "speaker": "selena_ro",
                "text": "Impressive, Captain. You made it. Now, step away from the pedestal.",
                "emotion": "threatening"
            },
            {
                "speaker": "narrator",
                "text": "Селена Ро входит в камеру, сопровождаемая вооружёнными пиратами. Елена замерла — её оружие нацелено, но пиратов больше."
            }
        ],
        "choices": [
            {
                "text": "Чего ты хочешь, Селена?",
                "effects": {"negotiation": 10},
                "next": "ch5_selena_demand"
            },
            {
                "text": "Напасть! Шанс застать врасплох!",
                "effects": {"combat": 15},
                "next": "ch5_sudden_attack"
            },
            {
                "text": "Положить Ключ в пьедестал. Пусть сработает",
                "effects": {"risk": 20, "artifact_bond": 10},
                "next": "ch5_activate_key"
            },
            {
                "text": "Блеф: «Артефакт уже активирован. Мы все в опасности!»",
                "effects": {"deception": 15},
                "next": "ch5_bluff_danger"
            }
        ]
    },

    "ch5_selena_demand": {
        "id": "ch5_selena_demand",
        "dialogues": [
            {
                "speaker": "selena_ro",
                "text": "Просто. Ключ в пьедестал. Я получаю координаты остальных. Ты получаешь... жизнь. Честный обмен.",
                "emotion": "confident"
            },
            {
                "speaker": "selena_ro",
                "text": "Семь Ключей откроют путь к наследию Хранителей. Технологии, опережающие нашу на миллионы лет. Представь, что можно с ними сделать.",
                "emotion": "ambitious"
            },
            {
                "speaker": "elena_sokolova",
                "text": "*шёпот* Не делай этого, Макс. Хранители исчезли не просто так. То, что они оставили... это может быть опасно.",
                "emotion": "worried"
            }
        ],
        "choices": [
            {
                "text": "А если я откажусь?",
                "effects": {"defiance": 10},
                "next": "ch5_refuse_selena"
            },
            {
                "text": "Кто твой клиент? Для кого ты это делаешь?",
                "effects": {"knowledge": 10},
                "next": "ch5_client_reveal"
            },
            {
                "text": "Хорошо. Я согласен [Блеф]",
                "effects": {"deception": 15},
                "next": "ch5_feint_cooperation"
            }
        ]
    },

    "ch5_activate_key": {
        "id": "ch5_activate_key",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Вы помещаете Ключ в углубление. Мир взрывается светом!"
            },
            {
                "speaker": "narrator",
                "text": "Голограммы семи точек выстраиваются в линию. Голос — древний, непостижимый — наполняет камеру:"
            },
            {
                "speaker": "keeper_voice",
                "text": "*[Древний голос]* Носитель признан. Карта семи врат активирована. Предупреждение: пробуждение всех врат вызовет Слияние. Выбор за носителем.",
                "emotion": "ancient"
            },
            {
                "speaker": "narrator",
                "text": "Селена и её люди отброшены световой волной. Елена стоит рядом с вами, ослеплённая."
            },
            {
                "speaker": "selena_ro",
                "text": "*с трудом поднимается* Что... что это было?! Карта! Я видела координаты! *ярость* Ты заплатишь за это, Велл!",
                "emotion": "furious"
            }
        ],
        "choices": [
            {
                "text": "Елена, уходим! Пока она не пришла в себя!",
                "effects": {"escape": 10},
                "next": "ch5_escape_temple"
            },
            {
                "text": "Селена, остановись! Ты не понимаешь силу Ключей!",
                "effects": {"negotiation": 10},
                "next": "ch5_warn_selena"
            },
            {
                "text": "У нас карта. Курс на следующий Ключ!",
                "effects": {"progress": 15, "path": "independence"},
                "next": "ch5_next_key"
            }
        ],
        "flags": {"map_activated": True, "selena_enemy": True}
    },

    "ch5_escape_temple": {
        "id": "ch5_escape_temple",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Вы бежите через коридоры храма. Стены сдвигаются за вами — храм защищает своего носителя."
            },
            {
                "speaker": "elena_sokolova",
                "text": "Что ты сделал?! Этот голос... Хранители? Они говорят через тебя?",
                "emotion": "shocked"
            },
            {
                "speaker": "player",
                "text": "Я не знаю. Но знаю, что нам нужно найти остальные Ключи. И понять, что такое «Слияние»."
            },
            {
                "speaker": "narrator",
                "text": "Вы выбираетесь из храма. «Элея» ждёт на орбите. Елена смотрит на вас — по-новому."
            },
            {
                "speaker": "elena_sokolova",
                "text": "Я иду с тобой. Если это то, о чём я думаю... Тебе понадобится помощь Альянса. И... я хочу быть рядом. Снова.",
                "emotion": "determined"
            }
        ],
        "choices": [
            {
                "text": "Добро пожаловать в команду, Елена",
                "effects": {"elena": 20, "alliance": 15, "crew_add": "elena"},
                "next": "ch5_path_choice"
            },
            {
                "text": "Мне нужно подумать. Возвращайся на «Искатель»",
                "effects": {"elena": -10, "independence": 10},
                "next": "ch5_solo_path"
            },
            {
                "text": "Ты можешь помочь, но Альянс не должен знать о Ключах",
                "effects": {"elena": 5, "observer": 10},
                "next": "ch5_secret_path"
            }
        ]
    },

    "ch5_path_choice": {
        "id": "ch5_path_choice",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "«Элея» уходит от планеты. Позади — храм Хранителей, разбитые корабли Селены, и прошлое, которое вы начинаете вспоминать."
            },
            {
                "speaker": "athena",
                "text": "Капитан, карта Ключей загружена. Семь точек. Ближайшая — система Тау-7. Но у меня есть предупреждение.",
                "emotion": "serious"
            },
            {
                "speaker": "athena",
                "text": "Активация карты послала сигнал. Все, кто ищет Ключи, теперь знают, что один из них активен. Вы — цель.",
                "emotion": "worried"
            },
            {
                "speaker": "eisen",
                "text": "Это означает одно: гонка началась. «Наследие», Селена, и кто знает кто ещё. Мы не одни в этом поиске.",
                "emotion": "serious"
            }
        ],
        "choices": [
            {
                "text": "Мы найдём Ключи первыми. Курс на Тау-7!",
                "effects": {"path": "independence", "determination": 15},
                "next": "ch6_preview"
            },
            {
                "text": "Свяжемся с Альянсом. Нам нужны союзники",
                "effects": {"path": "alliance", "diplomacy": 15},
                "next": "ch6_alliance_route"
            },
            {
                "text": "Соберём информацию. Действуем осторожно",
                "effects": {"path": "observer", "tactical": 15},
                "next": "ch6_observer_route"
            }
        ],
        "flags": {"chapter_5_complete": True, "path_chosen": True}
    },

    "ch6_preview": {
        "id": "ch6_preview",
        "type": "preview",
        "dialogues": [
            {
                "speaker": "narrator",
                "text": "Конец первого акта. Ключи ждут. Враги пробуждаются. А вы — капитан звездолёта с древней силой внутри."
            },
            {
                "speaker": "narrator",
                "text": "Что ждёт впереди? Новые союзники? Опасные враги? Истина о Хранителях?"
            },
            {
                "speaker": "narrator",
                "text": "Продолжение следует в главах 6-10..."
            }
        ],
        "flags": {"act_1_complete": True}
    }
}

# ============================================================================
# СИСТЕМА ПОСЛЕДСТВИЙ
# ============================================================================

CHOICE_CONSEQUENCES = {
    "chapter_1": {
        "pirate_negotiation": {
            "description": "Попытались договориться с пиратами",
            "effects": {
                "selena_relationship": 5,
                "crew_trust": -5,
                "future_options": ["selena_negotiation_available"]
            }
        },
        "pirate_battle": {
            "description": "Вступили в бой с пиратами",
            "effects": {
                "selena_relationship": -20,
                "crew_trust": 10,
                "combat_reputation": 15,
                "future_options": ["selena_enemy_permanent"]
            }
        },
        "pirate_escape": {
            "description": "Сбежать через астероиды",
            "effects": {
                "selena_relationship": -10,
                "nadezhda_trust": 15,
                "future_options": ["asteroid_route_known"]
            }
        }
    },
    "chapter_2": {
        "artifact_bond": {
            "description": "Связались с артефактом",
            "effects": {
                "artifact_integration": 50,
                "mental_changes": True,
                "future_options": ["artifact_voices", "map_access"]
            }
        },
        "alia_romance": {
            "description": "Начали роман с Алиёй",
            "effects": {
                "alia_romantic_partner": True,
                "alia_abilities_boost": 20,
                "future_options": ["alia_romance_events", "azari_knowledge"]
            }
        }
    },
    "chapter_3": {
        "recruited_eisen": {
            "description": "Наняли Эйзен",
            "effects": {
                "intel_network": 30,
                "eisen_loyalty": 50,
                "future_options": ["eisen_missions", "shadow_contacts"]
            }
        }
    },
    "chapter_4": {
        "elena_alliance": {
            "description": "Союз с Еленой Соколовой",
            "effects": {
                "alliance_reputation": 20,
                "elena_romance_available": True,
                "future_options": ["alliance_missions", "memory_recovery"]
            }
        }
    },
    "chapter_5": {
        "path_independence": {
            "description": "Выбрали путь Независимости",
            "effects": {
                "path": "independence",
                "freedom_bonus": 20,
                "future_options": ["solo_missions", "no_faction_constraints"]
            }
        },
        "path_alliance": {
            "description": "Выбрали путь Альянса",
            "effects": {
                "path": "alliance",
                "alliance_support": 30,
                "future_options": ["alliance_resources", "military_backing"]
            }
        },
        "path_observer": {
            "description": "Выбрали путь Наблюдателя",
            "effects": {
                "path": "observer",
                "knowledge_bonus": 20,
                "future_options": ["neutral_ground", "all_faction_access"]
            }
        }
    }
}

# ============================================================================
# ФУНКЦИИ ДОСТУПА
# ============================================================================

def _convert_choice_to_object(choice_data: Dict[str, Any]) -> Choice:
    """Конвертировать словарь выбора в объект Choice"""
    effect_map = {
        "none": ChoiceEffect.NONE,
        "relationship_up": ChoiceEffect.RELATIONSHIP_UP,
        "relationship_down": ChoiceEffect.RELATIONSHIP_DOWN,
        "trust_up": ChoiceEffect.TRUST_UP,
        "trust_down": ChoiceEffect.TRUST_DOWN,
        "stat_change": ChoiceEffect.STAT_CHANGE,
        "story_branch": ChoiceEffect.STORY_BRANCH,
    }
    
    # Определяем эффект из данных
    effects = choice_data.get("effects", {})
    effect = ChoiceEffect.NONE
    effect_value = None
    
    # Проверяем изменения отношений
    for key, value in effects.items():
        if key == "path":
            effect = ChoiceEffect.STORY_BRANCH
            effect_value = ("path", value)
        elif key in ["athena", "alia_naar", "irina_lebedeva", "rina_mirai", "nadezhda", 
                     "ekaterina", "max_well", "selena_ro", "selena_enemy", "selena_friend"]:
            if value > 0:
                effect = ChoiceEffect.RELATIONSHIP_UP
            elif value < 0:
                effect = ChoiceEffect.RELATIONSHIP_DOWN
            effect_value = (key, value)
    
    # Генерируем уникальный ID
    choice_id = choice_data.get("id", choice_data.get("text", "choice")[:20].replace(" ", "_"))
    
    return Choice(
        id=choice_id,
        text=choice_data.get("text", ""),
        next_node=choice_data.get("next", ""),
        effect=effect,
        effect_value=effect_value
    )


def _convert_dialogues_dict_to_objects(dialogues_dict: Dict[str, Dict]) -> Dict[str, Dialogue]:
    """Конвертировать словарь диалогов в объекты Dialogue
    
    Возвращает словарь, где ключи - оригинальные ID диалогов (например, 'intro_awakening'),
    а значения - объекты Dialogue.
    """
    result = {}
    
    for dialogue_key, dialogue_data in dialogues_dict.items():
        # Создаём объект Dialogue
        # dialogue_key - это оригинальный ключ (например, 'intro_awakening')
        # dialogue_data.get("id") - это внутренний ID из данных (например, 'ch1_intro')
        # Используем dialogue_key как основной ID для совместимости
        dialogue = Dialogue(
            id=dialogue_key,  # Используем ключ словаря как ID
            title=dialogue_data.get("title", dialogue_key),
            start_node="start"
        )
        
        # Создаём узлы диалога
        # Для упрощения создаём один узел "start" с текстом и выборами
        start_text = ""
        
        # Собираем текст из всех реплик
        dialogues_list = dialogue_data.get("dialogues", [])
        for dlg in dialogues_list:
            speaker = dlg.get("speaker", "")
            text = dlg.get("text", "")
            start_text += f"{speaker}: {text}\n"
        
        # Конвертируем выборы
        choices_data = dialogue_data.get("choices", [])
        choices = [_convert_choice_to_object(c) for c in choices_data]
        
        # Добавляем узел start
        dialogue.add_node(DialogueNode(
            id="start",
            speaker="narrator",
            text=start_text.strip(),
            choices=choices
        ))
        
        result[dialogue_key] = dialogue
    
    return result


def get_chapter_dialogues(chapter_number):
    """Получить все диалоги главы"""
    chapters = {
        1: CHAPTER_1_DIALOGUES,
        2: CHAPTER_2_DIALOGUES,
        3: CHAPTER_3_DIALOGUES,
        4: CHAPTER_4_DIALOGUES,
        5: CHAPTER_5_DIALOGUES
    }
    raw_dialogues = chapters.get(chapter_number, {})
    
    # Конвертируем словари в объекты Dialogue
    return _convert_dialogues_dict_to_objects(raw_dialogues)


def get_dialogue_by_id(chapter, dialogue_id):
    """Получить конкретный диалог"""
    dialogues = get_chapter_dialogues(chapter)
    return dialogues.get(dialogue_id)

def apply_choice_consequence(chapter, choice_id, game_state):
    """Применить последствия выбора"""
    consequence = CHOICE_CONSEQUENCES.get(f"chapter_{chapter}", {}).get(choice_id)
    if consequence:
        for key, value in consequence.get("effects", {}).items():
            if isinstance(value, bool):
                game_state["flags"][key] = value
            elif isinstance(value, (int, float)):
                game_state["stats"][key] = game_state["stats"].get(key, 0) + value

        for option in consequence.get("future_options", []):
            game_state["available_options"].add(option)

    return game_state

def get_available_branches(game_state, chapter):
    """Получить доступные ветки на основе предыдущих выборов"""
    available = []
    dialogues = get_chapter_dialogues(chapter)

    for dialogue_id, dialogue in dialogues.items():
        # Проверка условий
        trigger = dialogue.get("trigger", {})
        conditions_met = True

        for key, value in trigger.items():
            if key == "flag":
                if not game_state.get("flags", {}).get(value):
                    conditions_met = False
                    break
            elif key == "relationship":
                char, amount = value.split(":")
                if game_state.get("relationships", {}).get(char, 0) < int(amount):
                    conditions_met = False
                    break

        if conditions_met:
            available.append(dialogue_id)

    return available

# ============================================================================
# ЭКСПОРТ
# ============================================================================

__all__ = [
    "CHAPTER_1_DIALOGUES",
    "CHAPTER_2_DIALOGUES",
    "CHAPTER_3_DIALOGUES",
    "CHAPTER_4_DIALOGUES",
    "CHAPTER_5_DIALOGUES",
    "CHOICE_CONSEQUENCES",
    "get_chapter_dialogues",
    "get_dialogue_by_id",
    "apply_choice_consequence",
    "get_available_branches"
]
