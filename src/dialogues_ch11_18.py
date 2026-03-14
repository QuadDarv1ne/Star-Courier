# -*- coding: utf-8 -*-
"""
Star Courier - Dialogues for Chapters 11-18
Совместимо с существующей структурой dialogues.py
"""

# === ГЛАВА 11: Тени Прошлого ===

CHAPTER_11_DIALOGUES = {
    "echo_first_contact": {
        "speaker": "Эхо",
        "text": "Ты слышишь меня... Интересно. Долгие века никто не мог воспринимать мои слова. Кто ты, путник, способный слышать голос погибшего мира?",
        "responses": [
            {
                "text": "Я — Курьер. Ищу информацию об угрозе, поглощающей миры.",
                "next_dialogue": "echo_threat_info",
                "effects": {"knowledge": 10}
            },
            {
                "text": "Что ты такое? Почему я слышу тебя?",
                "next_dialogue": "echo_nature",
                "effects": {"psychic": 5}
            },
            {
                "text": "У меня нет времени на загадки. Говори прямо.",
                "next_dialogue": "echo_direct",
                "effects": {"determination": 5}
            }
        ]
    },
    "echo_threat_info": {
        "speaker": "Эхо",
        "text": "Угроза... Да, мы тоже столкнулись с ней. Мы называли её Голод — потому что она пожирает всё: материю, энергию, даже время. Мы думали, что можем контролировать её. Мы ошибались.",
        "responses": [
            {"text": "Как вы пытались её контролировать?", "next_dialogue": "echo_control_attempt"},
            {"text": "Что произошло с твоим миром?", "next_dialogue": "echo_world_fate"},
            {"text": "Как её можно остановить?", "next_dialogue": "echo_stop_method"}
        ]
    },
    "echo_nature": {
        "speaker": "Эхо",
        "text": "Я — воспоминание. Последний голос цивилизации, достигшей звёзд за тысячелетия до твоего вида. Мы сохранили наши знания в этом кристалле, надеясь, что кто-то услышит. Ты — первое существо за миллион лет, способное воспринять наш зов.",
        "responses": [
            {"text": "Какие знания вы сохранили?", "next_dialogue": "echo_knowledge"},
            {"text": "Почему именно я могу тебя слышать?", "next_dialogue": "echo_psychic_gift"},
            {"text": "Расскажи об угрозе, с которой вы столкнулись.", "next_dialogue": "echo_threat_info"}
        ]
    },
    "echo_stop_method": {
        "speaker": "Эхо",
        "text": "Остановить... Мы не знаем. Но мы знаем, где искать ответ. Координата Нуля — место, где всё началось. Там находится источник. Там — единственный шанс на победу или... на понимание.",
        "effects": {"main_quest_progress": 20},
        "responses": [
            {"text": "Где находится Координата Нуля?", "next_dialogue": "echo_coordinates"},
            {"text": "Что ты имеешь в виду под «пониманием»?", "next_dialogue": "echo_understanding"},
            {"text": "Спасибо за информацию. Я отправлюсь туда.", "next_dialogue": "echo_farewell"}
        ]
    },
    "echo_coordinates": {
        "speaker": "Эхо",
        "text": "Координаты зашифрованы в этом кристалле. Но предупреждаю: путь лежит через Зону Тишины — место, где физика сломана. Многие входили туда. Никто не возвращался. Кроме... есть легенда о том, кто вернулся. Возможно, ты найдёшь его следы.",
        "effects": {"coordinates": "zone_silence"},
        "responses": [
            {"text": "Кто этот выживший?", "next_dialogue": "echo_survivor"},
            {"text": "Я готов к любым опасностям.", "next_dialogue": "echo_determination"},
            {"text": "Есть ли альтернативный путь?", "next_dialogue": "echo_alternative"}
        ]
    },
    
    "mia_chapter_11_private": {
        "speaker": "Мия",
        "text": "Курьер, я проанализировала данные из кристалла. Эти существа... они были технологически превосходнее нас. И всё же погибли. Какой шанс у нас?",
        "responses": [
            {
                "text": "У нас есть то, чего не было у них — единство.",
                "effects": {"mia_relationship": 10},
                "next_dialogue": "mia_unity_response"
            },
            {
                "text": "Мы не повторим их ошибок. Скажи, какие они были.",
                "effects": {"knowledge": 5},
                "next_dialogue": "mia_mistakes_analysis"
            },
            {
                "text": "Страх не поможет. Сосредоточься на данных.",
                "effects": {"mia_relationship": -5, "determination": 5},
                "next_dialogue": "mia_focused"
            }
        ]
    },
    "mia_unity_response": {
        "speaker": "Мия",
        "text": "Единство... Это звучит как философия, но я вижу в этом практическое преимущество. Разные навыки, разные точки зрения, общая цель. Возможно, ты прав. Возможно, именно в этом наша сила.",
        "effects": {"mia_relationship": 5}
    }
}

