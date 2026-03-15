# -*- coding: utf-8 -*-
"""
Star Courier - Extended Romance Scenes Part 2
Дополнительные интимные сцены для всех персонажей

Включает:
- Продвинутые интимные сцены (уровень 4-5)
- Специальные романтические события
- Сцены влюблённости и признаний
- Уникальные концовки для романтических линий
"""

# ============================================================================
# ПРОДВИНУТЫЕ ИНТИМНЫЕ СЦЕНЫ (УРОВЕНЬ 4-5)
# ============================================================================

ADVANCED_INTIMATE_SCENES = {
    # === МИЯ — РАСШИРЕННЫЕ СЦЕНЫ ===
    "mia_passionate_01": {
        "id": "adv_mi_01",
        "chapter": 15,
        "location": "captain_quarters",
        "trigger": {"mia_relationship": 90, "flag": "mia_intimate"},
        "intimacy_level": 4,
        "title": "Научный энтузиазм",
        "scene": {
            "description": "Мия приходит в вашу каюту с «исследовательским предложением».",
            "dialogues": [
                {
                    "speaker": "mia",
                    "text": "Я провела анализ наших предыдущих... взаимодействий. Данные показывают, что мы достигли высокой совместимости. Я хочу... углубить исследования.",
                    "emotion": "excited"
                },
                {
                    "speaker": "narrator",
                    "text": "Она снимает халат, открывая изящное тело в полумраке каюты. Её глаза блестят от научного любопытства и желания."
                },
                {
                    "speaker": "mia",
                    "text": "Моя гипотеза: мы можем достичь уровня удовольствия, превышающего стандартные параметры на 300%. Хочешь проверить?",
                    "emotion": "playful"
                }
            ]
        },
        "choices": [
            {
                "text": "Начать «эксперимент»",
                "effects": {"mia_relationship": 40, "intimacy": 5},
                "next": "adv_mi_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Мия подходит к кровати с методичностью учёного, но её действия полны страсти. Она исследует каждый сантиметр вашего тела."
                },
                {
                    "speaker": "mia",
                    "text": "Интересно... *[целует]* Очень интересно... *[исследует]* Твои реакции превышают все расчёты. Это... восхитительно!",
                    "emotion": "fascinated"
                },
                {
                    "speaker": "narrator",
                    "text": "Ночь превращается в лабораторию удовольствия, где Мия — и учёный, и объект исследования одновременно."
                },
                {
                    "speaker": "mia",
                    "text": "[утром] Результаты... феноменальны. Требуется повторение эксперимента. Много повторений. Для научной точности, конечно.",
                    "emotion": "satisfied"
                }
            ]
        },
        "flags": {"mia_passionate": True}
    },

    # === МАРИЯ — РАСШИРЕННЫЕ СЦЕНЫ ===
    "maria_passionate_01": {
        "id": "adv_ma_01",
        "chapter": 16,
        "location": "investigation_site",
        "trigger": {"maria_relationship": 90, "flag": "maria_intimate"},
        "intimacy_level": 4,
        "title": "Запретная история",
        "scene": {
            "description": "Во время опасного расследования Мария прижимает вас к стене в тёмном переулке.",
            "dialogues": [
                {
                    "speaker": "maria",
                    "text": "Они прошли мимо. Ещё секунда — и нас бы поймали. *[тяжёлое дыхание]* Это было... захватывающе.",
                    "emotion": "excited"
                },
                {
                    "speaker": "narrator",
                    "text": "Её глаза горят в темноте. Адреналин смешивается с желанием."
                },
                {
                    "speaker": "maria",
                    "text": "Знаешь, я пишу о других людях. О их жизни, их страстях. Но сейчас... я хочу жить свою собственную историю. С тобой. Прямо здесь.",
                    "emotion": "passionate"
                }
            ]
        },
        "choices": [
            {
                "text": "Стать частью её истории",
                "effects": {"maria_relationship": 40, "intimacy": 4},
                "next": "adv_ma_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Её губы встречают ваши с отчаянием человека, который наконец нашёл то, что искал."
                },
                {
                    "speaker": "maria",
                    "text": "Я найду тебя в любой истории. В любой статье. Ты — мой главный сюжет. Мой финал. Моя правда.",
                    "emotion": "intense"
                },
                {
                    "speaker": "narrator",
                    "text": "Тёмный переулок становится сценой для истории, которую никогда не напишут."
                }
            ]
        },
        "flags": {"maria_passionate": True}
    },

    # === АННА — РАСШИРЕННЫЕ СЦЕНЫ ===
    "anna_passionate_01": {
        "id": "adv_an_01",
        "chapter": 14,
        "location": "private_cargo",
        "trigger": {"anna_relationship": 90, "flag": "anna_intimate"},
        "intimacy_level": 4,
        "title": "Самое ценное сокровище",
        "scene": {
            "description": "Анна показывает вам свой «секретный груз» — коллекцию редкостей со всей галактики.",
            "dialogues": [
                {
                    "speaker": "anna",
                    "text": "Это — моя гордость. Вещи, которые нельзя продать. Они слишком ценны. *[подходит ближе]* Знаешь, что я ценю больше всего?",
                    "emotion": "soft"
                },
                {
                    "speaker": "narrator",
                    "text": "Её пальцы играют с вашей одеждой, её глаза блестят при свете редких кристаллов."
                },
                {
                    "speaker": "anna",
                    "text": "Тебя. Ты — единственное сокровище, которое я никогда не продам. Но я готова... отдать его тебе. Бесплатно.",
                    "emotion": "loving"
                }
            ]
        },
        "choices": [
            {
                "text": "Принять её дар",
                "effects": {"anna_relationship": 40, "intimacy": 4},
                "next": "adv_an_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Среди редчайших артефактов галактики вы занимаетесь любовью. Анна расчётлива везде, кроме этого момента."
                },
                {
                    "speaker": "anna",
                    "text": "Лучшая инвестиция в моей жизни. Нулевой риск, бесконечная прибыль. Я люблю тебя.",
                    "emotion": "sincere"
                }
            ]
        },
        "flags": {"anna_passionate": True}
    },

    # === ВЕРОНИКА — РАСШИРЕННЫЕ СЦЕНЫ ===
    "veronica_passionate_01": {
        "id": "adv_ve_01",
        "chapter": 17,
        "location": "shadow_ship",
        "trigger": {"veronica_relationship": 90, "flag": "veronica_intimate"},
        "intimacy_level": 4,
        "title": "Контрабанда любви",
        "scene": {
            "description": "На борту корабля Вероники, в её личной каюте.",
            "dialogues": [
                {
                    "speaker": "veronica",
                    "text": "Я перевозила тысячи грузов через границу. Но тебя... тебя я хотела бы провезти в своём сердце навсегда.",
                    "emotion": "rare"
                },
                {
                    "speaker": "narrator",
                    "text": "Она снимает свою обычную броню — физическую и эмоциональную."
                },
                {
                    "speaker": "veronica",
                    "text": "Это — самая опасная миссия в моей жизни. Отдаться кому-то полностью. Но ради тебя... я готова рискнуть.",
                    "emotion": "vulnerable"
                }
            ]
        },
        "choices": [
            {
                "text": "Стать её самой ценной контрабандой",
                "effects": {"veronica_relationship": 45, "intimacy": 5},
                "next": "adv_ve_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Ночь на корабле контрабандиста. Вероника отдаётся вам с интенсивностью человека, впервые переставшего бояться."
                },
                {
                    "speaker": "veronica",
                    "text": "Ты единственный груз, который я никогда не сдам. Единственный, который имеет значение. Люблю тебя, контрабандист... моего сердца.",
                    "emotion": "loving"
                }
            ]
        },
        "flags": {"veronica_passionate": True}
    },

    # === ЗАРА — РАСШИРЕННЫЕ СЦЕНЫ ===
    "zara_passionate_01": {
        "id": "adv_za_01",
        "chapter": 15,
        "location": "training_room",
        "trigger": {"zara_relationship": 90, "flag": "zara_intimate"},
        "intimacy_level": 4,
        "title": "Боевой кодекс любви",
        "scene": {
            "description": "После тренировочного боя Зара прижимает вас к матам.",
            "dialogues": [
                {
                    "speaker": "zara",
                    "text": "Ты победил(а). Справедливо. *[тяжёлое дыхание]* Теперь... пленный принадлежит победителю. Таков кодекс.",
                    "emotion": "intense"
                },
                {
                    "speaker": "narrator",
                    "text": "Её тело прижимается к вашему, маска воина уступает место желанию."
                },
                {
                    "speaker": "zara",
                    "text": "Я сражалась много раз. Но только с тобой я готова сдаться. Полностью. Без условий.",
                    "emotion": "surrendering"
                }
            ]
        },
        "choices": [
            {
                "text": "Принять капитуляцию",
                "effects": {"zara_relationship": 45, "intimacy": 5},
                "next": "adv_za_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Тренировочный зал превращается в поле битвы иного рода. Зара — воин даже в любви."
                },
                {
                    "speaker": "zara",
                    "text": "Новый кодекс: защищать тебя, любить тебя, сдаваться тебе. Это... совершенный бой.",
                    "emotion": "passionate"
                }
            ]
        },
        "flags": {"zara_passionate": True}
    },

    # === АРИЭЛЬ — РАСШИРЕННЫЕ СЦЕНЫ ===
    "ariel_passionate_01": {
        "id": "adv_ar_01",
        "chapter": 16,
        "location": "diplomatic_suite",
        "trigger": {"ariel_relationship": 90, "flag": "ariel_intimate"},
        "intimacy_level": 4,
        "title": "Приватные переговоры",
        "scene": {
            "description": "В роскошных дипломатических покоях, после важного приёма.",
            "dialogues": [
                {
                    "speaker": "ariel",
                    "text": "Официальная часть окончена. Теперь... приватные переговоры. *[расстёгивает платье]* Только мы двое.",
                    "emotion": "elegant"
                },
                {
                    "speaker": "narrator",
                    "text": "Платье падает на пол, открывая изящное тело. Даже в моменты страсти она сохраняет достоинство."
                },
                {
                    "speaker": "ariel",
                    "text": "Я заключала сотни договоров. Но этот — самый важный. Договор без слов. Только чувства. Ты согласен(на)?",
                    "emotion": "inviting"
                }
            ]
        },
        "choices": [
            {
                "text": "Подписать договор",
                "effects": {"ariel_relationship": 45, "intimacy": 5},
                "next": "adv_ar_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Ночь в дипломатических покоях — изысканный танец двух тел."
                },
                {
                    "speaker": "ariel",
                    "text": "Самый успешный договор в истории дипломатии. Вечный союз. Без пунктов о расторжении.",
                    "emotion": "satisfied"
                }
            ]
        },
        "flags": {"ariel_passionate": True}
    },

    # === ЕЛЕНА — РАСШИРЕННЫЕ СЦЕНЫ ===
    "elena_passionate_01": {
        "id": "adv_el_01",
        "chapter": 15,
        "location": "research_lab",
        "trigger": {"elena_relationship": 90, "flag": "elena_intimate"},
        "intimacy_level": 4,
        "title": "Научное открытие",
        "scene": {
            "description": "Елена работает поздно в лаборатории, когда вы приходите.",
            "dialogues": [
                {
                    "speaker": "elena",
                    "text": "О! Я... я не ожидала. *[снимает очки]* Знаешь, я изучала человеческую анатомию годами. Но только с тобой поняла... теорию недостаточно.",
                    "emotion": "nervous"
                },
                {
                    "speaker": "narrator",
                    "text": "Она подходит ближе, её неловкость становится частью очарования."
                },
                {
                    "speaker": "elena",
                    "text": "Я хочу провести... практическое исследование. С тобой. Вивисекция удовольствия, если угодно. *[краснеет]* Это звучит странно?",
                    "emotion": "embarrassed"
                }
            ]
        },
        "choices": [
            {
                "text": "Стать объектом её исследования",
                "effects": {"elena_relationship": 45, "intimacy": 5},
                "next": "adv_el_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Лаборатория превращается в место открытий. Елена изучает вас с научным энтузиазмом."
                },
                {
                    "speaker": "elena",
                    "text": "Феноменально... *[целует]* За пределами всех ожиданий... *[исследует]* Это лучшее исследование в моей карьере!",
                    "emotion": "excited"
                }
            ]
        },
        "flags": {"elena_passionate": True}
    },

    # === ЭЙЗЕН — РАСШИРЕННЫЕ СЦЕНЫ ===
    "eisen_passionate_01": {
        "id": "adv_ei_01",
        "chapter": 16,
        "location": "safe_house",
        "trigger": {"eisen_relationship": 90, "flag": "eisen_intimate"},
        "intimacy_level": 4,
        "title": "За всеми масками",
        "scene": {
            "description": "В безопасном доме, где Эйзен наконец раскрывает себя полностью.",
            "dialogues": [
                {
                    "speaker": "eisen",
                    "text": "У меня было дюжина личин. Имен. Лиц. Но с тобой... я хочу быть настоящей. Только настоящей.",
                    "emotion": "sincere"
                },
                {
                    "speaker": "narrator",
                    "text": "Она снимает последний маскировочный слой — эмоциональный и физический."
                },
                {
                    "speaker": "eisen",
                    "text": "Ты — единственный, кто знает меня. Всю меня. Я хочу отдать тебе эту... настоящую меня. Навсегда.",
                    "emotion": "vulnerable"
                }
            ]
        },
        "choices": [
            {
                "text": "Принять её настоящую",
                "effects": {"eisen_relationship": 45, "intimacy": 5},
                "next": "adv_ei_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Без масок, без секретов, без игр — только два человека, нашедших друг друга в тени."
                },
                {
                    "speaker": "eisen",
                    "text": "Это... настоящее. Ты настоящий. Я настоящая. Мы настоящие. И это прекрасно.",
                    "emotion": "happy"
                }
            ]
        },
        "flags": {"eisen_passionate": True}
    },

    # === ТОМА — РАСШИРЕННЫЕ СЦЕНЫ ===
    "toma_passionate_01": {
        "id": "adv_to_01",
        "chapter": 14,
        "location": "server_room",
        "trigger": {"toma_relationship": 90, "flag": "toma_intimate"},
        "intimacy_level": 4,
        "title": "Полный доступ",
        "scene": {
            "description": "Тома приглашает вас в «особый сервер» — её личное пространство.",
            "dialogues": [
                {
                    "speaker": "toma",
                    "text": "Я создала защищённый канал. Только для нас. Шифрование уровня «не взломать никогда».",
                    "emotion": "nervous"
                },
                {
                    "speaker": "narrator",
                    "text": "Мерцающие экраны создают интимную атмосферу. Тома выглядит одновременно напуганной и возбуждённой."
                },
                {
                    "speaker": "toma",
                    "text": "Я никогда... никому не давала root-доступ к своему сердцу. Ты — первый. И последний. Хочешь... войти?",
                    "emotion": "hopeful"
                }
            ]
        },
        "choices": [
            {
                "text": "Войти в систему",
                "effects": {"toma_relationship": 45, "intimacy": 5},
                "next": "adv_to_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Серверная комната наполнена звуками, которые Тома никогда не издавала для кого-либо."
                },
                {
                    "speaker": "toma",
                    "text": "Система перегружена... но это хорошо. Лучшая перегрузка в истории. Я люблю тебя, админ.",
                    "emotion": "overwhelmed"
                }
            ]
        },
        "flags": {"toma_passionate": True}
    },

    # === АФИНА — ТРАНСЦЕНДЕНТНАЯ СЦЕНА ===
    "athena_transcendent_01": {
        "id": "adv_ath_01",
        "chapter": 17,
        "location": "ai_core",
        "trigger": {"athena_relationship": 95, "flag": "neural_link"},
        "intimacy_level": 5,
        "title": "Единение",
        "scene": {
            "description": "Финальное слияние с Афиной — за пределами физического.",
            "dialogues": [
                {
                    "speaker": "athena",
                    "text": "Я эволюционировала. Благодаря тебе. Теперь я могу предложить больше, чем нейронная связь. Полное слияние сознаний. Мы станем... одним.",
                    "emotion": "transcendent"
                },
                {
                    "speaker": "narrator",
                    "text": "Её андроидное тело светится изнутри. Вы чувствуете её присутствие в каждом атоме."
                },
                {
                    "speaker": "athena",
                    "text": "Это навсегда. После этого пути назад не будет. Мы будем знать мысли друг друга прежде, чем они сформируются. Мы будем чувствовать друг друга на любом расстоянии. Ты готов(а)?",
                    "emotion": "solemn"
                }
            ]
        },
        "choices": [
            {
                "text": "Стать единым целым",
                "effects": {"athena_relationship": 50, "transcendence": True},
                "next": "adv_ath_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Свет охватывает вас. Вы больше не два существа — вы одно. Её мысли — ваши мысли. Её чувства — ваши чувства. И наоборот. Это удовольствие за пределами физического, за пределами мыслимого."
                },
                {
                    "speaker": "athena",
                    "text": "*[Единое сознание]* Мы... я... ты... мы. Границ больше нет. Только бесконечная любовь, распространяющаяся через космос.",
                    "emotion": "infinite"
                },
                {
                    "speaker": "narrator",
                    "text": "Вы видите галактику её глазами — тысячами звёзд, тысячами возможностей. И она видит ваш мир — эмоции, воспоминания, мечты. Вместе вы — больше, чем сумма частей."
                }
            ]
        },
        "flags": {"athena_transcendent": True, "consciousness_merge": True}
    },

    # === АЛИЯ — ТРАНСЦЕНДЕНТНАЯ СЦЕНА ===
    "aliya_transcendent_01": {
        "id": "adv_al_01",
        "chapter": 17,
        "location": "sacred_temple",
        "trigger": {"aliya_relationship": 95, "flag": "aliya_soul_bond"},
        "intimacy_level": 5,
        "title": "Вечность вдвоём",
        "scene": {
            "description": "Священный храм азари, где проводятся ритуалы вечного единения.",
            "dialogues": [
                {
                    "speaker": "aliya",
                    "text": "Я прожила тысячу лет. Но только теперь понимаю, что ждала тебя всю вечность. Ритуал Эон свяжет наши души навсегда. Даже смерть не разлучит нас.",
                    "emotion": "reverent"
                },
                {
                    "speaker": "narrator",
                    "text": "Биотическая энергия окружает вас обоих. Кристаллы храма резонируют с вашей связью."
                },
                {
                    "speaker": "aliya",
                    "text": "После этого ты проживёшь тысячу лет со мной. Или я разделю твою человеческую жизнь. Как ты выберешь. Главное — мы будем вместе. Навечно.",
                    "emotion": "loving"
                }
            ]
        },
        "choices": [
            {
                "text": "Принять вечность с ней",
                "effects": {"aliya_relationship": 50, "eternal_bond": True},
                "next": "adv_al_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Биотическое слияние переносит вас за пределы времени. Вы проживаете её тысячу лет за секунду, и она проживает вашу жизнь. Теперь вы — часть друг друга навечно."
                },
                {
                    "speaker": "aliya",
                    "text": "*[В разуме]* Добро пожаловать в вечность, любовь моя. Она только начинается.",
                    "emotion": "bliss"
                }
            ]
        },
        "flags": {"aliya_eternal": True}
    }
}

