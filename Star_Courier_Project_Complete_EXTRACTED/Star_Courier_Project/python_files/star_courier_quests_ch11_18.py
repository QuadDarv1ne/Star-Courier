# -*- coding: utf-8 -*-
"""
Star Courier - Quests for Chapters 11-18
Совместимо с существующей структурой quests.py
"""

# === ГЛАВА 11: Тени Прошлого ===

CHAPTER_11_QUESTS = {
    "echo_awakening": {
        "id": "q11_01",
        "name": "Пробуждение Эха",
        "description": "Кристалл из Координаты Нуля начал резонировать. Голос из прошлого пытается установить контакт. Узнайте, что он может предложить.",
        "type": "main",
        "prerequisites": ["q10_complete"],
        "stages": [
            {"id": "s1", "description": "Установите контакт с Эхом", "target": {"dialogue": "echo_first_contact"}},
            {"id": "s2", "description": "Узнайте о природе Сущности", "target": {"dialogue": "echo_threat_info"}},
            {"id": "s3", "description": "Получите координаты Зоны Тишины", "target": {"dialogue": "echo_coordinates"}}
        ],
        "rewards": {
            "experience": 500,
            "knowledge": 20,
            "quest_item": "ancient_coordinates"
        }
    },
    "survivor_trail": {
        "id": "q11_02",
        "name": "След выжившего",
        "description": "Эхо упомянуло кого-то, кто вернулся из Зоны Тишины. Найдите информацию об этом человеке.",
        "type": "side",
        "prerequisites": ["q11_01"],
        "stages": [
            {"id": "s1", "description": "Соберите информацию в портах", "target": {"visit": 3, "locations": ["port"]}},
            {"id": "s2", "description": "Найдите свидетеля", "target": {"npc": "old_sailor"}},
            {"id": "s3", "description": "Получите записи выжившего", "target": {"item": "survivor_journal"}}
        ],
        "rewards": {
            "experience": 300,
            "knowledge": 15,
            "quest_item": "survivor_notes"
        }
    }
}

# === ГЛАВА 12: Разлом ===

CHAPTER_12_QUESTS = {
    "horizon_station": {
        "id": "q12_01",
        "name": "Станция Горизонт",
        "description": "Вера хочет вернуться на заброшенную исследовательскую станцию, где хранятся её данные об аномалиях.",
        "type": "main",
        "prerequisites": ["q11_01"],
        "stages": [
            {"id": "s1", "description": "Получите координаты станции от Веры", "target": {"dialogue": "vera_mission_briefing"}},
            {"id": "s2", "description": "Доберитесь до станции", "target": {"location": "horizon_station"}},
            {"id": "s3", "description": "Обойдите систему безопасности", "target": {"dialogue": "station_ai_encounter"}},
            {"id": "s4", "description": "Загрузите данные об аномалиях", "target": {"action": "download_data"}}
        ],
        "rewards": {
            "experience": 600,
            "tech_upgrade": "anomaly_detector",
            "character_relationship": {"vera": 20}
        }
    },
    "veras_past": {
        "id": "q12_02",
        "name": "Прошлое Веры",
        "description": "Узнайте больше о том, почему Вера была вынуждена бежать.",
        "type": "side",
        "prerequisites": ["q12_01"],
        "stages": [
            {"id": "s1", "description": "Расспросите Веру о её бегстве", "target": {"dialogue": "vera_escape_reason"}},
            {"id": "s2", "description": "Найдите доказательства в личных файлах", "target": {"item": "vera_evidence"}},
            {"id": "s3", "description": "Решите, как использовать информацию", "target": {"choice": ["public", "private", "ignore"]}}
        ],
        "rewards": {
            "experience": 250,
            "character_relationship": {"vera": 25}
        }
    },
    "ancient_technology": {
        "id": "q12_03",
        "name": "Древние технологии",
        "description": "Станция содержит артефакты неизвестной цивилизации. Исследуйте их.",
        "type": "side",
        "prerequisites": ["q12_01"],
        "stages": [
            {"id": "s1", "description": "Найдите лабораторию артефактов", "target": {"location": "artifact_lab"}},
            {"id": "s2", "description": "Проанализуйте находки", "target": {"skill_check": {"intelligence": 50}}},
            {"id": "s3", "description": "Активируйте или уничтожьте артефакт", "target": {"choice": ["activate", "destroy"]}}
        ],
        "rewards": {
            "experience": 400,
            "item": "ancient_component"
        }
    }
}

