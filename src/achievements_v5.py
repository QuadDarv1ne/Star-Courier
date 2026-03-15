# -*- coding: utf-8 -*-
"""
Star Courier - Achievements System
Система достижений для отслеживания прогресса и награждения игрока
"""

# === СЮЖЕТНЫЕ ДОСТИЖЕНИЯ ===

STORY_ACHIEVEMENTS = {
    "first_flight": {
        "id": "ach_story_01",
        "name": "Первый полёт",
        "description": "Завершите главу 1 и получите свой первый корабль.",
        "icon": "rocket",
        "hidden": False,
        "unlock_condition": {"chapter_complete": 1},
        "rewards": {"credits": 500, "experience": 100}
    },
    "echo_contact": {
        "id": "ach_story_02",
        "name": "Голос из глубины",
        "description": "Установите контакт с Эхом в главе 11.",
        "icon": "crystal",
        "hidden": False,
        "unlock_condition": {"dialogue_complete": "echo_first_contact"},
        "rewards": {"knowledge": 20, "psychic": 5}
    },
    "path_chosen": {
        "id": "ach_story_03",
        "name": "Выбор сделан",
        "description": "Выберите свой путь в главе 13.",
        "icon": "crossroad",
        "hidden": False,
        "unlock_condition": {"event": "path_selected"},
        "rewards": {"experience": 500}
    },
    "survivor_found": {
        "id": "ach_story_04",
        "name": "След выжившего",
        "description": "Найдите информацию о выжившем из Зоны Тишины.",
        "icon": "footprint",
        "hidden": False,
        "unlock_condition": {"quest_complete": "q11_02"},
        "rewards": {"knowledge": 15}
    },
    "crystal_obtained": {
        "id": "ach_story_05",
        "name": "Кристалл Времени",
        "description": "Получите Кристалл Времени из древнего храма.",
        "icon": "time_crystal",
        "hidden": False,
        "unlock_condition": {"item_obtained": "time_crystal"},
        "rewards": {"psychic": 10, "ability": "future_glimpse"}
    },
    "traitor_revealed": {
        "id": "ach_story_06",
        "name": "Лицо врага",
        "description": "Раскройте предателя в главе 15.",
        "icon": "mask",
        "hidden": True,
        "unlock_condition": {"event": "traitor_confronted"},
        "rewards": {"determination": 15}
    },
    "zone_silence_entered": {
        "id": "ach_story_07",
        "name": "Зона Тишины",
        "description": "Войдите в Зону Тишины и выживите.",
        "icon": "void",
        "hidden": False,
        "unlock_condition": {"location_visited": "zone_silence"},
        "rewards": {"experience": 300, "mental_resistance": 10}
    },
    "guardian_met": {
        "id": "ach_story_08",
        "name": "Древний Страж",
        "description": "Встретьтесь со Стражем Ядра.",
        "icon": "guardian",
        "hidden": False,
        "unlock_condition": {"dialogue_complete": "guardian_encounter"},
        "rewards": {"knowledge": 50}
    }
}

# === ДОСТИЖЕНИЯ КОНЦОВОК ===

ENDING_ACHIEVEMENTS = {
    "exile_hero": {
        "id": "ach_end_01",
        "name": "Изгнание Тьмы",
        "description": "Завершите игру финалом Изгнания.",
        "icon": "sun",
        "hidden": False,
        "unlock_condition": {"ending": "exile"},
        "rewards": {"title": "Герой Галактики", "unlock_skin": "exile_armor"}
    },
    "treaty_keeper": {
        "id": "ach_end_02",
        "name": "Хранитель Границы",
        "description": "Завершите игру финалом Договора.",
        "icon": "balance",
        "hidden": False,
        "unlock_condition": {"ending": "treaty"},
        "rewards": {"title": "Хранитель Границы", "unlock_skin": "keeper_robe"}
    },
    "transcendent": {
        "id": "ach_end_03",
        "name": "Трансценденция",
        "description": "Завершите игру финалом Слияния.",
        "icon": "infinity",
        "hidden": True,
        "unlock_condition": {"ending": "merge"},
        "rewards": {"title": "Трансцендентный", "unlock_skin": "entity_form"}
    },
    "all_endings": {
        "id": "ach_end_04",
        "name": "Мастер судеб",
        "description": "Получите все три концовки.",
        "icon": "trident",
        "hidden": True,
        "unlock_condition": {"endings_count": 3},
        "rewards": {"title": "Мастер Судеб", "credits": 50000}
    }
}