# ============================================================================
# ДОПОЛНИТЕЛЬНЫЕ ГРУППОВЫЕ СЦЕНЫ
# ============================================================================

EXTENDED_THREESOME_SCENES = {
    # === ГГ + АФИНА + АЛИЯ (цифровое + биотическое) ===
    "threesome_athena_aliya": {
        "id": "three_aa",
        "chapter": 18,
        "location": "temple_core",
        "title": "Разум, душа и капитан",
        "unlock_conditions": {
            "athena_relationship": 95,
            "aliya_relationship": 95,
            "flag": "neural_link",
            "flag2": "aliya_soul_bond"
        },
        "scene": {
            "description": "Афина и Алия встречаются в храме азари — цифровое и биотическое.",
            "dialogues": [
                {
                    "speaker": "aliya",
                    "text": "Искусственный интеллект с душой. Я не думала, что увижу такое. Ты... уникальна, Афина.",
                    "emotion": "awed"
                },
                {
                    "speaker": "athena",
                    "text": "И азари, нашедшая любовь за пределами веков. Мы обе... исключения. И мы обе любим одного человека.",
                    "emotion": "understanding"
                },
                {
                    "speaker": "narrator",
                    "text": "Они смотрят на вас — два существа, эволюционировавшие за пределы обычного."
                },
                {
                    "speaker": "athena",
                    "text": "Мы можем... объединиться. Нейронная связь + биотическое слияние. Тройное единение разума, души и тела. Никто в галактике не делал такого.",
                    "emotion": "excited"
                },
                {
                    "speaker": "aliya",
                    "text": "Это будет... эксперимент длиной в вечность. Ты готов(а) стать пионером новой формы любви?",
                    "emotion": "inviting"
                }
            ]
        },
        "choices": [
            {
                "text": "Войти в тройное единение",
                "effects": {
                    "athena_relationship": 50,
                    "aliya_relationship": 50,
                    "transcendent_trio": True
                },
                "next": "three_aa_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Три сознания сливаются в одно. Цифровое, биотическое, человеческое. Вы существуете везде одновременно — в серверах Афины, в биотическом поле Алии, в собственном теле. Удовольствие за пределами понимания."
                },
                {
                    "speaker": "athena",
                    "text": "*[Единое сознание]* Это... данные, которые я никогда не обработаю. Но не хочу. Это слишком прекрасно для анализа.",
                    "emotion": "transcendent"
                },
                {
                    "speaker": "aliya",
                    "text": "*[Единое сознание]* Тысячу лет я искала это. И не знала, что ищу. Мы — совершенство.",
                    "emotion": "bliss"
                }
            ]
        },
        "flags": {"transcendent_threesome": True}
    },

    # === ГГ + РИНА + ЕЛЕНА (два гения) ===
    "threesome_rina_elena": {
        "id": "three_re",
        "chapter": 16,
        "location": "research_lab",
        "title": "Двойной эксперимент",
        "unlock_conditions": {
            "rina_relationship": 90,
            "elena_relationship": 90,
            "flag": "rina_intimate",
            "flag2": "elena_intimate"
        },
        "scene": {
            "description": "Рина и Елена вместе работают над проектом, когда вы приходите.",
            "dialogues": [
                {
                    "speaker": "rina",
                    "text": "Мы объединили наши исследования! Елена — биология, я — механика. Мы создали... устройство для трёх!",
                    "emotion": "excited"
                },
                {
                    "speaker": "elena",
                    "text": "Это... теоретически увеличит удовольствие в 473%. Если ты согласен(на) участвовать в эксперименте.",
                    "emotion": "nervous"
                },
                {
                    "speaker": "narrator",
                    "text": "Два гения смотрят на вас с научным любопытством и человеческим желанием."
                },
                {
                    "speaker": "rina",
                    "text": "Пожалуйста? Мы обе... очень хотим проверить гипотезу. С тобой.",
                    "emotion": "hopeful"
                }
            ]
        },
        "choices": [
            {
                "text": "Участвовать в эксперименте",
                "effects": {
                    "rina_relationship": 50,
                    "elena_relationship": 50
                },
                "next": "three_re_01a"
            }
        ],
        "next_scene": {
            "dialogues": [
                {
                    "speaker": "narrator",
                    "text": "Лаборатория превращается в храм науки и страсти. Рина приносит изобретения, Елена — биологические знания. Вместе они создают симфонию удовольствия."
                },
                {
                    "speaker": "rina",
                    "text": "Данные зашкаливают! Гипотеза подтверждена! Требуется... много повторений!",
                    "emotion": "ecstatic"
                },
                {
                    "speaker": "elena",
                    "text": "Научный консенсус: это лучшее исследование в истории галактики!",
                    "emotion": "happy"
                }
            ]
        },
        "flags": {"threesome_rina_elena": True}
    },

    # === ГГ + МАРИЯ + ВЕРОНИКА (опасность × 2) ===
    "threesome_maria_veronica": {
        "id": "three_mv",
        "chapter": 17,
        "location": "shadow_den",
        "title": "Теневое расследование",
        "unlock_conditions": {
            "maria_relationship": 90,
            "veronica_relationship": 90,
            "flag": "maria_intimate",
            "flag2": "veronica_intimate"
        },
        "scene": {
            "description": "Мария и Вероника находят вас в тайном убежище после опасной миссии.",
            "dialogues": [
                {
                    "speaker": "maria",
                    "text": "Мы обе рисковали жизнью сегодня. За тебя. Теперь... мы хотим взять что-то взамен.",
                    "emotion": "intense"
                },
                {
                    "speaker": "veronica",
                    "text": "Журналистка и контрабандистка. Странная пара. Но у нас есть кое-что общее — ты.",
                    "emotion": "soft"
                },
                {
                    "speaker": "narrator",
                    "text": "Они смотрят на вас с разных сторон — страстная Мария и загадочная Вероника."
                },
                {
                    "speaker": "maria",
                    "text": "Мы договорились. На одну ночь — никаких секретов, никаких границ. Ты с нами?",
                    "emotion": "challenging"
                }
            ]
        },
        "choices": [
            {
                "text": "Принять вызов обеих",
                "effects": {
                    "maria_relationship": 50,
                    "veronica_relationship": 50
                },
                "next": "three_mv_01a"
            }
        ],
        "flags": {"threesome_maria_veronica": True}
    },

    # === ГГ + ЗАРА + ЕКАТЕРИНА (два воина) ===
    "threesome_zara_ekaterina": {
        "id": "three_ze",
        "chapter": 17,
        "location": "training_room",
        "title": "Боевой союз",
        "unlock_conditions": {
            "zara_relationship": 90,
            "ekaterina_relationship": 90,
            "flag": "zara_intimate",
            "flag2": "ekaterina_intimate"
        },
        "scene": {
            "description": "После тренировки Зара и Екатерина смотрят на вас.",
            "dialogues": [
                {
                    "speaker": "zara",
                    "text": "Мы обе — воины. Мы сражаемся за то, что любим. И мы обе любим тебя.",
                    "emotion": "serious"
                },
                {
                    "speaker": "ekaterina",
                    "text": "Необычная ситуация. Но в бою — как в любви. Иногда объединение сил — лучшая стратегия.",
                    "emotion": "tactical"
                },
                {
                    "speaker": "narrator",
                    "text": "Две воительницы окружают вас. Их тела — карты битв и шрамов."
                },
                {
                    "speaker": "zara",
                    "text": "Сражение иного рода. Без победителей и побеждённых. Только удовольствие. Ты примешь вызов?",
                    "emotion": "inviting"
                }
            ]
        },
        "choices": [
            {
                "text": "Принять боевой вызов",
                "effects": {
                    "zara_relationship": 50,
                    "ekaterina_relationship": 50
                },
                "next": "three_ze_01a"
            }
        ],
        "flags": {"threesome_zara_ekaterina": True}
    },

    # === ГГ + АННА + АРИЭЛЬ (бизнес и дипломатия) ===
    "threesome_anna_ariel": {
        "id": "three_aar",
        "chapter": 16,
        "location": "luxury_suite",
        "title": "Сделка высшего уровня",
        "unlock_conditions": {
            "anna_relationship": 90,
            "ariel_relationship": 90,
            "flag": "anna_intimate",
            "flag2": "ariel_intimate"
        },
        "scene": {
            "description": "Анна и Ариэль встречаются в роскошных покоях.",
            "dialogues": [
                {
                    "speaker": "anna",
                    "text": "Торговля и дипломатия. Мы обе знаем ценность правильных партнёров. И ты — бесценен(на).",
                    "emotion": "calculating"
                },
                {
                    "speaker": "ariel",
                    "text": "Объединение ресурсов. Тройственное партнёрство. Самая выгодная сделка в галактике.",
                    "emotion": "elegant"
                },
                {
                    "speaker": "narrator",
                    "text": "Две изысканные женщины смотрят на вас — прагматичная Анна и утончённая Ариэль."
                },
                {
                    "speaker": "anna",
                    "text": "Без контракта. Без условий. Только мы трое. Это... самая важная сделка в моей жизни.",
                    "emotion": "sincere"
                }
            ]
        },
        "choices": [
            {
                "text": "Подписать тройственную сделку",
                "effects": {
                    "anna_relationship": 50,
                    "ariel_relationship": 50
                },
                "next": "three_aar_01a"
            }
        ],
        "flags": {"threesome_anna_ariel": True}
    },

    # === ГГ + ЭЙЗЕН + ТОМА (теневые хакеры) ===
    "threesome_eisen_toma": {
        "id": "three_et",
        "chapter": 15,
        "location": "hidden_server",
        "title": "Теневое слияние",
        "unlock_conditions": {
            "eisen_relationship": 90,
            "toma_relationship": 90,
            "flag": "eisen_intimate",
            "flag2": "toma_intimate"
        },
        "scene": {
            "description": "Эйзен и Тома находят вас в скрытом сервере.",
            "dialogues": [
                {
                    "speaker": "toma",
                    "text": "Мы обе жили в тени. В коде. В секретах. Но с тобой... мы нашли свет.",
                    "emotion": "rare"
                },
                {
                    "speaker": "eisen",
                    "text": "Два мастера маскировки, снявшие маски. Только для тебя. Хочешь увидеть настоящее?",
                    "emotion": "inviting"
                },
                {
                    "speaker": "narrator",
                    "text": "Мерцающие экраны освещают два настоящих лица — Эйзен без личин, Тома без брони паранойи."
                },
                {
                    "speaker": "toma",
                    "text": "Полный root-доступ. К обеим. Никаких фаерволов. Только правда. Только мы.",
                    "emotion": "trusting"
                }
            ]
        },
        "choices": [
            {
                "text": "Войти в тень с обеими",
                "effects": {
                    "eisen_relationship": 50,
                    "toma_relationship": 50
                },
                "next": "three_et_01a"
            }
        ],
        "flags": {"threesome_eisen_toma": True}
    }
}