# === ГЛАВА 13: Выбор Пути ===

CHAPTER_13_QUESTS = {
    "path_decision": {
        "id": "q13_01",
        "name": "Выбор пути",
        "description": "Три силы предлагают поддержку. Выберите свой путь в борьбе с Сущностью.",
        "type": "main",
        "prerequisites": ["q12_01"],
        "stages": [
            {"id": "s1", "description": "Встретьтесь с представителями трёх сил", "target": {"location": "neutral_ground"}},
            {"id": "s2", "description": "Изучите предложения каждой стороны", "target": {"dialogue": "path_choice_intro"}},
            {"id": "s3", "description": "Принмите решение", "target": {"choice": ["alliance", "observer", "independence"]}}
        ],
        "rewards": {
            "experience": 1000,
            "path_unlock": True
        }
    },
    "alliance_proving": {
        "id": "q13_02",
        "name": "Доказательство верности (Альянс)",
        "description": "Альянс требует доказательства лояльности перед полноценным сотрудничеством.",
        "type": "path_alliance",
        "prerequisites": ["q13_01"],
        "path_required": "alliance",
        "stages": [
            {"id": "s1", "description": "Выполните миссию для Альянса", "target": {"mission": "alliance_mission_1"}},
            {"id": "s2", "description": "Получите допуск к ресурсам флота", "target": {"item": "fleet_credentials"}}
        ],
        "rewards": {
            "experience": 500,
            "alliance_reputation": 50,
            "unlock": "fleet_support"
        }
    },
    "observer_training": {
        "id": "q13_03",
        "name": "Обучение Наблюдателя",
        "description": "Зара предлагает пройти древние ритуалы Ордена для пробуждения скрытого потенциала.",
        "type": "path_observer",
        "prerequisites": ["q13_01"],
        "path_required": "observer",
        "stages": [
            {"id": "s1", "description": "Пройдите испытание разума", "target": {"skill_check": {"psychic": 60}}},
            {"id": "s2", "description": "Изучите древние тексты", "target": {"item": "observer_tome"}},
            {"id": "s3", "description": "Пройдите ритуал инициации", "target": {"dialogue": "observer_ritual"}}
        ],
        "rewards": {
            "experience": 500,
            "observer_reputation": 50,
            "ability": "resonance_sense"
        }
    },
    "independence_network": {
        "id": "q13_04",
        "name": "Сеть Независимых",
        "description": "Волков предлагает расширить контакты с независимыми агентами по всей галактике.",
        "type": "path_independence",
        "prerequisites": ["q13_01"],
        "path_required": "independence",
        "stages": [
            {"id": "s1", "description": "Встретьтесь с тремя ключевыми контактами", "target": {"npcs": ["contact_1", "contact_2", "contact_3"]}},
            {"id": "s2", "description": "Докажите свою независимость", "target": {"mission": "independence_test"}},
            {"id": "s3", "description": "Получите доступ к сети", "target": {"item": "network_key"}}
        ],
        "rewards": {
            "experience": 500,
            "independence_reputation": 50,
            "unlock": "smuggler_network"
        }
    }
}

# === ГЛАВА 14: Кристалл Времени ===

CHAPTER_14_QUESTS = {
    "temple_journey": {
        "id": "q14_01",
        "name": "Храм Времени",
        "description": "Координаты из кристалла указывают на древний храм, где хранится артефакт, способный показать будущее.",
        "type": "main",
        "prerequisites": ["q13_01"],
        "stages": [
            {"id": "s1", "description": "Доберитесь до планеты храма", "target": {"location": "temple_planet"}},
            {"id": "s2", "description": "Найдите вход в храм", "target": {"skill_check": {"perception": 40}}},
            {"id": "s3", "description": "Пройдите испытания храма", "target": {"challenges": 3}},
            {"id": "s4", "description": "Встретьтесь со Стражем", "target": {"dialogue": "temple_guardian"}},
            {"id": "s5", "description": "Получите Кристалл Времени", "target": {"item": "time_crystal"}}
        ],
        "rewards": {
            "experience": 800,
            "artifact": "time_crystal",
            "ability": "future_glimpse"
        }
    },
    "memory_price": {
        "id": "q14_02",
        "name": "Цена памяти",
        "description": "Страж предупредил о цене использования Кристалла. Узнайте больше о последствиях.",
        "type": "side",
        "prerequisites": ["q14_01"],
        "stages": [
            {"id": "s1", "description": "Изучите записи предыдущих пользователей", "target": {"item": "temple_records"}},
            {"id": "s2", "description": "Проконсультируйтесь с командой", "target": {"dialogues": ["maria_temple_concern", "mia_input"]}},
            {"id": "s3", "description": "Решите, стоит ли платить цену", "target": {"choice": ["accept", "find_alternative"]}}
        ],
        "rewards": {
            "experience": 300,
            "knowledge": 20
        }
    }
}

