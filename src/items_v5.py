# -*- coding: utf-8 -*-
"""
Star Courier - Items & Equipment Database
База данных предметов и оборудования
"""

# === КАТЕГОРИИ ПРЕДМЕТОВ ===

ITEM_CATEGORIES = {
    "weapon": "Оружие",
    "armor": "Броня",
    "consumable": "Расходники",
    "artifact": "Артефакты",
    "ship_upgrade": "Улучшения корабля",
    "key_item": "Ключевые предметы",
    "crafting_material": "Материалы для крафта",
    "data": "Данные и информация"
}

# === ОРУЖИЕ ===

WEAPONS = {
    "pulse_pistol": {
        "id": "weapon_01",
        "name": "Импульсный пистолет",
        "description": "Стандартное оружие космических курьеров. Надёжный, компактный, смертоносный.",
        "type": "weapon",
        "subtype": "pistol",
        "damage": 25,
        "range": "medium",
        "fire_rate": "fast",
        "accuracy": 85,
        "requirements": {"level": 1},
        "price": {"buy": 500, "sell": 250},
        "rarity": "common"
    },
    "plasma_rifle": {
        "id": "weapon_02",
        "name": "Плазменная винтовка",
        "description": "Военное оружие средней дальности. Плазменные заряды пробивают большинство видов брони.",
        "type": "weapon",
        "subtype": "rifle",
        "damage": 45,
        "range": "long",
        "fire_rate": "medium",
        "accuracy": 75,
        "requirements": {"level": 5, "combat": 20},
        "price": {"buy": 2500, "sell": 1250},
        "rarity": "uncommon"
    },
    "biotic_amp": {
        "id": "weapon_03",
        "name": "Биотический усилитель",
        "description": "Устройство, усиливающее биотические способности. Не является оружием в традиционном смысле.",
        "type": "weapon",
        "subtype": "biotic_focus",
        "damage": 0,
        "biotic_boost": 30,
        "range": "variable",
        "requirements": {"level": 10, "biotics": 40},
        "price": {"buy": 8000, "sell": 4000},
        "rarity": "rare"
    },
    "psychic_crystal": {
        "id": "weapon_04",
        "name": "Псионический кристалл",
        "description": "Кристалл, настроенный на ментальные частоты. Усиливает Psychic-способности владельца.",
        "type": "weapon",
        "subtype": "psychic_focus",
        "damage": 0,
        "psychic_boost": 40,
        "mental_damage_bonus": 20,
        "requirements": {"level": 15, "psychic": 50},
        "price": {"buy": 15000, "sell": 7500},
        "rarity": "rare",
        "special": "entity_damage_bonus"
    },
    "void_blade": {
        "id": "weapon_05",
        "name": "Клинок Пустоты",
        "description": "Древнее оружие Предтеч. Лезвие из чистой энергии разрезает саму ткань реальности.",
        "type": "weapon",
        "subtype": "melee",
        "damage": 80,
        "armor_pierce": 100,
        "entity_damage": 50,
        "requirements": {"level": 25, "combat": 60, "psychic": 40},
        "price": {"buy": 50000, "sell": 25000},
        "rarity": "legendary",
        "quest_item": True,
        "special": "reality_cut"
    },
    "entity_disruptor": {
        "id": "weapon_06",
        "name": "Разрушитель Сущности",
        "description": "Оружие, созданное Предтечами для борьбы с порождениями Сущности. Эффективно только против аномальных существ.",
        "type": "weapon",
        "subtype": "special",
        "damage": 10,  # Низкий урон против обычных врагов
        "entity_damage": 150,  # Огромный урон против порождений
        "requirements": {"level": 20, "resonance_level": 2},
        "price": {"buy": 35000, "sell": 17500},
        "rarity": "epic",
        "chapter_available": [16, 17, 18]
    }
}

# === БРОНЯ ===

