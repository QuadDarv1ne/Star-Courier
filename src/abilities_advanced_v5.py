# -*- coding: utf-8 -*-
"""
Star Courier - Abilities System Extension for Chapters 11-18
Расширение системы способностей для финальной части игры
"""

# === ALCHEMY ABILITIES (Уровни 50-100) ===

ALCHEMY_ADVANCED = {
    "anomaly_antidote": {
        "id": "alc_50",
        "name": "Противоядие от Аномалий",
        "description": "Создание препаратов, защищающих от воздействия аномальных зон.",
        "branch": "alchemy",
        "level_required": 50,
        "effects": {
            "anomaly_resistance": 40,
            "mental_protection": 20
        },
        "cost": {"ingredients": 3, "credits": 500},
        "chapters": [11, 12, 16, 17],
        "quest_unlock": "q12_01"
    },
    "combat_stim_supreme": {
        "id": "alc_60",
        "name": "Боевой Стимулятор Высшего класса",
        "description": "Мощный стимулятор, временно увеличивающий все боевые характеристики.",
        "branch": "alchemy",
        "level_required": 60,
        "effects": {
            "combat_boost": 50,
            "duration": 3,
            "side_effect": "fatigue_after"
        },
        "cost": {"ingredients": 5, "credits": 1000},
        "chapters": [14, 15, 17, 18]
    },
    "mental_shield_serum": {
        "id": "alc_70",
        "name": "Сыворотка Ментального Щита",
        "description": "Защита от Psychic атак и ментального воздействия Сущности.",
        "branch": "alchemy",
        "level_required": 70,
        "effects": {
            "psychic_resistance": 60,
            "entity_contact_protection": True
        },
        "cost": {"ingredients": 7, "rare_components": 1, "credits": 2500},
        "chapters": [16, 17, 18],
        "quest_unlock": "q16_01"
    },
    "resurrection_draft": {
        "id": "alc_80",
        "name": "Эликсир Возрождения",
        "description": "Экстремальный препарат, способный вернуть к жизни при критических ранениях.",
        "branch": "alchemy",
        "level_required": 80,
        "effects": {
            "revive": True,
            "hp_restore": 30,
            "uses_per_chapter": 1
        },
        "cost": {"ingredients": 10, "rare_components": 3, "credits": 10000},
        "chapters": [17, 18],
        "quest_unlock": "q17_02"
    },
    "entity_essence_extract": {
        "id": "alc_90",
        "name": "Экстракт Сущности",
        "description": "Опасный препарат из останков порождений Тьмы. Даёт временное усиление, но имеет риск мутации.",
        "branch": "alchemy",
        "level_required": 90,
        "effects": {
            "all_stats_boost": 30,
            "mutation_risk": 25,
            "psychic_sensitivity": 50
        },
        "cost": {"entity_remains": 5, "rare_components": 5, "credits": 50000},
        "chapters": [17, 18],
        "special_requirement": "entity_sample"
    },
    "transcendence_formula": {
        "id": "alc_100",
        "name": "Формула Трансценденции",
        "description": "Легендарный препарат, открывающий путь к финалу Слияния.",
        "branch": "alchemy",
        "level_required": 100,
        "effects": {
            "merge_ending_unlock": True,
            "psychic_boost": 100,
            "permanent_transformation": True
        },
        "cost": {"time_crystal_fragment": 1, "entity_core": 1, "ancient_knowledge": 10},
        "chapters": [18],
        "quest_unlock": "q17_03"
    }
}

# === BIOTICS ABILITIES (Уровни 50-100) ===