# === РОМАНТИЧЕСКИЕ ДОСТИЖЕНИЯ ===

ROMANCE_ACHIEVEMENTS = {
    "first_kiss": {
        "id": "ach_rom_01",
        "name": "Первый поцелуй",
        "description": "Начните романтические отношения с персонажем.",
        "icon": "heart",
        "hidden": False,
        "unlock_condition": {"romance_level": 50},
        "rewards": {"experience": 200}
    },
    "true_love_mia": {
        "id": "ach_rom_02",
        "name": "Тактический союз",
        "description": "Достигните максимальных отношений с Мией.",
        "icon": "heart_mia",
        "hidden": False,
        "unlock_condition": {"character_relationship": {"mia": 100}},
        "rewards": {"title": "Партнёры навек", "bonus": {"tactical_bonus": 20}}
    },
    "true_love_maria": {
        "id": "ach_rom_03",
        "name": "Исцеление сердца",
        "description": "Достигните максимальных отношений с Марией.",
        "icon": "heart_maria",
        "hidden": False,
        "unlock_condition": {"character_relationship": {"maria": 100}},
        "rewards": {"title": "Хранитель жизни", "bonus": {"healing_bonus": 20}}
    },
    "true_love_anna": {
        "id": "ach_rom_04",
        "name": "Звёздный навигатор",
        "description": "Достигните максимальных отношений с Анной.",
        "icon": "heart_anna",
        "hidden": False,
        "unlock_condition": {"character_relationship": {"anna": 100}},
        "rewards": {"title": "Проводник звёзд", "bonus": {"navigation_bonus": 20}}
    },
    "true_love_veronica": {
        "id": "ach_rom_05",
        "name": "Теневой альянс",
        "description": "Достигните максимальных отношений с Вероникой.",
        "icon": "heart_veronica",
        "hidden": False,
        "unlock_condition": {"character_relationship": {"veronica": 100}},
        "rewards": {"title": "Владелец сети", "bonus": {"intel_bonus": 30}}
    },
    "true_love_zara": {
        "id": "ach_rom_06",
        "name": "Рыцарь и мистик",
        "description": "Достигните максимальных отношений с Зарой.",
        "icon": "heart_zara",
        "hidden": False,
        "unlock_condition": {"character_relationship": {"zara": 100}},
        "rewards": {"title": "Посвящённый", "bonus": {"psychic_bonus": 25}}
    },
    "true_love_kira": {
        "id": "ach_rom_07",
        "name": "Два курьера",
        "description": "Достигните максимальных отношений с Кирой.",
        "icon": "heart_kira",
        "hidden": False,
        "unlock_condition": {"character_relationship": {"kira": 100}},
        "rewards": {"title": "Легендарный дуэт", "bonus": {"smuggling_bonus": 30}}
    },
    "heartbreaker": {
        "id": "ach_rom_08",
        "name": "Разбиватель сердец",
        "description": "Отвергните 3 романтических предложения.",
        "icon": "broken_heart",
        "hidden": True,
        "unlock_condition": {"romance_rejections": 3},
        "rewards": {"title": "Одиночка"}
    },
    "harem_end": {
        "id": "ach_rom_09",
        "name": "Невозможный выбор",
        "description": "Достигните отношений 80+ с 4 персонажами одновременно.",
        "icon": "hearts",
        "hidden": True,
        "unlock_condition": {"multiple_relationships": 4},
        "rewards": {"title": "Любимец команды"}
    }
}