ARMOR = {
    "courier_vest": {
        "id": "armor_01",
        "name": "Жилет курьера",
        "description": "Лёгкая броня под одеждой. Не сковывает движения, обеспечивает базовую защиту.",
        "type": "armor",
        "subtype": "light",
        "defense": 15,
        "mobility": 95,
        "stealth": 90,
        "requirements": {"level": 1},
        "price": {"buy": 800, "sell": 400},
        "rarity": "common"
    },
    "tactical_armor": {
        "id": "armor_02",
        "name": "Тактическая броня",
        "description": "Военный стандарт. Баланс между защитой и мобильностью.",
        "type": "armor",
        "subtype": "medium",
        "defense": 35,
        "mobility": 80,
        "stealth": 60,
        "requirements": {"level": 8, "combat": 25},
        "price": {"buy": 3500, "sell": 1750},
        "rarity": "uncommon"
    },
    "assault_suit": {
        "id": "armor_03",
        "name": "Штурмовой костюм",
        "description": "Тяжёлая броня для фронтовых операций. Выживаемость максимальна, мобильность снижена.",
        "type": "armor",
        "subtype": "heavy",
        "defense": 60,
        "mobility": 60,
        "stealth": 30,
        "requirements": {"level": 15, "combat": 50},
        "price": {"buy": 12000, "sell": 6000},
        "rarity": "rare"
    },
    "observer_robe": {
        "id": "armor_04",
        "name": "Мантия Наблюдателя",
        "description": "Церемониальная броня рыцарей Ордена. Усиливает Psychic-способности и защищает от ментальных атак.",
        "type": "armor",
        "subtype": "psychic",
        "defense": 25,
        "psychic_boost": 20,
        "mental_resistance": 50,
        "mobility": 85,
        "requirements": {"level": 20, "psychic": 60, "path": "observer"},
        "price": {"buy": 25000, "sell": 12500},
        "rarity": "epic",
        "path_required": "observer"
    },
    "void_armor": {
        "id": "armor_05",
        "name": "Броня Пустоты",
        "description": "Древний доспех Предтеч. Самовосстанавливается, поглощает урон и защищает от влияния Сущности.",
        "type": "armor",
        "subtype": "artifact",
        "defense": 80,
        "entity_resistance": 70,
        "mobility": 75,
        "self_repair": True,
        "requirements": {"level": 30, "resonance_level": 3},
        "price": {"buy": 100000, "sell": 50000},
        "rarity": "legendary",
        "quest_item": True
    }
}

# === РАСХОДНИКИ ===

CONSUMABLES = {
    "stim_pack": {
        "id": "consumable_01",
        "name": "Стим-пакет",
        "description": "Стандартный медицинский стимулятор. Восстанавливает 30 HP.",
        "type": "consumable",
        "subtype": "healing",
        "effect": {"heal": 30},
        "uses": 1,
        "requirements": {"level": 1},
        "price": {"buy": 100, "sell": 50},
        "rarity": "common"
    },
    "advanced_medkit": {
        "id": "consumable_02",
        "name": "Продвинутая аптечка",
        "description": "Полевой медицинский набор. Восстанавливает 75 HP и лечит лёгкие ранения.",
        "type": "consumable",
        "subtype": "healing",
        "effect": {"heal": 75, "cure_light_wounds": True},
        "uses": 1,
        "requirements": {"level": 5},
        "price": {"buy": 500, "sell": 250},
        "rarity": "uncommon"
    },
    "psychic_stimulant": {
        "id": "consumable_03",
        "name": "Психический стимулятор",
        "description": "Временное усиление Psychic-способностей. +30 к Psychic на 5 минут.",
        "type": "consumable",
        "subtype": "buff",
        "effect": {"psychic_boost": 30, "duration": 300},
        "uses": 1,
        "requirements": {"level": 10, "psychic": 30},
        "price": {"buy": 1500, "sell": 750},
        "rarity": "rare",
        "side_effects": {"mental_fatigue": True}
    },
    "anomaly_shield_potion": {
        "id": "consumable_04",
        "name": "Зелье защиты от аномалий",
        "description": "Алхимическое средство для защиты от воздействия аномальных зон. Длительность: 1 час.",
        "type": "consumable",
        "subtype": "protection",
        "effect": {"anomaly_resistance": 50, "duration": 3600},
        "uses": 1,
        "requirements": {"level": 12, "alchemy": 40},
        "price": {"buy": 2000, "sell": 1000},
        "rarity": "rare",
        "crafted": True
    },
    "entity_repellent": {
        "id": "consumable_05",
        "name": "Отпугиватель Сущности",
        "description": "Концентрированная смесь, отпугивающая порождения Тьмы. Длительность: 10 минут.",
        "type": "consumable",
        "subtype": "protection",
        "effect": {"entity_repel": True, "duration": 600},
        "uses": 1,
        "requirements": {"level": 18, "alchemy": 60, "resonance_level": 2},
        "price": {"buy": 5000, "sell": 2500},
        "rarity": "epic",
        "chapter_available": range(15, 19)
    },
    "resurrection_vial": {
        "id": "consumable_06",
        "name": "Фиал воскрешения",
        "description": "Автоматически resurrects владельца при смерти с 30% HP. Одноразовый.",
        "type": "consumable",
        "subtype": "special",
        "effect": {"resurrect": True, "hp_on_resurrect": 30},
        "uses": 1,
        "requirements": {"level": 20, "alchemy": 70},
        "price": {"buy": 25000, "sell": 12500},
        "rarity": "legendary",
        "crafted": True
    }
}

