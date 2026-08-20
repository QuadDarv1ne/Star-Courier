"""
Интеграционные тесты для проверок улучшений
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.save_system import GameState
from src.abilities import AbilityType, AbilityTier
from src.path_system import PathType
from src.quests_ch6_10 import register_all_new_quests
from src.quests_ch11_12 import create_all_chapter11_12_quests
from src.quests_ch14_18 import create_all_chapter14_18_quests
from src.random_events_v5 import SPACE_EVENTS, STATION_EVENTS
from src.banters_v5 import CHARACTER_BANTERS
from src.ending_system import EndingType


def test_game_state():
    """Тест создания GameState"""
    gs = GameState()
    gs.new_game()
    assert gs.save_data is not None
    assert gs.crew_manager is not None
    assert gs.abilities_manager is not None
    print("1. GameState created OK")


def test_abilities():
    """Тест системы способностей"""
    gs = GameState()
    tier = gs.abilities_manager.get_tier(AbilityType.PSYCHIC)
    assert tier == AbilityTier.NONE

    # Тест add_xp
    result = gs.abilities_manager.add_xp("psychic", 15)
    assert result is True
    new_tier = gs.abilities_manager.get_tier(AbilityType.PSYCHIC)
    assert new_tier == AbilityTier.BASIC
    print("2. Abilities add_xp OK")


def test_resonance():
    """Тест системы резонанса"""
    gs = GameState()
    initial_level = gs.resonance_system.get_level_number()
    gs.resonance_system.add_experience(10)
    assert gs.resonance_system.experience == 10
    print(f"3. Resonance OK (level={initial_level}, exp=10)")


def test_path_system():
    """Тест системы путей"""
    gs = GameState()
    result = gs.path_system.choose_path(PathType.ALLIANCE)
    assert result is True
    current = gs.path_system.get_current_path()
    assert current is not None
    assert current.name == "Альянс"
    print("4. Path system OK")


def test_factions():
    """Тест системы фракций"""
    gs = GameState()
    standings = gs.faction_manager.get_all_standings()
    assert len(standings) >= 3  # Минимум 3 фракции

    gs.change_faction_reputation("alliance", 10, "test")
    rep = gs.faction_manager.get_reputation("alliance")
    assert rep == 10
    print(f"5. Factions OK (count={len(standings)})")


def test_empathy_calculation():
    """Тест расчёта эмпатии"""
    gs = GameState()
    gs.new_game()

    # Начальная эмпатия должна быть 0
    empathy = gs._calculate_empathy()
    assert empathy == 0

    # После установки отношений
    gs.save_data.relationships["test_char"] = 50
    gs.save_data.trust_values["test_char"] = 50
    empathy = gs._calculate_empathy()
    assert empathy > 0
    assert empathy <= 100
    print(f"6. Empathy calculation OK (empathy={empathy})")


def test_ending_check():
    """Тест проверки концовок"""
    gs = GameState()
    gs.new_game()

    # Эмпатия должна рассчитываться корректно
    empathy = gs._calculate_empathy()
    psychic = gs.abilities_manager.get_tier(AbilityType.PSYCHIC).value * 25
    resonance_level = gs.resonance_system.get_level_number()
    abilities = gs._collect_ending_abilities()
    completed_quests = gs.quest_manager.completed_quests

    for ending_type in EndingType:
        unlocked = gs.check_ending_unlock(ending_type)
        # В начале игры ни одна концовка не разблокирована
        assert unlocked is False
    print("7. Ending check OK")


def test_quests():
    """Тест квестов"""
    # Квесты глав 11-12
    quests_11_12 = create_all_chapter11_12_quests()
    assert len(quests_11_12) > 0

    # Квесты глав 14-18
    quests_14_18 = create_all_chapter14_18_quests()
    assert len(quests_14_18) > 0

    # Квесты глав 6-10
    from src.quests import QuestManager
    qm = QuestManager()
    register_all_new_quests(qm)
    assert len(qm.active_quests) > 0
    print(f"8. Quests OK (ch11-12: {len(quests_11_12)}, ch14-18: {len(quests_14_18)}, ch6-10: {len(qm.active_quests)})")


def test_random_events():
    """Тест случайных событий"""
    assert len(SPACE_EVENTS) > 0
    assert len(STATION_EVENTS) > 0
    print(f"9. Random events OK (space: {len(SPACE_EVENTS)}, station: {len(STATION_EVENTS)})")


def test_banters():
    """Тест бантеров"""
    assert len(CHARACTER_BANTERS) > 0
    print(f"10. Banters OK (count: {len(CHARACTER_BANTERS)})")


def test_save_load():
    """Тест сохранения/загрузки"""
    gs = GameState()
    gs.new_game()

    # Используем реальные ID персонажей
    gs.save_data.flags["test_flag"] = True
    athena = gs.crew_manager.get_character("athena")
    if athena:
        athena.relationship = 50
        athena.trust = 30

    gs.save_game("test_integration_save.json")
    assert gs.save_manager.current_save is not None

    loaded = gs.save_manager.load_game("test_integration_save.json")
    assert loaded is not None
    assert loaded.flags.get("test_flag") is True
    assert loaded.relationships is not None and loaded.relationships.get("athena") == 50
    assert loaded.trust_values is not None and loaded.trust_values.get("athena") == 30
    print("11. Save/Load OK")


if __name__ == "__main__":
    tests = [
        test_game_state,
        test_abilities,
        test_resonance,
        test_path_system,
        test_factions,
        test_empathy_calculation,
        test_ending_check,
        test_quests,
        test_random_events,
        test_banters,
        test_save_load,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            test()
            passed += 1
        except Exception as e:
            print(f"FAILED: {test.__name__}: {e}")
            failed += 1

    print(f"\n{'='*40}")
    print(f"Результаты: {passed} passed, {failed} failed")
    if failed == 0:
        print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
