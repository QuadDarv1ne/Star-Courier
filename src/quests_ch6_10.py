"""
Новые квесты для глав 6-10
Интегрируется с существующей системой quests.py
"""

from typing import Dict
from quests import Quest, QuestType, QuestState, QuestReward, Objective, ObjectiveType, QuestManager


def create_chapter6_quests() -> Dict[str, Quest]:
    """Создать квесты для главы 6: Орбис-9"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Встреча с Волковым ===
    main_002 = Quest(
        id="main_002",
        title="Тайны Орбиса-9",
        description="Прибыть на станцию Орбис-9 и встретиться с профессором Волковым.",
        quest_type=QuestType.MAIN,
        state=QuestState.ACTIVE,
        giver="Командование флота",
        journal_entry="Станция Орбис-9 хранит секреты проекта «Эхо». "
                     "Профессор Волков может раскрыть правду об артефактах.",
        prerequisites=["main_001"]
    )

    main_002.add_objective(Objective(
        id="obj_arrive",
        type=ObjectiveType.EXPLORE,
        description="Прибыть на станцию Орбис-9",
        target_id="orbis_station",
        required=1,
        is_completed=False
    ))

    main_002.add_objective(Objective(
        id="obj_meet_volkov",
        type=ObjectiveType.TALK,
        description="Встретиться с профессором Волковым",
        target_id="volkov",
        required=1,
        is_completed=False
    ))

    main_002.add_objective(Objective(
        id="obj_learn_artifacts",
        type=ObjectiveType.MAKE_CHOICE,
        description="Узнать о семи ключах Хранителей",
        target_id="keepers_lore",
        required=1,
        is_completed=False
    ))

    main_002.reward = QuestReward(
        credits=2000,
        experience=500,
        relationship_changes={"volkov": 10},
        unlocks=["side_003", "side_004"]
    )

    quests["main_002"] = main_002

    # === ПОБОЧНЫЙ: Сектор Д-7 ===
    side_003 = Quest(
        id="side_003",
        title="Закрытый сектор",
        description="Исследовать таинственный сектор Д-7 станции.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Афина (обнаружено автоматически)",
        journal_entry="Афина обнаружила аномалии в секторе Д-7. "
                     "Официально он закрыт, но фиксируются энергетические всплески.",
        prerequisites=["main_002"]
    )

    side_003.add_objective(Objective(
        id="obj_find_entrance",
        type=ObjectiveType.EXPLORE,
        description="Найти вход в сектор Д-7",
        target_id="sector_d7_entrance",
        required=1,
        is_completed=False
    ))

    side_003.add_objective(Objective(
        id="obj_bypass_lock",
        type=ObjectiveType.USE_ITEM,
        description="Обойти замки безопасности",
        target_id="hacking_tool",
        required=1,
        is_completed=False
    ))

    side_003.add_objective(Objective(
        id="obj_discover_truth",
        type=ObjectiveType.EXPLORE,
        description="Раскрыть правду о содержащихся",
        target_id="containment_chambers",
        required=1,
        is_completed=False
    ))

    side_003.add_objective(Objective(
        id="obj_collect_evidence",
        type=ObjectiveType.COLLECT,
        description="Собрать доказательства экспериментов",
        required=5,
        current=0,
        is_completed=False,
        is_optional=True
    ))

    side_003.reward = QuestReward(
        credits=1500,
        experience=400,
        relationship_changes={"irina_lebedeva": 10, "nadezhda": 5},
        items=[{"classified_documents": 1}],
        unlocks=["side_004"]
    )

    quests["side_003"] = side_003

    # === ПОБОЧНЫЙ: Проект Эхо ===
    side_004 = Quest(
        id="side_004",
        title="Эхо прошлого",
        description="Узнать правду о провале проекта «Эхо».",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Профессор Волков",
        journal_entry="Проект «Эхо» пытался создать искусственный ключ Хранителей. "
                     "Эксперимент провалился катастрофически. Нужно узнать детали.",
        prerequisites=["side_003"]
    )

    side_004.add_objective(Objective(
        id="obj_access_files",
        type=ObjectiveType.USE_ITEM,
        description="Получить доступ к засекреченным файлам",
        target_id="volkov_credentials",
        required=1,
        is_completed=False
    ))

    side_004.add_objective(Objective(
        id="obj_find_survivors",
        type=ObjectiveType.TALK,
        description="Найти выживших участников проекта",
        target_id="echo_survivors",
        required=1,
        is_completed=False
    ))

    side_004.add_objective(Objective(
        id="obj_understand_portal",
        type=ObjectiveType.COLLECT,
        description="Собрать информацию о портале",
        required=3,
        current=0,
        is_completed=False
    ))

    side_004.reward = QuestReward(
        credits=1000,
        experience=600,
        relationship_changes={"irina_lebedeva": 15, "athena": 10},
        unlocks=["resonance_ability_basic"]
    )

    quests["side_004"] = side_004

    # === ИССЛЕДОВАТЕЛЬСКИЙ: Артефакты станции ===
    research_002 = Quest(
        id="research_002",
        title="Спящие ключи",
        description="Помочь Ирине исследовать неактивные артефакты на станции.",
        quest_type=QuestType.RESEARCH,
        state=QuestState.AVAILABLE,
        giver="Ирина Лебедева",
        journal_entry="На станции хранятся два «спящих» артефакта. "
                     "Ирина хочет понять, почему они неактивны.",
        prerequisites=["main_002"]
    )

    research_002.add_objective(Objective(
        id="obj_scan_artifacts",
        type=ObjectiveType.USE_ITEM,
        description="Провести сканирование артефактов станции",
        target_id="station_artifacts",
        required=2,
        current=0,
        is_completed=False
    ))

    research_002.add_objective(Objective(
        id="obj_compare",
        type=ObjectiveType.COLLECT,
        description="Сравнить показатели с нашим артефактом",
        required=1,
        is_completed=False
    ))

    research_002.add_objective(Objective(
        id="obj_theory",
        type=ObjectiveType.TALK,
        description="Обсудить теорию с Ириной",
        target_id="irina_lebedeva",
        required=1,
        is_completed=False
    ))

    research_002.reward = QuestReward(
        credits=800,
        experience=350,
        relationship_changes={"irina_lebedeva": 20},
        items=[{"artifact_scanner": 1}],
        unlocks=["resonance_theory"]
    )

    quests["research_002"] = research_002

    return quests


def create_chapter7_quests() -> Dict[str, Quest]:
    """Создать квесты для главы 7: Предатель"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Обнаружение шпиона ===
    main_003 = Quest(
        id="main_003",
        title="Тень на борту",
        description="Выяснить, кто передаёт информацию пиратам.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Афина",
        journal_entry="Зашифрованный канал связи ведёт с Элеи на пиратский корабль. "
                     "Кто-то из экипажа — предатель. Нужно найти правду.",
        prerequisites=["main_002"]
    )

    main_003.add_objective(Objective(
        id="obj_trace_signal",
        type=ObjectiveType.EXPLORE,
        description="Отследить источник сигнала",
        target_id="signal_trace",
        required=1,
        is_completed=False
    ))

    main_003.add_objective(Objective(
        id="obj_confront_suspect",
        type=ObjectiveType.TALK,
        description="Confront подозреваемого",
        target_id="ekaterina",
        required=1,
        is_completed=False
    ))

    main_003.add_objective(Objective(
        id="obj_make_decision",
        type=ObjectiveType.MAKE_CHOICE,
        description="Решить судьбу предателя",
        target_id="judgment",
        required=1,
        is_completed=False
    ))

    main_003.reward = QuestReward(
        credits=1500,
        experience=600,
        unlocks=["main_004", "personal_001"]
    )

    quests["main_003"] = main_003

    # === ЛИЧНЫЙ КВЕСТ ЕКАТЕРИНЫ: Спасение Анны ===
    personal_001 = Quest(
        id="personal_001",
        title="Семья превыше всего",
        description="Помочь Екатерине спасти её сестру Анну из рук пиратов.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Екатерина",
        journal_entry="Екатерина предала нас, чтобы спасти сестру. "
                     "Анна — заложница на базе Селены Ро. Мы можем исправить ситуацию.",
        prerequisites=["main_003"]
    )

    personal_001.add_objective(Objective(
        id="obj_get_intel",
        type=ObjectiveType.COLLECT,
        description="Собрать разведданные о базе пиратов",
        required=3,
        current=0,
        is_completed=False
    ))

    personal_001.add_objective(Objective(
        id="obj_plan_raid",
        type=ObjectiveType.MAKE_CHOICE,
        description="Разработать план проникновения",
        target_id="raid_plan",
        required=1,
        is_completed=False
    ))

    personal_001.add_objective(Objective(
        id="obj_rescue_anna",
        type=ObjectiveType.TALK,
        description="Спасти Анну",
        target_id="anna",
        required=1,
        is_completed=False
    ))

    personal_001.reward = QuestReward(
        credits=2500,
        experience=800,
        relationship_changes={"ekaterina": 30, "anna": 25},
        items=[{"anna_journal": 1}],
        achievements=["family_reunion"],
        unlocks=["anna_as_companion"]
    )

    quests["personal_001"] = personal_001

    return quests