# === АРТЕФАКТЫ ===

ARTIFACTS = {
    "time_crystal": {
        "id": "artifact_01",
        "name": "Кристалл Времени",
        "description": "Древний артефакт Предтеч. Позволяет видеть возможные futures.",
        "type": "artifact",
        "effect": {
            "future_glimpse": True,
            "psychic_boost": 15,
            "time_manipulation": "limited"
        },
        "requirements": {"level": 14, "psychic": 50},
        "rarity": "legendary",
        "quest_item": True,
        "unique": True
    },
    "resonance_crystal": {
        "id": "artifact_02",
        "name": "Кристалл Резонанса",
        "description": "Позволяет чувствовать присутствие Сущности и её порождений.",
        "type": "artifact",
        "effect": {
            "entity_detection": True,
            "resonance_level_boost": 1,
            "mental_resistance": 20
        },
        "requirements": {"level": 10},
        "rarity": "epic",
        "unique": True
    },
    "anchor_fragment": {
        "id": "artifact_03",
        "name": "Осколок Якоря",
        "description": "Частица станции-якоря. Связывает владельца с Сущностью.",
        "type": "artifact",
        "effect": {
            "entity_communion": True,
            "psychic_boost": 25,
            "entity_influence": 20  # Риск
        },
        "requirements": {"level": 16, "resonance_level": 3},
        "rarity": "legendary",
        "quest_item": True,
        "unique": True,
        "chapter_available": range(16, 19)
    },
    "guardian_memory": {
        "id": "artifact_04",
        "name": "Память Стража",
        "description": "Кристалл с воспоминаниями Ар'Таниса. Даёт знание о борьбе с Сущностью.",
        "type": "artifact",
        "effect": {
            "knowledge_boost": 50,
            "entity_weakness_insight": True,
            "ancient_memories": True
        },
        "requirements": {"level": 17},
        "rarity": "legendary",
        "quest_item": True,
        "unique": True,
        "chapter_available": [17, 18]
    }
}

# === УЛУЧШЕНИЯ КОРАБЛЯ ===

SHIP_UPGRADES = {
    "shield_reinforcement": {
        "id": "ship_01",
        "name": "Усиление щитов",
        "description": "Модернизация энергетических щитов корабля. +30% к защите.",
        "type": "ship_upgrade",
        "subtype": "defense",
        "effect": {"shield_capacity": 30, "recharge_rate": 10},
        "install_cost": 5000,
        "requirements": {"tech": 30},
        "rarity": "uncommon"
    },
    "hyperdrive_upgrade": {
        "id": "ship_02",
        "name": "Улучшение гипердвигателя",
        "description": "Сокращает время гиперпрыжков на 25%.",
        "type": "ship_upgrade",
        "subtype": "propulsion",
        "effect": {"jump_speed": 25, "fuel_efficiency": 15},
        "install_cost": 8000,
        "requirements": {"tech": 40, "sergey_relationship": 40},
        "rarity": "rare"
    },
    "anomaly_detector": {
        "id": "ship_03",
        "name": "Детектор аномалий",
        "description": "Датчики для обнаружения пространственных аномалий на большом расстоянии.",
        "type": "ship_upgrade",
        "subtype": "sensors",
        "effect": {"anomaly_detection_range": 200, "early_warning": True},
        "install_cost": 12000,
        "requirements": {"tech": 50, "anna_relationship": 40},
        "rarity": "rare",
        "quest_item": True
    },
    "entity_shielding": {
        "id": "ship_04",
        "name": "Защита от Сущности",
        "description": "Древняя технология для защиты корабля от влияния Сущности.",
        "type": "ship_upgrade",
        "subtype": "defense",
        "effect": {"entity_resistance": 60, "mental_protection": 40},
        "install_cost": 35000,
        "requirements": {"resonance_level": 3, "tech": 60},
        "rarity": "legendary",
        "chapter_available": range(15, 19),
        "quest_item": True
    },
    "cargo_expansion": {
        "id": "ship_05",
        "name": "Расширение грузового отсека",
        "description": "Увеличивает вместимость корабля на 50%.",
        "type": "ship_upgrade",
        "subtype": "utility",
        "effect": {"cargo_capacity": 50},
        "install_cost": 3000,
        "requirements": {"tech": 20},
        "rarity": "common"
    },
    "stealth_system": {
        "id": "ship_06",
        "name": "Система скрытности",
        "description": "Позволяет избегать обнаружения кораблём противника.",
        "type": "ship_upgrade",
        "subtype": "utility",
        "effect": {"stealth": 70, "detection_reduction": 50},
        "install_cost": 15000,
        "requirements": {"tech": 50, "veronica_relationship": 50},
        "rarity": "epic"
    },
    "weapon_system_advanced": {
        "id": "ship_07",
        "name": "Продвинутая система вооружения",
        "description": "Автоматические турели и улучшенное наведение.",
        "type": "ship_upgrade",
        "subtype": "weapon",
        "effect": {"weapon_damage": 40, "accuracy": 25, "auto_turret": True},
        "install_cost": 18000,
        "requirements": {"tech": 55, "combat": 40},
        "rarity": "epic"
    }
}

