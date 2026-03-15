# -*- coding: utf-8 -*-
"""
Star Courier - Random Events System
Система случайных событий для разнообразия геймплея
"""

import random

# === КОСМИЧЕСКИЕ СОБЫТИЯ ===

SPACE_EVENTS = {
    "distress_signal": {
        "id": "event_space_01",
        "name": "Сигнал бедствия",
        "description": "Вы обнаруживаете аварийный сигнал с повреждённого корабля.",
        "type": "space",
        "rarity": "common",
        "chapters": range(1, 16),
        "trigger": {"travel": True, "random_chance": 0.15},
        "scene": {
            "description": "Датчики засекают слабый сигнал бедствия с небольшого судна в астероидном поле.",
            "dialogues": [
                {"speaker": "anna", "text": "Капитан, засекла аварийный сигнал. Корабль торгового класса, повреждения двигателей. Жизненные показатели... неопределённые."},
                {"speaker": "mia", "text": "Это может быть ловушка пиратов. Рекомендую осторожность."}
            ]
        },
        "choices": [
            {
                "text": "Ответить на сигнал и помочь",
                "effects": {"credits": 500, "reputation": 10},
                "risk": {"trap_chance": 0.3, "trap_event": "pirate_ambush"}
            },
            {
                "text": "Отправить дрон для разведки",
                "effects": {"intel": 5},
                "requirements": {"tech": 30}
            },
            {
                "text": "Игнорировать — у нас своя миссия",
                "effects": {"reputation": -5, "determination": 2}
            }
        ]
    },
    
    "anomaly_discovery": {
        "id": "event_space_02",
        "name": "Неизвестная аномалия",
        "description": "Датчики засекают странное энергетическое образование.",
        "type": "space",
        "rarity": "uncommon",
        "chapters": range(6, 18),
        "trigger": {"travel": True, "random_chance": 0.08, "resonance_level_min": 1},
        "scene": {
            "description": "Пространство впереди искажается странным образом — нечто вроде пространственного разрыва.",
            "dialogues": [
                {"speaker": "sergey", "text": "Капитан, это не похоже ни на что из того, что я видел. Показания зашкаливают."},
                {"speaker": "narrator", "text": "Вы чувствуете странное притяжение — резонанс с аномалией."}
            ]
        },
        "choices": [
            {
                "text": "[Resonance] Исследовать аномалию",
                "effects": {"resonance_experience": 20, "rare_material": 1},
                "requirements": {"resonance_level": 2}
            },
            {
                "text": "Обойти стороной — слишком опасно",
                "effects": {}
            },
            {
                "text": "Собрать данные дистанционно",
                "effects": {"knowledge": 10}
            }
        ]
    },
    
    "merchant_convoy": {
        "id": "event_space_03",
        "name": "Торговый конвой",
        "description": "Вы встречаете торговый конвой с редкими товарами.",
        "type": "space",
        "rarity": "common",
        "chapters": range(1, 18),
        "trigger": {"travel": True, "random_chance": 0.12},
        "scene": {
            "description": "Три крупных транспортных корабля под охраной фрегата движутся по торговому маршруту.",
            "dialogues": [
                {"speaker": "veronica", "text": "Это конвой Гильдии Торговцев. У них обычно хорошие цены и редкий товар. Можем поторговать."}
            ]
        },
        "choices": [
            {
                "text": "Торговать (скидка 20%)",
                "effects": {"shop_access": True, "discount": 20}
            },
            {
                "text": "Провести сделку на чёрном рынке",
                "effects": {"smuggled_goods": True},
                "requirements": {"veronica_relationship": 30}
            },
            {
                "text": "Продолжить путь",
                "effects": {}
            }
        ]
    },
    
    "nebula_storm": {
        "id": "event_space_04",
        "name": "Туманная буря",
        "description": "Вы попадаете в естественную космическую бурю.",
        "type": "space",
        "rarity": "uncommon",
        "chapters": range(1, 18),
        "trigger": {"travel": True, "random_chance": 0.1},
        "scene": {
            "description": "Корабль трясёт — вы попали в электромагнитную бурю внутри туманности.",
            "dialogues": [
                {"speaker": "sergey", "text": "Щиты на 60%! Электроника глючит. Нужно продержаться!"},
                {"speaker": "dmitry", "text": "Маневренность снижена на 40%. Мы словно в каше!"}
            ]
        },
        "choices": [
            {
                "text": "[Biotics] Стабилизировать щиты",
                "effects": {"ship_damage": -10},
                "requirements": {"biotics": 50}
            },
            {
                "text": "Переждать бурю",
                "effects": {"time_loss": 2, "ship_damage": 15}
            },
            {
                "text": "Прорываться на максимальной скорости",
                "effects": {"time_loss": 0, "ship_damage": 30},
                "risk": {"critical_failure_chance": 0.2}
            }
        ]
    }
}

