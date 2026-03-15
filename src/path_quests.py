"""
Квесты для каждого пути: Альянс, Наблюдатель, Независимость
Глава 11-18, зависит от выбора в главе 10
"""

from typing import Dict, List

try:
    from .quests import Quest, QuestType, QuestState, QuestReward, Objective, ObjectiveType
except ImportError:
    from quests import Quest, QuestType, QuestState, QuestReward, Objective, ObjectiveType


# ============================================================
# ПУТЬ АЛЬЯНСА
# ============================================================

def create_alliance_path_quests() -> Dict[str, Quest]:
    """Квесты для пути Альянса — официальная поддержка, но ограниченная свобода"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Интеграция ===
    alliance_main_001 = Quest(
        id="alliance_main_001",
        title="Вступление в Альянс",
        description="Пройти процедуру интеграции в структуру Совета Альянса.",
        quest_type=QuestType.MAIN,
        state=QuestState.ACTIVE,
        giver="Капитан Сергей Волков",
        journal_entry="Вы выбрали путь Альянса. Теперь «Элея» — часть официального флота. "
                     "Это даёт ресурсы, но ограничивает независимость.",
        prerequisites=["main_006"]
    )

    alliance_main_001.add_objective(Objective(
        id="obj_report",
        type=ObjectiveType.TALK,
        description="Доложить командованию на станции «Цитадель»",
        target_id="alliance_command",
        required=1,
        is_completed=False
    ))

    alliance_main_001.add_objective(Objective(
        id="obj_receive_rank",
        type=ObjectiveType.MAKE_CHOICE,
        description="Получить звание и назначение",
        target_id="rank_assignment",
        required=1,
        is_completed=False
    ))

    alliance_main_001.add_objective(Objective(
        id="obj_first_mission",
        type=ObjectiveType.EXPLORE,
        description="Выполнить первое официальное задание",
        target_id="first_alliance_mission",
        required=1,
        is_completed=False
    ))

    alliance_main_001.reward = QuestReward(
        credits=10000,
        experience=1000,
        relationship_changes={"sergey_volkov": 20},
        unlocks=["alliance_main_002"],
        items=[{"alliance_credentials": 1}, {"flot_access_codes": 1}]
    )

    quests["alliance_main_001"] = alliance_main_001

    # === ГЛАВНЫЙ КВЕСТ: Протокол безопасности ===
    alliance_main_002 = Quest(
        id="alliance_main_002",
        title="Протокол безопасности",
        description="Разработать протокол защиты артефактов по стандартам Альянса.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Командование Альянса",
        journal_entry="Альянс требует, чтобы артефакты были защищены по их протоколам. "
                     "Это ограничивает доступ команды к ним.",
        prerequisites=["alliance_main_001"]
    )

    alliance_main_002.add_objective(Objective(
        id="obj_security_protocol",
        type=ObjectiveType.COLLECT,
        description="Установить системы защиты Альянса",
        required=3,
        current=0,
        is_completed=False
    ))

    alliance_main_002.add_objective(Objective(
        id="obj_team_compliance",
        type=ObjectiveType.TALK,
        description="Убедить команду принять протокол",
        target_id="crew_meeting",
        required=1,
        is_completed=False
    ))

    alliance_main_002.add_objective(Objective(
        id="obj_inspection",
        type=ObjectiveType.EXPLORE,
        description="Пройти инспекцию",
        target_id="alliance_inspector",
        required=1,
        is_completed=False
    ))

    alliance_main_002.reward = QuestReward(
        credits=5000,
        experience=500,
        relationship_changes={"nadezhda": 15, "sergey_volkov": 10},
        unlocks=["alliance_main_003"]
    )

    quests["alliance_main_002"] = alliance_main_002

    # === ГЛАВНЫЙ КВЕСТ: Миссия Альянса ===
    alliance_main_003 = Quest(
        id="alliance_main_003",
        title="Операция «Щит Галактики»",
        description="Участвовать в совместной операции Альянса против Сущности.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Адмирал Корсо",
        journal_entry="Альянс мобилизует все силы для противостояния Сущности. "
                     "«Элея» — ключевая единица благодаря артефактам.",
        prerequisites=["alliance_main_002"]
    )

    alliance_main_003.add_objective(Objective(
        id="obj_briefing",
        type=ObjectiveType.TALK,
        description="Присутствовать на стратегическом брифинге",
        target_id="admiral_corso",
        required=1,
        is_completed=False
    ))

    alliance_main_003.add_objective(Objective(
        id="obj_coordinate",
        type=ObjectiveType.COLLECT,
        description="Координировать с другими капитанами",
        required=3,
        current=0,
        is_completed=False
    ))

    alliance_main_003.add_objective(Objective(
        id="obj_lead_strike",
        type=ObjectiveType.EXPLORE,
        description="Возглавить ударную группу",
        target_id="strike_force",
        required=1,
        is_completed=False
    ))

    alliance_main_003.reward = QuestReward(
        credits=15000,
        experience=2000,
        relationship_changes={"sergey_volkov": 25},
        unlocks=["chapter_16"],
        achievements=["alliance_hero"]
    )

    quests["alliance_main_003"] = alliance_main_003

    # === ПОБОЧНЫЙ КВЕСТ: Конфликт лояльности ===
    alliance_side_001 = Quest(
        id="alliance_side_001",
        title="Между двумя мирами",
        description="Решить конфликт между приказами Альянса и верностью команде.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Екатерина",
        journal_entry="Альянс требует передачи Екатерины для допроса о её связях с пиратами. "
                     "Вы можете защитить её или выполнить приказ.",
        prerequisites=["alliance_main_001"]
    )

    alliance_side_001.add_objective(Objective(
        id="obj_receive_order",
        type=ObjectiveType.TALK,
        description="Получить приказ о передаче",
        target_id="alliance_officer",
        required=1,
        is_completed=False
    ))

    alliance_side_001.add_objective(Objective(
        id="obj_talk_ekaterina",
        type=ObjectiveType.TALK,
        description="Поговорить с Екатериной",
        target_id="ekaterina",
        required=1,
        is_completed=False
    ))

    alliance_side_001.add_objective(Objective(
        id="obj_make_choice",
        type=ObjectiveType.MAKE_CHOICE,
        description="Принять решение",
        target_id="loyalty_choice",
        required=1,
        is_completed=False
    ))

    alliance_side_001.reward = QuestReward(
        credits=2000,
        experience=600
    )

    quests["alliance_side_001"] = alliance_side_001

    # === ПОБОЧНЫЙ КВЕСТ: Доступ к архивам ===
    alliance_side_002 = Quest(
        id="alliance_side_002",
        title="Секретные архивы",
        description="Получить доступ к засекреченным данным Альянса о Хранителях.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Ирина Лебедева",
        journal_entry="Ирина узнала о секретном архиве Альянса с информацией о проекте «Эхо». "
                     "Официально доступа нет, но можно найти способ.",
        prerequisites=["alliance_main_002"]
    )

    alliance_side_002.add_objective(Objective(
        id="obj_find_archive",
        type=ObjectiveType.EXPLORE,
        description="Найти расположение архива",
        target_id="archive_location",
        required=1,
        is_completed=False
    ))

    alliance_side_002.add_objective(Objective(
        id="obj_get_clearance",
        type=ObjectiveType.USE_ITEM,
        description="Получить допуск",
        target_id="security_clearance",
        required=1,
        is_completed=False
    ))

    alliance_side_002.add_objective(Objective(
        id="obj_extract_data",
        type=ObjectiveType.COLLECT,
        description="Извлечь данные",
        required=1,
        is_completed=False
    ))

    alliance_side_002.reward = QuestReward(
        credits=3000,
        experience=800,
        relationship_changes={"irina_lebedeva": 20},
        items=[{"classified_documents": 1}],
        unlocks=["alliance_secret_info"]
    )

    quests["alliance_side_002"] = alliance_side_002

    return quests


# ============================================================
# ПУТЬ НАБЛЮДАТЕЛЯ
# ============================================================

def create_observer_path_quests() -> Dict[str, Quest]:
    """Квесты для пути Наблюдателя — истина и древние знания"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Контакт ===
    observer_main_001 = Quest(
        id="observer_main_001",
        title="Голос из глубины",
        description="Установить контакт с Наблюдателем — ИИ Хранителей.",
        quest_type=QuestType.MAIN,
        state=QuestState.ACTIVE,
        giver="Наблюдатель",
        journal_entry="Наблюдатель — древний ИИ, оставшийся от Хранителей. "
                     "Он предлагает истину о происхождении артефактов и Сущности.",
        prerequisites=["main_006"]
    )

    observer_main_001.add_objective(Objective(
        id="obj_receive_signal",
        type=ObjectiveType.EXPLORE,
        description="Следовать сигналу Наблюдателя",
        target_id="observer_signal",
        required=1,
        is_completed=False
    ))

    observer_main_001.add_objective(Objective(
        id="obj_find_station",
        type=ObjectiveType.EXPLORE,
        description="Найти скрытую станцию Хранителей",
        target_id="hidden_station",
        required=1,
        is_completed=False
    ))

    observer_main_001.add_objective(Objective(
        id="obj_first_contact",
        type=ObjectiveType.TALK,
        description="Первый контакт с Наблюдателем",
        target_id="the_observer",
        required=1,
        is_completed=False
    ))

    observer_main_001.reward = QuestReward(
        credits=5000,
        experience=1500,
        relationship_changes={"athena": 25, "anna": 20},
        unlocks=["observer_main_002"],
        items=[{"keeper_comm_device": 1}]
    )

    quests["observer_main_001"] = observer_main_001

    # === ГЛАВНЫЙ КВЕСТ: Испытание ===
    observer_main_002 = Quest(
        id="observer_main_002",
        title="Испытание Хранителей",
        description="Пройти испытания, чтобы доказать достойность.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Наблюдатель",
        journal_entry="Наблюдатель не доверяет просто так. "
                     "Он требует доказательств, что человечество достойно наследия Хранителей.",
        prerequisites=["observer_main_001"]
    )

    observer_main_002.add_objective(Objective(
        id="obj_trial_wisdom",
        type=ObjectiveType.MAKE_CHOICE,
        description="Испытание мудрости",
        target_id="trial_wisdom",
        required=1,
        is_completed=False
    ))

    observer_main_002.add_objective(Objective(
        id="obj_trial_sacrifice",
        type=ObjectiveType.MAKE_CHOICE,
        description="Испытание жертвы",
        target_id="trial_sacrifice",
        required=1,
        is_completed=False
    ))

    observer_main_002.add_objective(Objective(
        id="obj_trial_vision",
        type=ObjectiveType.MAKE_CHOICE,
        description="Испытание видения",
        target_id="trial_vision",
        required=1,
        is_completed=False
    ))

    observer_main_002.reward = QuestReward(
        credits=8000,
        experience=2500,
        relationship_changes={"the_observer": 30},
        unlocks=["observer_main_003", "resonance_level_3"],
        achievements=["keeper_trusted"]
    )

    quests["observer_main_002"] = observer_main_002

    # === ГЛАВНЫЙ КВЕСТ: Знание ===
    observer_main_003 = Quest(
        id="observer_main_003",
        title="Полная истина",
        description="Узнать правду о Хранителях, Сущности и судьбе галактики.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Наблюдатель",
        journal_entry="Пройдя испытания, вы заслужили право знать всю правду. "
                     "Но готовы ли вы к ней?",
        prerequisites=["observer_main_002"]
    )

    observer_main_003.add_objective(Objective(
        id="obj_enter_core",
        type=ObjectiveType.EXPLORE,
        description="Войти в ядро знаний",
        target_id="knowledge_core",
        required=1,
        is_completed=False
    ))

    observer_main_003.add_objective(Objective(
        id="obj_absorb_truth",
        type=ObjectiveType.MAKE_CHOICE,
        description="Принять истину",
        target_id="accept_truth",
        required=1,
        is_completed=False
    ))

    observer_main_003.add_objective(Objective(
        id="obj_decide_fate",
        type=ObjectiveType.MAKE_CHOICE,
        description="Решить судьбу Сущности",
        target_id="entity_fate",
        required=1,
        is_completed=False
    ))

    observer_main_003.reward = QuestReward(
        credits=10000,
        experience=4000,
        unlocks=["chapter_16", "observer_endings"],
        achievements=["truth_seeker"]
    )

    quests["observer_main_003"] = observer_main_003

    # === ПОБОЧНЫЙ КВЕСТ: Синхронизация ===
    observer_side_001 = Quest(
        id="observer_side_001",
        title="Резонанс с Афиной",
        description="Помочь Афине синхронизироваться с системами Хранителей.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Афина",
        journal_entry="После контакта с Наблюдателем Афина чувствует связь с его системами. "
                     "Это может усилить её способности.",
        prerequisites=["observer_main_001"]
    )

    observer_side_001.add_objective(Objective(
        id="obj_prepare_athena",
        type=ObjectiveType.TALK,
        description="Подготовить Афину к синхронизации",
        target_id="athena_preparation",
        required=1,
        is_completed=False
    ))

    observer_side_001.add_objective(Objective(
        id="obj_find_interface",
        type=ObjectiveType.EXPLORE,
        description="Найти интерфейс Хранителей",
        target_id="keeper_interface",
        required=1,
        is_completed=False
    ))

    observer_side_001.add_objective(Objective(
        id="obj_sync_process",
        type=ObjectiveType.MAKE_CHOICE,
        description="Провести синхронизацию",
        target_id="sync_choice",
        required=1,
        is_completed=False
    ))

    observer_side_001.reward = QuestReward(
        credits=5000,
        experience=1000,
        relationship_changes={"athena": 30},
        unlocks=["athena_power_boost"]
    )

    quests["observer_side_001"] = observer_side_001

    # === ПОБОЧНЫЙ КВЕСТ: Анна-медиум ===
    observer_side_002 = Quest(
        id="observer_side_002",
        title="Голос Анны",
        description="Развить способности Анны как связи между мирами.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Анна",
        journal_entry="Анна — единственная, кто слышит Хранителей напрямую. "
                     "Её способности могут быть ключом к победе над Сущностью.",
        prerequisites=["observer_main_002"]
    )

    observer_side_002.add_objective(Objective(
        id="obj_train_resonance",
        type=ObjectiveType.COLLECT,
        description="Тренировать резонанс Анны",
        required=5,
        current=0,
        is_completed=False
    ))

    observer_side_002.add_objective(Objective(
        id="obj_stabilize",
        type=ObjectiveType.USE_ITEM,
        description="Стабилизировать её психику",
        target_id="stabilizer",
        required=1,
        is_completed=False
    ))

    observer_side_002.add_objective(Objective(
        id="obj_contact_keepers",
        type=ObjectiveType.TALK,
        description="Установить контакт через Анну",
        target_id="keepers_contact",
        required=1,
        is_completed=False
    ))

    observer_side_002.reward = QuestReward(
        credits=6000,
        experience=1500,
        relationship_changes={"anna": 25},
        unlocks=["anna_ability_max"]
    )

    quests["observer_side_002"] = observer_side_002

    return quests