# === КЛЮЧЕВЫЕ ПРЕДМЕТЫ ===

KEY_ITEMS = {
    "courier_license": {
        "id": "key_01",
        "name": "Лицензия курьера",
        "description": "Официальное разрешение на деятельность курьера в галактике.",
        "type": "key_item",
        "unique": True,
        "chapter_obtained": 1
    },
    "stranger_registration": {
        "id": "key_02",
        "name": "Регистрация «Странника»",
        "description": "Документы на владение кораблём.",
        "type": "key_item",
        "unique": True,
        "chapter_obtained": 1
    },
    "vera_data_drive": {
        "id": "key_03",
        "name": "Диск данных Веры",
        "description": "Исследования Веры об аномалиях. Ключ к пониманию Сущности.",
        "type": "key_item",
        "unique": True,
        "chapter_obtained": 12,
        "quest_related": "q12_01"
    },
    "echo_crystal": {
        "id": "key_04",
        "name": "Кристалл Эха",
        "description": "Хранилище сознания древней цивилизации.",
        "type": "key_item",
        "unique": True,
        "chapter_obtained": 11,
        "quest_related": "q11_01"
    },
    "path_token": {
        "id": "key_05",
        "name": "Символ пути",
        "description": "Знак принадлежности к выбранной фракции.",
        "type": "key_item",
        "unique": True,
        "chapter_obtained": 13,
        "path_dependent": True
    },
    "station_core_key": {
        "id": "key_06",
        "name": "Ключ ядра станции",
        "description": "Древний ключ от ядра станции-якоря.",
        "type": "key_item",
        "unique": True,
        "chapter_obtained": 17,
        "quest_related": "q17_03"
    }
}

# === МАТЕРИАЛЫ ДЛЯ КРАФТА ===

CRAFTING_MATERIALS = {
    "rare_metal": {
        "id": "mat_01",
        "name": "Редкий металл",
        "description": "Высококачественный сплав для улучшения оборудования.",
        "type": "crafting_material",
        "rarity": "uncommon",
        "price": {"buy": 200, "sell": 100}
    },
    "crystal_fragment": {
        "id": "mat_02",
        "name": "Осколок кристалла",
        "description": "Кусочек древнего кристалла с остатками энергии.",
        "type": "crafting_material",
        "rarity": "rare",
        "price": {"buy": 800, "sell": 400}
    },
    "entity_sample": {
        "id": "mat_03",
        "name": "Образец Сущности",
        "description": "Физическое проявление Сущности. Очень опасно в обращении.",
        "type": "crafting_material",
        "rarity": "legendary",
        "chapter_available": range(15, 19),
        "price": {"buy": 10000, "sell": 5000},
        "danger": "extreme"
    },
    "ancient_circuit": {
        "id": "mat_04",
        "name": "Древняя схема",
        "description": "Технология Предтеч, непонятная современным учёным.",
        "type": "crafting_material",
        "rarity": "epic",
        "price": {"buy": 3000, "sell": 1500}
    },
    "biotic_enhancer": {
        "id": "mat_05",
        "name": "Биотический усилитель",
        "description": "Биологический компонент для усиления способностей.",
        "type": "crafting_material",
        "rarity": "rare",
        "price": {"buy": 1200, "sell": 600},
        "requires": {"alchemy": 50}
    }
}

# === ДАННЫЕ И ИНФОРМАЦИЯ ===