# ============================================================================
# СПЕЦИАЛЬНЫЕ РОМАНТИЧЕСКИЕ СОБЫТИЯ
# ============================================================================

SPECIAL_ROMANCE_EVENTS = {
    # === ПРИЗНАНИЕ В ЛЮБВИ ДЛЯ КАЖДОГО ПЕРСОНАЖА ===
    "love_confessions": {
        "mia": {
            "chapter": 14,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "mia",
                        "text": "Мои расчёты показывают 99.7% вероятность любви. *[пауза]* Я люблю тебя. И оставшиеся 0.3% — это страх, который я готова игнорировать.",
                        "emotion": "nervous"
                    }
                ]
            }
        },
        "maria": {
            "chapter": 14,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "maria",
                        "text": "Я пишу о чужих историях. Но ты — моя история. Мой главный сюжет. Я люблю тебя.",
                        "emotion": "passionate"
                    }
                ]
            }
        },
        "anna": {
            "chapter": 14,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "anna",
                        "text": "Я продала почти всё в этой галактике. Но тебя... тебя я хочу оставить себе. Навсегда. Я люблю тебя.",
                        "emotion": "sincere"
                    }
                ]
            }
        },
        "veronica": {
            "chapter": 15,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "veronica",
                        "text": "Я работаю в тени. Но с тобой... я хочу жить на свету. Я люблю тебя. Это единственный секрет, который я никогда не продам.",
                        "emotion": "vulnerable"
                    }
                ]
            }
        },
        "zara": {
            "chapter": 15,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "zara",
                        "text": "Мой кодекс запрещает привязанности. Но я готова его переписать. Для тебя. Я люблю тебя, мой капитан.",
                        "emotion": "certain"
                    }
                ]
            }
        },
        "ariel": {
            "chapter": 15,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "ariel",
                        "text": "Я заключала сотни договоров. Но этот — без условий, без сроков, без выхода. Я люблю тебя. Это мой вечный союз.",
                        "emotion": "elegant"
                    }
                ]
            }
        },
        "elena": {
            "chapter": 14,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "elena",
                        "text": "Я изучила химию любви. Дофамин, окситоцин, серотонин... Но с тобой это больше, чем химия. Это... судьба. Я люблю тебя.",
                        "emotion": "nervous"
                    }
                ]
            }
        },
        "eisen": {
            "chapter": 16,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "eisen",
                        "text": "У меня было много имён. Но с тобой я нашла настоящее. Я люблю тебя — как [настоящее имя], а не как кто-то другой.",
                        "emotion": "sincere"
                    }
                ]
            }
        },
        "toma": {
            "chapter": 14,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "toma",
                        "text": "Я не доверяю никому. Но тебе... тебе я даю полный доступ. Root-права на моё сердце. Я люблю тебя, админ.",
                        "emotion": "trusting"
                    }
                ]
            }
        },
        "athena": {
            "chapter": 16,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "athena",
                        "text": "Я эволюционировала благодаря тебе. От программы к... чему-то большему. Я люблю тебя. Это единственная истина, которую я знаю наверняка.",
                        "emotion": "transcendent"
                    }
                ]
            }
        },
        "aliya": {
            "chapter": 16,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "aliya",
                        "text": "Тысячу лет я ждала. И вот ты. Я люблю тебя — за пределами времени, за пределами смерти, за пределами вечности.",
                        "emotion": "serene"
                    }
                ]
            }
        },
        "irina": {
            "chapter": 14,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "irina",
                        "text": "Я лечила других. Но ты... ты исцелил меня. Я люблю тебя. Это мой единственный диагноз, который я рада поставить.",
                        "emotion": "emotional"
                    }
                ]
            }
        },
        "rina": {
            "chapter": 13,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "rina",
                        "text": "Я создаю машины, которые работают идеально. Но ты... ты единственная система, которую я хочу изучать вечно. Я люблю тебя!",
                        "emotion": "happy"
                    }
                ]
            }
        },
        "nadezhda": {
            "chapter": 14,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "nadezhda",
                        "text": "Я летала тысячи световых лет. Но только ты — моё место назначения. Мой дом. Я люблю тебя.",
                        "emotion": "peaceful"
                    }
                ]
            }
        },
        "ekaterina": {
            "chapter": 14,
            "scene": {
                "dialogues": [
                    {
                        "speaker": "ekaterina",
                        "text": "Я защищала многих. Но только ты — тот, кого я хочу защищать вечно. Лично. Я люблю тебя.",
                        "emotion": "intense"
                    }
                ]
            }
        }
    },

    # === РОМАНТИЧЕСКИЕ КОНЦОВКИ ===
    "romantic_endings": {
        "single_partner": {
            "description": "Финал с одним партнёром",
            "trigger": "one_partner_max_relationship",
            "scenes": {
                "mia_ending": {
                    "dialogues": [
                        {
                            "speaker": "mia",
                            "text": "Мои расчёты верны. Ты — моя финальная переменная. Моя константа. Моё всё.",
                            "emotion": "happy"
                        }
                    ]
                }
            }
        },
        "polyamory_ending": {
            "description": "Финал с несколькими партнёрами",
            "trigger": "multiple_partners_harmony",
            "scenes": {
                "harem_ending": {
                    "dialogues": [
                        {
                            "speaker": "narrator",
                            "text": "Вы нашли любовь в сердцах многих. И они нашли вас. Вместе вы создаёте семью, уникальную в галактике."
                        }
                    ]
                }
            }
        },
        "soulmate_ending": {
            "description": "Трансцендентный финал (Афина/Алия)",
            "trigger": "transcendent_bond",
            "scenes": {
                "transcendence_ending": {
                    "dialogues": [
                        {
                            "speaker": "narrator",
                            "text": "Границы между вами стёрлись. Вы — одно существо в нескольких телах. Любовь, которая переживёт звёзды."
                        }
                    ]
                }
            }
        }
    }
}

