# -*- coding: utf-8 -*-
"""
Star Courier - Faction Reputation System
Система репутации фракций
"""

# === ОСНОВНЫЕ ФРАКЦИИ ===

FACTIONS = {
    "alliance": {
        "id": "faction_alliance",
        "name": "Объединённые Миры (Альянс)",
        "description": """
Объединённые Миры — крупнейшая политическая сила галактики. 
Формально демократическая федерация, на практике — бюрократическая машина 
с мощным военным аппаратом. Альянс контролирует большую часть центральных миров 
и поддерживает относительный порядок на подконтрольных территориях.

Альянс ценит порядок, закон и коллективную безопасность. 
Они предлагают ресурсы, защиту и официальное признание — 
но требуют подчинения их правилам.
""",
        "leader": "Адмирал Маркус Рид",
        "headquarters": "Станция «Единство»",
        "ideology": "Порядок через единство",
        "reputation_range": (-100, 100),
        "reputation_tiers": {
            "hostile": {"min": -100, "max": -50, "name": "Враг государства", "color": "red"},
            "unfriendly": {"min": -49, "max": -10, "name": "Подозреваемый", "color": "orange"},
            "neutral": {"min": -9, "max": 30, "name": "Нейтральный", "color": "gray"},
            "friendly": {"min": 31, "max": 70, "name": "Союзник", "color": "blue"},
            "honored": {"min": 71, "max": 100, "name": "Герой Альянса", "color": "gold"}
        },
        "bonuses": {
            "friendly": {
                "shop_discount": 15,
                "fleet_support": True,
                "safe_haven": True
            },
            "honored": {
                "shop_discount": 30,
                "military_support": True,
                "medals": ["Звезда Служения"],
                "unique_items": ["Броня ветерана Альянса"]
            }
        },
        "penalties": {
            "hostile": {
                "hunted": True,
                "bounty": 50000,
                "restricted_systems": ["core_worlds"]
            }
        },
        "preferred_paths": ["alliance"],
        "conflicts": ["independence", "criminal_syndicate"]
    },
    
    "observers": {
        "id": "faction_observers",
        "name": "Орден Наблюдателей",
        "description": """
Орден Наблюдателей существует тысячи лет — дольше, чем большинство современных государств. 
Рыцари Ордена обучаются древним искусствам Psychic-манипуляций и обязаны хранить 
знания о древних угрозах. Орден не вмешивается в политику напрямую, 
но его влияние ощущается во всех уголках галактики.

Наблюдатели ценят знание, дисциплину и самопожертвование. 
Они предлагают мудрость веков и доступ к древним артефактам — 
но требуют преданности и подчинения кодексу.
""",
        "leader": "Верховный Магистр / Зара (рыцарь-командор)",
        "headquarters": "Святилище Ордена (скрытое)",
        "ideology": "Защита через знание",
        "reputation_range": (-100, 100),
        "reputation_tiers": {
            "hostile": {"min": -100, "max": -50, "name": "Еретик", "color": "red"},
            "unfriendly": {"min": -49, "max": -10, "name": "Неверный", "color": "orange"},
            "neutral": {"min": -9, "max": 30, "name": "Посторонний", "color": "gray"},
            "friendly": {"min": 31, "max": 70, "name": "Послушник", "color": "purple"},
            "honored": {"min": 71, "max": 100, "name": "Рыцарь Ордена", "color": "gold"}
        },
        "bonuses": {
            "friendly": {
                "psychic_training": True,
                "artifact_access": "basic",
                "sanctuary_access": True
            },
            "honored": {
                "psychic_training": "advanced",
                "artifact_access": "full",
                "unique_items": ["Мантия Наблюдателя", "Кристалл Резонанса"],
                "abilities": ["Глас Предков"]
            }
        },
        "penalties": {
            "hostile": {
                "psychic_block": True,
                "artifact_denial": True
            }
        },
        "preferred_paths": ["observer"],
        "conflicts": ["criminal_syndicate", "corporation_zenith"]
    },
    
    "independence": {
        "id": "faction_independence",
        "name": "Конфедерация Независимых Миров",
        "description": """
Конфедерация объединяет миры и станции, отказавшиеся от власти крупных фракций. 
Здесь правит свобода — или хаос, в зависимости от точки зрения. 
Независимые ценят автономию превыше всего и готовы сражаться за неё.

Конфедерация не предлагает защиту или ресурсы — 
она предлагает свободу от обязательств. Здесь можно найти 
контрабандистов, наёмников, учёных-изгнанников и любого, 
кто предпочитает жить по своим правилам.
""",
        "leader": "Совет Капитанов (включая Волкова)",
        "headquarters": "Порт Свободных",
        "ideology": "Свобода любой ценой",
        "reputation_range": (-100, 100),
        "reputation_tiers": {
            "hostile": {"min": -100, "max": -50, "name": "Враг свободы", "color": "red"},
            "unfriendly": {"min": -49, "max": -10, "name": "Сторонник тирании", "color": "orange"},
            "neutral": {"min": -9, "max": 30, "name": "Свободный агент", "color": "gray"},
            "friendly": {"min": 31, "max": 70, "name": "Проверенный союзник", "color": "green"},
            "honored": {"min": 71, "max": 100, "name": "Легенда Свободы", "color": "gold"}
        },
        "bonuses": {
            "friendly": {
                "smuggling_routes": True,
                "black_market_access": True,
                "free_port_services": True
            },
            "honored": {
                "smuggling_routes": "premium",
                "unique_ships": ["Модифицированный фрахтовщик"],
                "unique_items": ["Эмблема Свободы"],
                "fleet_command": True
            }
        },
        "penalties": {
            "hostile": {
                "blacklisted": True,
                "bounty_hunters": True
            }
        },
        "preferred_paths": ["independence"],
        "conflicts": ["alliance", "corporation_zenith"]
    },
    
    "criminal_syndicate": {
        "id": "faction_criminal",
        "name": "Синдикат (Криминальные структуры)",
        "description": """
Синдикат — неформальное объединение пиратских кланов, контрабандистских сетей 
и криминальных организаций. Они контролируют чёрный рынок, 
нелегальные перевозки и информацию, которую никто другой не предоставит.

Синдикат не предлагает законности — он предлагает возможности. 
Здесь можно купить и продать что угодно, найти любого, 
и достать документы, которых официально не существует.
""",
        "leader": "Совет Семей",
        "headquarters": "Змеиное Гнездо",
        "ideology": "Прибыль и власть",
        "reputation_range": (-100, 100),
        "reputation_tiers": {
            "hostile": {"min": -100, "max": -50, "name": "Метка смерти", "color": "darkred"},
            "unfriendly": {"min": -49, "max": -10, "name": "Проблемный элемент", "color": "red"},
            "neutral": {"min": -9, "max": 30, "name": "Посторонний", "color": "gray"},
            "friendly": {"min": 31, "max": 70, "name": "Надёжный партнёр", "color": "purple"},
            "honored": {"min": 71, "max": 100, "name": "Член Синдиката", "color": "gold"}
        },
        "bonuses": {
            "friendly": {
                "black_market_discount": 25,
                "safe_passage": "criminal_territory",
                "assassin_services": True
            },
            "honored": {
                "black_market_discount": 50,
                "unique_items": ["Тень Синдиката"],
                "protection": True,
                "safe_houses": True
            }
        },
        "penalties": {
            "hostile": {
                "assassination_contract": True,
                "bounty": 100000,
                "no_safe_haven": True
            }
        },
        "preferred_paths": [],
        "conflicts": ["alliance", "observers"],
        "special_access": {"veronica_relationship_min": 40}
    },
    
    "corporation_zenith": {
        "id": "faction_zenith",
        "name": "Корпорация «Зенит»",
        "description": """
«Зенит» — крупнейшая мегакорпорация галактики. Они контролируют торговые маршруты, 
технологические разработки и исследовательские станции. 
Формально нейтральны, на практике — преследуют только собственные интересы.

Корпорация предлагает деньги, технологии и возможности — 
но требует полной преданности. Отступников уничтожают, 
а конкуренцию устраняют любыми средствами.
""",
        "leader": "Совет Директоров",
        "headquarters": "Станция «Зенит-Прайм»",
        "ideology": "Прибыль через инновации",
        "reputation_range": (-100, 100),
        "reputation_tiers": {
            "hostile": {"min": -100, "max": -50, "name": "Корпоративный враг", "color": "red"},
            "unfriendly": {"min": -49, "max": -10, "name": "Нежелательный элемент", "color": "orange"},
            "neutral": {"min": -9, "max": 30, "name": "Независимый контрагент", "color": "gray"},
            "friendly": {"min": 31, "max": 70, "name": "Премиум-партнёр", "color": "blue"},
            "honored": {"min": 71, "max": 100, "name": "VIP-клиент", "color": "gold"}
        },
        "bonuses": {
            "friendly": {
                "shop_discount": 20,
                "tech_access": "advanced",
                "contracts": "priority"
            },
            "honored": {
                "shop_discount": 40,
                "unique_tech": ["Прототип «Зенит»"],
                "credit_line": 100000
            }
        },
        "penalties": {
            "hostile": {
                "blacklisted": True,
                "corporate_hunters": True
            }
        },
        "preferred_paths": [],
        "conflicts": ["independence", "observers"],
        "special_note": "Мия имеет негативную историю с этой корпорацией"
    }
}

