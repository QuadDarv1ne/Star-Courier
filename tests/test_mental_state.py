"""
Тесты для системы ментального состояния
"""

import unittest
import sys
from pathlib import Path

src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from mental_state import (
    MentalState, MentalStateSystem, MentalCondition,
    EntityInfluenceLevel
)


class TestMentalCondition(unittest.TestCase):
    """Тесты состояний ментального здоровья"""

    def test_stable_condition(self):
        state = MentalState(health=90)
        self.assertEqual(state.get_condition(), MentalCondition.STABLE)

    def test_stressed_condition(self):
        state = MentalState(health=70)
        self.assertEqual(state.get_condition(), MentalCondition.STRESSED)

    def test_traumatized_condition(self):
        state = MentalState(health=50)
        self.assertEqual(state.get_condition(), MentalCondition.TRAUMATIZED)

    def test_corrupted_condition(self):
        state = MentalState(health=30)
        self.assertEqual(state.get_condition(), MentalCondition.CORRUPTED)

    def test_broken_condition(self):
        state = MentalState(health=10)
        self.assertEqual(state.get_condition(), MentalCondition.BROKEN)


class TestEntityInfluence(unittest.TestCase):
    """Тесты влияния Сущности"""

    def test_clean_influence(self):
        state = MentalState(entity_influence=5)
        self.assertEqual(state.get_influence_level(), EntityInfluenceLevel.CLEAN)

    def test_exposed_influence(self):
        state = MentalState(entity_influence=20)
        self.assertEqual(state.get_influence_level(), EntityInfluenceLevel.EXPOSED)

    def test_infected_influence(self):
        state = MentalState(entity_influence=50)
        self.assertEqual(state.get_influence_level(), EntityInfluenceLevel.INFECTED)

    def test_corrupted_influence(self):
        state = MentalState(entity_influence=80)
        self.assertEqual(state.get_influence_level(), EntityInfluenceLevel.CORRUPTED)

    def test_assimilated_influence(self):
        state = MentalState(entity_influence=95)
        self.assertEqual(state.get_influence_level(), EntityInfluenceLevel.ASSIMILATED)


class TestMentalStateSystem(unittest.TestCase):
    """Тесты системы управления ментальным состоянием"""

    def setUp(self):
        self.system = MentalStateSystem()

    def test_init(self):
        self.assertEqual(self.system.player_state.health, 100)
        self.assertEqual(self.system.player_state.entity_influence, 0)
        self.assertEqual(self.system.player_state.stress, 0)

    def test_initialize_crew(self):
        crew_ids = ["crew1", "crew2", "crew3"]
        self.system.initialize_crew(crew_ids)
        self.assertEqual(len(self.system.crew_states), 3)
        self.assertIn("crew1", self.system.crew_states)

    def test_change_mental_health_increase(self):
        self.system.change_mental_health(20)
        self.assertEqual(self.system.player_state.health, 100)  # cap at 100

    def test_change_mental_health_decrease(self):
        self.system.change_mental_health(-30)
        self.assertEqual(self.system.player_state.health, 70)

    def test_change_mental_health_floor(self):
        self.system.change_mental_health(-150)
        self.assertEqual(self.system.player_state.health, 0)

    def test_change_entity_influence(self):
        self.system.change_entity_influence(40)
        self.assertEqual(self.system.player_state.entity_influence, 40)

    def test_change_entity_influence_cap(self):
        self.system.change_entity_influence(150)
        self.assertEqual(self.system.player_state.entity_influence, 100)

    def test_add_stress(self):
        self.system.add_stress(50)
        self.assertEqual(self.system.player_state.stress, 50)

    def test_reduce_stress(self):
        self.system.add_stress(50)
        self.system.reduce_stress(30)
        self.assertEqual(self.system.player_state.stress, 20)

    def test_stress_affects_health(self):
        self.system.add_stress(80)
        self.assertEqual(self.system.player_state.health, 90)  # -10 from high stress

    def test_add_effect(self):
        self.system.add_effect("buff", 5)
        self.assertTrue(self.system.has_effect("buff"))

    def test_tick_effects(self):
        self.system.add_effect("temp", 1)
        self.system.tick_effects()
        self.assertFalse(self.system.has_effect("temp"))

    def test_add_trauma(self):
        self.system.add_trauma("combat_trauma")
        self.assertTrue(self.system.has_trauma("combat_trauma"))

    def test_remove_trauma(self):
        self.system.add_trauma("combat_trauma")
        self.system.remove_trauma("combat_trauma")
        self.assertFalse(self.system.has_trauma("combat_trauma"))


