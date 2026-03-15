# -*- coding: utf-8 -*-
"""
Star Courier - Quests for Chapters 14-18
Квесты для финальных глав игры
"""

from typing import Dict

try:
    from .quests import Quest, QuestType, QuestState, QuestReward, Objective, ObjectiveType
except ImportError:
    from quests import Quest, QuestType, QuestState, QuestReward, Objective, ObjectiveType


# === ГЛАВА 14: Кристалл Времени ===

def create_chapter14_quests() -> Dict[str, Quest]:
    """Квесты для главы 14: Храм Времени"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Храм Времени ===
    ch14_main_001 = Quest(
        id="ch14_main_001",
        title="Храм Времени",
        description="Координаты из кристалла указывают на древний храм, где хранится артефакт, способный показать будущее.",
        quest_type=QuestType.MAIN,
        state=QuestState.ACTIVE,
        giver="Древний Кристалл",
        journal_entry="Кристалл времени показывает путь к древнему храму. Там вы сможете увидеть возможные будущие линии."
    )

    ch14_main_001.add_objective(Objective(
        id="obj_reach_planet",
        type=ObjectiveType.EXPLORE,
        description="Добраться до планеты храма",
        target_id="temple_planet",
        required=1,
        is_completed=False
    ))

    ch14_main_001.add_objective(Objective(
        id="obj_find_entrance",
        type=ObjectiveType.EXPLORE,
        description="Найти вход в храм",
        target_id="temple_entrance",
        required=1,
        is_completed=False
    ))

    ch14_main_001.add_objective(Objective(
        id="obj_pass_trials",
        type=ObjectiveType.EXPLORE,
        description="Пройти испытания храма",
        required=3,
        current=0,
        is_completed=False
    ))

    ch14_main_001.add_objective(Objective(
        id="obj_meet_guardian",
        type=ObjectiveType.TALK,
        description="Встретиться со Стражем",
        target_id="temple_guardian",
        required=1,
        is_completed=False
    ))

    ch14_main_001.add_objective(Objective(
        id="obj_get_crystal",
        type=ObjectiveType.COLLECT,
        description="Получить Кристалл Времени",
        target_id="time_crystal",
        required=1,
        is_completed=False
    ))

    ch14_main_001.reward = QuestReward(
        credits=1000,
        experience=800,
        items=[{"time_crystal": 1}],
        unlocks=["ch14_side_001"]
    )

    quests["ch14_main_001"] = ch14_main_001

    # === ПОБОЧНЫЙ КВЕСТ: Цена памяти ===
    ch14_side_001 = Quest(
        id="ch14_side_001",
        title="Цена памяти",
        description="Страж предупредил о цене использования Кристалла. Узнайте больше о последствиях.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Страж Храма",
        journal_entry="Кристалл показывает будущее, но забирает воспоминания о прошлом. Стоит ли цена знания?"
    )

    ch14_side_001.add_objective(Objective(
        id="obj_study_records",
        type=ObjectiveType.COLLECT,
        description="Изучить записи предыдущих пользователей",
        target_id="temple_records",
        required=1,
        is_completed=False
    ))

    ch14_side_001.add_objective(Objective(
        id="obj_consult_team",
        type=ObjectiveType.TALK,
        description="Проконсультироваться с командой",
        target_id="crew_consultation",
        required=1,
        is_completed=False
    ))

    ch14_side_001.add_objective(Objective(
        id="obj_make_choice",
        type=ObjectiveType.MAKE_CHOICE,
        description="Решить, стоит ли платить цену",
        target_id="memory_choice",
        required=1,
        is_completed=False
    ))

    ch14_side_001.reward = QuestReward(
        credits=500,
        experience=300,
        relationship_changes={"maria": 10, "mia": 10}
    )

    quests["ch14_side_001"] = ch14_side_001

    return quests


# === ГЛАВА 15: Предательство ===

def create_chapter15_quests() -> Dict[str, Quest]:
    """Квесты для главы 15: Предательство"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Лицо предателя ===
    ch15_main_001 = Quest(
        id="ch15_main_001",
        title="Лицо предателя",
        description="Кто-то в вашем окружении работает на Сущность. Выясните, кто и почему.",
        quest_type=QuestType.MAIN,
        state=QuestState.ACTIVE,
        giver="???",
        journal_entry="Странное поведение кого-то из команды. Нужно собрать улики и вычислить предателя."
    )

    ch15_main_001.add_objective(Objective(
        id="obj_notice_signs",
        type=ObjectiveType.EXPLORE,
        description="Обратить внимание на странное поведение",
        target_id="suspicious_activity",
        required=1,
        is_completed=False
    ))

    ch15_main_001.add_objective(Objective(
        id="obj_gather_evidence",
        type=ObjectiveType.COLLECT,
        description="Собрать улики",
        required=2,
        current=0,
        is_completed=False
    ))

    ch15_main_001.add_objective(Objective(
        id="obj_confront",
        type=ObjectiveType.TALK,
        description="Конфронтировать с предателем",
        target_id="double_agent_reveal",
        required=1,
        is_completed=False
    ))

    ch15_main_001.add_objective(Objective(
        id="obj_decide_fate",
        type=ObjectiveType.MAKE_CHOICE,
        description="Решить судьбу предателя",
        target_id="traitor_fate",
        required=1,
        is_completed=False
    ))

    ch15_main_001.reward = QuestReward(
        credits=1000,
        experience=600,
        relationship_changes={"team_morale": -20},
        unlocks=["ch15_main_002"]
    )

    quests["ch15_main_001"] = ch15_main_001

    # === ГЛАВНЫЙ КВЕСТ: Предложение Сущности ===
    ch15_main_002 = Quest(
        id="ch15_main_002",
        title="Предложение Сущности",
        description="Через предателя Сущность сделала предложение. Узнайте все детали перед принятием решения.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Сущность (через предателя)",
        journal_entry="Сущность предлагает сделку: присоединиться добровольно в обмен на безопасность близких."
    )

    ch15_main_002.add_objective(Objective(
        id="obj_listen_terms",
        type=ObjectiveType.TALK,
        description="Выслушать условия",
        target_id="entity_proposal",
        required=1,
        is_completed=False
    ))

    ch15_main_002.add_objective(Objective(
        id="obj_discuss_team",
        type=ObjectiveType.TALK,
        description="Обсудить с командой",
        target_id="mia_after_betrayal",
        required=1,
        is_completed=False
    ))

    ch15_main_002.add_objective(Objective(
        id="obj_make_decision",
        type=ObjectiveType.MAKE_CHOICE,
        description="Принять или отвергнуть предложение",
        target_id="entity_decision",
        required=1,
        is_completed=False
    ))

    ch15_main_002.reward = QuestReward(
        credits=0,
        experience=400,
        unlocks=["chapter_16"]
    )

    quests["ch15_main_002"] = ch15_main_002

    # === ПОБОЧНЫЙ КВЕСТ: Восстановление доверия ===
    ch15_side_001 = Quest(
        id="ch15_side_001",
        title="Восстановление доверия",
        description="После предательства команда деморализована. Верните их доверие и боевой дух.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Мия",
        journal_entry="Предательство подорвало доверие в команде. Нужно провести индивидуальные разговоры и доказать надёжность."
    )

    ch15_side_001.add_objective(Objective(
        id="obj_individual_talks",
        type=ObjectiveType.TALK,
        description="Провести индивидуальные разговоры",
        required=4,
        current=0,
        is_completed=False
    ))

    ch15_side_001.add_objective(Objective(
        id="obj_prove_reliability",
        type=ObjectiveType.EXPLORE,
        description="Доказать надёжность делом",
        target_id="trust_mission",
        required=1,
        is_completed=False
    ))

    ch15_side_001.add_objective(Objective(
        id="obj_restore_morale",
        type=ObjectiveType.MAKE_CHOICE,
        description="Восстановить командный дух",
        target_id="team_morale_80",
        required=1,
        is_completed=False
    ))

    ch15_side_001.reward = QuestReward(
        credits=500,
        experience=350,
        relationship_changes={"all_crew": 10}
    )

    quests["ch15_side_001"] = ch15_side_001

    return quests