BIOTICS_ADVANCED = {
    "gravity_mastery": {
        "id": "bio_50",
        "name": "Мастерство Гравитации",
        "description": "Точное управление гравитационными полями для боя и навигации.",
        "branch": "biotics",
        "level_required": 50,
        "effects": {
            "gravity_damage": 40,
            "enemy_slow": 50,
            "mobility_boost": 30
        },
        "cooldown": 3,
        "chapters": [11, 12, 13, 14, 15]
    },
    "kinetic_barricade": {
        "id": "bio_60",
        "name": "Кинетическая Баррикада",
        "description": "Мощный щит из биотической энергии, защищающий всю команду.",
        "branch": "biotics",
        "level_required": 60,
        "effects": {
            "team_shield": 200,
            "duration": 4,
            "damage_reflection": 25
        },
        "cooldown": 5,
        "chapters": [14, 15, 16, 17, 18]
    },
    "biotic_charge_devastating": {
        "id": "bio_70",
        "name": "Разрушительный Биотический Заряд",
        "description": "Телепортация сквозь врагов с массивным уроном по площади.",
        "branch": "biotics",
        "level_required": 70,
        "effects": {
            "aoe_damage": 150,
            "stun": 2,
            "self_shield": 50
        },
        "cooldown": 4,
        "chapters": [16, 17, 18]
    },
    "nova_burst": {
        "id": "bio_80",
        "name": "Взрыв Новы",
        "description": "Высвобождение всей биотической энергии в разрушительной волне.",
        "branch": "biotics",
        "level_required": 80,
        "effects": {
            "massive_aoe_damage": 300,
            "knockback": "large",
            "self_stun": 1
        },
        "cooldown": 8,
        "chapters": [17, 18]
    },
    "singularity_control": {
        "id": "bio_90",
        "name": "Контроль Сингулярности",
        "description": "Создание контролируемой мини-сингулярности, поглощающей врагов.",
        "branch": "biotics",
        "level_required": 90,
        "effects": {
            "black_hole": True,
            "duration": 5,
            "damage_per_second": 50
        },
        "cooldown": 10,
        "chapters": [17, 18]
    },
    "reality_anchor": {
        "id": "bio_100",
        "name": "Якорь Реальности",
        "description": "Биотическая стабилизация пространства против аномалий Сущности.",
        "branch": "biotics",
        "level_required": 100,
        "effects": {
            "anomaly_negation": True,
            "reality_stabilization": 100,
            "exile_ending_boost": True
        },
        "cooldown": 15,
        "chapters": [17, 18],
        "quest_unlock": "q17_03"
    }
}

# === PSYCHIC ABILITIES (Уровни 50-100) ===

PSYCHIC_ADVANCED = {
    "mind_shield_collective": {
        "id": "psy_50",
        "name": "Коллективный Ментальный Щит",
        "description": "Защита разума всей команды от Psychic атак.",
        "branch": "psychic",
        "level_required": 50,
        "effects": {
            "team_psychic_defense": 60,
            "confusion_immunity": True
        },
        "sustain": True,
        "chapters": [11, 12, 13, 14, 15, 16]
    },
    "domination_mass": {
        "id": "psy_60",
        "name": "Массовое Доминирование",
        "description": "Одновременный контроль над несколькими противниками.",
        "branch": "psychic",
        "level_required": 60,
        "effects": {
            "dominate_count": 3,
            "duration": 5,
            "damage_on_release": 50
        },
        "cooldown": 6,
        "chapters": [14, 15, 16, 17]
    },
    "future_glimpse": {
        "id": "psy_70",
        "name": "Взгляд в Будущее",
        "description": "Способность видеть возможные исходы боёв и решений.",
        "branch": "psychic",
        "level_required": 70,
        "effects": {
            "preview_outcomes": True,
            "dodge_boost": 40,
            "critical_chance": 30
        },
        "quest_requirement": "q14_01",
        "chapters": [15, 16, 17, 18]
    },
    "entity_communion": {
        "id": "psy_80",
        "name": "Причастие к Сущности",
        "description": "Способность безопасно коммуницировать с Сущностью.",
        "branch": "psychic",
        "level_required": 80,
        "effects": {
            "entity_dialogue_safe": True,
            "entity_weakness_insight": True,
            "mental_damage_reduction": 50
        },
        "quest_requirement": "q16_01",
        "chapters": [16, 17, 18]
    },
    "reality_perception": {
        "id": "psy_90",
        "name": "Восприятие Реальности",
        "description": "Способность видеть истинную природу пространства и аномалий.",
        "branch": "psychic",
        "level_required": 90,
        "effects": {
            "illusion_immunity": True,
            "hidden_path_vision": True,
            "entity_core_vision": True,
            "merge_ending_unlock": True
        },
        "quest_requirement": "q17_02",
        "chapters": [17, 18]
    },
    "transcendence": {
        "id": "psy_100",
        "name": "Трансценденция",
        "description": "Полное пробуждение Psychic потенциала. Открывает финал Слияния.",
        "branch": "psychic",
        "level_required": 100,
        "effects": {
            "merge_ending_available": True,
            "all_psychic_boost": 50,
            "entity_integration": True,
            "reality_manipulation": True
        },
        "quest_requirement": "q17_03",
        "chapters": [18]
    }
}

# === RESONANCE SYSTEM (Новая механика) ===

