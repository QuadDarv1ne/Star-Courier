# -*- coding: utf-8 -*-
"""
Star Courier - Locations & Zones System
Система локаций и зон для исследования галактики
"""

# === ТИПЫ ЛОКАЦИЙ ===

LOCATION_TYPES = {
    "space_station": {
        "name": "Космическая станция",
        "description": "Орбитальная станция с торговыми и сервисными возможностями",
        "available_actions": ["trade", "repair", "recruit", "rest", "gather_intel"],
        "random_events": ["bar_fight", "mysterious_stranger", "smuggler_deal"],
        "danger_level": "low"
    },
    "planet": {
        "name": "Планета",
        "description": "Обитаемая или необитаемая планета для исследования",
        "available_actions": ["explore", "gather_resources", "trade", "mission"],
        "random_events": ["creature_encounter", "ancient_ruins", "local_festival"],
        "danger_level": "variable"
    },
    "asteroid_field": {
        "name": "Астероидное поле",
        "description": "Опасная зона с ресурсами и скрытыми угрозами",
        "available_actions": ["mine", "scan", "navigate_carefully"],
        "random_events": ["pirate_ambush", "hidden_cache", "anomaly_discovery"],
        "danger_level": "medium"
    },
    "nebula": {
        "name": "Туманность",
        "description": "Мистическая область космоса с аномалиями",
        "available_actions": ["scan", "research", "brave_traversal"],
        "random_events": ["nebula_storm", "entity_whisper", "time_dilation"],
        "danger_level": "high"
    },
    "anomaly_zone": {
        "name": "Зона аномалий",
        "description": "Место влияния Сущности или древних артефактов",
        "available_actions": ["investigate", "collect_samples", "retreat"],
        "random_events": ["entity_manifestation", "reality_distortion", "echo_contact"],
        "danger_level": "extreme"
    },
    "ship_interior": {
        "name": "Интерьер корабля",
        "description": "Внутренние помещения «Странника»",
        "available_actions": ["rest", "craft", "talk_crew", "upgrade"],
        "random_events": ["system_malfunction", "crew_conflict", "nightmare"],
        "danger_level": "none"
    },
    "neutral_ground": {
        "name": "Нейтральная территория",
        "description": "Место встречи для переговоров и сделок",
        "available_actions": ["negotiate", "trade", "gather_intel"],
        "random_events": ["diplomatic_incident", "assassination_attempt"],
        "danger_level": "low"
    },
    "hostile_territory": {
        "name": "Враждебная территория",
        "description": "Зона под контролем врагов или пиратов",
        "available_actions": ["stealth", "fight", "bribe"],
        "random_events": ["patrol_encounter", "ambush", "prisoner_rescue"],
        "danger_level": "extreme"
    }
}

# === КОНКРЕТНЫЕ ЛОКАЦИИ ===