# === БОЕВЫЕ ДОСТИЖЕНИЯ ===

COMBAT_ACHIEVEMENTS = {
    "first_blood": {
        "id": "ach_combat_01",
        "name": "Первая кровь",
        "description": "Победите первого врага.",
        "icon": "sword",
        "hidden": False,
        "unlock_condition": {"enemies_defeated": 1},
        "rewards": {"experience": 50}
    },
    "veteran": {
        "id": "ach_combat_02",
        "name": "Ветеран",
        "description": "Победите 100 врагов.",
        "icon": "medal",
        "hidden": False,
        "unlock_condition": {"enemies_defeated": 100},
        "rewards": {"credits": 2000, "combat_bonus": 5}
    },
    "entity_slayer": {
        "id": "ach_combat_03",
        "name": "Убийца порождений",
        "description": "Уничтожьте 10 порождений Тьмы.",
        "icon": "void_sword",
        "hidden": False,
        "unlock_condition": {"entity_spawn_killed": 10},
        "rewards": {"mental_resistance": 20, "title": "Охотник на Тьму"}
    },
    "flawless": {
        "id": "ach_combat_04",
        "name": "Безупречная победа",
        "description": "Победите босса без получения урона.",
        "icon": "shield",
        "hidden": False,
        "unlock_condition": {"boss_no_damage": True},
        "rewards": {"experience": 1000}
    },
    "pacifist_run": {
        "id": "ach_combat_05",
        "name": "Пацифист",
        "description": "Завершите главу без убийств.",
        "icon": "dove",
        "hidden": True,
        "unlock_condition": {"chapter_no_kills": True},
        "rewards": {"diplomacy": 20, "title": "Миротворец"}
    }
}

# === ДОСТИЖЕНИЯ ИССЛЕДОВАНИЯ ===

EXPLORATION_ACHIEVEMENTS = {
    "explorer_10": {
        "id": "ach_exp_01",
        "name": "Путешественник",
        "description": "Посетите 10 различных локаций.",
        "icon": "compass",
        "hidden": False,
        "unlock_condition": {"locations_visited": 10},
        "rewards": {"credits": 1000}
    },
    "explorer_all": {
        "id": "ach_exp_02",
        "name": "Картограф",
        "description": "Посетите все доступные локации.",
        "icon": "map",
        "hidden": False,
        "unlock_condition": {"all_locations": True},
        "rewards": {"title": "Картограф Галактики", "credits": 5000}
    },
    "anomaly_seeker": {
        "id": "ach_exp_03",
        "name": "Искатель аномалий",
        "description": "Обнаружьте 5 скрытых аномалий через Резонанс.",
        "icon": "radar",
        "hidden": False,
        "unlock_condition": {"anomalies_found": 5},
        "rewards": {"resonance_experience": 50}
    },
    "temple_delver": {
        "id": "ach_exp_04",
        "name": "Исследователь храмов",
        "description": "Найдите все секреты в Храме Времени.",
        "icon": "temple",
        "hidden": True,
        "unlock_condition": {"temple_secrets": True},
        "rewards": {"ancient_artifact": "time_fragment"}
    },
    "zone_survivor": {
        "id": "ach_exp_05",
        "name": "Выживший в Зоне",
        "description": "Проведите 10 единиц времени в Зоне Тишины без ментального срыва.",
        "icon": "hazard",
        "hidden": False,
        "unlock_condition": {"zone_time": 10, "no_mental_break": True},
        "rewards": {"mental_resistance": 30, "title": "Сталкер"}
    }
}

# === ДОСТИЖЕНИЯ СПОСОБНОСТЕЙ ===