def create_chapter8_quests() -> Dict[str, Quest]:
    """Создать квесты для главы 8: Рейд на пиратскую базу"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Рейд ===
    main_004 = Quest(
        id="main_004",
        title="Удар в сердце",
        description="Проникнуть на базу Селены Ро и спасти Анну.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Макс Велл",
        journal_entry="База пиратов скрыта в астероидном поясе. "
                     "У нас есть один шанс проникнуть внутрь.",
        prerequisites=["main_003"]
    )

    main_004.add_objective(Objective(
        id="obj_approach_base",
        type=ObjectiveType.EXPLORE,
        description="Подойти к базе пиратов",
        target_id="pirate_base",
        required=1,
        is_completed=False
    ))

    main_004.add_objective(Objective(
        id="obj_infiltrate",
        type=ObjectiveType.EXPLORE,
        description="Проникнуть на станцию",
        target_id="pirate_station_interior",
        required=1,
        is_completed=False
    ))

    main_004.add_objective(Objective(
        id="obj_find_anna",
        type=ObjectiveType.TALK,
        description="Найти Анну",
        target_id="anna_cell",
        required=1,
        is_completed=False
    ))

    main_004.add_objective(Objective(
        id="obj_confront_selena",
        type=ObjectiveType.TALK,
        description="Конфронтация с Селеной Ро",
        target_id="selena_ro",
        required=1,
        is_completed=False
    ))

    main_004.add_objective(Objective(
        id="obj_escape",
        type=ObjectiveType.EXPLORE,
        description="Эвакуироваться с базы",
        target_id="escape_route",
        required=1,
        is_completed=False
    ))

    main_004.reward = QuestReward(
        credits=5000,
        experience=1500,
        relationship_changes={"anna": 30, "ekaterina": 25},
        unlocks=["main_005", "side_005"]
    )

    quests["main_004"] = main_004

    # === БОЕВОЙ КВЕСТ: Зачистка ===
    combat_002 = Quest(
        id="combat_002",
        title="Боевые действия",
        description="Отразить атаку пиратской охраны.",
        quest_type=QuestType.COMBAT,
        state=QuestState.AVAILABLE,
        giver="Надежда",
        journal_entry="Пираты знают о нашем присутствии. "
                     "Нужно прорваться к цели.",
        prerequisites=["main_004"]
    )

    combat_002.add_objective(Objective(
        id="obj_defeat_guards",
        type=ObjectiveType.KILL,
        description="Нейтрализовать охрану",
        required=10,
        current=0,
        is_completed=False
    ))

    combat_002.add_objective(Objective(
        id="obj_secure_route",
        type=ObjectiveType.EXPLORE,
        description="Обеспечить путь отступления",
        target_id="escape_shuttle",
        required=1,
        is_completed=False
    ))

    combat_002.reward = QuestReward(
        credits=2000,
        experience=600,
        relationship_changes={"nadezhda": 15, "alia_naar": 10},
        items=[{"plasma_rifle": 1}, {"combat_armor": 1}],
        achievements=["pirate_slayer"]
    )

    quests["combat_002"] = combat_002

    # === ПОБОЧНЫЙ: Секреты базы ===
    side_005 = Quest(
        id="side_005",
        title="Сокровищница пиратов",
        description="Найти артефакты и ценности на базе пиратов.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Рина Мирай",
        journal_entry="Селена Ро коллекционировала древние артефакты. "
                     "Может, здесь есть что-то полезное.",
        prerequisites=["main_004"]
    )

    side_005.add_objective(Objective(
        id="obj_search_vault",
        type=ObjectiveType.EXPLORE,
        description="Найти хранилище",
        target_id="pirate_vault",
        required=1,
        is_completed=False
    ))

    side_005.add_objective(Objective(
        id="obj_collect_artifacts",
        type=ObjectiveType.COLLECT,
        description="Собрать артефакты",
        required=5,
        current=0,
        is_completed=False
    ))

    side_005.add_objective(Objective(
        id="obj_find_third_key_info",
        type=ObjectiveType.COLLECT,
        description="Найти информацию о третьем ключе",
        required=1,
        is_completed=False,
        is_optional=True
    ))

    side_005.reward = QuestReward(
        credits=3000,
        experience=400,
        relationship_changes={"rina_mirai": 15},
        items=[{"artifact_fragment": 3}, {"ancient_map": 1}]
    )

    quests["side_005"] = side_005

    return quests


def create_chapter9_10_quests() -> Dict[str, Quest]:
    """Создать квесты для глав 9-10"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Семь ключей ===
    main_005 = Quest(
        id="main_005",
        title="Семь ключей Хранителей",
        description="Узнать правду о предназначении артефактов.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Анна",
        journal_entry="Хранители оставили семь ключей, чтобы открыть дверь... "
                     "или закрыть её навсегда. Выбор за нами.",
        prerequisites=["main_004"]
    )

    main_005.add_objective(Objective(
        id="obj_listen_anna",
        type=ObjectiveType.TALK,
        description="Выслушать историю Анны",
        target_id="anna_revelation",
        required=1,
        is_completed=False
    ))

    main_005.add_objective(Objective(
        id="obj_understand_keepers",
        type=ObjectiveType.COLLECT,
        description="Собрать информацию о Хранителях",
        required=3,
        current=0,
        is_completed=False
    ))

    main_005.add_objective(Objective(
        id="obj_choose_carrier",
        type=ObjectiveType.MAKE_CHOICE,
        description="Выбрать носителя резонанса",
        target_id="carrier_selection",
        required=1,
        is_completed=False
    ))

    main_005.reward = QuestReward(
        credits=2000,
        experience=1000,
        unlocks=["main_006", "resonance_system"]
    )

    quests["main_005"] = main_005

    # === ГЛАВНЫЙ КВЕСТ: Выбор пути ===
    main_006 = Quest(
        id="main_006",
        title="Распутье",
        description="Выбрать путь: Альянс, Наблюдатель или независимость.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Макс Велл",
        journal_entry="Три силы хотят контролировать ключи. "
                     "Совет Альянса. Наблюдатель. Или мы сами. "
                     "Решение определит судьбу галактики.",
        prerequisites=["main_005"]
    )

    main_006.add_objective(Objective(
        id="obj_hear_alliance",
        type=ObjectiveType.TALK,
        description="Выслушать предложение Альянса",
        target_id="sergey_volkov",
        required=1,
        is_completed=False
    ))

    main_006.add_objective(Objective(
        id="obj_hear_observer",
        type=ObjectiveType.TALK,
        description="Услышать голос Наблюдателя",
        target_id="the_observer",
        required=1,
        is_completed=False
    ))

    main_006.add_objective(Objective(
        id="obj_consult_crew",
        type=ObjectiveType.TALK,
        description="Советоваться с командой",
        target_id="crew_meeting",
        required=1,
        is_completed=False
    ))

    main_006.add_objective(Objective(
        id="obj_make_final_choice",
        type=ObjectiveType.MAKE_CHOICE,
        description="Принять окончательное решение",
        target_id="path_choice",
        required=1,
        is_completed=False
    ))

    main_006.add_objective(Objective(
        id="obj_confirm_romance",
        type=ObjectiveType.MAKE_CHOICE,
        description="Закрепить романтические отношения",
        target_id="romance_confirmation",
        required=1,
        is_completed=False,
        is_optional=True
    ))

    main_006.reward = QuestReward(
        credits=3000,
        experience=2000,
        achievements=["path_chosen"],
        unlocks=["chapter_11"]  # Следующая глава
    )

    quests["main_006"] = main_006

    # === ЛИЧНЫЙ КВЕСТ АФИНЫ: Идентичность ===
    personal_002 = Quest(
        id="personal_002",
        title="Больше чем машина",
        description="Помочь Афине раскрыть свою связь с Хранителями.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Афина",
        journal_entry="После контакта с артефактом Афина изменилась. "
                     "Она чувствует ключи. Что это значит для неё?",
        prerequisites=["main_005"]
    )

    personal_002.add_objective(Objective(
        id="obj_analyze_athena",
        type=ObjectiveType.USE_ITEM,
        description="Провести анализ кода Афины",
        target_id="athena_core",
        required=1,
        is_completed=False
    ))

    personal_002.add_objective(Objective(
        id="obj_find_origin",
        type=ObjectiveType.COLLECT,
        description="Узнать о происхождении Афины",
        required=3,
        current=0,
        is_completed=False
    ))

    personal_002.add_objective(Objective(
        id="obj_help_decision",
        type=ObjectiveType.MAKE_CHOICE,
        description="Помочь Афине принять себя",
        target_id="athena_identity",
        required=1,
        is_completed=False
    ))

    personal_002.reward = QuestReward(
        credits=1500,
        experience=800,
        relationship_changes={"athena": 35},
        unlocks=["athena_romance", "athena_android_body"]
    )

    quests["personal_002"] = personal_002

    return quests


def register_all_new_quests(quest_manager: QuestManager):
    """Зарегистрировать все новые квесты в менеджере"""
    all_quests = {}
    all_quests.update(create_chapter6_quests())
    all_quests.update(create_chapter7_quests())
    all_quests.update(create_chapter8_quests())
    all_quests.update(create_chapter9_10_quests())

    for quest_id, quest in all_quests.items():
        quest_manager.add_quest(quest)

    return all_quests