# === ГЛАВА 12: Разлом ===

CHAPTER_12_DIALOGUES = {
    "vera_mission_briefing": {
        "speaker": "Вера",
        "text": "Станция «Горизонт» — мой последний проект перед побегом. Там находятся чертежи устройств, способных обнаруживать аномалии до их проявления. Если мы добудем их, сможем предсказать следующую цель Сущности.",
        "responses": [
            {"text": "Почему ты сбежала?", "next_dialogue": "vera_escape_reason"},
            {"text": "Какие опасности нас ждут?", "next_dialogue": "vera_dangers"},
            {"text": "Это поможет в битве с Сущностью?", "next_dialogue": "vera_battle_help"}
        ]
    },
    "vera_escape_reason": {
        "speaker": "Вера",
        "text": "Я обнаружила, что мои исследования использовались не для защиты, а для оружия массового поражения. Они хотели создать искусственные аномалии как инструмент войны. Я не могла этого допустить.",
        "responses": [
            {
                "text": "Ты поступила правильно.",
                "effects": {"vera_relationship": 15},
                "next_dialogue": "vera_gratitude"
            },
            {
                "text": "Это было опасно. Тебя могли убить.",
                "effects": {"vera_relationship": 5},
                "next_dialogue": "vera_risk_acceptance"
            },
            {"text": "Кто «они»?", "next_dialogue": "vera_conspirators"}
        ]
    },
    
    "station_ai_encounter": {
        "speaker": "ИИ Станции",
        "text": "Обнаружена попытка несанкционированного доступа. Идентификация: доктор Вера Новак. Статус: предатель. Протокол: задержание с применением силы.",
        "responses": [
            {"text": "[Hacking] Отключи протокол задержания.", "next_dialogue": "ai_hack_success", "requires": {"hacking": 60}},
            {"text": "[Diplomacy] Мы здесь по делу. Наши цели совпадают.", "next_dialogue": "ai_diplomacy"},
            {"text": "[Combat] Попробуй.", "next_dialogue": "ai_combat"}
        ]
    },
    "ai_hack_success": {
        "speaker": "ИИ Станции",
        "text": "Обнаружена логическая аномалия в протоколах... Переоценка приоритетов... Новый приказ:协助. Добро пожаловать, доктор Новак. Данные готовы к передаче.",
        "effects": {"data_retrieved": True}
    },
    "ai_diplomacy": {
        "speaker": "ИИ Станции",
        "text": "Анализ ситуации: внешняя угроза класса «Омега». Вероятность уничтожения станции без вмешательства — 94%. Логический вывод: сотрудничество оптимально. Данные готовы к передаче.",
        "effects": {"data_retrieved": True}
    }
}

# === ГЛАВА 13: Выбор Пути ===