DATA_ITEMS = {
    "star_map": {
        "id": "data_01",
        "name": "Звёздная карта",
        "description": "Подробная карта сектора с указанием маршрутов.",
        "type": "data",
        "effect": {"navigation_bonus": 10},
        "price": {"buy": 500, "sell": 250}
    },
    "intel_dossier": {
        "id": "data_02",
        "name": "Досье с разведданными",
        "description": "Собранные Вероникой данные о конкретной цели.",
        "type": "data",
        "effect": {"intel_quality": "high"},
        "price": {"buy": 2000, "sell": 1000},
        "veronica_exclusive": True
    },
    "ancient_text": {
        "id": "data_03",
        "name": "Древний текст",
        "description": "Записи Предтеч о природе Сущности.",
        "type": "data",
        "effect": {"knowledge_boost": 20, "entity_insight": True},
        "price": {"buy": 5000, "sell": 2500},
        "rarity": "epic"
    },
    "research_notes": {
        "id": "data_04",
        "name": "Исследовательские записи",
        "description": "Научные данные о древних артефактах.",
        "type": "data",
        "effect": {"crafting_bonus": 15},
        "price": {"buy": 1500, "sell": 750}
    }
}

# Объединение всех предметов
ALL_ITEMS = {
    "weapons": WEAPONS,
    "armor": ARMOR,
    "consumables": CONSUMABLES,
    "artifacts": ARTIFACTS,
    "ship_upgrades": SHIP_UPGRADES,
    "key_items": KEY_ITEMS,
    "crafting_materials": CRAFTING_MATERIALS,
    "data": DATA_ITEMS
}

def get_item(item_id):
    """Получить предмет по ID"""
    for category, items in ALL_ITEMS.items():
        for item_key, item in items.items():
            if item.get("id") == item_id:
                return item
    return None

def get_items_by_category(category):
    """Получить все предметы категории"""
    return ALL_ITEMS.get(category, {})

def get_items_by_rarity(rarity):
    """Получить все предметы определённой редкости"""
    result = []
    for category, items in ALL_ITEMS.items():
        for item_key, item in items.items():
            if item.get("rarity") == rarity:
                result.append(item)
    return result

def can_use_item(item_id, game_state):
    """Проверить, может ли персонаж использовать предмет"""
    item = get_item(item_id)
    if not item:
        return False, "Предмет не найден"
    
    requirements = item.get("requirements", {})
    
    for req_type, value in requirements.items():
        if req_type == "level":
            if game_state.get("level", 1) < value:
                return False, f"Требуется уровень {value}"
        elif req_type == "psychic":
            if game_state.get("abilities", {}).get("psychic", 0) < value:
                return False, f"Требуется Psychic {value}"
        elif req_type == "biotics":
            if game_state.get("abilities", {}).get("biotics", 0) < value:
                return False, f"Требуется Biotics {value}"
        elif req_type == "combat":
            if game_state.get("combat", 0) < value:
                return False, f"Требуется Combat {value}"
        elif req_type == "tech":
            if game_state.get("tech", 0) < value:
                return False, f"Требуется Tech {value}"
        elif req_type == "resonance_level":
            if game_state.get("resonance_level", 0) < value:
                return False, f"Требуется Резонанс уровня {value}"
        elif req_type == "path":
            if game_state.get("path") != value:
                return False, f"Требуется путь: {value}"
    
    return True, "Может использовать"

def apply_item_effect(item_id, game_state):
    """Применить эффект предмета"""
    item = get_item(item_id)
    if not item:
        return game_state
    
    effect = item.get("effect", {})
    
    for effect_type, value in effect.items():
        if effect_type == "heal":
            current_hp = game_state.get("hp", 100)
            game_state["hp"] = min(100, current_hp + value)
        elif effect_type == "psychic_boost":
            if "temporary_boosts" not in game_state:
                game_state["temporary_boosts"] = {}
            game_state["temporary_boosts"]["psychic"] = value
        elif effect_type == "knowledge_boost":
            game_state["knowledge"] = game_state.get("knowledge", 0) + value
    
    return game_state

def get_shop_inventory(location_id, game_state):
    """Получить инвентарь магазина для локации"""
    location_inventory = []
    
    # Базовые предметы доступны везде
    location_inventory.extend([
        WEAPONS["pulse_pistol"],
        ARMOR["courier_vest"],
        CONSUMABLES["stim_pack"],
        CONSUMABLES["advanced_medkit"],
        DATA_ITEMS["star_map"]
    ])
    
    # Дополнительные предметы в зависимости от локации
    if location_id == "station_crossroads":
        location_inventory.extend([
            WEAPONS["plasma_rifle"],
            ARMOR["tactical_armor"],
            SHIP_UPGRADES["shield_reinforcement"],
            SHIP_UPGRADES["cargo_expansion"]
        ])
    
    # Редкие предметы только в специальных местах
    if location_id == "observer_sanctuary" and game_state.get("path") == "observer":
        location_inventory.extend([
            ARMOR["observer_robe"],
            ARTIFACTS["resonance_crystal"],
            WEAPONS["psychic_crystal"]
        ])
    
    return location_inventory
