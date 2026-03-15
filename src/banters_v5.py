# -*- coding: utf-8 -*-
"""
Star Courier - Character Banters System
Система бантеров между персонажами для оживления путешествий
"""

# === ТИПЫ БАНТЕРОВ ===

BANTER_TYPES = {
    "travel": "Бантеры во время путешествия",
    "rest": "Бантеры во время отдыха",
    "combat_after": "Бантеры после боя",
    "location_specific": "Бантеры в определённых локациях",
    "event_reaction": "Реакции на события",
    "personal": "Личные разговоры",
    "romantic": "Романтические моменты",
    "tension": "Напряжённые моменты"
}

# === БАНТЕРЫ МЕЖДУ ПЕРСОНАЖАМИ ===

CHARACTER_BANTERS = {
    # === МИЯ И МАРИЯ ===
    "mia_maría_travel_1": {
        "id": "banter_mia_mar_01",
        "characters": ["mia", "maria"],
        "type": "travel",
        "trigger": {"random_chance": 0.1, "chapter": range(4, 18)},
        "scene": {
            "location": "ship_interior",
            "dialogues": [
                {"speaker": "mia", "text": "Мария, у тебя есть минута? Я analysирую паттерны снабжения наших миссий."},
                {"speaker": "maria", "text": "Конечно, Мия. Что тебя беспокоит?"},
                {"speaker": "mia", "text": "Медицинские расходы на 15% выше расчётных. Ты... используешь что-то, о чём мне стоит знать?"},
                {"speaker": "maria", "text": "Я лечу людей, Мия. Не всё можно predict через твои таблицы."},
                {"speaker": "mia", "text": "Я не критикую. Я пытаюсь оптимизировать, чтобы у тебя было достаточно ресурсов."},
                {"speaker": "maria", "text": "...Извини. Я привыкла защищаться. Спасибо за заботу."},
                {"speaker": "mia", "text": "Это не забота. Это... эффективность. Взаимовыгодная эффективность."}
            ]
        },
        "effects": {"mia_relationship": 2, "maria_relationship": 2}
    },
    
    "mia_maría_rest_1": {
        "id": "banter_mia_mar_02",
        "characters": ["mia", "maria"],
        "type": "rest",
        "trigger": {"random_chance": 0.08, "location": "observation_deck"},
        "scene": {
            "dialogues": [
                {"speaker": "narrator", "text": "Мия находит Марию на смотровой площадке, смотрящей на звёзды."},
                {"speaker": "mia", "text": "Не могу спать. Слишком много переменных для processing."},
                {"speaker": "maria", "text": "Присоединяйся. Иногда... просто смотреть на звёзды помогает."},
                {"speaker": "mia", "text": "Ты считаешь это... терапевтичным?"},
                {"speaker": "maria", "text": "Я считаю это напоминанием о том, что некоторые вещи больше нас. И это... утешает."},
                {"speaker": "narrator", "text": "Мия садится рядом. Долгое молчание."},
                {"speaker": "mia", "text": "...Спасибо. Это... переменная, которую я не учитывала."}
            ]
        },
        "effects": {"mia_relationship": 5, "maria_relationship": 5}
    },
    
    # === МИЯ И АННА ===
    "mia_anna_travel_1": {
        "id": "banter_mia_ann_01",
        "characters": ["mia", "anna"],
        "type": "travel",
        "trigger": {"random_chance": 0.1, "chapter": range(5, 18)},
        "scene": {
            "dialogues": [
                {"speaker": "mia", "text": "Анна, твои карты. Они... неточны."},
                {"speaker": "anna", "text": "Они точны настолько, насколько возможно. Туманности постоянно меняются."},
                {"speaker": "mia", "text": "Это создаёт неопределённость в моих расчётах. Мне не нравится неопределённость."},
                {"speaker": "anna", "text": "Добро пожаловать в реальность, Мия. Не всё можно предсказать."},
                {"speaker": "mia", "text": "Всё МОЖНО предсказать. Вопрос в данных."},
                {"speaker": "anna", "text": "А если данные... чувствуют? Если пространство само решает, что показать?"},
                {"speaker": "mia", "text": "...Ты говоришь загадками. Это... неэффективно."},
                {"speaker": "anna", "text": "Я говорю правдой. Просто ты ещё не готова её услышать."}
            ]
        },
        "effects": {"mia_relationship": 1, "anna_relationship": 2}
    },
    
    "mia_anna_tension_1": {
        "id": "banter_mia_ann_02",
        "characters": ["mia", "anna"],
        "type": "tension",
        "trigger": {"event": "entity_contact", "chapter": range(10, 18)},
        "scene": {
            "dialogues": [
                {"speaker": "mia", "text": "Анна, после того, как ты активировала те врата... ты изменилась."},
                {"speaker": "anna", "text": "Мы все изменились после того, как узнали о Сущности."},
                {"speaker": "mia", "text": "Ты знаешь что-то, чего не говоришь. Я вижу это в твоих данных."},
                {"speaker": "anna", "text": "Некоторые знания... опасны, Мия. Не потому, что они ложны — потому, что они правда."},
                {"speaker": "mia", "text": "Информация должна быть доступна для анализа. Скрытие — это... угроза."},
                {"speaker": "anna", "text": "Или защита. От тех, кто не готов понять."},
                {"speaker": "narrator", "text": "Напряжённое молчание. Две женщины смотрят друг на друга, каждая со своей правдой."}
            ]
        },
        "effects": {}
    },
    
    # === МАРИЯ И ВЕРОНИКА ===
    "maria_veronica_travel_1": {
        "id": "banter_mar_ver_01",
        "characters": ["maria", "veronica"],
        "type": "travel",
        "trigger": {"random_chance": 0.1, "chapter": range(7, 18)},
        "scene": {
            "dialogues": [
                {"speaker": "maria", "text": "Вероника, у меня к тебе вопрос. Профессиональный."},
                {"speaker": "veronica", "text": "Спрашивай. Хотя ответы стоят денег."},
                {"speaker": "maria", "text": "Ты знаешь что-нибудь о синдроме хронической боли? И методах... нестандартного лечения?"},
                {"speaker": "veronica", "text": "...Зависит от того, кто спрашивает. И почему."},
                {"speaker": "maria", "text": "Это... для исследования. Научный интерес."},
                {"speaker": "veronica", "text": "Мария, я продаю информацию, не покупаю наивные оправдания. Если тебе нужна помощь — скажи прямо."},
                {"speaker": "narrator", "text": "Мария молчит, потом тихо кивает."},
                {"speaker": "maria", "text": "...Да. Мне нужна помощь. Но я не хочу, чтобы капитан знал."},
                {"speaker": "veronica", "text": "Договорились. Но за это ты расскажешь мне, что на самом деле произошло на Тариусе-4."}
            ]
        },
        "effects": {"maria_relationship": 3, "veronica_relationship": 3},
        "flags": {"veronica_knows_maria_pain": True}
    },
    
    # === СЕРГЕЙ И ДМИТРИЙ ===
    "sergey_dmitry_travel_1": {
        "id": "banter_srg_dm_01",
        "characters": ["sergey", "dmitry"],
        "type": "travel",
        "trigger": {"random_chance": 0.15, "chapter": range(4, 18)},
        "scene": {
            "dialogues": [
                {"speaker": "dmitry", "text": "Сергей, ты слышал эту вибрацию в двигателе на 15% мощности?"},
                {"speaker": "sergey", "text": "Слышал. Уже исправил. Третий подшипник в системе охлаждения."},
                {"speaker": "dmitry", "text": "Я думал, это резонанс от гравитационного компенсатора."},
                {"speaker": "sergey", "text": "Ты перепроверяешь мою работу?"},
                {"speaker": "dmitry", "text": "Я пилот. Моя жизнь зависит от твоих систем. Да, перепроверяю."},
                {"speaker": "sergey", "text": "Хорошо. Я бы тоже перепроверял. Но третий подшипник — проверено."},
                {"speaker": "dmitry", "text": "...Спасибо. За то, что не обиделся."},
                {"speaker": "sergey", "text": "Обижаться на паранойю пилота? Это как обижаться на гравитацию. Бесполезно."}
            ]
        },
        "effects": {"sergey_relationship": 2, "dmitry_relationship": 2}
    },
    
    "sergey_dmitry_combat_1": {
        "id": "banter_srg_dm_02",
        "characters": ["sergey", "dmitry"],
        "type": "combat_after",
        "trigger": {"event": "ship_combat_win"},
        "scene": {
            "dialogues": [
                {"speaker": "dmitry", "text": "Тот маневр с бочкой! Ты видел, как щиты мигнули?"},
                {"speaker": "sergey", "text": "Видел. И видел, как ты перегрузил маневровые при выходе."},
                {"speaker": "dmitry", "text": "Это было необходимо! Они целились в reactors!"},
                {"speaker": "sergey", "text": "Я знаю. Поэтому я перераспределил энергию в последний момент."},
                {"speaker": "dmitry", "text": "...Ты это сделал? Я думал, система сама..."},
                {"speaker": "sergey", "text": "Система не думает. Думаю я. Вот почему мы ещё живы."},
                {"speaker": "dmitry", "text": "Ладно, ладно. Ты гений. Я — простой пилот, который просто спас нам жизни."},
                {"speaker": "sergey", "text": "...Командная работа. Это называется командная работа."}
            ]
        },
        "effects": {"sergey_relationship": 3, "dmitry_relationship": 3}
    },
    
    # === ЗАРА И КУРЬЕР (НЕЙТРАЛЬНЫЙ) ===
    "zara_player_travel_1": {
        "id": "banter_zara_pl_01",
        "characters": ["zara"],
        "type": "travel",
        "trigger": {"random_chance": 0.08, "chapter": range(8, 18), "zara_relationship_min": 20},
        "scene": {
            "dialogues": [
                {"speaker": "narrator", "text": "Зара появляется рядом с вами в коридоре, двигаясь бесшумно."},
                {"speaker": "zara", "text": "Ты не спишь. Я чувствую твоё беспокойство."},
                {"speaker": "player", "text": "Многое происходит. Сложно отключиться."},
                {"speaker": "zara", "text": "Ты несёшь груз, который не обязан нести в одиночку."},
                {"speaker": "player", "text": "Это мой корабль. Моя команда. Моя ответственность."},
                {"speaker": "zara", "text": "...Гордость. Она может быть силой и слабостью одновременно. Я видела, как гордость погубила лучших."},
                {"speaker": "narrator", "text": "Она касается вашего плеча — жест одновременно утешительный и древний."},
                {"speaker": "zara", "text": "Ты не один. Помни это, когда тьма кажется непреодолимой."}
            ]
        },
        "effects": {"zara_relationship": 5, "psychic": 1}
    },
    
    # === КИРА И РАЙНЕР ===
    "kira_rainer_travel_1": {
        "id": "banter_kir_rain_01",
        "characters": ["kira", "rainer"],
        "type": "travel",
        "trigger": {"random_chance": 0.12, "chapter": range(7, 18)},
        "scene": {
            "dialogues": [
                {"speaker": "kira", "text": "Райнер, помнишь ту гонку на Новая Япония? Когда я обогнала тебя на финальном повороте?"},
                {"speaker": "rainer", "text": "Я позволил тебе победить."},
                {"speaker": "kira", "text": "Конечно позволил. Именно поэтому ты три месяца дулся."},
                {"speaker": "rainer", "text": "Я не дулся. Я... анализировал свои ошибки."},
                {"speaker": "kira", "text": "Анализировал ошибки? Ты? Это же я аналитик в нашей паре!"},
                {"speaker": "rainer", "text": "Именно. Поэтому ты пилот, а я — тот, кто прикрывает твою спину, когда ты делаешь что-то безумное."},
                {"speaker": "kira", "text": "...Это было спасибо? Райнер, ты научился говорить спасибо?"},
                {"speaker": "rainer", "text": "Не привыкай. Это разовая акция."}
            ]
        },
        "effects": {"kira_relationship": 2}
    },
    
    # === ВЕРОНИКА И ЗАРА ===
    "veronica_zara_tension_1": {
        "id": "banter_ver_zar_01",
        "characters": ["veronica", "zara"],
        "type": "tension",
        "trigger": {"random_chance": 0.06, "chapter": range(8, 18)},
        "scene": {
            "dialogues": [
                {"speaker": "veronica", "text": "Ты наблюдала за мной. Я чувствую."},
                {"speaker": "zara", "text": "Я наблюдаю за всеми. Это моя природа."},
                {"speaker": "veronica", "text": "Не пихай мне эту «природу Наблюдателя». Я знаю, когда за мной следят с конкретной целью."},
                {"speaker": "zara", "text": "...Ты продаёшь секреты. Секреты, которые могут погубить невинных."},
                {"speaker": "veronica", "text": "Я продаю информацию. Что с ней делают — не моя проблема."},
                {"speaker": "zara", "text": "Это и есть проблема. Ты отказываешься от ответственности."},
                {"speaker": "veronica", "text": "И что ты собираешься делать? Судить меня по законам твоего древнего Ордена?"},
                {"speaker": "zara", "text": "Нет. Я буду наблюдать. И когда твой выбор приведёт к последствиям — я буду готова."},
                {"speaker": "narrator", "text": "Напряжённое молчание. Две женщины — одна древняя, одна потерянная — смотрят друг на друга."}
            ]
        },
        "effects": {}
    },
    
    # === РОМАНТИЧЕСКИЕ БАНТЕРЫ ===
    "mia_romantic_1": {
        "id": "banter_mia_rom_01",
        "characters": ["mia"],
        "type": "romantic",
        "trigger": {"mia_relationship_min": 70, "romantic_partner": "mia", "location": "observation_deck"},
        "scene": {
            "dialogues": [
                {"speaker": "narrator", "text": "Вы находите Мию на смотровой площадке, смотрящей на звёзды."},
                {"speaker": "mia", "text": "Капитан. Я... искала вас. То есть, не искала — вычислила наиболее вероятное местоположение."},
                {"speaker": "player", "text": "И какое оно?"},
                {"speaker": "mia", "text": "...Здесь. С вами. Это... переменная, которую я не могу объяснить. Мои алгоритмы не работают, когда вы рядом."},
                {"speaker": "narrator", "text": "Она поворачивается к вам, и в её глазах — что-то, что не укладывается в формулы."},
                {"speaker": "mia", "text": "Я думала, что контролирую всё. Что всё можно просчитать. Но когда я думаю о вас... Я теряюсь. И это... пугает. И... нравится одновременно."},
                {"speaker": "narrator", "text": "Она берёт вас за руку — жест неуверенный, почти пугающий для обычно собранной Мии."}
            ]
        },
        "effects": {"mia_relationship": 10},
        "flags": {"mia_romantic_moment": True}
    },
    
    "maria_romantic_1": {
        "id": "banter_mar_rom_01",
        "characters": ["maria"],
        "type": "romantic",
        "trigger": {"maria_relationship_min": 70, "romantic_partner": "maria", "location": "medbay"},
        "scene": {
            "dialogues": [
                {"speaker": "narrator", "text": "Мария проверяет ваше состояние после миссии. Её руки задерживаются дольше, чем необходимо."},
                {"speaker": "maria", "text": "Вы... в порядке. Никаких серьёзных повреждений."},
                {"speaker": "player", "text": "Спасибо, Мария. За всё."},
                {"speaker": "maria", "text": "Это моя работа. Лечить людей."},
                {"speaker": "player", "text": "Это больше, чем работа. Ты заботишься о каждом из нас."},
                {"speaker": "maria", "text": "...Кто-то должен. Я не могу позволить себе потерять ещё кого-то."},
                {"speaker": "narrator", "text": "Её голос дрожит. Она отводит взгляд."},
                {"speaker": "maria", "text": "Особенно... тебя. Я не думала, что смогу снова кого-то впустить. После всего. Но ты... ты сломал мои стены."},
                {"speaker": "narrator", "text": "Она касается вашего лица, её глаза блестят от невыплаканных слёз."},
                {"speaker": "maria", "text": "Обещай мне... что будешь осторожен. Я не переживу ещё одну потерю."}
            ]
        },
        "effects": {"maria_relationship": 10},
        "flags": {"maria_romantic_moment": True}
    },
    
    "zara_romantic_1": {
        "id": "banter_zar_rom_01",
        "characters": ["zara"],
        "type": "romantic",
        "trigger": {"zara_relationship_min": 70, "romantic_partner": "zara", "chapter": range(12, 18)},
        "scene": {
            "dialogues": [
                {"speaker": "narrator", "text": "Зара находит вас в коридоре. Её обычное спокойствие нарушено чем-то... уязвимым."},
                {"speaker": "zara", "text": "Ты бодрствуешь. Как и я."},
                {"speaker": "player", "text": "Не могу спать. Слишком много мыслей."},
                {"speaker": "zara", "text": "За тысячи лет я видела многое. Но есть вещи, которые... не становятся проще."},
                {"speaker": "narrator", "text": "Она смотрит на вас со странной интенсивностью."},
                {"speaker": "zara", "text": "Я думала, что закрыла своё сердце. Что оно умерло вместе с ним, тысячелетия назад. Но когда я смотрю на тебя... Я слышу, как оно бьётся снова."},
                {"speaker": "player", "text": "Зара..."},
                {"speaker": "zara", "text": "Не говори ничего. Просто... позволь мне побыть рядом. Этого достаточно. Этого больше, чем я надеялась."}
            ]
        },
        "effects": {"zara_relationship": 10},
        "flags": {"zara_romantic_moment": True}
    }
}

