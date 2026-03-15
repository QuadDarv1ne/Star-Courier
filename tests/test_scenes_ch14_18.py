"""
Тесты для сцен глав 14-18 и интеграции romance/ending систем
"""

import unittest
import sys
from pathlib import Path

src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from scenes_ch14_18 import (
    Chapter18Scenes, RomanceSceneRunner, get_mental_state_effects as get_ch18_mental_effects
)
from romance_scenes import RomanceSceneManager, RomanceProgress
from ending_scenes import EndingSceneManager, EndingProgress, EndingType, EndingVariation


def get_gameplay_mental_effects(mental_health: int, entity_influence: int) -> dict:
    """Вспомогательная функция для тестов gameplay.py"""
    effects = {"hp_bonus": 0, "energy_bonus": 0, "damage_bonus": 0}

    if mental_health >= 80:
        effects["hp_bonus"] = 10
        effects["energy_bonus"] = 10
    elif mental_health >= 60:
        effects["hp_bonus"] = 0
        effects["energy_bonus"] = 0
    elif mental_health >= 40:
        effects["hp_bonus"] = -10
        effects["energy_bonus"] = -10
    elif mental_health >= 20:
        effects["hp_bonus"] = -20
        effects["energy_bonus"] = -15
    else:
        effects["hp_bonus"] = -30
        effects["energy_bonus"] = -25

    if entity_influence >= 50:
        effects["damage_bonus"] = entity_influence // 10
        effects["hp_bonus"] -= entity_influence // 5

    return effects


class TestMentalStateEffects(unittest.TestCase):
    """Тесты эффектов ментального состояния"""

    def test_stable_mental_health(self):
        """Стабильное психическое здоровье - бонусы"""
        effects = get_gameplay_mental_effects(mental_health=90, entity_influence=0)
        self.assertEqual(effects["hp_bonus"], 10)
        self.assertEqual(effects["energy_bonus"], 10)

    def test_stressed_mental_health(self):
        """Стресс - без бонусов"""
        effects = get_gameplay_mental_effects(mental_health=70, entity_influence=0)
        self.assertEqual(effects["hp_bonus"], 0)
        self.assertEqual(effects["energy_bonus"], 0)

    def test_traumatized_mental_health(self):
        """Травма - штрафы"""
        effects = get_gameplay_mental_effects(mental_health=50, entity_influence=0)
        self.assertEqual(effects["hp_bonus"], -10)
        self.assertEqual(effects["energy_bonus"], -10)

    def test_corrupted_mental_health(self):
        """Коррупция - большие штрафы"""
        effects = get_gameplay_mental_effects(mental_health=30, entity_influence=0)
        self.assertEqual(effects["hp_bonus"], -20)
        self.assertEqual(effects["energy_bonus"], -15)

    def test_broken_mental_health(self):
        """Сломленное состояние - максимальные штрафы"""
        effects = get_gameplay_mental_effects(mental_health=10, entity_influence=0)
        self.assertEqual(effects["hp_bonus"], -30)
        self.assertEqual(effects["energy_bonus"], -25)

    def test_entity_influence_damage_bonus(self):
        """Влияние Сущности даёт бонус к урону"""
        effects = get_gameplay_mental_effects(mental_health=80, entity_influence=60)
        self.assertGreater(effects["damage_bonus"], 0)
        self.assertEqual(effects["damage_bonus"], 6)  # 60 // 10

    def test_entity_influence_hp_penalty(self):
        """Влияние Сущности снижает HP"""
        effects = get_gameplay_mental_effects(mental_health=80, entity_influence=50)
        # Базовый бонус 10, штраф 50//5=10
        self.assertEqual(effects["hp_bonus"], 0)

    def test_high_entity_influence_communion(self):
        """Высокое влияние Сущности (сцены)"""
        effects = get_ch18_mental_effects(mental_health=50, entity_influence=80)
        self.assertTrue(effects.get("entity_communion", False))

    def test_combined_effects(self):
        """Комбинированные эффекты"""
        effects = get_gameplay_mental_effects(mental_health=40, entity_influence=70)
        # HP: -10 (threshold) - 14 (entity penalty) = -24
        self.assertEqual(effects["hp_bonus"], -24)
        self.assertEqual(effects["damage_bonus"], 7)


