"""
Тесты для модулей Star Courier
"""

import unittest
import sys
from pathlib import Path

# Добавляем src в путь
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from config import GAME_TITLE, VERSION, DEFAULT_STATS, DEFAULT_HP, DEFAULT_ENERGY, MAX_RELATIONSHIP
from characters import Character, Role, CrewManager
from abilities import (
    AbilitiesManager, AbilityType, AbilityTier,
    AlchemyAbility, BioticAbility, PsychicAbility, CombatSystem
)
from dialogues import (
    Dialogue, DialogueNode, Choice, ChoiceEffect, DialogueManager
)
from save_system import SaveData, SaveManager, GameState
from items import (
    Item, ItemType, Rarity, Inventory, ItemStack, ItemDatabase, ItemEffect
)
from quests import (
    Quest, QuestType, QuestState, Objective, ObjectiveType, QuestManager, QuestReward
)
from abilities import AbilitiesManager, AbilityType, AbilityTier, CombatSystem


class TestConfig(unittest.TestCase):
    """Тесты конфигурации"""
    
    def test_game_title(self):
        self.assertEqual(GAME_TITLE, "Star Courier")
    
    def test_version(self):
        self.assertIsInstance(VERSION, str)
        self.assertTrue(len(VERSION) > 0)
    
    def test_default_stats(self):
        self.assertIn("alchemy", DEFAULT_STATS)
        self.assertIn("biotics", DEFAULT_STATS)
        self.assertIn("psychic", DEFAULT_STATS)


class TestCharacters(unittest.TestCase):
    """Тесты системы персонажей"""
    
    def test_character_creation(self):
        char = Character(
            id="test_char",
            name="Тестовый Персонаж",
            role=Role.SCIENTIST
        )
        self.assertEqual(char.name, "Тестовый Персонаж")
        self.assertEqual(char.role, Role.SCIENTIST)
        self.assertEqual(char.relationship, 0)
    
    def test_relationship_increase(self):
        char = Character(
            id="test_char",
            name="Тест",
            role=Role.ENGINEER
        )
        new_value = char.change_relationship(10)
        self.assertEqual(new_value, 10)
        self.assertEqual(char.relationship, 10)

    def test_relationship_cap(self):
        char = Character(
            id="test_char",
            name="Тест",
            role=Role.PILOT
        )
        char.change_relationship(150)
        self.assertEqual(char.relationship, 100)
    
    def test_relationship_status(self):
        char = Character(id="test", name="Тест", role=Role.NAVIGATOR)
        
        char.relationship = 0
        self.assertEqual(char.get_relationship_status(), "Холодные")
        
        char.relationship = 50
        self.assertEqual(char.get_relationship_status(), "Профессиональные")
        
        char.relationship = 90
        self.assertEqual(char.get_relationship_status(), "Близкие")
    
    def test_crew_manager(self):
        crew = CrewManager()
        all_crew = crew.get_all_crew()
        
        self.assertGreater(len(all_crew), 0)
        
        max_well = crew.get_character("max_well")
        self.assertIsNotNone(max_well)
        self.assertEqual(max_well.role, Role.CAPTAIN)
        
        athena = crew.get_by_role(Role.AI)
        self.assertEqual(len(athena), 1)