# === ГЛАВА 15: Предательство ===

CHAPTER_15_QUESTS = {
    "traitor_revealed": {
        "id": "q15_01",
        "name": "Лицо предателя",
        "description": "Кто-то в вашем окружении работает на Сущность. Выясните, кто и почему.",
        "type": "main",
        "prerequisites": ["q14_01"],
        "stages": [
            {"id": "s1", "description": "Обратите внимание на странное поведение", "target": {"event": "suspicious_activity"}},
            {"id": "s2", "description": "Соберите улики", "target": {"items": ["evidence_1", "evidence_2"]}},
            {"id": "s3", "description": "Конфронтируйте с предателем", "target": {"dialogue": "double_agent_reveal"}},
            {"id": "s4", "description": "Решите судьбу предателя", "target": {"choice": ["execute", "imprison", "redeem"]}}
        ],
        "rewards": {
            "experience": 600,
            "team_morale": -20,
            "knowledge": 30
        }
    },
    "entity_proposal": {
        "id": "q15_02",
        "name": "Предложение Сущности",
        "description": "Через предателя Сущность сделала предложение. Узнайте все детали перед принятием решения.",
        "type": "main",
        "prerequisites": ["q15_01"],
        "stages": [
            {"id": "s1", "description": "Выслушайте условия", "target": {"dialogue": "entity_proposal"}},
            {"id": "s2", "description": "Обсудите с командой", "target": {"dialogue": "mia_after_betrayal"}},
            {"id": "s3", "description": "Примите или отвергните предложение", "target": {"choice": ["accept", "reject", "negotiate"]}}
        ],
        "rewards": {
            "experience": 400
        }
    },
    "team_recovery": {
        "id": "q15_03",
        "name": "Восстановление доверия",
        "description": "После предательства команда деморализована. Верните их доверие и боевой дух.",
        "type": "side",
        "prerequisites": ["q15_01"],
        "stages": [
            {"id": "s1", "description": "Проведите индивидуальные разговоры", "target": {"dialogues": 4}},
            {"id": "s2", "description": "Докажите свою надёжность делом", "target": {"mission": "trust_mission"}},
            {"id": "s3", "description": "Восстановите командный дух", "target": {"stat": "team_morale", "value": 80}}
        ],
        "rewards": {
            "experience": 350,
            "team_morale": 30,
            "relationship_boost": {"all": 10}
        }
    }
}

# === ГЛАВА 16: Пробуждение ===