# === СТАНЦИОННЫЕ СОБЫТИЯ ===

STATION_EVENTS = {
    "bar_fight": {
        "id": "event_station_01",
        "name": "Барная потасовка",
        "description": "Вы становитесь свидетелем драки в космопорту.",
        "type": "station",
        "rarity": "common",
        "chapters": range(1, 18),
        "trigger": {"location_type": "station", "random_chance": 0.15},
        "scene": {
            "description": "В баре вспыхивает драка между двумя группами — местными и членами экипажа торгового судна.",
            "dialogues": [
                {"speaker": "narrator", "text": "Один из драчунов случайно толкает вас. Ситуация накаляется."}
            ]
        },
        "choices": [
            {
                "text": "Вмешаться и разнять",
                "effects": {"reputation": 5, "credits": -50},
                "risk": {"injury_chance": 0.3}
            },
            {
                "text": "Присоединиться к драке",
                "effects": {"combat_experience": 10, "reputation": -5},
                "requirements": {"combat": 40}
            },
            {
                "text": "Незаметно уйти",
                "effects": {}
            }
        ]
    },
    
    "mysterious_stranger": {
        "id": "event_station_02",
        "name": "Таинственный незнакомец",
        "description": "К вам подходит незнакомец с интересным предложением.",
        "type": "station",
        "rarity": "uncommon",
        "chapters": range(3, 16),
        "trigger": {"location_type": "station", "random_chance": 0.08},
        "scene": {
            "description": "В тёмном углу станции к вам подходит капюшонная фигура.",
            "dialogues": [
                {"speaker": "stranger", "text": "Вы — Курьер? У меня есть... информация. Ценная информация. Но за неё придётся заплатить."},
                {"speaker": "narrator", "text": "Фигура оглядывается, проверяя, не следят ли."}
            ]
        },
        "choices": [
            {
                "text": "Купить информацию",
                "effects": {"intel": 20, "credits": -200},
                "risk": {"false_intel_chance": 0.25}
            },
            {
                "text": "[Psychic] Прочитать намерения",
                "effects": {"truth_revealed": True},
                "requirements": {"psychic": 50}
            },
            {
                "text": "Отказаться — слишком подозрительно",
                "effects": {}
            }
        ]
    },
    
    "smuggler_deal": {
        "id": "event_station_03",
        "name": "Контрабандная сделка",
        "description": "Контрабандисты предлагают незаконный товар.",
        "type": "station",
        "rarity": "uncommon",
        "chapters": range(1, 18),
        "trigger": {"location_type": "station", "random_chance": 0.1, "veronica_relationship_min": 20},
        "scene": {
            "description": "Группа людей с подозрительными ящиками делает вам знак подойти.",
            "dialogues": [
                {"speaker": "smuggler", "text": "Эй, капитан. Хочешь кое-что особенное? Без пошлин, без вопросов. Скидка для друзей Вероники."}
            ]
        },
        "choices": [
            {
                "text": "Купить редкий товар (-500 кредитов)",
                "effects": {"rare_item": 1, "credits": -500},
                "risk": {"patrol_chance": 0.2, "patrol_event": "patrol_inspection"}
            },
            {
                "text": "Доложить властям",
                "effects": {"alliance_reputation": 10, "independence_reputation": -10}
            },
            {
                "text": "Игнорировать",
                "effects": {}
            }
        ]
    },
    
    "tech_merchant": {
        "id": "event_station_04",
        "name": "Технический торговец",
        "description": "Странный торговец предлагает уникальные модификации.",
        "type": "station",
        "rarity": "rare",
        "chapters": range(5, 18),
        "trigger": {"location_type": "station", "random_chance": 0.05},
        "scene": {
            "description": "Старик с кибернетическим глазом приглашает вас в свою лавку.",
            "dialogues": [
                {"speaker": "merchant", "text": "Вы выглядите как человек, который ценит... уникальные решения. У меня есть кое-что, что может заинтересовать капитана вашего... положения."}
            ]
        },
        "choices": [
            {
                "text": "Посмотреть товары",
                "effects": {"special_shop": True}
            },
            {
                "text": "Спросить о происхождении товаров",
                "effects": {"lore": 5},
                "requirements": {"intelligence": 40}
            },
            {
                "text": "Уйти — слишком много секретов",
                "effects": {}
            }
        ]
    }
}