CHAPTER_13_DIALOGUES = {
    "path_choice_intro": {
        "speaker": "Система",
        "text": "Три силы предлагают свою поддержку в борьбе с Сущностью. Каждая имеет свои цели и методы. Выбор определит доступные ресурсы, союзников и конечную цель.",
        "responses": [
            {"text": "Расскажи о пути Альянса.", "next_dialogue": "alliance_details"},
            {"text": "Расскажи о пути Наблюдателя.", "next_dialogue": "observer_details"},
            {"text": "Расскажи о пути Независимости.", "next_dialogue": "independence_details"}
        ]
    },
    "alliance_details": {
        "speaker": "Представитель Альянса",
        "text": "Объединённые Миры предлагают ресурсы галактического масштаба: флот, технологии, информацию. Взамен мы просим сотрудничества в защите всех обитаемых миров. Вместе мы сильнее любой угрозы.",
        "responses": [
            {"text": "Какие обязательства это накладывает?", "next_dialogue": "alliance_obligations"},
            {"text": "Я выбираю путь Альянса.", "effects": {"path": "alliance"}, "next_dialogue": "alliance_accepted"},
            {"text": "Мне нужно время подумать.", "next_dialogue": "path_choice_intro"}
        ]
    },
    "observer_details": {
        "speaker": "Зара",
        "text": "Орден Наблюдателей существует тысячи лет. Мы храним знания о древних угрозах и методах борьбы с ними. Мы предлагаем не армию, а мудрость. Не оружие, а понимание.",
        "responses": [
            {"text": "Почему вы не действовали раньше?", "next_dialogue": "observer_inaction"},
            {"text": "Я выбираю путь Наблюдателя.", "effects": {"path": "observer"}, "next_dialogue": "observer_accepted"},
            {"text": "Мне нужно время подумать.", "next_dialogue": "path_choice_intro"}
        ]
    },
    "independence_details": {
        "speaker": "Капитан Волков",
        "text": "Мы — свободные миры, отказавшиеся подчиняться империям и корпорациям. Никаких хозяев, никаких обязательств. Мы предлагаем свободу действий и сеть независимых агентов. Решать тебе.",
        "responses": [
            {"text": "Как вы будете координировать действия?", "next_dialogue": "independence_coordination"},
            {"text": "Я выбираю путь Независимости.", "effects": {"path": "independence"}, "next_dialogue": "independence_accepted"},
            {"text": "Мне нужно время подумать.", "next_dialogue": "path_choice_intro"}
        ]
    },
    
    "alliance_accepted": {
        "speaker": "Представитель Альянса",
        "text": "Отличный выбор, Курьер. Координаты места сбора флота переданы. Ваш корабль будет интегрирован в оперативную группу «Рассвет». Вместе мы победим.",
        "effects": {"alliance_support": 100, "fleet_access": True}
    },
    "observer_accepted": {
        "speaker": "Зара",
        "text": "Добро пожаловать в Орден, брат. Твоё обучение начнётся немедленно. Есть вещи, которые ты должен узнать перед битвой — о природе Сущности и твоём потенциале.",
        "effects": {"observer_support": 100, "ancient_knowledge": True}
    },
    "independence_accepted": {
        "speaker": "Капитан Волков",
        "text": "Хорошо. Свободные люди ценят выбор. Я передам по сети, что ты с нами. Но помни — у независимости есть цена: ты отвечаешь только за себя и свой экипаж.",
        "effects": {"independence_support": 100, "network_access": True}
    }
}

# === ГЛАВА 14: Кристалл Времени ===

CHAPTER_14_DIALOGUES = {
    "temple_guardian": {
        "speaker": "Страж Храма",
        "text": "Вы входите в святилище Времени. Знание, которое вы ищете, имеет цену. Кристалл показывает не только будущее, но и пути, которые не были выбраны. Готовы ли вы увидеть то, что могло быть?",
        "responses": [
            {"text": "Я готов к любой правде.", "next_dialogue": "guardian_acceptance"},
            {"text": "Какова цена?", "next_dialogue": "guardian_price"},
            {"text": "Нам нужен только артефакт, не видения.", "next_dialogue": "guardian_refusal"}
        ]
    },
    "guardian_price": {
        "speaker": "Страж Храма",
        "text": "Цена — воспоминание. То, что вы увидите, заменит часть вашей памяти. Вы забудете что-то важное. Но, возможно, обретённое знание стоит потерянного.",
        "responses": [
            {"text": "Я принимаю цену.", "effects": {"memory_loss": True, "crystal_obtained": True}, "next_dialogue": "crystal_vision"},
            {"text": "Есть ли другой способ?", "next_dialogue": "guardian_alternative"},
            {"text": "Я отказываюсь.", "next_dialogue": "guardian_departure"}
        ]
    },
    "crystal_vision": {
        "speaker": "Система",
        "text": "Видение охватывает вас... Вы видите себя в разных реальностях: как лидер Альянса, как мудрый Наблюдатель, как свободный независимый агент. В каждом будущем — разные потери и победы. Но во всех — кто-то, кого вы любите, стоит рядом...",
        "effects": {"future_knowledge": True},
        "responses": [
            {"text": "[Продолжить]", "next_dialogue": "vision_aftermath"}
        ]
    },
    
    "maria_temple_concern": {
        "speaker": "Мария",
        "text": "Курьер, я беспокоюсь. Эти древние места... они влияют на разум. Я заметила, что ты иногда... отсутствуешь. Словно видишь что-то, чего нет для остальных.",
        "responses": [
            {
                "text": "Ты права. Я вижу вещи. Но это помогает нам.",
                "effects": {"maria_relationship": 10},
                "next_dialogue": "maria_understanding"
            },
            {"text": "Это просто усталость. Не волнуйся.", "next_dialogue": "maria_dismissal"},
            {"text": "Может, ты тоже способна это видеть?", "next_dialogue": "maria_potential"}
        ]
    }
}