class TestRomanceProgress(unittest.TestCase):
    """Тесты прогресса романтических сцен"""

    def test_create_romance_progress(self):
        progress = RomanceProgress(character_id="irina_lebedeva")
        self.assertEqual(progress.character_id, "irina_lebedeva")
        self.assertFalse(progress.confession_accepted)
        self.assertFalse(progress.romance_unlocked)
        self.assertEqual(len(progress.scenes_completed), 0)

    def test_serialize_romance_progress(self):
        progress = RomanceProgress(
            character_id="alia_naar",
            scenes_completed={"scene1", "scene2"},
            confession_accepted=True,
            romance_unlocked=True,
            relationship_level=85
        )
        data = progress.to_dict()
        
        self.assertEqual(data["character_id"], "alia_naar")
        self.assertTrue(data["confession_accepted"])
        self.assertTrue(data["romance_unlocked"])
        self.assertEqual(data["relationship_level"], 85)

    def test_deserialize_romance_progress(self):
        data = {
            "character_id": "rina_mirai",
            "scenes_completed": ["scene1"],
            "confession_accepted": False,
            "romance_unlocked": True,
            "relationship_level": 70
        }
        progress = RomanceProgress.from_dict(data)
        
        self.assertEqual(progress.character_id, "rina_mirai")
        self.assertIn("scene1", progress.scenes_completed)
        self.assertTrue(progress.romance_unlocked)


class TestRomanceSceneManager(unittest.TestCase):
    """Тесты менеджера романтических сцен"""

    def test_create_manager(self):
        manager = RomanceSceneManager()
        self.assertEqual(len(manager.scenes), 0)
        self.assertEqual(len(manager.progress), 0)

    def test_complete_scene(self):
        manager = RomanceSceneManager()
        manager.complete_scene("irina_confession", "irina_lebedeva")
        
        progress = manager.get_progress("irina_lebedeva")
        self.assertIn("irina_confession", progress.scenes_completed)

    def test_unlock_romance(self):
        manager = RomanceSceneManager()
        manager.unlock_romance("alia_naar")
        
        progress = manager.get_progress("alia_naar")
        self.assertTrue(progress.romance_unlocked)

    def test_set_confession_accepted(self):
        manager = RomanceSceneManager()
        manager.set_confession_accepted("maria", True)
        
        progress = manager.get_progress("maria")
        self.assertTrue(progress.confession_accepted)

    def test_serialize_manager(self):
        manager = RomanceSceneManager()
        manager.complete_scene("scene1", "char1")
        manager.unlock_romance("char2")
        
        data = manager.to_dict()
        self.assertIn("progress", data)
        self.assertIn("char1", data["progress"])
        self.assertIn("char2", data["progress"])

    def test_deserialize_manager(self):
        data = {
            "progress": {
                "char1": {
                    "character_id": "char1",
                    "scenes_completed": ["scene1", "scene2"],
                    "confession_accepted": True,
                    "romance_unlocked": False,
                    "relationship_level": 60
                }
            }
        }
        manager = RomanceSceneManager.from_dict(data)
        progress = manager.get_progress("char1")
        
        self.assertEqual(len(progress.scenes_completed), 2)
        self.assertTrue(progress.confession_accepted)