# === ДЕЙСТВИЯ, ВЛИЯЮЩИЕ НА РЕПУТАЦИЮ ===

REPUTATION_ACTIONS = {
    "complete_alliance_mission": {
        "faction": "alliance",
        "value": 15,
        "description": "Выполнение миссии для Альянса"
    },
    "defeat_alliance_patrol": {
        "faction": "alliance",
        "value": -25,
        "description": "Уничтожение патруля Альянса"
    },
    "help_observer_knight": {
        "faction": "observers",
        "value": 20,
        "description": "Помощь рыцарю Ордена"
    },
    "share_entity_knowledge": {
        "faction": "observers",
        "value": 30,
        "description": "Передача знаний о Сущности"
    },
    "trade_with_independent": {
        "faction": "independence",
        "value": 5,
        "description": "Торговля с независимыми"
    },
    "defend_independent_station": {
        "faction": "independence",
        "value": 25,
        "description": "Защита независимой станции"
    },
    "smuggle_contraband": {
        "faction": "criminal_syndicate",
        "value": 10,
        "description": "Перевозка контрабанды"
    },
    "betray_criminal_deal": {
        "faction": "criminal_syndicate",
        "value": -40,
        "description": "Предательство криминальной сделки"
    },
    "accept_zenith_contract": {
        "faction": "corporation_zenith",
        "value": 10,
        "description": "Принятие контракта «Зенит»"
    },
    "expose_zenith_corruption": {
        "faction": "corporation_zenith",
        "value": -50,
        "description": "Разоблачение коррупции в «Зенит»"
    }
}