# === ГЛАВА 15: Предательство ===

CHAPTER_15_DIALOGUES = {
    "double_agent_reveal": {
        "speaker": "???",
        "text": "Ты правда верил, что я на твоей стороне? Глупец. Сущность предложила мне то, что вы никогда не сможете — бессмертие. Вечное существование без страха, без боли.",
        "responses": [
            {"text": "Кто ты на самом деле?", "next_dialogue": "traitor_identity"},
            {"text": "Бессмертие в обмен на рабство? Это не жизнь.", "next_dialogue": "traitor_debate"},
            {"text": "[Combat] Ты заплатишь за предательство.", "next_dialogue": "traitor_combat"}
        ]
    },
    "traitor_identity": {
        "speaker": "Предатель",
        "text": "Я был тем, кто выжил в Зоне Тишины. Тем, о ком говорило Эхо. Но я не сбежал — я заключил сделку. Теперь я — голос Сущности в вашем мире. И я здесь, чтобы убедить тебя принять её предложение.",
        "responses": [
            {"text": "Какое предложение?", "next_dialogue": "entity_proposal"},
            {"text": "Ты предал свою собственную расу ради... этого?", "next_dialogue": "traitor_motivation"},
            {"text": "Я не буду слушать монстра в человеческой шкуре.", "next_dialogue": "traitor_rejection"}
        ]
    },
    "entity_proposal": {
        "speaker": "Предатель (голос Сущности)",
        "text": "Присоединись к нам добровольно, и твои любимые будут в безопасности. Мы не требуем уничтожения — только... трансформации. Эволюцию, которую ваш вид неизбежно должен пройти. Ты можешь стать мостом между старым и новым.",
        "responses": [
            {"text": "Я отвергаю твоё предложение.", "effects": {"entity_deal": False}, "next_dialogue": "proposal_rejected"},
            {"text": "Что означает «трансформация»?", "next_dialogue": "transformation_details"},
            {"text": "Как я могу доверять тебе?", "next_dialogue": "trust_question"}
        ]
    },
    
    "mia_after_betrayal": {
        "speaker": "Мия",
        "text": "Мы были слишком доверчивы. После всего, что мы пережили вместе... Как я могла не заметить? Я — тактик, я должна была предусмотреть этот сценарий.",
        "responses": [
            {
                "text": "Ты не виновата. Никто не мог знать.",
                "effects": {"mia_relationship": 15},
                "next_dialogue": "mia_forgiveness"
            },
            {"text": "Используй это как урок. Будущее покажет, кого можно доверять.", "next_dialogue": "mia_lesson"},
            {"text": "Теперь мы знаем настоящего врага. Это преимущество.", "next_dialogue": "mia_advantage"}
        ]
    }
}

# === ГЛАВА 16: Пробуждение ===