class TestMentalStateEvents(unittest.TestCase):
    """Тесты событий ментального состояния"""

    def setUp(self):
        self.system = MentalStateSystem()

    def test_on_combat_end_victory(self):
        initial_health = self.system.player_state.health
        self.system.on_combat_end(victory=True)
        self.assertLessEqual(self.system.player_state.health, initial_health)

    def test_on_combat_end_defeat(self):
        initial_health = self.system.player_state.health
        self.system.on_combat_end(victory=False)
        self.assertLess(self.system.player_state.health, initial_health)

    def test_on_combat_end_casualties(self):
        self.system.on_combat_end(victory=True, casualties=2)
        self.assertEqual(self.system.player_state.health, 60)  # 100 - 20*2

    def test_on_entity_encounter(self):
        self.system.on_entity_encounter(intensity=20)
        self.assertEqual(self.system.player_state.entity_influence, 20)
        self.assertEqual(self.system.player_state.health, 95)  # -5

    def test_on_nightmare(self):
        initial_health = self.system.player_state.health
        self.system.on_nightmare()
        self.assertEqual(self.system.player_state.health, initial_health - 10)
        self.assertTrue(self.system.player_state.has_nightmares)

    def test_on_rest(self):
        self.system.change_mental_health(-30)
        self.system.add_stress(50)
        self.system.on_rest(quality=2)
        self.assertEqual(self.system.player_state.health, 80)  # 70 + 10
        self.assertEqual(self.system.player_state.stress, 30)  # 50 - 20

    def test_on_therapy(self):
        self.system.change_mental_health(-40)
        self.system.add_stress(60)
        self.system.on_therapy(effectiveness=2)
        self.assertEqual(self.system.player_state.health, 90)  # 60 + 30
        self.assertEqual(self.system.player_state.stress, 20)  # 60 - 40


class TestResistanceChecks(unittest.TestCase):
    """Тесты проверок сопротивления"""

    def setUp(self):
        self.system = MentalStateSystem()

    def test_check_resistance_high_health(self):
        self.system.player_state.health = 100
        self.system.player_state.entity_influence = 0
        self.system.player_state.stress = 0
        # Шанс должен быть высоким, тестируем что метод работает
        result = self.system.check_resistance()
        self.assertIsInstance(result, bool)

    def test_check_resistance_low_health(self):
        self.system.player_state.health = 20
        self.system.player_state.entity_influence = 80
        self.system.player_state.stress = 60
        result = self.system.check_resistance()
        self.assertIsInstance(result, bool)

    def test_check_sanity_success(self):
        self.system.player_state.health = 100
        result = self.system.check_sanity(horror_level=30)
        self.assertIsInstance(result, bool)

    def test_check_sanity_failure(self):
        self.system.player_state.health = 30
        initial_health = self.system.player_state.health
        result = self.system.check_sanity(horror_level=80)
        if not result:
            self.assertLess(self.system.player_state.health, initial_health)


class TestSerialization(unittest.TestCase):
    """Тесты сериализации"""

    def test_to_dict(self):
        system = MentalStateSystem()
        system.change_mental_health(-20)
        system.change_entity_influence(30)
        system.add_stress(40)
        system.add_effect("buff", 5)
        system.add_trauma("trauma")

        data = system.to_dict()

        self.assertIn("player", data)
        self.assertEqual(data["player"]["health"], 80)
        self.assertEqual(data["player"]["entity_influence"], 30)
        self.assertEqual(data["player"]["stress"], 40)

    def test_from_dict(self):
        data = {
            "player": {
                "health": 60,
                "entity_influence": 50,
                "stress": 30,
                "traumas": ["combat_trauma"],
                "effects": {"buff": 3},
                "flags": {
                    "has_nightmares": True,
                    "hears_entity": False,
                    "sees_visions": True
                }
            },
            "crew": {},
            "event_log": []
        }

        system = MentalStateSystem.from_dict(data)

        self.assertEqual(system.player_state.health, 60)
        self.assertEqual(system.player_state.entity_influence, 50)
        self.assertEqual(system.player_state.stress, 30)
        self.assertTrue(system.player_state.has_nightmares)
        self.assertTrue(system.player_state.sees_visions)


if __name__ == "__main__":
    unittest.main(verbosity=2)