class TestAbilities(unittest.TestCase):
    """Тесты системы способностей"""
    
    def test_abilities_manager_init(self):
        manager = AbilitiesManager()
        
        # Проверяем что способности существуют в словаре
        self.assertIn("healing_potion", manager.abilities)
        self.assertIn("biotic_shield", manager.abilities)
        self.assertIn("mind_read", manager.abilities)
        
        # Проверяем типы способностей
        healing = manager.get_ability("healing_potion")
        self.assertEqual(healing.ability_type, AbilityType.ALCHEMY)
        
        shield = manager.get_ability("biotic_shield")
        self.assertEqual(shield.ability_type, AbilityType.BIOTICS)
        
        mind_read = manager.get_ability("mind_read")
        self.assertEqual(mind_read.ability_type, AbilityType.PSYCHIC)
    
    def test_tier_system(self):
        manager = AbilitiesManager()
        
        self.assertEqual(
            manager.get_tier(AbilityType.ALCHEMY),
            AbilityTier.NONE
        )
        
        manager.set_tier(AbilityType.ALCHEMY, AbilityTier.BASIC)
        self.assertEqual(
            manager.get_tier(AbilityType.ALCHEMY),
            AbilityTier.BASIC
        )
    
    def test_ability_availability(self):
        manager = AbilitiesManager()
        
        healing = manager.get_ability("healing_potion")
        self.assertIsNotNone(healing)
        self.assertTrue(healing.is_available())
        
        # Игрок не может использовать без установленного уровня
        self.assertFalse(manager.can_use_ability(healing))
        
        # Устанавливаем базовый уровень
        manager.set_tier(AbilityType.ALCHEMY, AbilityTier.BASIC)
        self.assertTrue(manager.can_use_ability(healing))
    
    def test_combat_system(self):
        manager = AbilitiesManager()
        manager.set_tier(AbilityType.ALCHEMY, AbilityTier.BASIC)
        
        combat = CombatSystem(manager)
        
        self.assertEqual(combat.player_hp, 100)
        self.assertEqual(combat.player_energy, 100)
        self.assertTrue(combat.is_alive())
        
        # Использование способности
        healing = manager.get_ability("healing_potion")
        result = combat.use_ability(healing)
        
        self.assertTrue(result["success"])
        self.assertEqual(combat.player_energy, 90)  # 100 - 10 (energy_cost)
    
    def test_damage_and_heal(self):
        manager = AbilitiesManager()
        combat = CombatSystem(manager)
        
        combat.take_damage(30)
        self.assertEqual(combat.player_hp, 70)
        
        combat.heal(20)
        self.assertEqual(combat.player_hp, 90)
        
        combat.take_damage(100)
        self.assertFalse(combat.is_alive())


class TestDialogues(unittest.TestCase):
    """Тесты диалоговой системы"""
    
    def test_dialogue_creation(self):
        dialogue = Dialogue(
            id="test_dialogue",
            title="Тестовый диалог",
            start_node="start"
        )
        
        node = DialogueNode(
            id="start",
            speaker="Тест",
            text="Привет!"
        )
        dialogue.add_node(node)
        
        self.assertEqual(dialogue.get_node("start"), node)
    
    def test_choice_system(self):
        choice = Choice(
            id="test_choice",
            text="Выбор",
            next_node="next",
            effect=ChoiceEffect.RELATIONSHIP_UP,
            effect_value=("test_char", 5)
        )
        
        self.assertEqual(choice.id, "test_choice")
        self.assertEqual(choice.effect, ChoiceEffect.RELATIONSHIP_UP)
    
    def test_choice_availability(self):
        # Выбор без требований доступен
        choice = Choice(
            id="free_choice",
            text="Свободный выбор",
            next_node="next"
        )
        self.assertTrue(choice.is_available({}, []))
        
        # Выбор с требованием стата
        choice_with_stat = Choice(
            id="stat_choice",
            text="Требует стат",
            next_node="next",
            required_stat={"biotics": 5}
        )
        self.assertFalse(choice_with_stat.is_available({"biotics": 3}, []))
        self.assertTrue(choice_with_stat.is_available({"biotics": 5}, []))
    
    def test_dialogue_manager(self):
        manager = DialogueManager()
        
        dialogue = Dialogue(
            id="test",
            title="Тест",
            start_node="start"
        )
        dialogue.add_node(DialogueNode(
            id="start",
            speaker="NPC",
            text="Привет!",
            choices=[Choice("continue", "Привет!", "end")]
        ))
        dialogue.add_node(DialogueNode(
            id="end",
            speaker="NPC",
            text="Пока!",
            is_end=True
        ))
        
        manager.add_dialogue(dialogue)
        
        self.assertTrue(manager.start_dialogue("test"))
        self.assertFalse(manager.is_finished())
        
        text = manager.get_current_text()
        self.assertIn("Привет!", text)
        
        choices = manager.get_available_choices()
        self.assertEqual(len(choices), 1)
        
        manager.make_choice("continue")
        self.assertTrue(manager.is_finished())