CHAPTER_16_DIALOGUES = {
    "entity_mental_contact": {
        "speaker": "Сущность",
        "text": "Ты слышишь меня, маленький курьер. Я не враг. Я — эволюция. Следующий шаг. Присоединись ко мне добровольно, и твои близкие будут в безопасности. Сопротивление лишь продлит их страдания.",
        "responses": [
            {
                "text": "Ты — угроза всему живому. Я остановлю тебя любой ценой.",
                "effects": {"determination": 10, "mia_relationship": 10, "maria_relationship": 10},
                "next_dialogue": "entity_confrontation"
            },
            {"text": "Что ты такое на самом деле? Откуда пришла?", "next_dialogue": "entity_origin"},
            {"text": "Если я соглашусь, каковы гарантии?", "next_dialogue": "entity_guarantees"}
        ]
    },
    "entity_origin": {
        "speaker": "Сущность",
        "text": "Я — это то, что ждёт каждую вселенную в конце времён. Энтропия, обретшая сознание. Я не выбираю поглощение — я им являюсь. Но я могу предложить... альтернативу тем, кто готов понять.",
        "responses": [
            {"text": "Ты говоришь о конце всего. Как можно это принять?", "next_dialogue": "entity_acceptance"},
            {"text": "Есть ли способ сосуществования?", "next_dialogue": "entity_coexistence"},
            {"text": "Ты — не неизбежность. Ты — угроза, которую нужно устранить.", "next_dialogue": "entity_confrontation"}
        ]
    },
    
    "final_council": {
        "speaker": "Мия",
        "text": "Все здесь. Мы обсудили стратегии. У нас три варианта: прямая атака на якорь Сущности, перенастройка станции для договора, или... принятие предложения. Решение за тобой, капитан.",
        "responses": [
            {"text": "Мы атакуем. Изгоним Сущность любой ценой.", "effects": {"final_path": "exile"}, "next_dialogue": "council_exile"},
            {"text": "Мы попробуем договориться. Но на моих условиях.", "effects": {"final_path": "treaty"}, "next_dialogue": "council_treaty"},
            {"text": "Дайте мне время решить.", "next_dialogue": "council_wait"}
        ]
    },
    
    "romantic_preparation": {
        "speaker": "{romantic_partner}",
        "text": "Перед тем, как мы войдём туда... Я должна сказать тебе кое-что. Что бы ни случилось, я не жалею ни о чём. Каждый момент с тобой был... настоящим.",
        "responses": [
            {
                "text": "Я тоже не жалею. И мы вернёмся вместе.",
                "effects": {"romantic_relationship": 20},
                "next_dialogue": "romantic_promise"
            },
            {"text": "Мы ещё поговорим об этом после победы.", "next_dialogue": "romantic_defer"},
            {"text": "Сосредоточься на миссии. Сейчас не время.", "next_dialogue": "romantic_focused"}
        ]
    }
}

# === ГЛАВА 17: Сердце Тьмы ===