LOCATIONS = {
    # === ГЛАВНЫЕ ЛОКАЦИИ ===
    "stranger_ship": {
        "id": "loc_main_01",
        "name": "Корабль «Странник»",
        "type": "ship_interior",
        "description": """
«Странник» — ваш верный корабль, модифицированный курьерский сосуд класса «Горизонт». 
Первоначально спроектированный для быстрых доставок, он был переделан для дальних путешествий 
и исследований. Каюты экипажа, мостик, машинный отсек, медотсек и грузовой отсок — 
всё, что нужно для жизни среди звёзд.
""",
        "sub_locations": {
            "bridge": {
                "name": "Мостик",
                "description": "Командный центр корабля с панелями навигации и коммуникации.",
                "characters": ["mia", "anna"],
                "available_actions": ["navigate", "scan_systems", "communicate"]
            },
            "medbay": {
                "name": "Медицинский отсек",
                "description": "Полностью оборудованный медицинский блок под руководством Марии.",
                "characters": ["maria"],
                "available_actions": ["heal", "craft_medicine", "check_crew_status"]
            },
            "engine_room": {
                "name": "Машинный отсек",
                "description": "Сердце корабля — реактор и гипердвигатель.",
                "characters": ["sergey"],
                "available_actions": ["repair", "upgrade_systems", "optimize"]
            },
            "cargo_hold": {
                "name": "Грузовой отсек",
                "description": "Просторное хранилище для товаров и ресурсов.",
                "characters": ["dmitry"],
                "available_actions": ["manage_cargo", "smuggler_compartments", "inventory"]
            },
            "crew_quarters": {
                "name": "Каюты экипажа",
                "description": "Личные комнаты команды и общая зона отдыха.",
                "characters": ["all"],
                "available_actions": ["rest", "private_conversation", "personal_items"]
            },
            "observation_deck": {
                "name": "Смотровая площадка",
                "description": "Стеклянный купол с видом на космос — место для размышлений.",
                "characters": [],
                "available_actions": ["contemplate", "stargazing", "romantic_scene"]
            }
        },
        "chapter_available": range(1, 19)
    },
    
    # === СТАНЦИИ ===
    "station_crossroads": {
        "id": "loc_station_01",
        "name": "Станция «Перекрёсток»",
        "type": "space_station",
        "sector": "neutral_zone",
        "description": """
«Перекрёсток» — крупнейшая нейтральная станция в галактике. Здесь встречаются 
представители всех фракций: торговцы, дипломаты, наёмники, шпионы. Станция разделена 
на сектора: торговой квартал, дипломатическая зона, подпольный рынок и доки. 
Здесь можно найти всё — от легального оборудования до запрещённых технологий.
""",
        "key_npcs": ["traders", "diplomats", "smugglers", "alliance_representative"],
        "available_services": {
            "trade": {"discount": 0, "variety": "excellent"},
            "repair": {"cost_modifier": 1.0, "quality": "good"},
            "recruit": {"available": True, "candidates": 5},
            "intel": {"cost": 500, "quality": "high"}
        },
        "chapter_available": range(3, 19),
        "special_events": ["path_choice", "faction_meetings"]
    },
    
    "station_horizon": {
        "id": "loc_station_02",
        "name": "Станция «Горизонт»",
        "type": "space_station",
        "sector": "frontier",
        "description": """
Заброшенная исследовательская станция, где работала Вера. Когда-то здесь 
изучали аномалии и древние артефакты. Теперь станция мертва — или кажется таковой. 
Системы работают на минимальной мощности, а некоторые секции полностью обесточены. 
Но что-то здесь ещё живёт...
""",
        "key_npcs": ["vera", "station_ai"],
        "available_services": {
            "research": {"available": True, "unique_items": True},
            "artifact_analysis": {"available": True}
        },
        "chapter_available": [12],
        "quest_related": "q12_01",
        "danger_level": "medium"
    },
    
    "station_echo": {
        "id": "loc_station_03",
        "name": "Станция «Эхо»",
        "type": "space_station",
        "sector": "deep_space",
        "description": """
Тайная станция Альянса на границе исследованного космоса. Здесь Деклан Рэйес 
впервые услышал голос Сущности. Сейчас станция заброшена, но её системы 
всё ещё функционируют — будто ожидая возвращения.
""",
        "key_npcs": [],
        "chapter_available": range(10, 16),
        "quest_related": "traitor_investigation",
        "danger_level": "high"
    },
    
    # === ПЛАНЕТЫ ===
    "planet_new_horizon": {
        "id": "loc_planet_01",
        "name": "Новая Надежда",
        "type": "planet",
        "sector": "orion_sector",
        "description": """
Аграрная колония на окраине освоенного космоса — родина Мии. Когда-то здесь 
были мирные фермы и исследовательские станции. После пиратского рейда 
колония так и не восстановилась полностью. Теперь это место с суровой атмосферой 
и редким населением.
""",
        "environment": "agricultural_colony",
        "population": "sparse",
        "key_npcs": ["old_colonists"],
        "available_services": {
            "trade": {"specialty": "agricultural_products", "prices": "low"},
            "rest": {"available": True, "cost": 50}
        },
        "chapter_available": range(6, 14),
        "personal_quest": "mia_homeland"
    },
    
    "planet_temple_world": {
        "id": "loc_planet_02",
        "name": "Святилище Времени",
        "type": "planet",
        "sector": "unknown_territory",
        "description": """
Планета, скрытая в глубине туманности. Здесь находится древний храм Предтеч, 
хранящий Кристалл Времени. Атмосфера планеты токсична для длительного пребывания, 
но храм имеет собственную систему жизнеобеспечения. Планета окружена 
пространственными аномалиями, делающими навигацию крайне сложной.
""",
        "environment": "ancient_sanctuary",
        "population": "none",
        "key_npcs": ["temple_guardian", "zara"],
        "chapter_available": [14],
        "quest_related": "q14_01",
        "danger_level": "extreme",
        "special_features": ["time_crystal", "ancient_knowledge"]
    },
    
    "planet_evergreen": {
        "id": "loc_planet_03",
        "name": "Эвергрин",
        "type": "planet",
        "sector": "alliance_territory",
        "description": """
Перенаселённая индустриальная планета Альянса — родина предателя Деклана. 
Города-ульи, фабрики, работающие круглосуточно, и резкое разделение 
между богатыми и бедными. Здесь легко потеряться — и сложно быть найденным.
""",
        "environment": "industrial",
        "population": "dense",
        "key_npcs": ["underground_contacts", "alliance_officials"],
        "chapter_available": range(8, 16),
        "special_features": ["underground_network", "black_market"]
    },
    
    "planet_tarius_4": {
        "id": "loc_planet_04",
        "name": "Тариус-4",
        "type": "planet",
        "sector": "war_zone",
        "description": """
Планета, опустошённая гражданской войной. Здесь Мария пережила катастрофу 
полевого госпиталя. Города в руинах, атмосфера загрязнена, а выжившие 
борются за ресурсы. Сущность уже начала проявляться здесь — 
исчезновения целых поселений списывают на войну.
""",
        "environment": "war_torn",
        "population": "scattered",
        "key_npcs": ["refugees", "militia_leaders"],
        "chapter_available": range(10, 18),
        "quest_related": "maria_past",
        "danger_level": "extreme",
        "entity_presence": "moderate"
    },
    
    # === АНОМАЛЬНЫЕ ЗОНЫ ===
    "zone_silence": {
        "id": "loc_zone_01",
        "name": "Зона Тишины",
        "type": "anomaly_zone",
        "sector": "coordinate_zero_perimeter",
        "description": """
Область пространства, где физические законы искажены присутствием Сущности. 
Сенсоры не работают, время течёт нелинейно, а пространство постоянно меняется. 
Корабли, вошедшие сюда, редко возвращаются. Те, кто вернулся, — изменились навсегда.
""",
        "danger_level": "extreme",
        "chapter_available": range(16, 19),
        "entity_presence": "extreme",
        "special_mechanics": {
            "time_distortion": True,
            "reality_shifts": True,
            "mental_damage": True,
            "resonance_required": 2
        }
    },
    
    "coordinate_zero": {
        "id": "loc_zone_02",
        "name": "Координата Нуля",
        "type": "anomaly_zone",
        "sector": "galaxy_core",
        "description": """
Эпицентр влияния Сущности — древняя станция-якорь, построенная Предтечами. 
Здесь реальность наиболее тонка, а граница между измерениями практически отсутствует. 
Станция живая — она реагирует на присутствие существ, перестраивает коридоры, 
создаёт и уничтожает комнаты. В её ядре находится ключ ко всему — 
якорь, связывающий Сущность с нашим измерением.
""",
        "danger_level": "extreme",
        "chapter_available": [17, 18],
        "entity_presence": "extreme",
        "sub_locations": {
            "station_surface": {
                "name": "Поверхность станции",
                "description": "Внешние доки и системы жизнеобеспечения."
            },
            "mirror_hall": {
                "name": "Зеркальный зал",
                "description": "Место, где Сущность создаёт иллюзии из страхов посетителей."
            },
            "guardian_chamber": {
                "name": "Покои Стража",
                "description": "Где Ар'Танис ждал миллионы лет."
            },
            "station_core": {
                "name": "Ядро станции",
                "description": "Точка контакта между измерениями — место финального выбора."
            }
        },
        "key_npcs": ["guardian", "entity"],
        "special_mechanics": {
            "final_battle": True,
            "ending_choice": True
        }
    },
    
    # === НЕЙТРАЛЬНЫЕ ТЕРРИТОРИИ ===
    "observer_sanctuary": {
        "id": "loc_neutral_01",
        "name": "Святилище Ордена",
        "type": "neutral_ground",
        "sector": "hidden_location",
        "description": """
Скрытая обитель Ордена Наблюдателей — древняя крепость на планете, 
не отмеченной ни на одной карте. Здесь хранятся знания тысячелетий, 
артефакты Предтеч и тренировочные залы рыцарей. Доступ разрешён только 
посвящённым — или тем, кого Зара приведёт лично.
""",
        "key_npcs": ["zara", "order_masters"],
        "chapter_available": range(13, 18),
        "path_required": "observer",
        "available_services": {
            "training": {"psychic": 20, "resonance": 1},
            "artifacts": {"unique_items": True},
            "knowledge": {"ancient_texts": True}
        }
    },
    
    "independent_port": {
        "id": "loc_neutral_02",
        "name": "Порт Свободных",
        "type": "space_station",
        "sector": "independent_territory",
        "description": """
Главная станция Конфедерации Независимых Миров. Здесь нет корпораций, 
нет правительств — только свободные люди, торгующие и работающие по своим правилам. 
Базар, доки, казино и арен — всё для тех, кто ценит свободу превыше всего.
""",
        "key_npcs": ["volkov", "independent_traders", "mercenaries"],
        "chapter_available": range(9, 18),
        "path_required": "independence",
        "available_services": {
            "trade": {"discount": 20, "variety": "good"},
            "recruit": {"mercenaries": True},
            "smuggle": {"safe_routes": True}
        }
    },
    
    "alliance_command": {
        "id": "loc_neutral_03",
        "name": "Штаб Альянса",
        "type": "space_station",
        "sector": "alliance_core",
        "description": """
Центр командования Объединёнными Мирами — огромная станция-крепость 
в сердце территории Альянса. Здесь принимаются решения, влияющие 
на судьбы миллиардов. Доступ строго ограничен, но для союзников 
открыты определённые уровни.
""",
        "key_npcs": ["marcus_reid", "alliance_admirals"],
        "chapter_available": range(13, 18),
        "path_required": "alliance",
        "available_services": {
            "fleet_support": {"available": True},
            "intelligence": {"quality": "excellent"},
            "equipment": {"military_grade": True}
        }
    },
    
    # === ВРАЖДЕБНЫЕ ТЕРРИТОРИИ ===
    "pirate_base": {
        "id": "loc_hostile_01",
        "name": "Пиратская база «Змеиное гнездо»",
        "type": "hostile_territory",
        "sector": "criminal_territory",
        "description": """
Крупнейшая база пиратского синдиката в нейтральной зоне. Здесь можно 
найти anything — за правильную цену. Но вход без приглашения 
означает смерть — или хуже.
""",
        "danger_level": "extreme",
        "chapter_available": range(5, 16),
        "available_services": {
            "black_market": {"illegal_items": True},
            "bounty_board": {"available": True}
        },
        "entry_requirements": {
            "reputation": "criminal",
            "bribe": 5000,
            "veronica_contact": True
        }
    }
}