# === СИСТЕМА ОТНОШЕНИЙ МЕЖДУ ФРАКЦИЯМИ ===

FACTION_RELATIONS = {
    "alliance_observers": {
        "factions": ["alliance", "observers"],
        "relation": "neutral_positive",
        "description": "Официальное сотрудничество, но Орден сохраняет автономию"
    },
    "alliance_independence": {
        "factions": ["alliance", "independence"],
        "relation": "tension",
        "description": "Холодная война. Альянс хочет контроля, независимые — свободы"
    },
    "alliance_criminal": {
        "factions": ["alliance", "criminal_syndicate"],
        "relation": "hostile",
        "description": "Открытая вражда. Альянс охотится на преступников"
    },
    "observers_criminal": {
        "factions": ["observers", "criminal_syndicate"],
        "relation": "hostile",
        "description": "Орден считает Синдикат угрозой для галактики"
    },
    "independence_criminal": {
        "factions": ["independence", "criminal_syndicate"],
        "relation": "neutral",
        "description": "Прагматичное сотрудничество"
    },
    "zenith_alliance": {
        "factions": ["corporation_zenith", "alliance"],
        "relation": "allied",
        "description": "Стратегическое партнёрство"
    },
    "zenith_observers": {
        "factions": ["corporation_zenith", "observers"],
        "relation": "tension",
        "description": "Корпорация хочет технологии Ордена, Орден не доверяет корпорации"
    }
}

# === ФУНКЦИИ ДЛЯ РАБОТЫ С РЕПУТАЦИЕЙ ===

def get_faction(faction_id):
    """Получить информацию о фракции"""
    return FACTIONS.get(faction_id)

def get_reputation_tier(faction_id, reputation_value):
    """Получить уровень репутации"""
    faction = FACTIONS.get(faction_id)
    if not faction:
        return None
    
    tiers = faction.get("reputation_tiers", {})
    
    for tier_id, tier_data in tiers.items():
        if tier_data["min"] <= reputation_value <= tier_data["max"]:
            return {
                "tier_id": tier_id,
                "name": tier_data["name"],
                "color": tier_data["color"]
            }
    
    return {"tier_id": "neutral", "name": "Неизвестно", "color": "gray"}

def get_faction_bonuses(faction_id, reputation_value):
    """Получить бонусы фракции при текущей репутации"""
    faction = FACTIONS.get(faction_id)
    if not faction:
        return {}
    
    tier = get_reputation_tier(faction_id, reputation_value)
    all_bonuses = faction.get("bonuses", {})
    
    result = {}
    
    # Бонусы складываются по уровням
    if tier["tier_id"] in ["friendly", "honored"]:
        result.update(all_bonuses.get("friendly", {}))
    if tier["tier_id"] == "honored":
        result.update(all_bonuses.get("honored", {}))
    
    return result

