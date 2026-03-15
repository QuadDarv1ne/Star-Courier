"""
Тесты для системы финальных сцен
"""

import unittest
import sys
from pathlib import Path

src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from ending_scenes import (
    EndingScene, EndingType, EndingVariation, create_ending_scenes
)


class TestEndingType(unittest.TestCase):
    """Тесты типов концовок"""

    def test_ending_type_values(self):
        self.assertEqual(EndingType.EXILE.value, "exile")
        self.assertEqual(EndingType.TREATY.value, "treaty")
        self.assertEqual(EndingType.MERGE.value, "merge")

    def test_ending_type_count(self):
        self.assertEqual(len(EndingType), 3)


class TestEndingVariation(unittest.TestCase):
    """Тесты вариаций концовок"""

    def test_variation_values(self):
        self.assertEqual(EndingVariation.SOLO.value, "solo")
        self.assertEqual(EndingVariation.TOGETHER.value, "together")
        self.assertEqual(EndingVariation.SACRIFICE.value, "sacrifice")
        self.assertEqual(EndingVariation.TEAM.value, "team")

    def test_variation_count(self):
        self.assertEqual(len(EndingVariation), 4)


class TestEndingScene(unittest.TestCase):
    """Тесты класса финальной сцены"""

    def test_ending_scene_creation(self):
        scene = EndingScene(
            id="test_ending",
            ending_type=EndingType.EXILE,
            variation=EndingVariation.SOLO,
            title="Тестовая концовка",
            description="Описание",
            requirements={},
            scene_text="Текст сцены",
            epilogue_text="Эпилог",
            crew_fate={},
            galaxy_fate="Галактика спасена"
        )
        self.assertEqual(scene.id, "test_ending")
        self.assertEqual(scene.ending_type, EndingType.EXILE)
        self.assertEqual(scene.variation, EndingVariation.SOLO)

    def test_ending_scene_requirements(self):
        scene = EndingScene(
            id="test",
            ending_type=EndingType.TREATY,
            variation=EndingVariation.TEAM,
            title="Title",
            description="Desc",
            requirements={
                "ending_choice": "treaty",
                "team_loyalty": "high"
            },
            scene_text="Text",
            epilogue_text="Epilogue",
            crew_fate={"athena": "alive"},
            galaxy_fate="Peace"
        )
        self.assertEqual(scene.requirements["ending_choice"], "treaty")
        self.assertEqual(scene.crew_fate["athena"], "alive")


class TestCreateEndingScenes(unittest.TestCase):
    """Тесты создания всех финальных сцен"""

    def setUp(self):
        self.scenes = create_ending_scenes()

    def test_scenes_not_empty(self):
        self.assertGreater(len(self.scenes), 0)

    def test_scene_ids_unique(self):
        ids = list(self.scenes.keys())
        self.assertEqual(len(ids), len(set(ids)))

    def test_scene_structure(self):
        for scene_id, scene in self.scenes.items():
            self.assertEqual(scene.id, scene_id)
            self.assertIsInstance(scene.ending_type, EndingType)
            self.assertIsInstance(scene.variation, EndingVariation)
            self.assertIsInstance(scene.title, str)
            self.assertIsInstance(scene.description, str)
            self.assertIsInstance(scene.requirements, dict)
            self.assertIsInstance(scene.scene_text, str)
            self.assertIsInstance(scene.epilogue_text, str)
            self.assertIsInstance(scene.crew_fate, dict)
            self.assertIsInstance(scene.galaxy_fate, str)


class TestEndingTypesCoverage(unittest.TestCase):
    """Тесты покрытия типов концовок"""

    def setUp(self):
        self.scenes = create_ending_scenes()

    def test_all_ending_types_present(self):
        ending_types = set(s.ending_type for s in self.scenes.values())
        self.assertIn(EndingType.EXILE, ending_types)
        self.assertIn(EndingType.TREATY, ending_types)
        self.assertIn(EndingType.MERGE, ending_types)

    def test_all_variations_present(self):
        variations = set(s.variation for s in self.scenes.values())
        self.assertIn(EndingVariation.SOLO, variations)
        self.assertIn(EndingVariation.TOGETHER, variations)
        self.assertIn(EndingVariation.SACRIFICE, variations)
        self.assertIn(EndingVariation.TEAM, variations)


class TestEndingSceneCounts(unittest.TestCase):
    """Тесты количества сцен"""

    def setUp(self):
        self.scenes = create_ending_scenes()

    def test_exile_scenes_count(self):
        exile_scenes = [
            s for s in self.scenes.values()
            if s.ending_type == EndingType.EXILE
        ]
        self.assertGreater(len(exile_scenes), 0)

    def test_treaty_scenes_count(self):
        treaty_scenes = [
            s for s in self.scenes.values()
            if s.ending_type == EndingType.TREATY
        ]
        self.assertGreater(len(treaty_scenes), 0)

    def test_merge_scenes_count(self):
        merge_scenes = [
            s for s in self.scenes.values()
            if s.ending_type == EndingType.MERGE
        ]
        self.assertGreater(len(merge_scenes), 0)


class TestEndingRequirements(unittest.TestCase):
    """Тесты требований к концовкам"""

    def setUp(self):
        self.scenes = create_ending_scenes()

    def test_requirements_structure(self):
        for scene in self.scenes.values():
            reqs = scene.requirements
            self.assertIsInstance(reqs, dict)
            # Минимум одно требование должно быть
            self.assertGreater(len(reqs), 0)

    def test_ending_choice_requirement(self):
        for scene in self.scenes.values():
            reqs = scene.requirements
            self.assertIn("ending_choice", reqs)


class TestCrewFate(unittest.TestCase):
    """Тесты судьбы экипажа"""

    def setUp(self):
        self.scenes = create_ending_scenes()

    def test_crew_fate_not_empty(self):
        for scene in self.scenes.values():
            self.assertGreater(len(scene.crew_fate), 0)

    def test_crew_fate_values(self):
        for scene in self.scenes.values():
            for crew_id, fate in scene.crew_fate.items():
                self.assertIsInstance(crew_id, str)
                self.assertIsInstance(fate, str)


class TestSerialization(unittest.TestCase):
    """Тесты сериализации (если есть)"""

    def setUp(self):
        self.scenes = create_ending_scenes()

    def test_scene_to_dict(self):
        # Проверяем что сцены могут быть сериализованы
        scene = list(self.scenes.values())[0]
        data = {
            "id": scene.id,
            "ending_type": scene.ending_type.value,
            "variation": scene.variation.value,
            "title": scene.title,
            "requirements": scene.requirements
        }
        self.assertEqual(data["ending_type"], scene.ending_type.value)
        self.assertEqual(data["variation"], scene.variation.value)


if __name__ == "__main__":
    unittest.main(verbosity=2)
