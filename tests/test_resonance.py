"""
Тесты для системы Resonance
"""

import unittest
import sys
from pathlib import Path

src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from resonance import ResonanceSystem, ResonanceLevel


class TestResonanceLevels(unittest.TestCase):
    """Тесты уровней Резонанса"""

    def test_initial_level(self):
        """Начальный уровень - Basic"""
        system = ResonanceSystem()
        self.assertEqual(system.get_level(), ResonanceLevel.BASIC)
        self.assertEqual(system.get_level_number(), 1)

    def test_level_up_to_mastery(self):
        """Повышение до Mastery (глава 14)"""
        system = ResonanceSystem()
        system.check_level_up(psychic_level=50, completed_chapters=[6, 10, 14])
        self.assertEqual(system.get_level(), ResonanceLevel.MASTERY)
        self.assertEqual(system.get_level_number(), 3)

    def test_level_up_to_transcendent(self):
        """Повышение до Transcendent (psychic 90+)"""
        system = ResonanceSystem()
        system.check_level_up(psychic_level=90, completed_chapters=[6, 10, 14, 18])
        self.assertEqual(system.get_level(), ResonanceLevel.TRANSCENDENT)
        self.assertEqual(system.get_level_number(), 4)

    def test_cannot_level_up_without_chapters(self):
        """Невозможно повысить уровень без глав"""
        system = ResonanceSystem()
        system.check_level_up(psychic_level=50, completed_chapters=[])
        self.assertEqual(system.get_level(), ResonanceLevel.BASIC)


class TestResonanceAbilities(unittest.TestCase):
    """Тесты способностей Резонанса"""

    def test_basic_abilities_unlocked(self):
        """Базовые способности разблокированы"""
        system = ResonanceSystem()
        # Проверяем что способности есть в системе
        self.assertIn("resonance_basics", system.abilities)
        ability = system.abilities["resonance_basics"]
        self.assertIn("anomaly_detection_range", ability.effects)
        self.assertTrue(ability.effects.get("entity_presence_warning", False))

    def test_mastery_abilities(self):
        """Способности Mastery"""
        system = ResonanceSystem()
        system.check_level_up(psychic_level=70, completed_chapters=[6, 10, 14])
        self.assertIn("resonance_mastery", system.abilities)
        ability = system.abilities["resonance_mastery"]
        self.assertTrue(ability.effects.get("anomaly_navigation", False))
        self.assertTrue(ability.effects.get("entity_communication", False))

    def test_transcendent_abilities(self):
        """Способности Transcendent"""
        system = ResonanceSystem()
        system.check_level_up(psychic_level=90, completed_chapters=[6, 10, 14, 18])
        self.assertIn("resonance_transcendent", system.abilities)
        ability = system.abilities["resonance_transcendent"]
        self.assertTrue(ability.effects.get("anomaly_immunity", False))
        self.assertTrue(ability.effects.get("entity_bond", False))
        self.assertEqual(ability.effects.get("psychic_amplification"), 50)


class TestResonanceExperience(unittest.TestCase):
    """Тесты опыта Резонанса"""

    def test_add_experience(self):
        """Добавление опыта"""
        system = ResonanceSystem()
        initial_exp = system.experience
        system.add_experience(100)
        self.assertEqual(system.experience, initial_exp + 100)

    def test_experience_accumulation(self):
        """Накопление опыта"""
        system = ResonanceSystem()
        system.add_experience(50)
        system.add_experience(75)
        self.assertEqual(system.experience, 125)


if __name__ == "__main__":
    unittest.main()