# === ЛОКАЦИОННЫЕ БАНТЕРЫ ===

LOCATION_BANTERS = {
    "stranger_ship_bridge": {
        "id": "loc_banter_bridge",
        "location": "bridge",
        "characters": ["mia", "anna"],
        "trigger": {"location": "bridge", "random_chance": 0.1},
        "scene": {
            "dialogues": [
                {"speaker": "anna", "text": "Знаешь, каждый раз когда я смотрю на эти звёзды, я вижу новые маршруты."},
                {"speaker": "mia", "text": "И каждый раз я вижу те же звёзды, но другие риски. Твой оптимизм... раздражает."},
                {"speaker": "anna", "text": "А твой пессимизм — обедняет. Звёзды — это возможности, Мия. Не угрозы."},
                {"speaker": "mia", "text": "Возможности БЫТЬ угрозами. Но... возможно, баланс необходим."}
            ]
        }
    },
    
    "stranger_ship_medbay": {
        "id": "loc_banter_medbay",
        "location": "medbay",
        "characters": ["maria"],
        "trigger": {"location": "medbay", "random_chance": 0.1},
        "scene": {
            "dialogues": [
                {"speaker": "maria", "text": "Ты зашёл проверить меня? Или за лекарствами?"},
                {"speaker": "narrator", "text": "Она продолжает работу, не поднимая головы."},
                {"speaker": "player", "text": "Просто хотел узнать, как ты."},
                {"speaker": "maria", "text": "...Никто раньше не спрашивал. Обычно все приходят только когда им что-то нужно."},
                {"speaker": "narrator", "text": "На мгновение её руки замирают. Потом она поворачивается с лёгкой улыбкой."},
                {"speaker": "maria", "text": "Я в порядке. Спасибо. За то, что спросил."}
            ]
        },
        "effects": {"maria_relationship": 3}
    }
}