# === ПЛАНЕТАРНЫЕ СОБЫТИЯ ===

PLANETARY_EVENTS = {
    "local_festival": {
        "id": "event_planet_01",
        "name": "Местный праздник",
        "description": "Вы попадаете на культурный праздник местной колонии.",
        "type": "planetary",
        "rarity": "uncommon",
        "chapters": range(1, 18),
        "trigger": {"location_type": "planet", "random_chance": 0.12},
        "scene": {
            "description": "Улицы колонии украшены гирляндами. Местные празднуют день основания.",
            "dialogues": [
                {"speaker": "local", "text": "Гость! Присоединяйся к нашему празднику! Сегодня мы чествуем всех, кто принёс мир в этот сектор!"},
                {"speaker": "maria", "text": "Капитан, это отличный шанс наладить отношения с местными."}
            ]
        },
        "choices": [
            {
                "text": "Принять участие в празднике",
                "effects": {"reputation": 15, "relationships": {"all": 5}}
            },
            {
                "text": "Провести дипломатическую беседу с лидером",
                "effects": {"alliance_reputation": 10},
                "requirements": {"diplomacy": 40}
            },
            {
                "text": "Остаться на корабле — дела важнее",
                "effects": {"determination": 5}
            }
        ]
    },
    
    "ancient_ruins": {
        "id": "event_planet_02",
        "name": "Древние руины",
        "description": "Вы обнаруживаете следы древней цивилизации.",
        "type": "planetary",
        "rarity": "rare",
        "chapters": range(6, 18),
        "trigger": {"location_type": "planet", "random_chance": 0.06, "resonance_level_min": 1},
        "scene": {
            "description": "Сканеры показывают аномалию под поверхностью — искусственные структуры.",
            "dialogues": [
                {"speaker": "anna", "text": "Это не природное образование. Кто-то... или что-то построило это тысячи лет назад."},
                {"speaker": "zara", "text": "Если рядом... я чувствую отголоски древней силы. Нам стоит быть осторожными."}
            ]
        },
        "choices": [
            {
                "text": "[Resonance] Исследовать руины",
                "effects": {"ancient_artifact": 1, "knowledge": 30, "resonance_experience": 15},
                "requirements": {"resonance_level": 2}
            },
            {
                "text": "Отправить дрон для разведки",
                "effects": {"intel": 10},
                "risk": {"drone_loss_chance": 0.3}
            },
            {
                "text": "Зафиксировать координаты и уйти",
                "effects": {"coordinates_saved": True}
            }
        ]
    },
    
    "creature_encounter": {
        "id": "event_planet_03",
        "name": "Встреча с фауной",
        "description": "Вы сталкиваетесь с местной формой жизни.",
        "type": "planetary",
        "rarity": "common",
        "chapters": range(1, 18),
        "trigger": {"location_type": "planet", "random_chance": 0.15},
        "scene": {
            "description": "Из зарослей появляется существо — крупное, с несколькими глазами, явно настороженное.",
            "dialogues": [
                {"speaker": "maria", "text": "Не делайте резких движений. Оно оценивает угрозу. Или... пищу."},
                {"speaker": "narrator", "text": "Существо издаёт низкий звук, не отрывая от вас взгляда."}
            ]
        },
        "choices": [
            {
                "text": "[Alchemy] Предложить еду",
                "effects": {"creature_friendly": True},
                "requirements": {"alchemy": 30}
            },
            {
                "text": "Медленно отступить",
                "effects": {}
            },
            {
                "text": "Напугать громким звуком",
                "effects": {},
                "risk": {"attack_chance": 0.4, "attack_event": "creature_attack"}
            }
        ]
    }
}

