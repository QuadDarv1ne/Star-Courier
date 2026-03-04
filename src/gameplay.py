"""
Модуль интеграции систем: боевая, квесты, предметы
Интегрирует Abilities, Items, Quests в основной геймплей
"""

import logging
from typing import Optional, Dict, List

from .abilities import AbilitiesManager, CombatSystem
from .items import ItemDatabase, Inventory, Consumable
from .quests import QuestManager, ObjectiveType
from .characters import CrewManager
from .config import DEFAULT_HP, DEFAULT_ENERGY, MAX_INVENTORY_SLOTS

logger = logging.getLogger('gameplay')


class GameplaySystem:
    """
    Основная система интеграции всех игровых механик.
    Объединяет способности, предметы, квесты и команду.
    """

    def __init__(self):
        self.abilities_manager = AbilitiesManager()
        self.combat_system: Optional[CombatSystem] = None
        self.item_database = ItemDatabase()
        self.inventory = Inventory(max_slots=MAX_INVENTORY_SLOTS)
        self.quest_manager = QuestManager()
        self.crew_manager: Optional[CrewManager] = None

        # Инициализация стартовых предметов
        self._init_starting_items()

    def _init_starting_items(self):
        """Выдать стартовые предметы"""
        # Стартовые расходники
        starter_items = [
            ("healing_potion", 3),
            ("energy_cell", 2),
        ]

        for item_id, quantity in starter_items:
            item = self.item_database.get_item(item_id)
            if item:
                self.inventory.add_item(item, quantity)

    def set_crew_manager(self, crew_manager: CrewManager):
        """Установить менеджера команды"""
        self.crew_manager = crew_manager

    def set_game_state(self, game_state):
        """
        Установить связь с GameState.
        Нужно для синхронизации HP/Energy с CombatSystem.
        """
        self.game_state = game_state

    # ==================== БОЕВАЯ СИСТЕМА ====================

    def start_combat(self, enemy_name: str = "Враг"):
        """Начать бой"""
        self.combat_system = CombatSystem(self.abilities_manager)
        self.combat_system.enemy_name = enemy_name
        logger.info(f"Начат бой с {enemy_name}")
        return True

    def end_combat(self, victory: bool = True):
        """Завершить бой"""
        if not self.combat_system:
            return

        if victory:
            logger.info("Бой окончен победой")
        else:
            logger.info("Бой окончен поражением")

        # Синхронизация с game_state
        if hasattr(self, 'game_state') and self.game_state:
            self.game_state.save_data.hp = self.combat_system.player_hp
            self.game_state.save_data.energy = self.combat_system.player_energy

        self.combat_system = None

    def is_in_combat(self) -> bool:
        """Проверить, идёт ли бой"""
        return self.combat_system is not None

    def use_ability_in_combat(self, ability_id: str) -> dict:
        """Использовать способность в бою"""
        if not self.combat_system:
            return {"success": False, "message": "Не в бою"}

        ability = self.abilities_manager.get_ability(ability_id)
        if not ability:
            return {"success": False, "message": "Способность не найдена"}

        result = self.combat_system.use_ability(ability)

        # Обработка эффектов
        if result["success"]:
            if "healing" in ability.name.lower():
                heal_amount = 25  # Из эффекта способности
                self.combat_system.heal(heal_amount)
                result["healed"] = heal_amount

        return result

    def take_damage(self, amount: int) -> bool:
        """Получить урон в бою"""
        if not self.combat_system:
            return True
        return self.combat_system.take_damage(amount)

    def get_combat_status(self) -> Optional[Dict]:
        """Получить статус боя"""
        if not self.combat_system:
            return None

        return {
            "hp": self.combat_system.player_hp,
            "max_hp": self.combat_system.player_max_hp,
            "energy": self.combat_system.player_energy,
            "max_energy": self.combat_system.player_max_energy,
            "turn": self.combat_system.turn,
            "enemy": getattr(self.combat_system, 'enemy_name', 'Враг'),
            "alive": self.combat_system.is_alive(),
        }

    # ==================== СИСТЕМА ПРЕДМЕТОВ ====================

    def get_inventory_summary(self) -> Dict:
        """Получить сводку инвентаря"""
        items = self.inventory.get_all_items()
        return {
            "total_items": sum(stack.quantity for stack in items),
            "free_slots": self.inventory.get_free_slots(),
            "total_weight": self.inventory.get_total_weight(),
            "credits": self.inventory.credits,
        }

    def use_item(self, item_id: str) -> dict:
        """
        Использовать предмет.
        Возвращает результат использования.
        """
        if not self.inventory.has_item(item_id):
            return {"success": False, "message": "Предмет не найден"}

        item = self.inventory.get_item(item_id)
        if not item:
            return {"success": False, "message": "Предмет не найден"}

        # Проверка типа предмета
        if not item.is_consumable and not isinstance(item, Consumable):
            return {"success": False, "message": "Нельзя использовать"}

        result = {"success": True, "item_name": item.name, "effects": []}

        # Применение эффектов
        if isinstance(item, Consumable):
            if item.heal_amount > 0:
                if self.combat_system:
                    self.combat_system.heal(item.heal_amount)
                result["effects"].append(f"Восстановлено {item.heal_amount} HP")

            if item.energy_amount > 0:
                if self.combat_system:
                    self.combat_system.restore_energy(item.energy_amount)
                result["effects"].append(f"Восстановлено {item.energy_amount} энергии")

        # Удаляем предмет из инвентаря
        self.inventory.remove_item(item_id, 1)

        logger.info(f"Использован предмет: {item.name}")
        return result

    def add_item(self, item_id: str, quantity: int = 1) -> bool:
        """Добавить предмет в инвентарь"""
        item = self.item_database.get_item(item_id)
        if not item:
            logger.warning(f"Предмет не найден: {item_id}")
            return False

        return self.inventory.add_item(item, quantity)

    def remove_item(self, item_id: str, quantity: int = 1) -> bool:
        """Удалить предмет из инвентаря"""
        return self.inventory.remove_item(item_id, quantity)

    def has_item(self, item_id: str, quantity: int = 1) -> bool:
        """Проверить наличие предмета"""
        return self.inventory.has_item(item_id, quantity)

    def get_item_display_list(self) -> List[Dict]:
        """Получить список предметов для отображения"""
        items = []
        for stack in self.inventory.get_all_items():
            items.append({
                "id": stack.item.id,
                "name": stack.item.name,
                "icon": stack.item.icon,
                "quantity": stack.quantity,
                "description": stack.item.description,
                "type": stack.item.item_type.value,
            })
        return items

    # ==================== СИСТЕМА КВЕСТОВ ====================

    def get_active_quests_display(self) -> List[Dict]:
        """Получить активные квесты для отображения"""
        quests = []
        for quest in self.quest_manager.get_active_quests():
            completed, total = quest.get_progress()
            quests.append({
                "id": quest.id,
                "title": quest.title,
                "type": quest.quest_type.value,
                "description": quest.description,
                "progress": f"{completed}/{total}",
                "journal": quest.journal_entry,
            })
        return quests

    def get_available_quests_display(self) -> List[Dict]:
        """Получить доступные квесты для принятия"""
        quests = []
        for quest in self.quest_manager.get_available_quests():
            quests.append({
                "id": quest.id,
                "title": quest.title,
                "type": quest.quest_type.value,
                "description": quest.description,
                "giver": quest.giver,
            })
        return quests

    def accept_quest(self, quest_id: str) -> bool:
        """Принять квест"""
        return self.quest_manager.accept_quest(quest_id)

    def complete_quest(self, quest_id: str) -> Optional[Dict]:
        """
        Завершить квест.
        Возвращает награду.
        """
        reward = self.quest_manager.complete_quest(quest_id)
        if not reward:
            return None

        result = {
            "credits": reward.credits,
            "experience": reward.experience,
            "items": [],
            "relationship_changes": reward.relationship_changes,
        }

        # Выдача наград
        if reward.credits > 0:
            self.inventory.credits += reward.credits

        if reward.items:
            for item_dict in reward.items:
                for item_id, quantity in item_dict.items():
                    if self.add_item(item_id, quantity):
                        result["items"].append(f"{quantity} x {item_id}")

        # Изменения отношений
        if self.crew_manager and reward.relationship_changes:
            for char_id, amount in reward.relationship_changes.items():
                self.crew_manager.get_character(char_id).change_relationship(amount)

        logger.info(f"Квест {quest_id} завершён, награда: {reward.credits} кредитов")
        return result

    def update_quest_objective(self, quest_id: str, objective_id: str, amount: int = 1):
        """Обновить цель квеста"""
        self.quest_manager.update_objective(quest_id, objective_id, amount)

    def check_quest_completion(self, quest_id: str) -> bool:
        """Проверить, можно ли завершить квест"""
        quest = self.quest_manager.get_quest(quest_id)
        if not quest:
            return False
        return quest.can_complete()

    def get_quest_by_objective(self, objective_type: ObjectiveType,
                                target_id: str = "") -> Optional[str]:
        """
        Найти активный квест по типу цели.
        Возвращает ID квеста или None.
        """
        for quest in self.quest_manager.get_active_quests():
            for obj in quest.objectives:
                if obj.type == objective_type and not obj.is_completed:
                    if not target_id or obj.target_id == target_id:
                        return quest.id
        return None

    # ==================== ИНТЕГРАЦИЯ С СОБЫТИЯМИ ====================

    def on_explore_location(self, location_id: str):
        """Событие: исследование локации"""
        # Обновляем цели квестов
        for quest in self.quest_manager.get_active_quests():
            for obj in quest.objectives:
                if obj.type == ObjectiveType.EXPLORE and obj.target_id == location_id:
                    quest.update_objective(obj.id, 1)

    def on_item_collected(self, item_id: str, quantity: int = 1):
        """Событие: предмет подобран"""
        self.add_item(item_id, quantity)

        # Обновляем цели квестов
        for quest in self.quest_manager.get_active_quests():
            for obj in quest.objectives:
                if obj.type == ObjectiveType.COLLECT and obj.target_id == item_id:
                    quest.update_objective(obj.id, quantity)

    def on_enemy_defeated(self, enemy_id: str):
        """Событие: враг побеждён"""
        # Обновляем цели квестов
        for quest in self.quest_manager.get_active_quests():
            for obj in quest.objectives:
                if obj.type == ObjectiveType.KILL:
                    if not obj.target_id or obj.target_id == enemy_id:
                        quest.update_objective(obj.id, 1)

    def on_dialogue_choice(self, choice_id: str, npc_id: str = ""):
        """Событие: выбор в диалоге"""
        # Обновляем цели квестов
        for quest in self.quest_manager.get_active_quests():
            for obj in quest.objectives:
                if obj.type == ObjectiveType.MAKE_CHOICE:
                    quest.update_objective(obj.id, 1)

    def on_npc_talked(self, npc_id: str):
        """Событие: разговор с NPC"""
        # Обновляем цели квестов
        for quest in self.quest_manager.get_active_quests():
            for obj in quest.objectives:
                if obj.type == ObjectiveType.TALK and obj.target_id == npc_id:
                    quest.update_objective(obj.id, 1)

    # ==================== ОТОБРАЖЕНИЕ ====================

    def print_status(self, print_func):
        """Вывести статус системы"""
        print_func("\n  [СТАТУС ИГРОКА]")
        print_func("  " + "-" * 40)

        # HP и Energy
        if self.combat_system:
            hp = self.combat_system.player_hp
            max_hp = self.combat_system.player_max_hp
            energy = self.combat_system.player_energy
            max_energy = self.combat_system.player_max_energy
        else:
            # Берём из game_state если есть
            if hasattr(self, 'game_state') and self.game_state.save_data:
                hp = self.game_state.save_data.hp
                max_hp = DEFAULT_HP
                energy = self.game_state.save_data.energy
                max_energy = DEFAULT_ENERGY
            else:
                hp, max_hp = DEFAULT_HP, DEFAULT_HP
                energy, max_energy = DEFAULT_ENERGY, DEFAULT_ENERGY

        print_func(f"  ❤️  Здоровье: {hp}/{max_hp}")
        print_func(f"  ⚡ Энергия:   {energy}/{max_energy}")
        print_func(f"  💰 Кредиты:  {self.inventory.credits}")

        # Квесты
        active_quests = self.quest_manager.get_active_quests()
        if active_quests:
            print_func("\n  [АКТИВНЫЕ КВЕСТЫ]")
            print_func("  " + "-" * 40)
            for quest in active_quests[:3]:  # Показываем до 3 квестов
                completed, total = quest.get_progress()
                type_icon = {"main": "📖", "side": "📜", "combat": "⚔️"}.get(
                    quest.quest_type.value, "📋"
                )
                print_func(f"  {type_icon} {quest.title} [{completed}/{total}]")

        # Предметы
        items = self.inventory.get_all_items()
        if items:
            print_func("\n  [ПРЕДМЕТЫ]")
            print_func("  " + "-" * 40)
            for stack in items[:5]:  # Показываем до 5 предметов
                icon = stack.item.icon if hasattr(stack.item, 'icon') else "📦"
                qty_text = f" x{stack.quantity}" if stack.quantity > 1 else ""
                print_func(f"  {icon} {stack.item.name}{qty_text}")

            if len(items) > 5:
                print_func(f"  ... и ещё {len(items) - 5} предметов")

        print_func()

    def to_dict(self) -> dict:
        """Сериализация для сохранения"""
        combat_data = None
        if self.combat_system:
            combat_data = {
                "hp": self.combat_system.player_hp,
                "energy": self.combat_system.player_energy,
            }

        return {
            "inventory": self.inventory.to_dict(),
            "quests": self.quest_manager.to_dict(),
            "combat": combat_data,
        }

    @classmethod
    def from_dict(cls, data: dict, crew_manager: CrewManager) -> "GameplaySystem":
        """Десериализация"""
        system = cls()
        system.crew_manager = crew_manager

        # Загружаем инвентарь
        if "inventory" in data:
            system.inventory = Inventory.from_dict(data["inventory"])

        # Загружаем квесты
        if "quests" in data:
            system.quest_manager = QuestManager.from_dict(data["quests"])

        return system