CHAPTER_16_QUESTS = {
    "zone_silence": {
        "id": "q16_01",
        "name": "Путь к нулю",
        "description": "Проложите курс через Зону Тишины к Координате Нуля, используя древние карты.",
        "type": "main",
        "prerequisites": ["q15_02"],
        "stages": [
            {"id": "s1", "description": "Активируйте навигацию по древним координатам", "target": {"item": "ancient_coordinates"}},
            {"id": "s2", "description": "Пересеките границу Зоны Тишины", "target": {"location": "zone_silence"}},
            {"id": "s3", "description": "Выдержите ментальный контакт с Сущностью", "target": {"dialogue": "entity_mental_contact"}},
            {"id": "s4", "description": "Достигните Координаты Нуля", "target": {"location": "coordinate_zero"}}
        ],
        "rewards": {
            "experience": 700,
            "story_progress": 85
        }
    },
    "final_council": {
        "id": "q16_02",
        "name": "Последний совет",
        "description": "Соберите экипаж для обсуждения финальной стратегии.",
        "type": "main",
        "prerequisites": ["q16_01"],
        "stages": [
            {"id": "s1", "description": "Соберите команду в главном отсеке", "target": {"event": "council_meeting"}},
            {"id": "s2", "description": "Выслушайте все мнения", "target": {"dialogues": 5}},
            {"id": "s3", "description": "Определите общую стратегию", "target": {"dialogue": "final_council"}}
        ],
        "rewards": {
            "experience": 300,
            "team_morale": 20
        }
    },
    "combat_readiness": {
        "id": "q16_03",
        "name": "Боевая готовность",
        "description": "Подготовьте корабль и экипаж к финальной битве.",
        "type": "side",
        "prerequisites": ["q16_02"],
        "stages": [
            {"id": "s1", "description": "Проверьте системы корабля с Сергеем", "target": {"npc": "sergey"}},
            {"id": "s2", "description": "Подготовьте медотсек с Марией", "target": {"npc": "maria"}},
            {"id": "s3", "description": "Усиление вооружения с Дмитрием", "target": {"npc": "dmitry"}},
            {"id": "s4", "description": "Получите последние разведданные от Вероники", "target": {"npc": "veronica"}}
        ],
        "rewards": {
            "experience": 400,
            "ship_bonus": {"shields": 20, "weapons": 15}
        }
    },
    "promise": {
        "id": "q16_04",
        "name": "Обещание",
        "description": "Проведите приватный разговор с романтическим партнёром перед битвой.",
        "type": "side",
        "prerequisites": ["q16_02"],
        "romance_required": True,
        "stages": [
            {"id": "s1", "description": "Найдите момент для разговора наедине", "target": {"location": "private_quarters"}},
            {"id": "s2", "description": "Выскажите свои чувства", "target": {"dialogue": "romantic_preparation"}},
            {"id": "s3", "description": "Дайте обещание", "target": {"choice": ["together", "protect", "freedom"]}}
        ],
        "rewards": {
            "experience": 200,
            "romantic_relationship": 20
        }
    }
}

# === ГЛАВА 17: Сердце Тьмы ===

CHAPTER_17_QUESTS = {
    "station_infiltration": {
        "id": "q17_01",
        "name": "Проникновение",
        "description": "Доберитесь до центрального ядра станции, где находится якорь Сущности.",
        "type": "main",
        "prerequisites": ["q16_02"],
        "stages": [
            {"id": "s1", "description": "Высадитесь на поверхность станции", "target": {"location": "station_surface"}},
            {"id": "s2", "description": "Найдите точку входа", "target": {"skill_check": {"perception": 50}}},
            {"id": "s3", "description": "Продвигайтесь к ядру", "target": {"location": "station_core"}},
            {"id": "s4", "description": "Отразите атаки порождений Тьмы", "target": {"combat_wins": 3}}
        ],
        "rewards": {
            "experience": 600,
            "combat_experience": 300
        }
    },
    "personal_demons": {
        "id": "q17_02",
        "name": "Личные демоны",
        "description": "Преодолейте иллюзии в Зеркальном зале, где Сущность использует ваши страхи против вас.",
        "type": "main",
        "prerequisites": ["q17_01"],
        "stages": [
            {"id": "s1", "description": "Войдите в Зеркальный зал", "target": {"location": "mirror_hall"}},
            {"id": "s2", "description": "Столкнитесь с личными страхами", "target": {"dialogue": "mirror_trap"}},
            {"id": "s3", "description": "Помогите команде преодолеть их страхи", "target": {"skill_checks": 3}},
            {"id": "s4", "description": "Выберитесь из зала", "target": {"stat": "mental_damage", "max": 50}}
        ],
        "rewards": {
            "experience": 500,
            "psychic": 10,
            "mental_resistance": 20
        }
    },
    "guardian_encounter": {
        "id": "q17_03",
        "name": "Древний страж",
        "description": "Встретьтесь со Стражем Ядра и узнайте правду о Сущности.",
        "type": "main",
        "prerequisites": ["q17_02"],
        "stages": [
            {"id": "s1", "description": "Достигните покоев Стража", "target": {"location": "guardian_chamber"}},
            {"id": "s2", "description": "Выслушайте историю древней цивилизации", "target": {"dialogue": "guardian_encounter"}},
            {"id": "s3", "description": "Узнайте о трёх вариантах решения", "target": {"dialogue": "guardian_exile_path"}},
            {"id": "s4", "description": "Примите предварительное решение", "target": {"choice": ["exile", "treaty", "merge"]}}
        ],
        "rewards": {
            "experience": 800,
            "knowledge": 50,
            "final_choice_unlocked": True
        }
    }
}