RESONANCE_ABILITIES = {
    "resonance_basics": {
        "id": "res_1",
        "name": "Основы Резонанса",
        "description": "Базовая способность чувствовать присутствие аномалий и Сущности.",
        "unlock_condition": "chapter_6_complete",
        "effects": {
            "anomaly_detection_range": 100,
            "entity_presence_warning": True
        }
    },
    "resonance_amplification": {
        "id": "res_2",
        "name": "Усиление Резонанса",
        "description": "Улучшенное чувствование и частичное сопротивление аномалиям.",
        "unlock_condition": "chapter_10_complete",
        "effects": {
            "anomaly_detection_range": 500,
            "entity_weakness_perception": True,
            "mental_resistance": 20
        }
    },
    "resonance_mastery": {
        "id": "res_3",
        "name": "Мастерство Резонанса",
        "description": "Полный контроль над резонансом с пространством.",
        "unlock_condition": "chapter_14_complete",
        "effects": {
            "anomaly_navigation": True,
            "entity_communication": True,
            "future_fragments": True
        }
    },
    "resonance_transcendent": {
        "id": "res_4",
        "name": "Трансцендентный Резонанс",
        "description": "Единение с тканью реальности. Требуется для финала Слияния.",
        "unlock_condition": "psychic_90_or_entity_communion",
        "effects": {
            "reality_manipulation": True,
            "entity_integration_safe": True,
            "merge_ending_unlock": True
        }
    }
}

# === CARRIER SYSTEM (Система перевозки) ===

CARRIER_ABILITIES = {
    "cargo_optimization": {
        "id": "car_1",
        "name": "Оптимизация Груза",
        "description": "Увеличение грузоподъёмности корабля.",
        "unlock_condition": "ship_upgrade_1",
        "effects": {
            "cargo_capacity": 50,
            "fuel_efficiency": 10
        }
    },
    "smuggler_compartments": {
        "id": "car_2",
        "name": "Контрабандные Отсеки",
        "description": "Скрытые отсеки для нелегальных грузов.",
        "unlock_condition": "veronica_relationship_40",
        "effects": {
            "hidden_cargo": 20,
            "scan_evasion": 60
        }
    },
    "anomaly_containment": {
        "id": "car_3",
        "name": "Сдерживание Аномалий",
        "description": "Специальные контейнеры для аномальных артефактов.",
        "unlock_condition": "q12_01_complete",
        "effects": {
            "anomaly_transport": True,
            "radiation_shielding": 80
        }
    },
    "entity_sample_storage": {
        "id": "car_4",
        "name": "Хранилище Образцов Сущности",
        "description": "Биоконтейнеры для безопасного хранения останков порождений.",
        "unlock_condition": "q17_01_complete",
        "effects": {
            "entity_sample_transport": True,
            "alchemy_ingredient_access": True
        }
    }
}

# === PATH-SPECIFIC ABILITIES ===

PATH_ABILITIES = {
    "alliance": {
        "fleet_coordination": {
            "id": "path_all_1",
            "name": "Координация Флота",
            "description": "Вызов поддержки флота Объединённых Миров.",
            "effects": {
                "fleet_support": True,
                "combat_advantage": 30
            },
            "unlock": "alliance_path_chapter_13"
        },
        "alliance_resources": {
            "id": "path_all_2",
            "name": "Ресурсы Альянса",
            "description": "Доступ к оборудованию и технологиям Альянса.",
            "effects": {
                "credit_bonus": 5000,
                "equipment_discount": 40
            },
            "unlock": "alliance_path_chapter_14"
        },
        "united_front": {
            "id": "path_all_3",
            "name": "Единый Фронт",
            "description": "Финальная поддержка Альянса в битве с Сущностью.",
            "effects": {
                "final_battle_allies": "alliance_fleet",
                "exile_ending_army": True
            },
            "unlock": "alliance_path_chapter_16"
        }
    },
    "observer": {
        "ancient_knowledge_access": {
            "id": "path_obs_1",
            "name": "Древние Знания",
            "description": "Доступ к архивам Ордена Наблюдателей.",
            "effects": {
                "lore_unlock": True,
                "psychic_boost": 20
            },
            "unlock": "observer_path_chapter_13"
        },
        "resonance_training": {
            "id": "path_obs_2",
            "name": "Обучение Резонансу",
            "description": "Ускоренное развитие резонанса под руководством Зары.",
            "effects": {
                "resonance_level_boost": 2,
                "anomaly_mastery": True
            },
            "unlock": "observer_path_chapter_14"
        },
        "order_blessing": {
            "id": "path_obs_3",
            "name": "Благословение Ордена",
            "description": "Финальная поддержка Ордена и Зары.",
            "effects": {
                "final_battle_allies": "knights_of_order",
                "treaty_ending_knowledge": True
            },
            "unlock": "observer_path_chapter_16"
        }
    },
    "independence": {
        "network_access": {
            "id": "path_ind_1",
            "name": "Сеть Независимых",
            "description": "Доступ к сети агентов Волкова.",
            "effects": {
                "intel_bonus": True,
                "smuggler_routes": True
            },
            "unlock": "independence_path_chapter_13"
        },
        "freedom_fighters": {
            "id": "path_ind_2",
            "name": "Бойцы Свободы",
            "description": "Привлечение наёмников и независимых капитанов.",
            "effects": {
                "mercenary_discount": 50,
                "unique_contracts": True
            },
            "unlock": "independence_path_chapter_14"
        },
        "independent_fleet": {
            "id": "path_ind_3",
            "name": "Независимый Флот",
            "description": "Собственная флотилия из независимых кораблей.",
            "effects": {
                "final_battle_allies": "independent_squadron",
                "freedom_ending": True
            },
            "unlock": "independence_path_chapter_16"
        }
    }
}