class TestSaveSystem(unittest.TestCase):
    """Тесты системы сохранений"""
    
    def test_save_data_creation(self):
        save = SaveData()
        
        self.assertEqual(save.chapter, 1)
        self.assertEqual(save.stats["alchemy"], 0)
        self.assertIsInstance(save.inventory, list)
    
    def test_save_data_serialization(self):
        save = SaveData()
        save.chapter = 2
        save.stats["biotics"] = 2
        save.credits = 1000
        save.relationships["alia_naar"] = 50
        
        data = save.to_dict()
        
        self.assertEqual(data["meta"]["chapter"], 2)
        self.assertEqual(data["player"]["stats"]["biotics"], 2)
        self.assertEqual(data["player"]["credits"], 1000)
    
    def test_save_data_deserialization(self):
        data = {
            "meta": {"chapter": 3, "scene": "test_scene"},
            "player": {"stats": {"alchemy": 1}, "credits": 500, "inventory": []},
            "relationships": {"athena": 30},
            "progress": {"flags": {"quest_done": True}, "completed_quests": [], "active_quests": []},
            "history": {"choices": []}
        }
        
        save = SaveData.from_dict(data)
        
        self.assertEqual(save.chapter, 3)
        self.assertEqual(save.scene, "test_scene")
        self.assertEqual(save.stats["alchemy"], 1)
        self.assertEqual(save.credits, 500)
    
    def test_save_manager(self):
        manager = SaveManager("test_saves")
        save = manager.create_new_save()
        save.chapter = 1
        
        result = manager.save_game("test_save.json")
        self.assertTrue(result)
        
        loaded = manager.load_game("test_save.json")
        self.assertIsNotNone(loaded)
        self.assertEqual(loaded.chapter, 1)
        
        # Очистка
        manager.delete_save("test_save.json")
    
    def test_game_state(self):
        state = GameState()
        state.new_game()
        
        self.assertIsNotNone(state.save_data)
        self.assertEqual(state.save_data.chapter, 1)
        
        # Изменение отношений
        state.change_relationship("athena", 10)
        athena = state.crew_manager.get_character("athena")
        self.assertEqual(athena.relationship, 10)

        # Установка флага
        state.set_flag("test_flag", True)
        self.assertTrue(state.get_flag("test_flag"))


class TestItems(unittest.TestCase):
    """Тесты системы предметов"""

    def test_item_creation(self):
        item = Item(
            id="test_item",
            name="Тестовый предмет",
            description="Тест",
            item_type=ItemType.MATERIAL,
            value=100,
            weight=0.5
        )
        self.assertEqual(item.name, "Тестовый предмет")
        self.assertEqual(item.value, 100)
        self.assertEqual(item.weight, 0.5)

    def test_item_validation(self):
        item = Item(
            id="test_item",
            name="Тест",
            description="Тест",
            item_type=ItemType.MATERIAL,
            value=-100,
            weight=-0.5,
            max_stack=0
        )
        self.assertEqual(item.value, 0)
        self.assertEqual(item.weight, 0.0)
        self.assertEqual(item.max_stack, 1)

    def test_inventory_add_remove(self):
        inv = Inventory(max_slots=5)
        db = ItemDatabase()

        item = db.get_item("healing_potion")
        self.assertIsNotNone(item)

        result = inv.add_item(item, 3)
        self.assertTrue(result)
        self.assertTrue(inv.has_item("healing_potion", 3))

        result = inv.remove_item("healing_potion", 2)
        self.assertTrue(result)
        self.assertTrue(inv.has_item("healing_potion", 1))

    def test_inventory_full(self):
        inv = Inventory(max_slots=2)
        db = ItemDatabase()

        item1 = db.get_item("healing_potion")
        item2 = db.get_item("energy_cell")
        item3 = db.get_item("biotic_stim")

        inv.add_item(item1, 99)
        inv.add_item(item2, 99)
        
        result = inv.add_item(item3, 1)
        self.assertFalse(result)

    def test_item_stack(self):
        db = ItemDatabase()
        item = db.get_item("healing_potion")
        stack = ItemStack(item, 50)

        self.assertFalse(stack.is_full())
        self.assertEqual(stack.quantity, 50)

        remaining = stack.add(49)
        self.assertEqual(remaining, 0)
        self.assertTrue(stack.is_full())

        remaining = stack.add(10)
        self.assertEqual(remaining, 10)

        removed = stack.remove(30)
        self.assertEqual(removed, 30)
        self.assertEqual(stack.quantity, 69)