# === ФУНКЦИИ ===

def get_random_banter(game_state):
    """Получить случайный бантер на основе состояния игры"""
    import random
    
    available_banters = []
    
    for banter_id, banter in CHARACTER_BANTERS.items():
        if check_banter_trigger(banter, game_state):
            available_banters.append(banter)
    
    if available_banters:
        return random.choice(available_banters)
    return None

def check_banter_trigger(banter, game_state):
    """Проверить триггер бантера"""
    trigger = banter.get("trigger", {})
    
    for key, value in trigger.items():
        if key == "random_chance":
            import random
            if random.random() > value:
                return False
        elif key == "chapter":
            if game_state.get("current_chapter", 1) not in value:
                return False
        elif key == "location":
            if game_state.get("current_location") != value:
                return False
        elif key == "event":
            if game_state.get("last_event") != value:
                return False
        elif key == "mia_relationship_min":
            if game_state.get("relationships", {}).get("mia", 0) < value:
                return False
        elif key == "maria_relationship_min":
            if game_state.get("relationships", {}).get("maria", 0) < value:
                return False
        elif key == "zara_relationship_min":
            if game_state.get("relationships", {}).get("zara", 0) < value:
                return False
        elif key == "romantic_partner":
            if game_state.get("romantic_partner") != value:
                return False
    
    return True

def get_banter_by_characters(char1, char2, game_state):
    """Получить бантер между двумя персонажами"""
    available = []
    
    for banter_id, banter in CHARACTER_BANTERS.items():
        characters = banter.get("characters", [])
        
        if len(characters) == 2 and char1 in characters and char2 in characters:
            if check_banter_trigger(banter, game_state):
                available.append(banter)
        elif len(characters) == 1 and (char1 in characters or char2 in characters):
            if check_banter_trigger(banter, game_state):
                available.append(banter)
    
    import random
    return random.choice(available) if available else None

def get_location_banter(location_id, game_state):
    """Получить бантер для локации"""
    available = []
    
    for banter_id, banter in LOCATION_BANTERS.items():
        if banter.get("location") == location_id:
            if check_banter_trigger(banter, game_state):
                available.append(banter)
    
    import random
    return random.choice(available) if available else None