# === FINAL BATTLE ABILITIES ===

FINAL_BATTLE_ABILITIES = {
    "sacrifice_strike": {
        "id": "final_1",
        "name": "Удар Жертвы",
        "description": "Мощная атака ценой собственного здоровья. Требуется для финала Изгнания.",
        "effects": {
            "damage": 500,
            "self_damage": 50,
            "anchor_damage": 100
        },
        "requirement": "exile_path_chosen"
    },
    "diplomatic_communion": {
        "id": "final_2",
        "name": "Дипломатическое Причастие",
        "description": "Ментальная связь с Сущностью для переговоров. Требуется для финала Договора.",
        "effects": {
            "entity_negotiation": True,
            "treaty_establishment": True
        },
        "requirement": "psychic_70_or_empathy_80"
    },
    "entity_absorption": {
        "id": "final_3",
        "name": "Поглощение Сущности",
        "description": "Интеграция Сущности в собственное сознание. Требуется для финала Слияния.",
        "effects": {
            "merge_with_entity": True,
            "transcendence": True
        },
        "requirement": "psychic_90_and_resonance_transcendent"
    }
}

# Объединение всех способностей
ALL_ADVANCED_ABILITIES = {
    "alchemy": ALCHEMY_ADVANCED,
    "biotics": BIOTICS_ADVANCED,
    "psychic": PSYCHIC_ADVANCED,
    "resonance": RESONANCE_ABILITIES,
    "carrier": CARRIER_ABILITIES,
    "path": PATH_ABILITIES,
    "final": FINAL_BATTLE_ABILITIES
}

def get_ability(branch, ability_id):
    """Получить способность по ветке и ID"""
    branch_abilities = ALL_ADVANCED_ABILITIES.get(branch, {})
    return branch_abilities.get(ability_id)

def get_available_abilities(character, chapter):
    """Получить доступные способности для персонажа в текущей главе"""
    available = []
    
    for branch, abilities in ALL_ADVANCED_ABILITIES.items():
        if branch == "path":
            # Способности пути проверяются отдельно
            path = character.get("path")
            if path and path in abilities:
                for ability_id, ability in abilities[path].items():
                    if chapter in ability.get("chapters", range(1, 19)):
                        available.append(ability)
        else:
            for ability_id, ability in abilities.items():
                # Проверка уровня
                level_req = ability.get("level_required", 0)
                if character.get(branch, 0) >= level_req:
                    # Проверка главы
                    if chapter in ability.get("chapters", range(1, 19)):
                        # Проверка квеста
                        quest_req = ability.get("quest_unlock")
                        if quest_req:
                            if quest_req in character.get("completed_quests", []):
                                available.append(ability)
                        else:
                            available.append(ability)
    
    return available

def check_ability_requirements(ability, character, game_state):
    """Проверить, соответствует ли персонаж требованиям способности"""
    requirements = ability.get("requirement", "")
    
    if not requirements:
        return True
    
    # Парсинг требований
    if "psychic_90" in requirements:
        if character.get("psychic", 0) < 90:
            return False
    
    if "resonance_transcendent" in requirements:
        if not game_state.get("resonance_transcendent"):
            return False
    
    return True