# === СЕКТОРЫ ГАЛАКТИКИ ===

SECTORS = {
    "core_worlds": {
        "name": "Центральные Миры",
        "description": "Сердце галактической цивилизации — развитые, населённые миры.",
        "controlling_faction": "alliance",
        "danger_level": "low",
        "available_services": ["trade", "repair", "medical", "military"]
    },
    "alliance_territory": {
        "name": "Территория Альянса",
        "description": "Миры под контролем Объединённых Миров.",
        "controlling_faction": "alliance",
        "danger_level": "low",
        "available_services": ["trade", "repair", "military_support"]
    },
    "neutral_zone": {
        "name": "Нейтральная Зона",
        "description": "Неконтролируемая территория между крупными державами.",
        "controlling_faction": "none",
        "danger_level": "medium",
        "available_services": ["trade", "smuggling", "mercenaries"]
    },
    "frontier": {
        "name": "Граница",
        "description": "Край освоенного космоса — дикие, малоисследованные системы.",
        "controlling_faction": "none",
        "danger_level": "high",
        "available_services": ["minimal"]
    },
    "independent_territory": {
        "name": "Территория Независимых",
        "description": "Миры, отказавшиеся от крупных фракций.",
        "controlling_faction": "independence",
        "danger_level": "medium",
        "available_services": ["trade", "smuggling", "information"]
    },
    "criminal_territory": {
        "name": "Криминальные Секторы",
        "description": "Территории под контролем пиратских кланов и синдикатов.",
        "controlling_faction": "criminal",
        "danger_level": "extreme",
        "available_services": ["black_market", "bounties"]
    },
    "unknown_territory": {
        "name": "Неизведанные Пространства",
        "description": "Регионы, куда редко заходят корабли.",
        "controlling_faction": "none",
        "danger_level": "extreme",
        "available_services": ["none"],
        "special_features": ["ancient_artifacts", "anomalies"]
    },
    "coordinate_zero_perimeter": {
        "name": "Периметр Координаты Нуля",
        "description": "Зона аномалий вокруг эпицентра влияния Сущности.",
        "controlling_faction": "entity",
        "danger_level": "extreme",
        "available_services": ["none"],
        "special_features": ["time_distortion", "entity_presence"]
    }
}