ABILITY_ACHIEVEMENTS = {
    "alchemy_master": {
        "id": "ach_ab_01",
        "name": "Мастер Алхимии",
        "description": "Достигните 100 уровня в ветке Алхимии.",
        "icon": "potion",
        "hidden": False,
        "unlock_condition": {"ability_level": {"alchemy": 100}},
        "rewards": {"title": "Великий Алхимик", "recipe": "transcendence_formula"}
    },
    "biotics_master": {
        "id": "ach_ab_02",
        "name": "Мастер Биотики",
        "description": "Достигните 100 уровня в ветке Биотики.",
        "icon": "force",
        "hidden": False,
        "unlock_condition": {"ability_level": {"biotics": 100}},
        "rewards": {"title": "Биотический Мастер", "ability": "reality_anchor"}
    },
    "psychic_master": {
        "id": "ach_ab_03",
        "name": "Мастер Псионики",
        "description": "Достигните 100 уровня в ветке Псионики.",
        "icon": "mind",
        "hidden": False,
        "unlock_condition": {"ability_level": {"psychic": 100}},
        "rewards": {"title": "Псионический Мастер", "ability": "transcendence"}
    },
    "jack_of_trades": {
        "id": "ach_ab_04",
        "name": "Мастер на все руки",
        "description": "Достигните 50 уровня во всех ветках способностей.",
        "icon": "star",
        "hidden": False,
        "unlock_condition": {"all_branches_50": True},
        "rewards": {"title": "Универсал", "all_bonus": 10}
    },
    "resonance_master": {
        "id": "ach_ab_05",
        "name": "Резонанс достигнут",
        "description": "Достигните 4 уровня Резонанса.",
        "icon": "wave",
        "hidden": True,
        "unlock_condition": {"resonance_level": 4},
        "rewards": {"merge_ending_unlock": True}
    }
}

# === ДОСТИЖЕНИЯ ПУТИ ===

PATH_ACHIEVEMENTS = {
    "alliance_ally": {
        "id": "ach_path_01",
        "name": "Герой Альянса",
        "description": "Завершите игру на пути Альянса.",
        "icon": "alliance",
        "hidden": False,
        "unlock_condition": {"path": "alliance", "game_complete": True},
        "rewards": {"title": "Герой Альянса", "unlock_ship": "alliance_cruiser"}
    },
    "observer_adept": {
        "id": "ach_path_02",
        "name": "Посвящённый Ордена",
        "description": "Завершите игру на пути Наблюдателя.",
        "icon": "observer",
        "hidden": False,
        "unlock_condition": {"path": "observer", "game_complete": True},
        "rewards": {"title": "Посвящённый", "unlock_ability": "ancient_knowledge"}
    },
    "independent_legend": {
        "id": "ach_path_03",
        "name": "Легенда Независимости",
        "description": "Завершите игру на пути Независимости.",
        "icon": "independence",
        "hidden": False,
        "unlock_condition": {"path": "independence", "game_complete": True},
        "rewards": {"title": "Свободный Капитан", "unlock_ship": "custom_freighter"}
    },
    "all_paths": {
        "id": "ach_path_04",
        "name": "Все дороги",
        "description": "Завершите игру на всех трёх путях.",
        "icon": "triple",
        "hidden": True,
        "unlock_condition": {"all_paths_complete": True},
        "rewards": {"title": "Повелитель Судеб", "credits": 100000}
    }
}

# === СЕКРЕТНЫЕ ДОСТИЖЕНИЯ ===