# === КОРАБЕЛЬНЫЕ СОБЫТИЯ ===

SHIP_EVENTS = {
    "crew_conflict": {
        "id": "event_ship_01",
        "name": "Конфликт в команде",
        "description": "Между членами экипажа возникает напряжённость.",
        "type": "ship",
        "rarity": "common",
        "chapters": range(3, 18),
        "trigger": {"location": "ship", "random_chance": 0.1, "team_morale_max": 70},
        "scene": {
            "description": "Вы слышите спор на камбузе — два члена экипажа выясняют отношения.",
            "dialogues": [
                {"speaker": "narrator", "text": "Голоса становятся всё громче. Ситуация накаляется."}
            ]
        },
        "choices": [
            {
                "text": "Вмешаться и разобраться",
                "effects": {"team_morale": 10},
                "requirements": {"leadership": 30}
            },
            {
                "text": "Позволить им выяснить сами",
                "effects": {"team_morale": -5}
            },
            {
                "text": "Вызвать Мию для урегулирования",
                "effects": {"team_morale": 5},
                "requirements": {"mia_relationship": 40}
            }
        ]
    },
    
    "system_malfunction": {
        "id": "event_ship_02",
        "name": "Системный сбой",
        "description": "На корабле происходит техническая авария.",
        "type": "ship",
        "rarity": "common",
        "chapters": range(1, 18),
        "trigger": {"location": "ship", "random_chance": 0.12},
        "scene": {
            "description": "Сирена тревоги — сбой в одной из систем корабля.",
            "dialogues": [
                {"speaker": "sergey", "text": "Капитан, у нас проблема! Отказала система жизнеобеспечения в секторе B. Нужна помощь!"},
                {"speaker": "dmitry", "text": "Маневровые двигатели тоже глючат. Ремонт займёт время."}
            ]
        },
        "choices": [
            {
                "text": "Помочь с ремонтом лично",
                "effects": {"repair_speed": 2, "sergey_relationship": 5}
            },
            {
                "text": "Координировать ремонт из рубки",
                "effects": {"repair_speed": 1}
            },
            {
                "text": "Довериться команде",
                "effects": {"repair_speed": 0.5, "team_morale": -5}
            }
        ]
    },
    
    "nightmare": {
        "id": "event_ship_03",
        "name": "Кошмар",
        "description": "Вам снятся странные сны под влиянием Сущности.",
        "type": "ship",
        "rarity": "uncommon",
        "chapters": range(10, 18),
        "trigger": {"location": "ship", "random_chance": 0.08, "entity_influence_min": 10},
        "scene": {
            "description": "Вы просыпаетесь в холодном поту от кошмара, который казался слишком реальным.",
            "dialogues": [
                {"speaker": "narrator", "text": "Видения всё ещё стоят перед глазами — галактика, поглощённая тьмой, и голос, зовущий вас по имени."},
                {"speaker": "entity_voice", "text": "[в отголоске сна] Ты слышишь нас... мы ждём... приближайся..."}
            ]
        },
        "choices": [
            {
                "text": "[Psychic] Попытаться запомнить детали",
                "effects": {"entity_knowledge": 5, "psychic": 3},
                "requirements": {"psychic": 50}
            },
            {
                "text": "Пойти к Марии за успокоительным",
                "effects": {"mental_recovery": 20, "maria_relationship": 3}
            },
            {
                "text": "Записать видения и вернуться ко сну",
                "effects": {"knowledge": 3}
            }
        ]
    },
    
    "secret_discovery": {
        "id": "event_ship_04",
        "name": "Секретный отсек",
        "description": "Вы обнаруживаете скрытый отсек на своём корабле.",
        "type": "ship",
        "rarity": "rare",
        "chapters": range(4, 16),
        "trigger": {"location": "ship", "random_chance": 0.04},
        "scene": {
            "description": "При осмотре корабля вы находите замаскированную панель, за которой — скрытый отсек.",
            "dialogues": [
                {"speaker": "narrator", "text": "Внутри — старые записи, странные артефакты и логотип корпорации, которую вы не узнаёте."},
                {"speaker": "veronica", "text": "Это... интересно. Предыдущий владелец вашего корабля явно был не простым курьером."}
            ]
        },
        "choices": [
            {
                "text": "Исследовать содержимое",
                "effects": {"secret_lore": True, "rare_item": 1}
            },
            {
                "text": "Спросить Веронику о корпорации",
                "effects": {"intel": 15},
                "requirements": {"veronica_relationship": 30}
            },
            {
                "text": "Заблокировать отсек — лучше не знать",
                "effects": {"determination": 5}
            }
        ]
    }
}