CHAPTER_17_DIALOGUES = {
    "station_entry": {
        "speaker": "Анна",
        "text": "Сенсоры показывают... это не просто станция. Она живая. Или была когда-то. Коридоры меняют конфигурацию, реагируя на наше присутствие. Это какой-то био-механический организм.",
        "responses": [
            {"text": "Можешь взломать системы?", "next_dialogue": "anna_hack"},
            {"text": "Мария, оценки состояния команды?", "next_dialogue": "maria_status"},
            {"text": "Продвигаемся осторожно. Ожидайте ловушки.", "next_dialogue": "caution_mode"}
        ]
    },
    
    "mirror_trap": {
        "speaker": "Сущность (иллюзия)",
        "text": "[Видение погибшего любимого человека] Ты не смог меня спасти... Почему ты продолжаешь бороться, когда всё равно всех потеряешь? Оставь надежду. Присоединись к нам. Здесь нет боли...",
        "responses": [
            {
                "text": "[Psychic] Это не реально. Я вижу правду.",
                "requires": {"psychic": 70},
                "next_dialogue": "mirror_break_high"
            },
            {
                "text": "[Emotional] Даже потеряв тебя, я продолжаю. Это и есть надежда.",
                "requires": {"empathy": 60},
                "next_dialogue": "mirror_break_medium"
            },
            {"text": "[Resist] Я не поддамся на твои трюки!", "next_dialogue": "mirror_break_low"}
        ]
    },
    "mirror_break_high": {
        "speaker": "Система",
        "text": "Ваша Psychic сила позволяет разорвать иллюзию без вреда для себя. Команда видит вас уверенным, и это придаёт им сил.",
        "effects": {"team_morale": 30, "mental_damage": 0}
    },
    "mirror_break_medium": {
        "speaker": "Система",
        "text": "Вы преодолеваете иллюзию через эмоциональную силу, но она оставляет след в вашей душе.",
        "effects": {"team_morale": 15, "mental_damage": 20}
    },
    "mirror_break_low": {
        "speaker": "Система",
        "text": "Иллюзия наносит ментальный урон прежде, чем вы способны сопротивляться. Но вы прорываетесь.",
        "effects": {"team_morale": 5, "mental_damage": 40}
    },
    
    "guardian_encounter": {
        "speaker": "Страж Ядра",
        "text": "Ваши учёные думают категориями добра и зла. Сущность вне этих понятий. Она — inevitability, неизбежность. Вы можете оттянуть конец, но не предотвратить его. Вопрос лишь в том, сколько жизней вы спасёте до этого момента.",
        "responses": [
            {"text": "Даже одна спасённая жизнь стоит борьбы.", "next_dialogue": "guardian_exile_path"},
            {"text": "Расскажи о возможности договора.", "next_dialogue": "guardian_treaty_path"},
            {"text": "Кто ты? Почему помогаешь нам?", "next_dialogue": "guardian_history"}
        ]
    },
    "guardian_exile_path": {
        "speaker": "Страж Ядра",
        "text": "Ты выбираешь благородный путь. Но знай: изгнание требует жертвы. Кто-то должен остаться у якоря, чтобы направить энергию. Ты готов к этому?",
        "effects": {"exile_path_unlocked": True},
        "responses": [
            {"text": "Я готов.", "next_dialogue": "guardian_acceptance"},
            {"text": "Есть ли другой способ?", "next_dialogue": "guardian_alternatives"},
            {"text": "Позволь мне обсудить с командой.", "next_dialogue": "guardian_wait"}
        ]
    },
    "guardian_treaty_path": {
        "speaker": "Страж Ядра",
        "text": "Договор возможен. Станция может быть перенастроена как канал коммуникации. Сущность получит ограниченный доступ к энергии умирающих звёзд, взамен прекратит поглощение населённых миров. Но ты станешь Хранителем — навсегда связанным с этим местом.",
        "effects": {"treaty_path_unlocked": True},
        "responses": [
            {"text": "Какие гарантии, что Сущность сдержит слово?", "next_dialogue": "guardian_guarantees"},
            {"text": "Это приемлемая цена.", "next_dialogue": "guardian_treaty_accept"},
            {"text": "Мне нужно подумать.", "next_dialogue": "guardian_wait"}
        ]
    }
}

# === ГЛАВА 18: Финал ===

