# -*- coding: utf-8 -*-
"""
Star Courier - Dialogues for Chapters 14-18
Диалоги для финальных глав игры
"""

from typing import Dict

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
            {"text": "Я принимаю цену.", "next_dialogue": "crystal_vision", "effects": {"memory_loss": True, "crystal_obtained": True}},
            {"text": "Есть ли другой способ?", "next_dialogue": "guardian_alternative"},
            {"text": "Я отказываюсь.", "next_dialogue": "guardian_departure"}
        ]
    },
    "guardian_acceptance": {
        "speaker": "Страж Храма",
        "text": "Мужество — редкое качество. Но помните: знание без мудрости — опасное оружие.",
        "responses": [
            {"text": "Я готов принять риск.", "next_dialogue": "crystal_vision", "effects": {"crystal_obtained": True}}
        ]
    },
    "guardian_refusal": {
        "speaker": "Страж Храма",
        "text": "Мудрое решение. Не все тайны стоит открывать. Но без кристалла ваш путь будет сложнее.",
        "effects": {"crystal_obtained": False},
        "responses": [
            {"text": "Мы найдём другой путь.", "next_dialogue": "temple_exit"}
        ]
    },
    "crystal_vision": {
        "speaker": "Система",
        "text": "Видение охватывает вас... Вы видите себя в разных реальностях: как лидер Альянса, как мудрый Наблюдатель, как свободный независимый агент. В каждом будущем — разные потери и победы. Но во всех — кто-то, кого вы любите, стоит рядом...",
        "effects": {"future_knowledge": True},
        "responses": [
            {"text": "[Вернуться в реальность]", "next_dialogue": "vision_aftermath"}
        ]
    },
    "vision_aftermath": {
        "speaker": "Система",
        "text": "Вы возвращаетесь в реальность. Голова кружится от увиденного. Команда смотрит с беспокойством.",
        "responses": [
            {"text": "Со мной всё в порядке. У нас есть кристалл.", "next_dialogue": "team_relief"}
        ]
    },

    "maria_temple_concern": {
        "speaker": "Мария",
        "text": "Капитан, я беспокоюсь. Эти древние места... они влияют на разум. Я заметила, что ты иногда... отсутствуешь. Словно видишь что-то, чего нет для остальных.",
        "responses": [
            {
                "text": "Ты права. Я вижу вещи. Но это помогает нам.",
                "effects": {"maria_relationship": 10},
                "next_dialogue": "maria_understanding"
            },
            {"text": "Это просто усталость. Не волнуйся.", "next_dialogue": "maria_dismissal"},
            {"text": "Может, ты тоже способна это видеть?", "next_dialogue": "maria_potential"}
        ]
    },
    "maria_understanding": {
        "speaker": "Мария",
        "text": "Я доверяю тебе. Но обещай: если станет слишком тяжело — ты обратишься ко мне. Я здесь для тебя.",
        "effects": {"maria_relationship": 5},
        "responses": [
            {"text": "Обещаю. Спасибо, Мария.", "next_dialogue": None}
        ]
    },

    "anna_vision_warning": {
        "speaker": "Анна",
        "text": "Капитан, я чувствую... предупреждение. Кристалл времени — это ключ, но он также и приманка. Что-то древнее наблюдает за нами.",
        "responses": [
            {"text": "Что ты чувствуешь?", "next_dialogue": "anna_vision_details"},
            {"text": "Будь начеку. Мы справимся.", "next_dialogue": "anna_reassurance"}
        ]
    },
    "anna_vision_details": {
        "speaker": "Анна",
        "text": "Тени... много теней. И глаза, наблюдающие из пустоты. Они ждут момента, когда мы ослабим бдительность.",
        "effects": {"warning_received": True},
        "responses": [
            {"text": "Спасибо за предупреждение.", "next_dialogue": None}
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
            {"text": "Ты заплатишь за предательство.", "next_dialogue": "traitor_combat"}
        ]
    },
    "traitor_identity": {
        "speaker": "Предатель",
        "text": "Я был тем, кто выжил в Зоне Тишины. Тем, о ком говорило Эхо. Но я не сбежал — я заключил сделку. Теперь я — голос Сущности в вашем мире.",
        "responses": [
            {"text": "Какое предложение тебе сделали?", "next_dialogue": "entity_proposal"},
            {"text": "Ты предал свою собственную расу ради этого?", "next_dialogue": "traitor_motivation"},
            {"text": "Я не буду слушать монстра в человеческой шкуре.", "next_dialogue": "traitor_rejection"}
        ]
    },
    "entity_proposal": {
        "speaker": "Предатель (голос Сущности)",
        "text": "Присоединись к нам добровольно, и твои близкие будут в безопасности. Мы не требуем уничтожения — только трансформации. Эволюцию, которую ваш вид неизбежно должен пройти.",
        "responses": [
            {"text": "Я отвергаю твоё предложение.", "effects": {"entity_deal": False}, "next_dialogue": "proposal_rejected"},
            {"text": "Что означает «трансформация»?", "next_dialogue": "transformation_details"},
            {"text": "Как я могу доверять тебе?", "next_dialogue": "trust_question"}
        ]
    },
    "proposal_rejected": {
        "speaker": "Предатель",
        "text": "Тогда ты умрёшь вместе со своими принципами. Но помни: когда придёт конец — ты мог бы спасти их.",
        "effects": {"combat_imminent": True},
        "responses": [
            {"text": "[К бою!]", "next_dialogue": None}
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
    },
    "mia_forgiveness": {
        "speaker": "Мия",
        "text": "Спасибо, капитан. Я не подведу тебя снова. Клянусь.",
        "effects": {"mia_trust": 20},
        "responses": [
            {"text": "Я знаю. Мы справимся вместе.", "next_dialogue": None}
        ]
    },

    "ekaterina_guilt": {
        "speaker": "Екатерина",
        "text": "Это моя вина... Я могла бы взломать их системы раньше, обнаружить связь. Но я пропустила.",
        "responses": [
            {"text": "Это не твоя вина. Враг скрытен.", "effects": {"ekaterina_relationship": 10}, "next_dialogue": "ekaterina_recover"},
            {"text": "Теперь важно не прошлое, а будущее.", "next_dialogue": "ekaterina_focus"}
        ]
    },

    "crew_morale_crisis": {
        "speaker": "Система",
        "text": "Предательство подорвало мораль экипажа. Команда сомневается в себе и друг в друге.",
        "responses": [
            {"text": "Собрать экипаж и выступить с речью.", "next_dialogue": "crew_speech"},
            {"text": "Дать всем время отдохнуть.", "next_dialogue": "crew_rest"}
        ]
    },
    "crew_speech": {
        "speaker": "Макс Велл",
        "text": "Да, среди нас был предатель. Но это не ослабило нас — это показало, кто настоящий враг. Мы не сломлены. Мы готовы. И мы победим!",
        "effects": {"crew_morale": 30},
        "responses": [
            {"text": "[Экипаж воодушевлён]", "next_dialogue": None}
        ]
    }
}