# === СПЕЦИАЛЬНЫЕ СОБЫТИЯ ===

SPECIAL_EVENTS = {
    "entity_whisper": {
        "id": "event_special_01",
        "name": "Шёпот Сущности",
        "description": "Сущность пытается установить контакт.",
        "type": "special",
        "rarity": "very_rare",
        "chapters": range(12, 18),
        "trigger": {"random_chance": 0.03, "psychic_min": 60, "entity_influence_min": 20},
        "scene": {
            "description": "Внезапно пространство вокруг вас искажается. Вы слышите голос Сущности напрямую.",
            "dialogues": [
                {"speaker": "entity", "text": "Маленький курьер... ты приближаешься. Мы чувствуем твой разум — яркий, как звезда. Почему ты сопротивляешься неизбежному?"},
                {"speaker": "narrator", "text": "Вы чувствуете одновременно страх и странное притяжение."}
            ]
        },
        "choices": [
            {
                "text": "[Psychic] Попытаться установить диалог",
                "effects": {"entity_communication": True, "psychic": 10, "entity_influence": 10},
                "requirements": {"psychic": 70}
            },
            {
                "text": "Закрыть разум и сопротивляться",
                "effects": {"mental_damage": 20, "determination": 10}
            },
            {
                "text": "Принять контакт",
                "effects": {"entity_knowledge": 30, "entity_influence": 30, "psychic": 5}
            }
        ]
    },
    
    "echo_fragment": {
        "id": "event_special_02",
        "name": "Отголосок Эха",
        "description": "Вы слышите фрагмент древнего сообщения.",
        "type": "special",
        "rarity": "rare",
        "chapters": range(11, 18),
        "trigger": {"random_chance": 0.05, "flag": "echo_contacted"},
        "scene": {
            "description": "Кристалл Эха внезапно активируется, передавая фрагмент информации.",
            "dialogues": [
                {"speaker": "echo", "text": "...ещё одна точка входа обнаружена в секторе 7-Gamma... если кто-то слышит это... мы оставили там... [помехи]..."},
                {"speaker": "narrator", "text": "Передача обрывается, но вы успеваете записать координаты."}
            ]
        },
        "choices": [
            {
                "text": "Записать координаты",
                "effects": {"secret_location": True}
            },
            {
                "text": "Попросить Эха повторить",
                "effects": {"intel": 10},
                "risk": {"energy_drain": 20}
            }
        ]
    }
}