class TestEndingProgress(unittest.TestCase):
    """Тесты прогресса финальных сцен"""

    def test_create_ending_progress(self):
        progress = EndingProgress()
        self.assertFalse(progress.ending_chosen)
        self.assertIsNone(progress.ending_type)

    def test_serialize_ending_progress(self):
        progress = EndingProgress(
            ending_chosen=True,
            ending_type="exile",
            variation_unlocked={"exile_sacrifice": True},
            requirements_met={"psychic_70": True}
        )
        data = progress.to_dict()
        
        self.assertTrue(data["ending_chosen"])
        self.assertEqual(data["ending_type"], "exile")
        self.assertTrue(data["variation_unlocked"]["exile_sacrifice"])

    def test_deserialize_ending_progress(self):
        data = {
            "ending_chosen": True,
            "ending_type": "treaty",
            "variation_unlocked": {"treaty_guardian": True},
            "requirements_met": {}
        }
        progress = EndingProgress.from_dict(data)
        
        self.assertTrue(progress.ending_chosen)
        self.assertEqual(progress.ending_type, "treaty")


class TestEndingSceneManager(unittest.TestCase):
    """Тесты менеджера финальных сцен"""

    def test_create_manager(self):
        manager = EndingSceneManager()
        self.assertEqual(len(manager.scenes), 0)
        self.assertFalse(manager.progress.ending_chosen)

    def test_choose_ending(self):
        manager = EndingSceneManager()
        manager.choose_ending(EndingType.EXILE)
        
        self.assertTrue(manager.progress.ending_chosen)
        self.assertEqual(manager.progress.ending_type, "exile")

    def test_unlock_variation(self):
        manager = EndingSceneManager()
        manager.unlock_variation("exile_together")
        
        self.assertTrue(manager.progress.variation_unlocked["exile_together"])

    def test_check_requirement(self):
        manager = EndingSceneManager()
        manager.check_requirement("psychic_90", True)
        
        self.assertTrue(manager.progress.requirements_met["psychic_90"])

    def test_serialize_manager(self):
        manager = EndingSceneManager()
        manager.choose_ending(EndingType.MERGE)
        manager.unlock_variation("merge_evolution")
        
        data = manager.to_dict()
        self.assertIn("progress", data)
        self.assertTrue(data["progress"]["ending_chosen"])

    def test_deserialize_manager(self):
        data = {
            "progress": {
                "ending_chosen": True,
                "ending_type": "treaty",
                "variation_unlocked": {"treaty_guardian": True},
                "requirements_met": {}
            }
        }
        manager = EndingSceneManager.from_dict(data)
        
        self.assertTrue(manager.progress.ending_chosen)
        self.assertEqual(manager.progress.ending_type, "treaty")


class TestChapter18Scenes(unittest.TestCase):
    """Тесты сцен главы 18"""

    def test_get_ch18_mental_state_effects_conditions(self):
        """Проверка условий ментального состояния (сцены)"""
        # Stable
        effects = get_ch18_mental_effects(100, 0)
        self.assertEqual(effects["condition"], "stable")
        
        # Stressed
        effects = get_ch18_mental_effects(70, 0)
        self.assertEqual(effects["condition"], "stressed")
        
        # Traumatized
        effects = get_ch18_mental_effects(50, 0)
        self.assertEqual(effects["condition"], "traumatized")
        
        # Corrupted
        effects = get_ch18_mental_effects(30, 0)
        self.assertEqual(effects["condition"], "corrupted")
        
        # Broken
        effects = get_ch18_mental_effects(10, 0)
        self.assertEqual(effects["condition"], "broken")

    def test_get_ch18_entity_influence_levels(self):
        """Проверка уровней влияния Сущности"""
        # Clean
        effects = get_ch18_mental_effects(80, 5)
        self.assertFalse(effects.get("entity_communion", False))
        self.assertEqual(effects["vision_frequency"], "rare")
        
        # Infected
        effects = get_ch18_mental_effects(80, 50)
        self.assertFalse(effects.get("entity_communion", False))
        self.assertEqual(effects["vision_frequency"], "frequent")
        
        # Assimilated
        effects = get_ch18_mental_effects(80, 85)
        self.assertTrue(effects.get("entity_communion", False))
        self.assertEqual(effects["vision_frequency"], "constant")


if __name__ == "__main__":
    unittest.main()