# === ФУНКЦИИ ДЛЯ РАБОТЫ С ЛОКАЦИЯМИ ===

def get_location(location_id):
    """Получить информацию о локации"""
    return LOCATIONS.get(location_id)

def get_available_locations(chapter, game_state):
    """Получить список доступных локаций для главы"""
    available = []
    
    for loc_id, location in LOCATIONS.items():
        # Проверка главы
        if chapter not in location.get("chapter_available", range(1, 19)):
            continue
        
        # Проверка пути
        path_required = location.get("path_required")
        if path_required:
            if game_state.get("path") != path_required:
                continue
        
        # Проверка квеста
        quest_required = location.get("quest_related")
        if quest_required:
            if quest_required not in game_state.get("active_quests", []):
                continue
        
        available.append(location)
    
    return available

def get_sub_location(location_id, sub_location_id):
    """Получить подлокацию"""
    location = LOCATIONS.get(location_id)
    if not location:
        return None
    
    sub_locations = location.get("sub_locations", {})
    return sub_locations.get(sub_location_id)

def get_sector_info(sector_id):
    """Получить информацию о секторе"""
    return SECTORS.get(sector_id)

def get_locations_by_sector(sector_id):
    """Получить все локации в секторе"""
    return [loc for loc in LOCATIONS.values() 
            if loc.get("sector") == sector_id]