# Объединение всех событий
ALL_RANDOM_EVENTS = {
    "space": SPACE_EVENTS,
    "station": STATION_EVENTS,
    "planetary": PLANETARY_EVENTS,
    "ship": SHIP_EVENTS,
    "special": SPECIAL_EVENTS
}

def get_random_event(location_type, game_state):
    """Получить случайное событие на основе контекста"""
    events = ALL_RANDOM_EVENTS.get(location_type, {})
    current_chapter = game_state.get("current_chapter", 1)
    
    available_events = []
    for event_id, event in events.items():
        # Проверка главы
        if current_chapter not in event.get("chapters", range(1, 19)):
            continue
        
        # Проверка редкости
        rarity = event.get("rarity", "common")
        trigger = event.get("trigger", {})
        base_chance = trigger.get("random_chance", 0.1)
        
        # Модификаторы редкости
        rarity_modifiers = {
            "common": 1.0,
            "uncommon": 0.7,
            "rare": 0.4,
            "very_rare": 0.2
        }
        
        final_chance = base_chance * rarity_modifiers.get(rarity, 1.0)
        
        # Проверка требований
        requirements_met = True
        for key, value in trigger.items():
            if key == "resonance_level_min":
                if game_state.get("resonance_level", 0) < value:
                    requirements_met = False
            elif key == "psychic_min":
                if game_state.get("abilities", {}).get("psychic", 0) < value:
                    requirements_met = False
            elif key == "entity_influence_min":
                if game_state.get("entity_influence", 0) < value:
                    requirements_met = False
            elif key == "flag":
                if not game_state.get(value):
                    requirements_met = False
            elif key == "team_morale_max":
                if game_state.get("team_morale", 100) > value:
                    requirements_met = False
        
        if requirements_met and random.random() < final_chance:
            available_events.append(event)
    
    if available_events:
        return random.choice(available_events)
    return None

def process_event_choice(event, choice_index, game_state):
    """Обработать выбор игрока в событии"""
    choice = event["choices"][choice_index]
    effects = choice.get("effects", {})
    
    # Применение эффектов
    for key, value in effects.items():
        if key == "credits":
            game_state["credits"] = game_state.get("credits", 0) + value
        elif key == "reputation":
            game_state["reputation"] = game_state.get("reputation", 0) + value
        elif key == "knowledge":
            game_state["knowledge"] = game_state.get("knowledge", 0) + value
        elif key == "team_morale":
            game_state["team_morale"] = game_state.get("team_morale", 50) + value
        elif key == "relationships":
            for char, amount in value.items():
                if char == "all":
                    for c in game_state.get("relationships", {}):
                        game_state["relationships"][c] = game_state["relationships"].get(c, 0) + amount
                else:
                    game_state["relationships"][char] = game_state["relationships"].get(char, 0) + amount
    
    # Проверка риска
    risk = choice.get("risk", {})
    for risk_type, chance in risk.items():
        if random.random() < chance:
            if risk_type == "trap_chance":
                return {"success": False, "event": risk.get("trap_event")}
            elif risk_type == "injury_chance":
                game_state["health"] = game_state.get("health", 100) - 20
            elif risk_type == "critical_failure_chance":
                game_state["ship_damage"] = game_state.get("ship_damage", 0) + 50
    
    return {"success": True}

def check_event_requirements(event, game_state):
    """Проверить, соответствует ли игрок требованиям события"""
    for choice in event.get("choices", []):
        requirements = choice.get("requirements", {})
        for key, value in requirements.items():
            if key == "resonance_level":
                if game_state.get("resonance_level", 0) < value:
                    choice["disabled"] = True
            elif key == "psychic":
                if game_state.get("abilities", {}).get("psychic", 0) < value:
                    choice["disabled"] = True
            elif key == "biotics":
                if game_state.get("abilities", {}).get("biotics", 0) < value:
                    choice["disabled"] = True
            elif key == "combat":
                if game_state.get("combat", 0) < value:
                    choice["disabled"] = True
            elif key == "leadership":
                if game_state.get("leadership", 0) < value:
                    choice["disabled"] = True
    
    return event