class TestQuests(unittest.TestCase):
    """Тесты системы квестов"""

    def test_quest_creation(self):
        quest = Quest(
            id="test_quest",
            title="Тестовый квест",
            description="Тест",
            quest_type=QuestType.SIDE
        )
        self.assertEqual(quest.title, "Тестовый квест")
        self.assertEqual(quest.state, QuestState.AVAILABLE)

    def test_quest_objectives(self):
        quest = Quest(
            id="test_quest",
            title="Тест",
            description="Тест",
            quest_type=QuestType.MAIN
        )
        quest.add_objective(Objective(
            id="obj1",
            type=ObjectiveType.KILL,
            description="Убить врага",
            required=5
        ))

        quest.update_objective("obj1", 3)
        self.assertEqual(quest.objectives[0].current, 3)
        self.assertFalse(quest.objectives[0].is_completed)

        quest.update_objective("obj1", 2)
        self.assertTrue(quest.objectives[0].is_completed)

    def test_quest_availability(self):
        quest = Quest(
            id="test_quest",
            title="Тест",
            description="Тест",
            quest_type=QuestType.SIDE,
            prerequisites=["prereq_quest"]
        )

        self.assertFalse(quest.is_available([], 0))
        self.assertTrue(quest.is_available(["prereq_quest"], 0))

    def test_quest_manager(self):
        manager = QuestManager()

        quests = manager.get_active_quests()
        self.assertGreater(len(quests), 0)

        quest = manager.get_quest("main_001")
        self.assertIsNotNone(quest)
        self.assertEqual(quest.quest_type, QuestType.MAIN)

    def test_quest_accept_complete(self):
        manager = QuestManager()
        initial_count = len(manager.get_active_quests())

        side_quest = Quest(
            id="side_test",
            title="Тест",
            description="Тест",
            quest_type=QuestType.SIDE
        )
        side_quest.add_objective(Objective(
            id="obj",
            type=ObjectiveType.COLLECT,
            description="Собрать",
            required=1
        ))
        manager.add_quest(side_quest)

        result = manager.accept_quest("side_test")
        self.assertTrue(result)
        self.assertEqual(len(manager.get_active_quests()), initial_count + 1)

        manager.update_objective("side_test", "obj", 1)
        reward = manager.complete_quest("side_test")
        self.assertIsNotNone(reward)
        self.assertTrue(manager.has_completed("side_test"))

    def test_quest_duplicate_prevention(self):
        manager = QuestManager()
        quest = Quest(
            id="duplicate_test",
            title="Тест",
            description="Тест",
            quest_type=QuestType.SIDE
        )

        result1 = manager.add_quest(quest)
        result2 = manager.add_quest(quest)

        self.assertTrue(result1)
        self.assertFalse(result2)


class TestConfig(unittest.TestCase):
    """Дополнительные тесты конфигурации"""

    def test_default_hp(self):
        self.assertEqual(DEFAULT_HP, 100)

    def test_default_energy(self):
        self.assertEqual(DEFAULT_ENERGY, 100)

    def test_max_relationship(self):
        self.assertEqual(MAX_RELATIONSHIP, 100)


class TestDialogueLogging(unittest.TestCase):
    """Тесты логгирования диалогов"""

    def test_dialogue_not_found(self):
        manager = DialogueManager()
        result = manager.start_dialogue("nonexistent")
        self.assertFalse(result)

    def test_choice_without_dialogue(self):
        manager = DialogueManager()
        result = manager.make_choice("any")
        self.assertIsNone(result)


class TestAbilitiesLogging(unittest.TestCase):
    """Тесты логгирования способностей"""

    def test_use_unavailable_ability(self):
        manager = AbilitiesManager()
        combat = CombatSystem(manager)

        healing = manager.get_ability("healing_potion")
        result = combat.use_ability(healing)

        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Способность недоступна")

    def test_not_enough_energy(self):
        manager = AbilitiesManager()
        manager.set_tier(AbilityType.ALCHEMY, AbilityTier.BASIC)
        combat = CombatSystem(manager)
        combat.player_energy = 5

        healing = manager.get_ability("healing_potion")
        result = combat.use_ability(healing)

        self.assertFalse(result["success"])
        self.assertEqual(result["message"], "Недостаточно энергии")


if __name__ == "__main__":
    unittest.main(verbosity=2)