SECRET_ACHIEVEMENTS = {
    "entity_friend": {
        "id": "ach_sec_01",
        "name": "Понимание",
        "description": "Проведите 5 мирных диалогов с Сущностью.",
        "icon": "handshake",
        "hidden": True,
        "unlock_condition": {"entity_peaceful_dialogues": 5},
        "rewards": {"entity_trust": 20}
    },
    "echo_memories": {
        "id": "ach_sec_02",
        "name": "Носитель памяти",
        "description": "Узнайте всю историю цивилизации Эха.",
        "icon": "memory",
        "hidden": True,
        "unlock_condition": {"echo_lore_complete": True},
        "rewards": {"ancient_knowledge": 50}
    },
    "time_paradox": {
        "id": "ach_sec_03",
        "name": "Парадокс времени",
        "description": "Используйте Кристалл Времени, чтобы увидеть своё будущее.",
        "icon": "clock",
        "hidden": True,
        "unlock_condition": {"time_paradox_seen": True},
        "rewards": {"psychic": 15}
    },
    "survivor_truth": {
        "id": "ach_sec_04",
        "name": "Правда выжившего",
        "description": "Узнайте истинную историю выжившего из Зоны Тишины.",
        "icon": "truth",
        "hidden": True,
        "unlock_condition": {"survivor_truth_revealed": True},
        "rewards": {"knowledge": 30}
    },
    "perfect_run": {
        "id": "ach_sec_05",
        "name": "Идеальное прохождение",
        "description": "Завершите игру: ни одного проваленного квеста, все отношения 80+.",
        "icon": "crown",
        "hidden": True,
        "unlock_condition": {"perfect_run": True},
        "rewards": {"title": "Идеальный Курьер", "skin": "golden_ship"}
    }
}

# === СТАТИСТИЧЕСКИЕ ДОСТИЖЕНИЯ ===

STATISTICS_ACHIEVEMENTS = {
    "credits_100k": {
        "id": "ach_stat_01",
        "name": "Богатый курьер",
        "description": "Накопите 100,000 кредитов.",
        "icon": "coins",
        "hidden": False,
        "unlock_condition": {"credits_earned": 100000},
        "rewards": {"title": "Миллионер"}
    },
    "quests_50": {
        "id": "ach_stat_02",
        "name": "Трудоголик",
        "description": "Завершите 50 квестов.",
        "icon": "scroll",
        "hidden": False,
        "unlock_condition": {"quests_completed": 50},
        "rewards": {"experience": 5000}
    },
    "dialogues_500": {
        "id": "ach_stat_03",
        "name": "Дипломат",
        "description": "Проведите 500 диалогов.",
        "icon": "speech",
        "hidden": False,
        "unlock_condition": {"dialogues_count": 500},
        "rewards": {"diplomacy": 30}
    },
    "time_played": {
        "id": "ach_stat_04",
        "name": "Преданный игрок",
        "description": "Проведите в игре 50 часов.",
        "icon": "hourglass",
        "hidden": False,
        "unlock_condition": {"playtime_hours": 50},
        "rewards": {"title": "Ветеран Космоса"}
    },
    "all_secrets": {
        "id": "ach_stat_05",
        "name": "Собиратель секретов",
        "description": "Найдите все секретные локации и предметы.",
        "icon": "key",
        "hidden": True,
        "unlock_condition": {"secrets_found": "all"},
        "rewards": {"title": "Хранитель Тайн", "artifact": "void_key"}
    }
}

# Объединение всех достижений
ALL_ACHIEVEMENTS = {
    "story": STORY_ACHIEVEMENTS,
    "ending": ENDING_ACHIEVEMENTS,
    "romance": ROMANCE_ACHIEVEMENTS,
    "combat": COMBAT_ACHIEVEMENTS,
    "exploration": EXPLORATION_ACHIEVEMENTS,
    "ability": ABILITY_ACHIEVEMENTS,
    "path": PATH_ACHIEVEMENTS,
    "secret": SECRET_ACHIEVEMENTS,
    "statistics": STATISTICS_ACHIEVEMENTS
}

def get_all_achievements():
    """Получить плоский список всех достижений"""
    flat_list = {}
    for category, achievements in ALL_ACHIEVEMENTS.items():
        for ach_id, ach_data in achievements.items():
            flat_list[ach_id] = ach_data
    return flat_list