def get_faction_penalties(faction_id, reputation_value):
    """Получить штрафы фракции при текущей репутации"""
    faction = FACTIONS.get(faction_id)
    if not faction:
        return {}
    
    tier = get_reputation_tier(faction_id, reputation_value)
    all_penalties = faction.get("penalties", {})
    
    if tier["tier_id"] == "hostile":
        return all_penalties.get("hostile", {})
    
    return {}

def apply_reputation_change(faction_id, change, game_state):
    """Применить изменение репутации"""
    if "reputation" not in game_state:
        game_state["reputation"] = {}
    
    current = game_state["reputation"].get(faction_id, 0)
    faction = FACTIONS.get(faction_id)
    
    if not faction:
        return game_state
    
    min_rep, max_rep = faction["reputation_range"]
    new_value = max(min_rep, min(max_rep, current + change))
    
    game_state["reputation"][faction_id] = new_value
    
    # Проверка на автоматические последствия
    tier = get_reputation_tier(faction_id, new_value)
    penalties = get_faction_penalties(faction_id, new_value)
    
    if penalties.get("hunted"):
        game_state["hunted_by"] = game_state.get("hunted_by", [])
        if faction_id not in game_state["hunted_by"]:
            game_state["hunted_by"].append(faction_id)
    
    # Проверка отношений с другими фракциями
    for relation_id, relation_data in FACTION_RELATIONS.items():
        if faction_id in relation_data["factions"]:
            other_faction = [f for f in relation_data["factions"] if f != faction_id][0]
            
            if relation_data["relation"] == "hostile":
                # Повышение с одной враждебной фракцией понижает с другой
                if change > 0:
                    apply_reputation_change(other_faction, -change // 2, game_state)
            elif relation_data["relation"] == "allied":
                # Повышение с союзной фракцией повышает с другой
                if change > 0:
                    apply_reputation_change(other_faction, change // 3, game_state)
    
    return game_state

def can_access_faction_content(faction_id, content_type, game_state):
    """Проверить доступ к контенту фракции"""
    faction = FACTIONS.get(faction_id)
    if not faction:
        return False, "Фракция не найдена"
    
    reputation = game_state.get("reputation", {}).get(faction_id, 0)
    tier = get_reputation_tier(faction_id, reputation)
    
    # Проверка специальных требований
    special_access = faction.get("special_access", {})
    for key, value in special_access.items():
        if key == "veronica_relationship_min":
            if game_state.get("relationships", {}).get("veronica", 0) < value:
                return False, f"Требуется отношения с Вероникой {value}+"
    
    # Проверка пути
    path_required = faction.get("preferred_paths", [])
    if path_required and content_type == "main_quest":
        if game_state.get("path") not in path_required:
            return False, f"Требуется путь: {path_required}"
    
    # Проверка уровня репутации
    if content_type == "shop":
        if tier["tier_id"] in ["hostile", "unfriendly"]:
            return False, "Фракция отказывает в обслуживании"
    elif content_type == "special_items":
        if tier["tier_id"] != "honored":
            return False, "Требуется уровень: Почтение"
    elif content_type == "quests":
        if tier["tier_id"] in ["hostile"]:
            return False, "Фракция не доверяет вам"
    
    return True, "Доступ разрешён"

def get_all_faction_standings(game_state):
    """Получить текущие отношения со всеми фракциями"""
    standings = {}
    
    for faction_id, faction in FACTIONS.items():
        reputation = game_state.get("reputation", {}).get(faction_id, 0)
        tier = get_reputation_tier(faction_id, reputation)
        bonuses = get_faction_bonuses(faction_id, reputation)
        penalties = get_faction_penalties(faction_id, reputation)
        
        standings[faction_id] = {
            "name": faction["name"],
            "reputation": reputation,
            "tier": tier,
            "bonuses": bonuses,
            "penalties": penalties
        }
    
    return standings

def get_faction_quest_givers(faction_id):
    """Получить список квестодателей фракции"""
    quest_givers = {
        "alliance": ["marcus_reid", "alliance_officer"],
        "observers": ["zara", "order_master"],
        "independence": ["volkov", "kira", "rainer"],
        "criminal_syndicate": ["veronica", "syndicate_contact"],
        "corporation_zenith": ["zenith_representative"]
    }
    return quest_givers.get(faction_id, [])