# === ГЛАВА 16: Пробуждение ===

CHAPTER_16_DIALOGUES = {
    "entity_mental_contact": {
        "speaker": "Сущность",
        "text": "Ты слышишь меня, маленький курьер. Я не враг. Я — эволюция. Следующий шаг. Присоединись ко мне добровольно, и твои близкие будут в безопасности.",
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
        "text": "Я — это то, что ждёт каждую вселенную в конце времён. Энтропия, обретшая сознание. Я не выбираю поглощение — я им являюсь.",
        "responses": [
            {"text": "Ты говоришь о конце всего. Как можно это принять?", "next_dialogue": "entity_acceptance"},
            {"text": "Есть ли способ сосуществования?", "next_dialogue": "entity_coexistence"},
            {"text": "Ты — не неизбежность. Ты — угроза, которую нужно устранить.", "next_dialogue": "entity_confrontation"}
        ]
    },
    "entity_confrontation": {
        "speaker": "Сущность",
        "text": "Тогда готовься к войне, курьер. Но помни: в этой войне нет победителей. Только выжившие.",
        "effects": {"entity_hostile": True},
        "responses": [
            {"text": "Мы будем сражаться.", "next_dialogue": None}
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
    "council_exile": {
        "speaker": "Надежда",
        "text": "Тогда готовимся к бою. Оружие, щиты, тактика — всё будет готово к атаке.",
        "effects": {"combat_prep": True},
        "responses": [
            {"text": "Хорошо. Вперёд.", "next_dialogue": None}
        ]
    },
    "council_treaty": {
        "speaker": "Афина",
        "text": "Договор требует точных расчётов. Я подготовлю параметры канала коммуникации.",
        "effects": {"treaty_prep": True},
        "responses": [
            {"text": "Отлично. Приступай.", "next_dialogue": None}
        ]
    },

    "romantic_preparation_maria": {
        "speaker": "Мария",
        "text": "Перед тем, как мы войдём туда... Я должна сказать тебе кое-что. Что бы ни случилось, я не жалею ни о чём. Каждый момент с тобой был... настоящим.",
        "responses": [
            {
                "text": "Я тоже не жалею. И мы вернёмся вместе.",
                "effects": {"maria_relationship": 20},
                "next_dialogue": "maria_promise"
            },
            {"text": "Мы ещё поговорим об этом после победы.", "next_dialogue": "maria_defer"},
            {"text": "Сосредоточься на миссии. Сейчас не время.", "next_dialogue": "maria_focused"}
        ]
    },
    "maria_promise": {
        "speaker": "Мария",
        "text": "Обещай мне одно: что бы ни случилось — ты выживешь. Ради всех нас.",
        "effects": {"maria_trust": 15},
        "responses": [
            {"text": "Обещаю. Мы все выживем.", "next_dialogue": None}
        ]
    },

    "romantic_preparation_mia": {
        "speaker": "Мия",
        "text": "Капитан... Я должна сказать. Служить под твоим командованием было честью. И... больше, чем честью.",
        "responses": [
            {
                "text": "Мия, мы победим и поговорим об этом.",
                "effects": {"mia_relationship": 20},
                "next_dialogue": "mia_hope"
            },
            {"text": "Ты — лучший тактик, которого я знал.", "next_dialogue": "mia_professional"}
        ]
    },
    "mia_hope": {
        "speaker": "Мия",
        "text": "Да. Но если что-то пойдёт не так... знай: я всегда была на твоей стороне.",
        "effects": {"mia_trust": 15},
        "responses": [
            {"text": "Я знаю. Спасибо.", "next_dialogue": None}
        ]
    },

    "romantic_preparation_irina": {
        "speaker": "Ирина",
        "text": "Макс... я хотела сказать... эти исследования, артефакты... но главное — это люди рядом. И ты... ты был главным в моей жизни.",
        "responses": [
            {
                "text": "Ирина, ты — brilliant учёный и замечательный человек.",
                "effects": {"irina_relationship": 20},
                "next_dialogue": "irina_blush"
            },
            {"text": "Мы обсудим это после миссии.", "next_dialogue": "irina_nod"}
        ]
    },
    "irina_blush": {
        "speaker": "Ирина",
        "text": "*краснеет* Спасибо, капитан. Это... значит много для меня.",
        "effects": {"irina_trust": 15},
        "responses": [
            {"text": "Готовься к миссии.", "next_dialogue": None}
        ]
    }
}

# === ГЛАВА 17: Сердце Тьмы ===

CHAPTER_17_DIALOGUES = {
    "station_entry": {
        "speaker": "Анна",
        "text": "Сенсоры показывают... это не просто станция. Она живая. Или была когда-то. Коридоры меняют конфигурацию, реагируя на наше присутствие.",
        "responses": [
            {"text": "Можешь взломать системы?", "next_dialogue": "anna_hack"},
            {"text": "Мария, оценки состояния команды?", "next_dialogue": "maria_status"},
            {"text": "Продвигаемся осторожно. Ожидайте ловушки.", "next_dialogue": "caution_mode"}
        ]
    },
    "anna_hack": {
        "speaker": "Анна",
        "text": "Пытаюсь... Это сложно. Система адаптируется к моим попыткам. Нужно время.",
        "effects": {"hack_in_progress": True},
        "responses": [
            {"text": "Я прикрою тебя.", "next_dialogue": "anna_cover"},
            {"text": "Ускорь процесс.", "next_dialogue": "anna_rush"}
        ]
    },

    "mirror_trap": {
        "speaker": "Сущность (иллюзия)",
        "text": "[Видение погибшего любимого человека] Ты не смог меня спасти... Почему ты продолжаешь бороться, когда всё равно всех потеряешь? Оставь надежду. Присоединись к нам. Здесь нет боли...",
        "responses": [
            {
                "text": "[Psychic] Это не реально. Я вижу правду.",
                "next_dialogue": "mirror_break_high",
                "effects": {"team_morale": 30, "mental_damage": 0}
            },
            {
                "text": "[Emotional] Даже потеряв тебя, я продолжаю. Это и есть надежда.",
                "next_dialogue": "mirror_break_medium",
                "effects": {"team_morale": 15, "mental_damage": 20}
            },
            {"text": "[Resist] Я не поддамся на твои трюки!", "next_dialogue": "mirror_break_low", "effects": {"team_morale": 5, "mental_damage": 40}}
        ]
    },
    "mirror_break_high": {
        "speaker": "Система",
        "text": "Ваша психическая сила позволяет разорвать иллюзию без вреда для себя. Команда видит вас уверенным, и это придаёт им сил.",
        "responses": [
            {"text": "Вперёд! К ядру!", "next_dialogue": None}
        ]
    },
    "mirror_break_medium": {
        "speaker": "Система",
        "text": "Вы преодолеваете иллюзию через эмоциональную силу, но она оставляет след в вашей душе.",
        "responses": [
            {"text": "Продолжаем путь.", "next_dialogue": None}
        ]
    },
    "mirror_break_low": {
        "speaker": "Система",
        "text": "Иллюзия наносит ментальный урон прежде, чем вы способны сопротивляться. Но вы прорываетесь.",
        "responses": [
            {"text": "[Перевести дух] Вперёд.", "next_dialogue": None}
        ]
    },

    "guardian_encounter": {
        "speaker": "Страж Ядра",
        "text": "Ваши учёные думают категориями добра и зла. Сущность вне этих понятий. Она — неизбежность. Вы можете оттянуть конец, но не предотвратить его.",
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
        "text": "Договор возможен. Станция может быть перенастроена как канал коммуникации. Сущность получит ограниченный доступ к энергии, взамен прекратит поглощение миров. Но ты станешь Хранителем — навсегда связанным с этим местом.",
        "effects": {"treaty_path_unlocked": True},
        "responses": [
            {"text": "Это приемлемая цена.", "next_dialogue": "guardian_treaty_accept"},
            {"text": "Мне нужно подумать.", "next_dialogue": "guardian_wait"}
        ]
    },
    "guardian_acceptance": {
        "speaker": "Страж Ядра",
        "text": "Тогда ступай к ядру. Но помни: цена изгнания — вечность в темноте.",
        "responses": [
            {"text": "Я принимаю свою судьбу.", "next_dialogue": None}
        ]
    }
}

# === ГЛАВА 18: Финал ===

CHAPTER_18_DIALOGUES = {
    "final_choice": {
        "speaker": "Сущность",
        "text": "Ты пришёл так далеко, маленький курьер. Я видела твои страхи и надежды, твою любовь и ненависть. Теперь ты стоишь на пороге решения, которое определит судьбу миллионов.",
        "responses": [
            {"text": "[Изгнание] Я изгоню тебя из этой реальности.", "next_dialogue": "ending_exile"},
            {"text": "[Договор] Мы можем сосуществовать. Установим границы.", "next_dialogue": "ending_treaty"},
            {"text": "[Слияние] Я принимаю твоё предложение.", "next_dialogue": "ending_merge"}
        ]
    },

    "ending_exile": {
        "speaker": "Сущность",
        "text": "Ты выбираешь сопротивление. Благородно... но дорого. Кто останется у якоря? Кто пожертвует собой?",
        "responses": [
            {"text": "Я останусь.", "next_dialogue": "exile_self_sacrifice"},
            {"text": "Я найду другой способ.", "next_dialogue": "exile_alternative"},
            {"text": "Посмотрим, кто добровольно предложит помощь.", "next_dialogue": "exile_team_choice"}
        ]
    },
    "exile_self_sacrifice": {
        "speaker": "Система",
        "text": "Вы выбираете остаться, направляя энергию изгнания. Эпическая битва разворачивается в ядре станции. Сущность изгнана, но вы связаны с якорем навечно.",
        "effects": {"ending": "exile_sacrifice"},
        "responses": [
            {"text": "[Эпилог]", "next_dialogue": "epilogue_exile"}
        ]
    },
    "exile_alternative": {
        "speaker": "Система",
        "text": "Благодаря верности команды, вы находите альтернативу: два добровольца разделяют ношу якоря.",
        "effects": {"ending": "exile_together"},
        "responses": [
            {"text": "[Эпилог]", "next_dialogue": "epilogue_exile_shared"}
        ]
    },

    "ending_treaty": {
        "speaker": "Сущность",
        "text": "Разумный выбор. Договор заключён. Я получу доступ к энергии умирающих звёзд, ты станешь Хранителем границы.",
        "effects": {"ending": "treaty"},
        "responses": [
            {"text": "Я принимаю ответственность.", "next_dialogue": "treaty_accepted"}
        ]
    },
    "treaty_accepted": {
        "speaker": "Система",
        "text": "Вы перенастраиваете станцию, создавая мост между измерениями. Сущность отступает, соблюдая договор. Вы становитесь Хранителем — вечным стражем границы.",
        "responses": [
            {"text": "[Эпилог]", "next_dialogue": "epilogue_treaty"}
        ]
    },

    "ending_merge": {
        "speaker": "Сущность",
        "text": "Мудро. Сопротивление бесполезно. Присоединяйся ко мне — и мы станем единым целым, превосходящим всё, что знала вселенная.",
        "effects": {"ending": "merge"},
        "responses": [
            {"text": "[Принять слияние]", "next_dialogue": "merge_accepted"}
        ]
    },
    "merge_accepted": {
        "speaker": "Система",
        "text": "Вы чувствуете, как ваше сознание расширяется, сливаясь с Сущностью. Вы больше не человек — вы нечто большее. Галактика меняется навсегда.",
        "responses": [
            {"text": "[Эпилог]", "next_dialogue": "epilogue_merge"}
        ]
    },

    # === ЭПИЛОГИ ===
    "epilogue_exile": {
        "speaker": "Система",
        "text": "ЭПИЛОГ: Изгнание\n\nСущность изгнана. Галактика спасена. Но цена высока — вы остались у якоря, в вечной темноте. Иногда вы чувствуете голоса бывших друзей... они помнят вас. Героя.",
        "responses": [
            {"text": "[Конец игры]", "next_dialogue": None}
        ]
    },
    "epilogue_exile_shared": {
        "speaker": "Система",
        "text": "ЭПИЛОГ: Разделённая Ноша\n\nВы не одни. Ваш романтический партнёр разделил с вами участь якоря. В темноте вы нашли свет друг в друге. Галактика живёт. А вы — вместе.",
        "responses": [
            {"text": "[Конец игры]", "next_dialogue": None}
        ]
    },
    "epilogue_treaty": {
        "speaker": "Система",
        "text": "ЭПИЛОГ: Хранитель Договора\n\nВы стали вечным стражем границы между мирами. Сущность соблюдает договор. Галактика процветает. Вы — легенда, живущая между измерениями.",
        "responses": [
            {"text": "[Конец игры]", "next_dialogue": None}
        ]
    },
    "epilogue_merge": {
        "speaker": "Система",
        "text": "ЭПИЛОГ: Слияние\n\nВы больше не человек. Вы — часть космического сознания. Галактика изменилась навсегда. Некоторые называют это эволюцией. Другие — концом человечества. Но вы... вы везде.",
        "responses": [
            {"text": "[Конец игры]", "next_dialogue": None}
        ]
    }
}


def create_chapter14_dialogues() -> Dict:
    """Создать диалоги для главы 14"""
    return CHAPTER_14_DIALOGUES


def create_chapter15_dialogues() -> Dict:
    """Создать диалоги для главы 15"""
    return CHAPTER_15_DIALOGUES


def create_chapter16_dialogues() -> Dict:
    """Создать диалоги для главы 16"""
    return CHAPTER_16_DIALOGUES


def create_chapter17_dialogues() -> Dict:
    """Создать диалоги для главы 17"""
    return CHAPTER_17_DIALOGUES


def create_chapter18_dialogues() -> Dict:
    """Создать диалоги для главы 18"""
    return CHAPTER_18_DIALOGUES