def get_location_danger(location_id, game_state):
    """Рассчитать уровень опасности локации с учётом состояния игры"""
    location = LOCATIONS.get(location_id)
    if not location:
        return "unknown"
    
    base_danger = location.get("danger_level", "medium")
    
    # Модификаторы от способностей
    psychic = game_state.get("abilities", {}).get("psychic", 0)
    resonance = game_state.get("resonance_level", 0)
    
    if psychic >= 70 or resonance >= 3:
        # Высокие способности снижают воспринимаемую опасность
        danger_levels = ["none", "low", "medium", "high", "extreme"]
        current_index = danger_levels.index(base_danger) if base_danger in danger_levels else 2
        reduced_index = max(0, current_index - 1)
        return danger_levels[reduced_index]
    
    return base_danger

def can_access_location(location_id, game_state):
    """Проверить возможность доступа к локации"""
    location = LOCATIONS.get(location_id)
    if not location:
        return False, "Локация не найдена"
    
    # Проверка требований входа
    entry_requirements = location.get("entry_requirements", {})
    
    for req_type, value in entry_requirements.items():
        if req_type == "reputation":
            if game_state.get("reputation_type") != value:
                return False, f"Требуется репутация: {value}"
        elif req_type == "bribe":
            if game_state.get("credits", 0) < value:
                return False, f"Требуется {value} кредитов для входа"
        elif req_type == "veronica_contact":
            if game_state.get("relationships", {}).get("veronica", 0) < 30:
                return False, "Требуется контакт с Вероникой"
    
    # Проверка специальных механик
    special_mechanics = location.get("special_mechanics", {})
    if "resonance_required" in special_mechanics:
        if game_state.get("resonance_level", 0) < special_mechanics["resonance_required"]:
            return False, "Требуется более высокий уровень резонанса"
    
    return True, "Доступ разрешён"