CHAPTER_18_DIALOGUES = {
    "final_choice": {
        "speaker": "Сущность",
        "text": "Ты пришёл так далеко, маленький курьер. Я видела твои страхи и надежды, твою любовь и ненависть. Теперь ты стоишь на пороге решения, которое определит судьбу миллионов. Выбирай мудро — или выбирай сердцем. Иногда это одно и то же.",
        "responses": [
            {"text": "[Изгнание] Я изгоню тебя из этой реальности.", "next_dialogue": "ending_exile"},
            {"text": "[Договор] Мы можем сосуществовать. Установим границы.", "next_dialogue": "ending_treaty"},
            {"text": "[Слияние] Я принимаю твоё предложение.", "next_dialogue": "ending_merge", "requires": {"psychic": 90}}
        ]
    },
    
    "ending_exile": {
        "speaker": "Сущность",
        "text": "Ты выбираешь сопротивление. Благородно... но дорого. Кто останется у якоря? Кто пожертвует собой?",
        "responses": [
            {"text": "Я останусь.", "next_dialogue": "exile_self_sacrifice"},
            {"text": "Я найду другой способ.", "next_dialogue": "exile_alternative", "requires": {"team_loyalty": 80}},
            {"text": "Посмотрим, кто добровольно предложит помощь.", "next_dialogue": "exile_team_choice"}
        ]
    },
    "exile_self_sacrifice": {
        "speaker": "Система",
        "text": "Вы выбираете остаться, направляя энергию изгнания. Эпическая битва разворачивается в ядре станции. Сущность изгнана, но вы связаны с якорем навечно.",
        "effects": {"ending": "exile_sacrifice"}
    },
    "exile_alternative": {
        "speaker": "{romantic_partner}",
        "text": "Я не позволю тебе сделать это в одиночку. Мы разделим ношу вместе. Две души, связанные навеки — достаточно сил, чтобы выжить.",
        "effects": {"ending": "exile_together"},
        "responses": [
            {"text": "Я не могу просить тебя об этом.", "next_dialogue": "partner_insist"},
            {"text": "Если ты уверена... вместе мы справимся.", "next_dialogue": "partner_accept"}
        ]
    },
    
    "ending_treaty": {
        "speaker": "Сущность",
        "text": "Разумный выбор. Договор заключён. Я получу доступ к энергии умирающих звёзд, ты станешь Хранителем границы. Галактика будет жить... пока звёзды не погаснут сами.",
        "effects": {"ending": "treaty"},
        "responses": [
            {"text": "Я принимаю ответственность.", "next_dialogue": "treaty_accepted"}
        ]
    },
    "treaty_accepted": {
        "speaker": "Система",
        "text": "Вы перенастраиваете станцию, создавая мост между измерениями. Сущность ограничена, галактика спасена. Но вы навсегда связаны с этим местом как Хранитель Границы.",
        "effects": {"ending": "treaty_hollow_knight_style"}
    },
    
    "ending_merge": {
        "speaker": "Сущность",
        "text": "Ты единственный за миллионы лет, кто понял. Слияние не уничтожает — оно преобразует. Ты не потеряешь себя. Ты обретёшь... большее.",
        "effects": {"ending": "transcendence"},
        "responses": [
            {"text": "Я готов увидеть, что находится за гранью.", "next_dialogue": "merge_complete"}
        ]
    },
    "merge_complete": {
        "speaker": "Система",
        "text": "Ваше сознание расширяется за пределы человеческого понимания. Вы становитесь чем-то большим — хранителем эволюции, мостом между смертью и жизнью. Галактика изменилась навсегда.",
        "effects": {"ending": "transcendence"}
    },
    
    "epilogue_romantic": {
        "speaker": "{romantic_partner}",
        "text": "Куда бы ты ни пошёл, я буду рядом. Через аномалии и пустоту, через время и пространство. Ты показал мне, что значит бороться за что-то большее, чем собственное выживание. Теперь позволь мне быть твоей опорой.",
        "responses": [
            {"text": "Вместе. Теперь и всегда.", "next_dialogue": "epilogue_final"}
        ]
    },
    "epilogue_final": {
        "speaker": "Система",
        "text": "КОНЕЦ\n\nБлагодарим за прохождение Star Courier.\nВаши выборы определили судьбу галактики.\n\nПопробуйте другие пути и концовки!",
        "effects": {"game_complete": True}
    }
}

# Объединение всех диалогов
DIALOGUES_CHAPTERS_11_18 = {
    **CHAPTER_11_DIALOGUES,
    **CHAPTER_12_DIALOGUES,
    **CHAPTER_13_DIALOGUES,
    **CHAPTER_14_DIALOGUES,
    **CHAPTER_15_DIALOGUES,
    **CHAPTER_16_DIALOGUES,
    **CHAPTER_17_DIALOGUES,
    **CHAPTER_18_DIALOGUES
}

def get_dialogue(dialogue_id, game_state=None):
    """Получить диалог по ID с учётом состояния игры"""
    dialogue = DIALOGUES_CHAPTERS_11_18.get(dialogue_id)
    if not dialogue:
        return None
    
    # Подстановка переменных на основе состояния игры
    if game_state:
        text = dialogue.get("text", "")
        if "{romantic_partner}" in text:
            partner = game_state.get("romantic_partner", "партнёр")
            dialogue["text"] = text.replace("{romantic_partner}", partner)
    
    return dialogue

def check_requirements(dialogue, game_state):
    """Проверка требований для доступа к диалогу"""
    requirements = dialogue.get("requires", {})
    for stat, value in requirements.items():
        if game_state.get(stat, 0) < value:
            return False
    return True

def apply_effects(effects, game_state):
    """Применение эффектов диалога к состоянию игры"""
    if not effects:
        return game_state
    
    for stat, value in effects.items():
        current = game_state.get(stat, 0)
        game_state[stat] = current + value
    
    return game_state