# === ГЛАВА 16: Пробуждение ===

def create_chapter16_quests() -> Dict[str, Quest]:
    """Квесты для главы 16: Пробуждение"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Путь к нулю ===
    ch16_main_001 = Quest(
        id="ch16_main_001",
        title="Путь к нулю",
        description="Проложите курс через Зону Тишины к Координате Нуля, используя древние карты.",
        quest_type=QuestType.MAIN,
        state=QuestState.ACTIVE,
        giver="Навигационный компьютер",
        journal_entry="Координаты Нуля получены. Путь лежит через опасную Зону Тишины, где физика сломана."
    )

    ch16_main_001.add_objective(Objective(
        id="obj_activate_nav",
        type=ObjectiveType.USE_ITEM,
        description="Активировать навигацию по древним координатам",
        target_id="ancient_coordinates",
        required=1,
        is_completed=False
    ))

    ch16_main_001.add_objective(Objective(
        id="obj_cross_boundary",
        type=ObjectiveType.EXPLORE,
        description="Пересечь границу Зоны Тишины",
        target_id="zone_silence",
        required=1,
        is_completed=False
    ))

    ch16_main_001.add_objective(Objective(
        id="obj_mental_contact",
        type=ObjectiveType.TALK,
        description="Выдержать ментальный контакт с Сущностью",
        target_id="entity_mental_contact",
        required=1,
        is_completed=False
    ))

    ch16_main_001.add_objective(Objective(
        id="obj_reach_zero",
        type=ObjectiveType.EXPLORE,
        description="Достичь Координаты Нуля",
        target_id="coordinate_zero",
        required=1,
        is_completed=False
    ))

    ch16_main_001.reward = QuestReward(
        credits=0,
        experience=700,
        unlocks=["ch16_main_002"]
    )

    quests["ch16_main_001"] = ch16_main_001

    # === ГЛАВНЫЙ КВЕСТ: Последний совет ===
    ch16_main_002 = Quest(
        id="ch16_main_002",
        title="Последний совет",
        description="Соберите экипаж для обсуждения финальной стратегии.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Макс Велл",
        journal_entry="Все члены экипажа собрались. Нужно определить финальную стратегию против Сущности."
    )

    ch16_main_002.add_objective(Objective(
        id="obj_council_meeting",
        type=ObjectiveType.TALK,
        description="Собрать команду в главном отсеке",
        target_id="council_meeting",
        required=1,
        is_completed=False
    ))

    ch16_main_002.add_objective(Objective(
        id="obj_listen_opinions",
        type=ObjectiveType.TALK,
        description="Выслушать все мнения",
        required=5,
        current=0,
        is_completed=False
    ))

    ch16_main_002.add_objective(Objective(
        id="obj_decide_strategy",
        type=ObjectiveType.MAKE_CHOICE,
        description="Определить общую стратегию",
        target_id="final_council",
        required=1,
        is_completed=False
    ))

    ch16_main_002.reward = QuestReward(
        credits=0,
        experience=300,
        relationship_changes={"team_morale": 20},
        unlocks=["ch16_side_001", "ch16_side_002"]
    )

    quests["ch16_main_002"] = ch16_main_002

    # === ПОБОЧНЫЙ КВЕСТ: Боевая готовность ===
    ch16_side_001 = Quest(
        id="ch16_side_001",
        title="Боевая готовность",
        description="Подготовьте корабль и экипаж к финальной битве.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Надежда",
        journal_entry="Финальная битва близка. Нужно подготовить все системы корабля и команду."
    )

    ch16_side_001.add_objective(Objective(
        id="obj_check_systems",
        type=ObjectiveType.TALK,
        description="Проверить системы корабля с Сергеем",
        target_id="sergey",
        required=1,
        is_completed=False
    ))

    ch16_side_001.add_objective(Objective(
        id="obj_prep_medbay",
        type=ObjectiveType.TALK,
        description="Подготовить медотсек с Марией",
        target_id="maria",
        required=1,
        is_completed=False
    ))

    ch16_side_001.add_objective(Objective(
        id="obj_upgrade_weapons",
        type=ObjectiveType.TALK,
        description="Усилить вооружение с Дмитрием",
        target_id="dmitry",
        required=1,
        is_completed=False
    ))

    ch16_side_001.add_objective(Objective(
        id="obj_get_intel",
        type=ObjectiveType.TALK,
        description="Получить разведданные от Вероники",
        target_id="veronica",
        required=1,
        is_completed=False
    ))

    ch16_side_001.reward = QuestReward(
        credits=1000,
        experience=400,
        ship_bonus={"shields": 20, "weapons": 15}
    )

    quests["ch16_side_001"] = ch16_side_001

    # === ПОБОЧНЫЙ КВЕСТ: Обещание (романтика) ===
    ch16_side_002 = Quest(
        id="ch16_side_002",
        title="Обещание",
        description="Проведите приватный разговор с романтическим партнёром перед битвой.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Романтический партнёр",
        journal_entry="Перед финальной битвой важно провести момент с тем, кто дорог.",
        prerequisites=["ch16_main_002"]
    )

    ch16_side_002.add_objective(Objective(
        id="obj_find_moment",
        type=ObjectiveType.EXPLORE,
        description="Найти момент для разговора наедине",
        target_id="private_quarters",
        required=1,
        is_completed=False
    ))

    ch16_side_002.add_objective(Objective(
        id="obj_express_feelings",
        type=ObjectiveType.TALK,
        description="Высказать свои чувства",
        target_id="romantic_preparation",
        required=1,
        is_completed=False
    ))

    ch16_side_002.add_objective(Objective(
        id="obj_make_promise",
        type=ObjectiveType.MAKE_CHOICE,
        description="Дать обещание",
        target_id="promise_choice",
        required=1,
        is_completed=False
    ))

    ch16_side_002.reward = QuestReward(
        credits=0,
        experience=200,
        relationship_changes={"romantic_partner": 20}
    )

    quests["ch16_side_002"] = ch16_side_002

    return quests


# === ГЛАВА 17: Сердце Тьмы ===

def create_chapter17_quests() -> Dict[str, Quest]:
    """Квесты для главы 17: Сердце Тьмы"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Проникновение ===
    ch17_main_001 = Quest(
        id="ch17_main_001",
        title="Проникновение",
        description="Доберитесь до центрального ядра станции, где находится якорь Сущности.",
        quest_type=QuestType.MAIN,
        state=QuestState.ACTIVE,
        giver="Макс Велл",
        journal_entry="Станция в Зоне Тишины — место обитания Сущности. Нужно достичь ядра."
    )

    ch17_main_001.add_objective(Objective(
        id="obj_land_station",
        type=ObjectiveType.EXPLORE,
        description="Высадиться на поверхность станции",
        target_id="station_surface",
        required=1,
        is_completed=False
    ))

    ch17_main_001.add_objective(Objective(
        id="obj_find_entry",
        type=ObjectiveType.EXPLORE,
        description="Найти точку входа",
        target_id="station_entry",
        required=1,
        is_completed=False
    ))

    ch17_main_001.add_objective(Objective(
        id="obj_reach_core",
        type=ObjectiveType.EXPLORE,
        description="Продвигаться к ядру",
        target_id="station_core",
        required=1,
        is_completed=False
    ))

    ch17_main_001.add_objective(Objective(
        id="obj_defeat_enemies",
        type=ObjectiveType.EXPLORE,
        description="Отразить атаки порождений Тьмы",
        required=3,
        current=0,
        is_completed=False
    ))

    ch17_main_001.reward = QuestReward(
        credits=0,
        experience=600,
        unlocks=["ch17_main_002"]
    )

    quests["ch17_main_001"] = ch17_main_001

    # === ГЛАВНЫЙ КВЕСТ: Личные демоны ===
    ch17_main_002 = Quest(
        id="ch17_main_002",
        title="Личные демоны",
        description="Преодолейте иллюзии в Зеркальном зале, где Сущность использует ваши страхи против вас.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Сущность",
        journal_entry="Зеркальный зал показывает ваши худшие страхи. Нужно преодолеть их.",
        prerequisites=["ch17_main_001"]
    )

    ch17_main_002.add_objective(Objective(
        id="obj_enter_hall",
        type=ObjectiveType.EXPLORE,
        description="Войти в Зеркальный зал",
        target_id="mirror_hall",
        required=1,
        is_completed=False
    ))

    ch17_main_002.add_objective(Objective(
        id="obj_face_fears",
        type=ObjectiveType.TALK,
        description="Столкнуться с личными страхами",
        target_id="mirror_trap",
        required=1,
        is_completed=False
    ))

    ch17_main_002.add_objective(Objective(
        id="obj_help_team",
        type=ObjectiveType.MAKE_CHOICE,
        description="Помочь команде преодолеть их страхи",
        target_id="team_fears",
        required=3,
        is_completed=False
    ))

    ch17_main_002.add_objective(Objective(
        id="obj_escape_hall",
        type=ObjectiveType.EXPLORE,
        description="Выйти из зала",
        target_id="mirror_exit",
        required=1,
        is_completed=False
    ))

    ch17_main_002.reward = QuestReward(
        credits=0,
        experience=500,
        relationship_changes={"psychic": 10, "mental_resistance": 20},
        unlocks=["ch17_main_003"]
    )

    quests["ch17_main_002"] = ch17_main_002

    # === ГЛАВНЫЙ КВЕСТ: Древний страж ===
    ch17_main_003 = Quest(
        id="ch17_main_003",
        title="Древний страж",
        description="Встретьтесь со Стражем Ядра и узнайте правду о Сущности.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Страж Ядра",
        journal_entry="Страж Ядра — последний из Древних. Он знает правду о Сущности и трёх путях.",
        prerequisites=["ch17_main_002"]
    )

    ch17_main_003.add_objective(Objective(
        id="obj_reach_chamber",
        type=ObjectiveType.EXPLORE,
        description="Достичь покоев Стража",
        target_id="guardian_chamber",
        required=1,
        is_completed=False
    ))

    ch17_main_003.add_objective(Objective(
        id="obj_listen_history",
        type=ObjectiveType.TALK,
        description="Выслушать историю древней цивилизации",
        target_id="guardian_encounter",
        required=1,
        is_completed=False
    ))

    ch17_main_003.add_objective(Objective(
        id="obj_learn_options",
        type=ObjectiveType.TALK,
        description="Узнать о трёх вариантах решения",
        target_id="guardian_options",
        required=1,
        is_completed=False
    ))

    ch17_main_003.add_objective(Objective(
        id="obj_prelim_choice",
        type=ObjectiveType.MAKE_CHOICE,
        description="Принять предварительное решение",
        target_id="final_choice_unlock",
        required=1,
        is_completed=False
    ))

    ch17_main_003.reward = QuestReward(
        credits=0,
        experience=800,
        relationship_changes={"knowledge": 50},
        unlocks=["chapter_18"]
    )

    quests["ch17_main_003"] = ch17_main_003

    return quests