def check_achievement_unlock(achievement_id, game_state):
    """Проверить, разблокировано ли достижение"""
    achievement = get_all_achievements().get(achievement_id)
    if not achievement:
        return False
    
    condition = achievement["unlock_condition"]
    
    for key, value in condition.items():
        if key == "chapter_complete":
            if game_state.get("current_chapter", 0) < value:
                return False
        elif key == "dialogue_complete":
            if value not in game_state.get("completed_dialogues", []):
                return False
        elif key == "quest_complete":
            if value not in game_state.get("completed_quests", []):
                return False
        elif key == "ending":
            if game_state.get("ending") != value:
                return False
        elif key == "path":
            if game_state.get("path") != value:
                return False
        elif key == "enemies_defeated":
            if game_state.get("enemies_defeated", 0) < value:
                return False
        elif key == "locations_visited":
            if len(game_state.get("visited_locations", set())) < value:
                return False
        elif key == "character_relationship":
            for char, level in value.items():
                if game_state.get("relationships", {}).get(char, 0) < level:
                    return False
        elif key == "ability_level":
            for branch, level in value.items():
                if game_state.get("abilities", {}).get(branch, 0) < level:
                    return False
        elif key == "resonance_level":
            if game_state.get("resonance_level", 0) < value:
                return False
        elif key == "game_complete":
            if not game_state.get("game_complete", False):
                return False
    
    return True

def unlock_achievement(achievement_id, game_state):
    """Разблокировать достижение и применить награды"""
    achievement = get_all_achievements().get(achievement_id)
    if not achievement:
        return None
    
    # Применение наград
    rewards = achievement.get("rewards", {})
    for reward_type, value in rewards.items():
        if reward_type == "credits":
            game_state["credits"] = game_state.get("credits", 0) + value
        elif reward_type == "experience":
            game_state["experience"] = game_state.get("experience", 0) + value
        elif reward_type == "psychic":
            game_state["abilities"]["psychic"] = game_state["abilities"].get("psychic", 0) + value
        elif reward_type == "knowledge":
            game_state["knowledge"] = game_state.get("knowledge", 0) + value
        elif reward_type == "title":
            if "titles" not in game_state:
                game_state["titles"] = []
            game_state["titles"].append(value)
    
    # Добавление в список разблокированных
    if "unlocked_achievements" not in game_state:
        game_state["unlocked_achievements"] = []
    game_state["unlocked_achievements"].append(achievement_id)
    
    return achievement

def get_achievement_progress(game_state):
    """Получить прогресс по достижениям"""
    all_ach = get_all_achievements()
    unlocked = game_state.get("unlocked_achievements", [])
    
    total = len(all_ach)
    unlocked_count = len(unlocked)
    percentage = (unlocked_count / total * 100) if total > 0 else 0
    
    # Прогресс по категориям
    by_category = {}
    for category, achievements in ALL_ACHIEVEMENTS.items():
        cat_total = len(achievements)
        cat_unlocked = sum(1 for ach_id in achievements if ach_id in unlocked)
        by_category[category] = {
            "total": cat_total,
            "unlocked": cat_unlocked,
            "percentage": (cat_unlocked / cat_total * 100) if cat_total > 0 else 0
        }
    
    return {
        "total": total,
        "unlocked": unlocked_count,
        "percentage": percentage,
        "by_category": by_category
    }

def get_visible_achievements(game_state):
    """Получить список видимых достижений (скрытые показываются только после разблокировки)"""
    all_ach = get_all_achievements()
    unlocked = set(game_state.get("unlocked_achievements", []))
    
    visible = {}
    for ach_id, ach_data in all_ach.items():
        if not ach_data.get("hidden", False) or ach_id in unlocked:
            visible[ach_id] = ach_data.copy()
            if ach_id not in unlocked:
                visible[ach_id]["unlocked"] = False
            else:
                visible[ach_id]["unlocked"] = True
    
    return visible
