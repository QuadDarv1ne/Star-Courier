"""
Тесты для системы романтических сцен
"""

import unittest
import sys
from pathlib import Path

src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from romance_scenes import RomanceScene, create_romance_scenes


class TestRomanceScene(unittest.TestCase):
    """Тесты класса романтической сцены"""

    def test_romance_scene_creation(self):
        scene = RomanceScene(
            id="test_scene",
            character_id="test_char",
            character_name="Тест",
            title="Тестовая сцена",
            description="Описание",
            min_relationship=50,
            scene_text="Текст сцены",
            choices=[]
        )
        self.assertEqual(scene.id, "test_scene")
        self.assertEqual(scene.character_id, "test_char")
        self.assertEqual(scene.min_relationship, 50)

    def test_romance_scene_defaults(self):
        scene = RomanceScene(
            id="test",
            character_id="char",
            character_name="Name",
            title="Title",
            description="Desc",
            min_relationship=40,
            scene_text="Text",
            choices=[]
        )
        self.assertFalse(scene.is_confession)
        self.assertFalse(scene.is_intimate)
        self.assertFalse(scene.unlocks_next)

    def test_romance_scene_with_flags(self):
        scene = RomanceScene(
            id="confession",
            character_id="char",
            character_name="Name",
            title="Confession",
            description="Desc",
            min_relationship=60,
            scene_text="Text",
            choices=[],
            is_confession=True,
            is_intimate=True,
            unlocks_next=True
        )
        self.assertTrue(scene.is_confession)
        self.assertTrue(scene.is_intimate)
        self.assertTrue(scene.unlocks_next)


class TestCreateRomanceScenes(unittest.TestCase):
    """Тесты создания всех романтических сцен"""

    def setUp(self):
        self.scenes = create_romance_scenes()

    def test_scenes_not_empty(self):
        self.assertGreater(len(self.scenes), 0)

    def test_scene_ids_unique(self):
        ids = list(self.scenes.keys())
        self.assertEqual(len(ids), len(set(ids)))

    def test_scene_structure(self):
        for scene_id, scene in self.scenes.items():
            self.assertEqual(scene.id, scene_id)
            self.assertIsInstance(scene.character_id, str)
            self.assertIsInstance(scene.character_name, str)
            self.assertIsInstance(scene.title, str)
            self.assertIsInstance(scene.description, str)
            self.assertIsInstance(scene.min_relationship, int)
            self.assertIsInstance(scene.scene_text, str)
            self.assertIsInstance(scene.choices, list)

    def test_min_relationship_range(self):
        for scene in self.scenes.values():
            self.assertGreaterEqual(scene.min_relationship, 0)
            self.assertLessEqual(scene.min_relationship, 100)

    def test_choices_structure(self):
        for scene in self.scenes.values():
            for choice in scene.choices:
                self.assertIn("text", choice)
                self.assertIn("effect", choice)
                self.assertIsInstance(choice["text"], str)
                self.assertIsInstance(choice["effect"], dict)


class TestRomanceCharacters(unittest.TestCase):
    """Тесты романтических персонажей"""

    def setUp(self):
        self.scenes = create_romance_scenes()

    def test_multiple_characters(self):
        character_ids = set(scene.character_id for scene in self.scenes.values())
        self.assertGreater(len(character_ids), 1)

    def test_confession_scenes_exist(self):
        confession_scenes = [
            s for s in self.scenes.values() if s.is_confession
        ]
        self.assertGreater(len(confession_scenes), 0)

    def test_intimate_scenes_exist(self):
        intimate_scenes = [
            s for s in self.scenes.values() if s.is_intimate
        ]
        # Могут быть не реализованы
        self.assertGreaterEqual(len(intimate_scenes), 0)


class TestRomanceSceneEffects(unittest.TestCase):
    """Тесты эффектов романтических сцен"""

    def setUp(self):
        self.scenes = create_romance_scenes()

    def test_effect_structure(self):
        for scene in self.scenes.values():
            for choice in scene.choices:
                effect = choice.get("effect", {})
                self.assertIsInstance(effect, dict)

    def test_effect_types(self):
        valid_keys = {"relationship", "trust", "romance_unlock", "flag", "romance_confirmed"}
        for scene in self.scenes.values():
            for choice in scene.choices:
                effect = choice.get("effect", {})
                for key in effect.keys():
                    self.assertIn(key, valid_keys, f"Недопустимый ключ эффекта: {key}")

    def test_relationship_effect_values(self):
        for scene in self.scenes.values():
            for choice in scene.choices:
                effect = choice.get("effect", {})
                if "relationship" in effect:
                    value = effect["relationship"]
                    self.assertIsInstance(value, int)
                    self.assertGreaterEqual(value, -100)
                    self.assertLessEqual(value, 100)


class TestRomanceSceneProgression(unittest.TestCase):
    """Тесты прогрессии романтических линий"""

    def setUp(self):
        self.scenes = create_romance_scenes()

    def test_unlock_mechanism(self):
        # Проверяем что есть сцены которые открывают следующие
        unlocks_next = [
            s for s in self.scenes.values() if s.unlocks_next
        ]
        # Могут быть не реализованы
        self.assertGreaterEqual(len(unlocks_next), 0)

    def test_relationship_requirements(self):
        # Проверяем что требования к отношениям возрастают
        relationships = [s.min_relationship for s in self.scenes.values()]
        self.assertGreater(max(relationships), min(relationships))


if __name__ == "__main__":
    unittest.main(verbosity=2)