# === ГЛАВА 18: Финал ===

CHAPTER_18_QUESTS = {
    "final_battle": {
        "id": "q18_01",
        "name": "Битва за будущее",
        "description": "Финальное противостояние в ядре станции. Судьба галактики в ваших руках.",
        "type": "main",
        "prerequisites": ["q17_03"],
        "stages": [
            {"id": "s1", "description": "Войдите в ядро станции", "target": {"location": "station_core_final"}},
            {"id": "s2", "description": "Столкнитесь с Сущностью лицом к лицу", "target": {"dialogue": "final_choice"}},
            {"id": "s3", "description": "Сделайте финальный выбор", "target": {"choice": ["exile", "treaty", "merge"]}},
            {"id": "s4", "description": "Завершите противостояние", "target": {"event": "final_resolution"}}
        ],
        "rewards": {
            "experience": 2000,
            "achievement": "galaxy_savior"
        }
    },
    "romantic_finale": {
        "id": "q18_02",
        "name": "Обещание любви",
        "description": "Финальная сцена с романтическим партнёром.",
        "type": "side",
        "prerequisites": ["q18_01"],
        "romance_required": True,
        "romance_level_min": 80,
        "stages": [
            {"id": "s1", "description": "Встретьтесь с партнёром после битвы", "target": {"event": "romantic_reunion"}},
            {"id": "s2", "description": "Обсудите будущее", "target": {"dialogue": "epilogue_romantic"}},
            {"id": "s3", "description": "Примите совместное решение", "target": {"choice": ["stay_together", "separate_peacefully"]}}
        ],
        "rewards": {
            "experience": 500,
            "achievement": "true_love"
        }
    },
    "epilogue": {
        "id": "q18_03",
        "name": "Эпилог",
        "description": "Увидьте последствия своих выборов.",
        "type": "main",
        "prerequisites": ["q18_01"],
        "stages": [
            {"id": "s1", "description": "Просмотрите последствия для галактики", "target": {"cutscene": "galaxy_aftermath"}},
            {"id": "s2", "description": "Узнайте судьбу спутников", "target": {"cutscene": "companions_fate"}},
            {"id": "s3", "description": "Получите итоговую статистику", "target": {"event": "game_statistics"}}
        ],
        "rewards": {
            "experience": 0,
            "game_complete": True
        }
    }
}

# Объединение всех квестов
QUESTS_CHAPTERS_11_18 = {
    **CHAPTER_11_QUESTS,
    **CHAPTER_12_QUESTS,
    **CHAPTER_13_QUESTS,
    **CHAPTER_14_QUESTS,
    **CHAPTER_15_QUESTS,
    **CHAPTER_16_QUESTS,
    **CHAPTER_17_QUESTS,
    **CHAPTER_18_QUESTS
}

def get_quest(quest_id):
    """Получить квест по ID"""
    return QUESTS_CHAPTERS_11_18.get(quest_id)

def get_available_quests(game_state, completed_quests):
    """Получить список доступных квестов"""
    available = []
    for quest_id, quest in QUESTS_CHAPTERS_11_18.items():
        # Проверка пути
        if quest.get("path_required"):
            if game_state.get("path") != quest["path_required"]:
                continue
        
        # Проверка романтики
        if quest.get("romance_required"):
            if not game_state.get("romantic_partner"):
                continue
            if quest.get("romance_level_min"):
                if game_state.get("relationships", {}).get(game_state["romantic_partner"], 0) < quest["romance_level_min"]:
                    continue
        
        # Проверка предпосылок
        prereqs = quest.get("prerequisites", [])
        if all(p in completed_quests for p in prereqs):
            if quest_id not in completed_quests:
                available.append(quest)
    
    return available

def complete_quest_stage(quest_id, stage_id, game_state):
    """Завершить этап квеста"""
    quest = get_quest(quest_id)
    if not quest:
        return False
    
    for stage in quest["stages"]:
        if stage["id"] == stage_id:
            stage["completed"] = True
            return True
    
    return False

def is_quest_complete(quest_id):
    """Проверить, завершён ли квест"""
    quest = get_quest(quest_id)
    if not quest:
        return False
    
    return all(stage.get("completed", False) for stage in quest["stages"])