# === ГЛАВА 18: Финал ===

def create_chapter18_quests() -> Dict[str, Quest]:
    """Квесты для главы 18: Финал"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Битва за будущее ===
    ch18_main_001 = Quest(
        id="ch18_main_001",
        title="Битва за будущее",
        description="Финальное противостояние в ядре станции. Судьба галактики в ваших руках.",
        quest_type=QuestType.MAIN,
        state=QuestState.ACTIVE,
        giver="Сущность",
        journal_entry="Момент истины настал. Три пути: Изгнание, Договор или Слияние. Выбор за вами."
    )

    ch18_main_001.add_objective(Objective(
        id="obj_enter_final_core",
        type=ObjectiveType.EXPLORE,
        description="Войти в ядро станции",
        target_id="station_core_final",
        required=1,
        is_completed=False
    ))

    ch18_main_001.add_objective(Objective(
        id="obj_face_entity",
        type=ObjectiveType.TALK,
        description="Столкнуться с Сущностью лицом к лицу",
        target_id="final_choice",
        required=1,
        is_completed=False
    ))

    ch18_main_001.add_objective(Objective(
        id="obj_final_choice",
        type=ObjectiveType.MAKE_CHOICE,
        description="Сделать финальный выбор",
        target_id="ending_choice",
        required=1,
        is_completed=False
    ))

    ch18_main_001.add_objective(Objective(
        id="obj_resolution",
        type=ObjectiveType.EXPLORE,
        description="Завершить противостояние",
        target_id="final_resolution",
        required=1,
        is_completed=False
    ))

    ch18_main_001.reward = QuestReward(
        credits=0,
        experience=2000,
        achievements=["galaxy_savior"],
        unlocks=["ch18_main_002"]
    )

    quests["ch18_main_001"] = ch18_main_001

    # === ПОБОЧНЫЙ КВЕСТ: Обещание любви (романтика) ===
    ch18_side_001 = Quest(
        id="ch18_side_001",
        title="Обещание любви",
        description="Финальная сцена с романтическим партнёром.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Романтический партнёр",
        journal_entry="После битвы время для личных обещаний.",
        prerequisites=["ch18_main_001"]
    )

    ch18_side_001.add_objective(Objective(
        id="obj_reunion",
        type=ObjectiveType.TALK,
        description="Встретиться с партнёром после битвы",
        target_id="romantic_reunion",
        required=1,
        is_completed=False
    ))

    ch18_side_001.add_objective(Objective(
        id="obj_discuss_future",
        type=ObjectiveType.TALK,
        description="Обсудить будущее",
        target_id="epilogue_romantic",
        required=1,
        is_completed=False
    ))

    ch18_side_001.add_objective(Objective(
        id="obj_joint_decision",
        type=ObjectiveType.MAKE_CHOICE,
        description="Принять совместное решение",
        target_id="future_choice",
        required=1,
        is_completed=False
    ))

    ch18_side_001.reward = QuestReward(
        credits=0,
        experience=500,
        achievements=["true_love"]
    )

    quests["ch18_side_001"] = ch18_side_001

    # === ГЛАВНЫЙ КВЕСТ: Эпилог ===
    ch18_main_002 = Quest(
        id="ch18_main_002",
        title="Эпилог",
        description="Увидьте последствия своих выборов.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Система",
        journal_entry="Время увидеть, к чему привели ваши решения."
    )

    ch18_main_002.add_objective(Objective(
        id="obj_galaxy_aftermath",
        type=ObjectiveType.EXPLORE,
        description="Просмотреть последствия для галактики",
        target_id="galaxy_aftermath",
        required=1,
        is_completed=False
    ))

    ch18_main_002.add_objective(Objective(
        id="obj_companions_fate",
        type=ObjectiveType.EXPLORE,
        description="Узнать судьбу спутников",
        target_id="companions_fate",
        required=1,
        is_completed=False
    ))

    ch18_main_002.add_objective(Objective(
        id="obj_statistics",
        type=ObjectiveType.EXPLORE,
        description="Получить итоговую статистику",
        target_id="game_statistics",
        required=1,
        is_completed=False
    ))

    ch18_main_002.reward = QuestReward(
        credits=0,
        experience=0,
        game_complete=True
    )

    quests["ch18_main_002"] = ch18_main_002

    return quests


# === ОБЪЕДИНЕНИЕ ВСЕХ КВЕСТОВ ===

def create_all_chapter14_18_quests() -> Dict[str, Quest]:
    """Создать все квесты для глав 14-18"""
    all_quests = {}
    all_quests.update(create_chapter14_quests())
    all_quests.update(create_chapter15_quests())
    all_quests.update(create_chapter16_quests())
    all_quests.update(create_chapter17_quests())
    all_quests.update(create_chapter18_quests())
    return all_quests