# ============================================================
# ПУТЬ НЕЗАВИСИМОСТИ
# ============================================================

def create_independent_path_quests() -> Dict[str, Quest]:
    """Квесты для пути Независимости — свобода, но без поддержки"""
    quests = {}

    # === ГЛАВНЫЙ КВЕСТ: Свободный путь ===
    independent_main_001 = Quest(
        id="independent_main_001",
        title="Свой путь",
        description="Начать независимую операцию против Сущности.",
        quest_type=QuestType.MAIN,
        state=QuestState.ACTIVE,
        giver="Макс Велл",
        journal_entry="Вы отказались от всех покровителей. "
                     "«Элея» — независимый корабль. Придётся всё делать самому.",
        prerequisites=["main_006"]
    )

    independent_main_001.add_objective(Objective(
        id="obj_inform_crew",
        type=ObjectiveType.TALK,
        description="Информировать экипаж о решении",
        target_id="crew_announcement",
        required=1,
        is_completed=False
    ))

    independent_main_001.add_objective(Objective(
        id="obj_gather_contacts",
        type=ObjectiveType.COLLECT,
        description="Собрать независимые контакты",
        required=5,
        current=0,
        is_completed=False
    ))

    independent_main_001.add_objective(Objective(
        id="obj_secure_funding",
        type=ObjectiveType.COLLECT,
        description="Обеспечить финансирование",
        required=20000,
        current=0,
        is_completed=False
    ))

    independent_main_001.reward = QuestReward(
        credits=2000,
        experience=800,
        relationship_changes={"alia_naar": 10, "rina_mirai": 10},
        unlocks=["independent_main_002"]
    )

    quests["independent_main_001"] = independent_main_001

    # === ГЛАВНЫЙ КВЕСТ: Сеть союзников ===
    independent_main_002 = Quest(
        id="independent_main_002",
        title="Коалиция независимых",
        description="Создать сеть независимых капитанов и организаций.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Сергей Волков (если союзник) или Вероника",
        journal_entry="Без официальной поддержки нужны союзники. "
                     "Другие независимые капитаны могут присоединиться.",
        prerequisites=["independent_main_001"]
    )

    independent_main_002.add_objective(Objective(
        id="obj_find_captains",
        type=ObjectiveType.TALK,
        description="Найти независимых капитанов",
        required=3,
        current=0,
        is_completed=False
    ))

    independent_main_002.add_objective(Objective(
        id="obj_convince_join",
        type=ObjectiveType.MAKE_CHOICE,
        description="Убедить присоединиться",
        target_id="convince_captains",
        required=1,
        is_completed=False
    ))

    independent_main_002.add_objective(Objective(
        id="obj_coordinate_fleet",
        type=ObjectiveType.EXPLORE,
        description="Координировать действия флота",
        target_id="fleet_coordination",
        required=1,
        is_completed=False
    ))

    independent_main_002.reward = QuestReward(
        credits=5000,
        experience=1200,
        relationship_changes={"sergey_volkov": 15, "veronika": 15},
        unlocks=["independent_main_003"]
    )

    quests["independent_main_002"] = independent_main_002

    # === ГЛАВНЫЙ КВЕСТ: Самостоятельный удар ===
    independent_main_003 = Quest(
        id="independent_main_003",
        title="Удар своими силами",
        description="Разработать и выполнить план атаки на Сущность без официальной поддержки.",
        quest_type=QuestType.MAIN,
        state=QuestState.AVAILABLE,
        giver="Макс Велл",
        journal_entry="Коалиция сформирована. План разработан. "
                     "Время нанести удар по Сущности своими силами.",
        prerequisites=["independent_main_002"]
    )

    independent_main_003.add_objective(Objective(
        id="obj_plan_attack",
        type=ObjectiveType.MAKE_CHOICE,
        description="Разработать план атаки",
        target_id="attack_plan",
        required=1,
        is_completed=False
    ))

    independent_main_003.add_objective(Objective(
        id="obj_gather_intel",
        type=ObjectiveType.COLLECT,
        description="Собрать разведданные",
        required=3,
        current=0,
        is_completed=False
    ))

    independent_main_003.add_objective(Objective(
        id="obj_execute_plan",
        type=ObjectiveType.EXPLORE,
        description="Выполнить план",
        target_id="mission_execution",
        required=1,
        is_completed=False
    ))

    independent_main_003.reward = QuestReward(
        credits=10000,
        experience=3000,
        unlocks=["chapter_16"],
        achievements=["independent_operator"]
    )

    quests["independent_main_003"] = independent_main_003

    # === ПОБОЧНЫЙ КВЕСТ: Контрабандный маршрут ===
    independent_side_001 = Quest(
        id="independent_side_001",
        title="Тайные пути",
        description="Использовать связи Вероники для скрытного перемещения.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Вероника",
        journal_entry="Вероника знает маршруты, неизвестные официальным властям. "
                     "Это может дать тактическое преимущество.",
        prerequisites=["independent_main_001"]
    )

    independent_side_001.add_objective(Objective(
        id="obj_meet_contact",
        type=ObjectiveType.TALK,
        description="Встретиться с контактом Вероники",
        target_id="veronica_contact",
        required=1,
        is_completed=False
    ))

    independent_side_001.add_objective(Objective(
        id="obj_test_route",
        type=ObjectiveType.EXPLORE,
        description="Протестировать маршрут",
        target_id="test_route",
        required=1,
        is_completed=False
    ))

    independent_side_001.add_objective(Objective(
        id="obj_secure_passage",
        type=ObjectiveType.COLLECT,
        description="Обеспечить проход для коалиции",
        required=1,
        is_completed=False
    ))

    independent_side_001.reward = QuestReward(
        credits=4000,
        experience=700,
        relationship_changes={"veronika": 20},
        unlocks=["hidden_routes"]
    )

    quests["independent_side_001"] = independent_side_001

    # === ПОБОЧНЫЙ КВЕСТ: Ресурсы пиратов ===
    independent_side_002 = Quest(
        id="independent_side_002",
        title="Наследие Селены",
        description="Захватить ресурсы и информацию с базы Селены Ро.",
        quest_type=QuestType.SIDE,
        state=QuestState.AVAILABLE,
        giver="Екатерина",
        journal_entry="База Селены Ро всё ещё содержит ценные ресурсы. "
                     "Нужно действовать быстро, пока другие не забрали.",
        prerequisites=["independent_main_001"]
    )

    independent_side_002.add_objective(Objective(
        id="obj_return_base",
        type=ObjectiveType.EXPLORE,
        description="Вернуться на базу пиратов",
        target_id="pirate_base_return",
        required=1,
        is_completed=False
    ))

    independent_side_002.add_objective(Objective(
        id="obj_secure_vault",
        type=ObjectiveType.EXPLORE,
        description="Обеспечить доступ к хранилищу",
        target_id="pirate_vault",
        required=1,
        is_completed=False
    ))

    independent_side_002.add_objective(Objective(
        id="obj_extract_resources",
        type=ObjectiveType.COLLECT,
        description="Извлечь ресурсы",
        required=1,
        is_completed=False
    ))

    independent_side_002.reward = QuestReward(
        credits=15000,
        experience=1000,
        items=[{"pirate_tech": 3}, {"ancient_data": 1}]
    )

    quests["independent_side_002"] = independent_side_002

    return quests


# ============================================================
# РЕГИСТРАЦИЯ ВСЕХ КВЕСТОВ
# ============================================================

def create_all_path_quests() -> Dict[str, Quest]:
    """Создать все квесты для всех путей"""
    all_quests = {}
    all_quests.update(create_alliance_path_quests())
    all_quests.update(create_observer_path_quests())
    all_quests.update(create_independent_path_quests())
    return all_quests


def register_path_quests(path: str, quest_manager) -> Dict[str, Quest]:
    """
    Зарегистрировать квесты в зависимости от выбранного пути.
    
    Args:
        path: Выбранный путь ("alliance", "observer", "independence")
        quest_manager: Менеджер квестов для регистрации
    
    Returns:
        Dict[str, Quest]: Словарь зарегистрированных квестов
    """
    if path == "alliance":
        quests = create_alliance_path_quests()
    elif path == "observer":
        quests = create_observer_path_quests()
    elif path == "independence":
        quests = create_independent_path_quests()
    else:
        quests = {}
    
    # Регистрируем квесты в менеджере
    for quest in quests.values():
        quest_manager.add_quest(quest)
    
    return quests