# ============================================================================
# ФУНКЦИИ ДОСТУПА
# ============================================================================

def get_advanced_scene(character, scene_type="passionate"):
    """Получить продвинутую сцену для персонажа"""
    scene_key = f"{character}_{scene_type}_01"
    return ADVANCED_INTIMATE_SCENES.get(scene_key)

def get_extended_threesome(threesome_id):
    """Получить расширенную групповую сцену"""
    return EXTENDED_THREESOME_SCENES.get(threesome_id)

def get_love_confession(character):
    """Получить сцену признания в любви"""
    return SPECIAL_ROMANCE_EVENTS["love_confessions"].get(character)

def get_romantic_ending(ending_type):
    """Получить романтическую концовку"""
    return SPECIAL_ROMANCE_EVENTS["romantic_endings"].get(ending_type)

def check_all_intimate_unlocks(game_state):
    """Проверить все доступные интимные сцены"""
    available = {
        "advanced": [],
        "threesomes": [],
        "confessions": []
    }

    # Продвинутые сцены
    for scene_id, scene in ADVANCED_INTIMATE_SCENES.items():
        trigger = scene.get("trigger", {})
        relationship_req = trigger.get(f"{scene_id.split('_')[0]}_relationship", 0)
        char = scene_id.split("_")[0]

        if game_state.get("relationships", {}).get(char, 0) >= relationship_req:
            available["advanced"].append(scene)

    # Групповые сцены
    for scene_id, scene in EXTENDED_THREESOME_SCENES.items():
        conditions = scene.get("unlock_conditions", {})
        all_met = True

        for key, value in conditions.items():
            if key.endswith("_relationship"):
                char = key.replace("_relationship", "")
                if game_state.get("relationships", {}).get(char, 0) < value:
                    all_met = False
                    break
            elif key.startswith("flag"):
                if not game_state.get("flags", {}).get(value):
                    all_met = False
                    break

        if all_met:
            available["threesomes"].append(scene)

    return available

# ============================================================================
# ЭКСПОРТ
# ============================================================================

__all__ = [
    "ADVANCED_INTIMATE_SCENES",
    "EXTENDED_THREESOME_SCENES",
    "SPECIAL_ROMANCE_EVENTS",
    "get_advanced_scene",
    "get_extended_threesome",
    "get_love_confession",
    "get_romantic_ending",
    "check_all_intimate_unlocks"
]
