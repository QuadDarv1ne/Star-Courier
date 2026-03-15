"""
Система сохранений и загрузок игры
"""

import json
import logging
import os
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, Optional, List
from pathlib import Path

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('game.log', encoding='utf-8', mode='a'),
    ]
)
logger = logging.getLogger('save_system')

try:
    from .config import SAVE_DIR, DEFAULT_SAVE, GAME_TITLE, VERSION, MAX_INVENTORY_SLOTS
    from .characters import CrewManager, Character, Role
    from .abilities import AbilitiesManager, AbilityType, AbilityTier
    from .items import Inventory, ItemDatabase
    from .quests import QuestManager
    from .resonance import ResonanceSystem, ResonanceLevel
    from .path_system import PathSystem, PathType
    from .ending_system import EndingSystem, EndingType, RomanceEndingSystem
    from .mental_state import MentalStateSystem
    from .romance_scenes import RomanceSceneManager
    from .ending_scenes import EndingSceneManager
except ImportError:
    from config import SAVE_DIR, DEFAULT_SAVE, GAME_TITLE, VERSION, MAX_INVENTORY_SLOTS
    from characters import CrewManager, Character, Role
    from abilities import AbilitiesManager, AbilityType, AbilityTier
    from items import Inventory, ItemDatabase
    from quests import QuestManager
    from resonance import ResonanceSystem, ResonanceLevel
    from path_system import PathSystem, PathType
    from ending_system import EndingSystem, EndingType, RomanceEndingSystem
    from mental_state import MentalStateSystem
    from romance_scenes import RomanceSceneManager
    from ending_scenes import EndingSceneManager


@dataclass
class SaveData:
    """Данные сохранения"""
    timestamp: str = ""
    game_version: str = VERSION
    chapter: int = 1
    scene: str = "start"
    stats: Dict[str, int] = field(default_factory=lambda: {"alchemy": 0, "biotics": 0, "psychic": 0})
    credits: int = 0
    inventory: list = field(default_factory=list)
    relationships: Dict[str, int] = field(default_factory=dict)
    trust_values: Dict[str, int] = field(default_factory=dict)
    flags: Dict[str, bool] = field(default_factory=dict)
    completed_quests: list = field(default_factory=list)
    active_quests: list = field(default_factory=list)
    choices_history: list = field(default_factory=list)
    quest_data: Dict[str, Any] = field(default_factory=dict)

    # Новые механики
    resonance: Dict[str, Any] = field(default_factory=dict)  # Система Резонанса
    path: Dict[str, Any] = field(default_factory=dict)  # Система Путей
    endings: Dict[str, Any] = field(default_factory=dict)  # Система Финалов
    romance: Dict[str, Any] = field(default_factory=dict)  # Романтические сцены
    mental_state: Dict[str, Any] = field(default_factory=dict)  # Ментальное состояние

    def to_dict(self) -> Dict[str, Any]:
        """Сериализовать в словарь"""
        return {
            "meta": {"timestamp": self.timestamp, "game_version": self.game_version,
                     "chapter": self.chapter, "scene": self.scene},
            "player": {"stats": self.stats, "credits": self.credits, "inventory": self.inventory},
            "relationships": self.relationships,
            "trust": self.trust_values,
            "progress": {"flags": self.flags, "completed_quests": self.completed_quests,
                         "active_quests": self.active_quests, "quest_data": self.quest_data},
            "history": {"choices": self.choices_history},
            # Новые механики
            "resonance": self.resonance,
            "path": self.path,
            "endings": self.endings,
            "romance": self.romance,
            "mental_state": self.mental_state,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SaveData":
        """Десериализовать из словаря"""
        save = cls()
        meta = data.get("meta", {})
        player = data.get("player", {})
        progress = data.get("progress", {})
        history = data.get("history", {})

        save.timestamp = meta.get("timestamp", "")
        save.game_version = meta.get("game_version", VERSION)
        save.chapter = meta.get("chapter", 1)
        save.scene = meta.get("scene", "start")
        save.stats = player.get("stats", save.stats)
        save.credits = player.get("credits", 0)
        save.inventory = player.get("inventory", [])
        save.relationships = data.get("relationships", {})
        save.trust_values = data.get("trust", {})
        save.flags = progress.get("flags", {})
        save.completed_quests = progress.get("completed_quests", [])
        save.active_quests = progress.get("active_quests", [])
        save.quest_data = progress.get("quest_data", {})
        save.choices_history = history.get("choices", [])

        # Новые механики
        save.resonance = data.get("resonance", {})
        save.path = data.get("path", {})
        save.endings = data.get("endings", {})
        save.romance = data.get("romance", {})
        save.mental_state = data.get("mental_state", {})

        return save


class SaveManager:
    """Менеджер сохранений"""
    
    def __init__(self, save_dir: str = SAVE_DIR):
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)
        self.current_save: Optional[SaveData] = None
    
    def create_new_save(self) -> SaveData:
        """Создать новое сохранение"""
        save = SaveData()
        save.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.current_save = save
        return save
    
    def save_game(self, filename: str = None) -> bool:
        """Сохранить игру"""
        if not self.current_save:
            logger.warning("Попытка сохранения без активного сохранения")
            return False

        if not filename:
            filename = DEFAULT_SAVE

        filepath = self.save_dir / filename
        if not filepath.suffix:
            filepath = filepath.with_suffix(".json")

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(self.current_save.to_dict(), f,
                         ensure_ascii=False, indent=2)
            logger.info(f"Игра сохранена в {filepath}")
            return True
        except Exception as e:
            logger.error(f"Ошибка сохранения: {e}")
            return False
    
    def load_game(self, filename: str = None) -> Optional[SaveData]:
        """Загрузить игру"""
        if not filename:
            filename = DEFAULT_SAVE

        filepath = self.save_dir / filename
        if not filepath.exists():
            filepath = filepath.with_suffix(".json")

        if not filepath.exists():
            logger.warning(f"Файл сохранения не найден: {filepath}")
            return None

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.current_save = SaveData.from_dict(data)
            logger.info(f"Игра загружена из {filepath}")
            return self.current_save
        except Exception as e:
            logger.error(f"Ошибка загрузки: {e}")
            return None
    
    def list_saves(self) -> list:
        """Получить список сохранений"""
        saves = []
        for file in self.save_dir.glob("*.json"):
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)

                meta = data.get("meta", {})
                saves.append({
                    "filename": file.name,
                    "timestamp": meta.get("timestamp", "Неизвестно"),
                    "chapter": meta.get("chapter", 1),
                    "scene": meta.get("scene", "Неизвестно"),
                })
            except (json.JSONDecodeError, IOError, KeyError) as e:
                logger.warning(f"Ошибка чтения сохранения {file}: {e}")
                saves.append({
                    "filename": file.name,
                    "timestamp": "Ошибка чтения",
                    "chapter": "?",
                    "scene": "?",
                })

        return sorted(saves, key=lambda x: x["timestamp"], reverse=True)
    
    def delete_save(self, filename: str) -> bool:
        """Удалить сохранение"""
        filepath = self.save_dir / filename
        if filepath.exists():
            filepath.unlink()
            return True
        return False
    
    def autosave(self) -> bool:
        """Автосохранение"""
        return self.save_game("autosave.json")


class GameState:
    """Состояние игры — объединяет все системы"""

    def __init__(self, max_inventory_slots: int = 20):
        self.save_manager = SaveManager()
        self.crew_manager = CrewManager()
        self.abilities_manager = AbilitiesManager()
        self.inventory = Inventory(max_slots=max_inventory_slots)
        self.item_db = ItemDatabase()
        self.quest_manager = QuestManager()
        self.save_data: Optional[SaveData] = None

        # Новые системы
        self.resonance_system = ResonanceSystem()
        self.path_system = PathSystem()
        self.ending_system = EndingSystem()
        self.romance_ending_system = RomanceEndingSystem()
        self.mental_state_system = MentalStateSystem()
        self.romance_manager = RomanceSceneManager()
        self.ending_manager = EndingSceneManager()

    def new_game(self):
        """Новая игра"""
        self.save_data = self.save_manager.create_new_save()
        self._sync_from_save()
        logger.info("Новая игра создана")
    
    def load_game(self, filename: str = None) -> bool:
        """Загрузить игру"""
        loaded = self.save_manager.load_game(filename)
        if loaded:
            self.save_data = loaded
            self._sync_from_save()
            logger.info(f"Игра загружена из {filename or DEFAULT_SAVE}")
            return True
        logger.warning(f"Не удалось загрузить игру из {filename or DEFAULT_SAVE}")
        return False

    def save_game(self, filename: str = None) -> bool:
        """Сохранить игру"""
        self._sync_to_save()
        result = self.save_manager.save_game(filename)
        if result:
            logger.info(f"Игра сохранена в {filename or DEFAULT_SAVE}")
        return result
    
    def _sync_to_save(self):
        """Синхронизировать состояние с данными сохранения"""
        if not self.save_data:
            return

        # Статистика
        self.save_data.stats["alchemy"] = \
            self.abilities_manager.get_tier(AbilityType.ALCHEMY).value
        self.save_data.stats["biotics"] = \
            self.abilities_manager.get_tier(AbilityType.BIOTICS).value
        self.save_data.stats["psychic"] = \
            self.abilities_manager.get_tier(AbilityType.PSYCHIC).value

        # Отношения и доверие
        self.save_data.relationships = {}
        self.save_data.trust_values = {}
        for char in self.crew_manager.get_all_crew():
            if char.role != Role.CAPTAIN:
                self.save_data.relationships[char.id] = char.relationship
                self.save_data.trust_values[char.id] = char.trust

        # Инвентарь
        self.save_data.inventory = self.inventory.to_dict()

        # Кредиты
        self.save_data.credits = self.inventory.credits

        # Квесты
        self.save_data.quest_data = self.quest_manager.to_dict()
        self.save_data.completed_quests = self.quest_manager.completed_quests
        self.save_data.active_quests = list(self.quest_manager.active_quests.keys())
        
        # Новые механики
        self.save_data.resonance = self.resonance_system.to_dict()
        self.save_data.path = self.path_system.to_dict()
        self.save_data.endings = {
            "main": self.ending_system.to_dict(),
            "romance": self.romance_ending_system.to_dict()
        }
        self.save_data.romance = self.romance_manager.to_dict()
        self.save_data.mental_state = self.mental_state_system.to_dict()
    
    def _sync_from_save(self):
        """Синхронизировать данные сохранения с состоянием"""
        if not self.save_data:
            return

        stats = self.save_data.stats
        tier_mapping = {
            "alchemy": AbilityType.ALCHEMY,
            "biotics": AbilityType.BIOTICS,
            "psychic": AbilityType.PSYCHIC,
        }

        for stat_key, ability_type in tier_mapping.items():
            tier_value = stats.get(stat_key, 0)
            if tier_value > 0:
                self.abilities_manager.set_tier(ability_type, AbilityTier(tier_value))

        for char_id, value in self.save_data.relationships.items():
            char = self.crew_manager.get_character(char_id)
            if char:
                char.relationship = value

        # Доверие
        for char_id, value in self.save_data.trust_values.items():
            char = self.crew_manager.get_character(char_id)
            if char:
                char.trust = value

        # Инвентарь
        if self.save_data.inventory:
            self.inventory = Inventory.from_dict(self.save_data.inventory)

        # Кредиты
        self.inventory.credits = self.save_data.credits

        # Квесты
        if self.save_data.quest_data:
            self.quest_manager = QuestManager.from_dict(self.save_data.quest_data)
        
        # Новые механики
        if self.save_data.resonance:
            self.resonance_system.from_dict(self.save_data.resonance)
        
        if self.save_data.path:
            self.path_system.from_dict(self.save_data.path)
        
        if self.save_data.endings:
            if "main" in self.save_data.endings:
                self.ending_system.from_dict(self.save_data.endings["main"])
            if "romance" in self.save_data.endings:
                self.romance_ending_system.from_dict(self.save_data.endings["romance"])

        if self.save_data.romance:
            self.romance_manager = RomanceSceneManager.from_dict(self.save_data.romance)

        if self.save_data.mental_state:
            self.mental_state_system = MentalStateSystem.from_dict(self.save_data.mental_state)
    
    def set_flag(self, flag: str, value: bool = True):
        """Установить флаг сюжета"""
        if self.save_data:
            self.save_data.flags[flag] = value
    
    def get_flag(self, flag: str, default: bool = False) -> bool:
        """Получить флаг сюжета"""
        if self.save_data:
            return self.save_data.flags.get(flag, default)
        return default
    
    def add_item(self, item_id: str, quantity: int = 1) -> bool:
        """Добавить предмет в инвентарь"""
        item = self.item_db.get_item(item_id)
        if item and self.inventory.add_item(item, quantity):
            return True
        return False

    def has_item(self, item_id: str, quantity: int = 1) -> bool:
        """Проверить наличие предмета"""
        return self.inventory.has_item(item_id, quantity)

    def remove_item(self, item_id: str, quantity: int = 1) -> bool:
        """Удалить предмет из инвентаря"""
        return self.inventory.remove_item(item_id, quantity)

    def get_inventory(self) -> Inventory:
        """Получить инвентарь"""
        return self.inventory

    def add_credits(self, amount: int):
        """Добавить кредиты"""
        if amount > 0:
            self.inventory.credits += amount

    def spend_credits(self, amount: int) -> bool:
        """Потратить кредиты"""
        if amount <= 0 or self.inventory.credits < amount:
            return False
        self.inventory.credits -= amount
        return True
    
    def change_relationship(self, char_id: str, amount: int):
        """Изменить отношение с персонажем"""
        char = self.crew_manager.get_character(char_id)
        if char:
            char.change_relationship(amount)
    
    def change_trust(self, char_id: str, amount: int):
        """Изменить доверие персонажа"""
        char = self.crew_manager.get_character(char_id)
        if char:
            char.change_trust(amount)
            logger.info(f"Доверие {char_id} изменено на {amount}")

    def get_crew_relationships(self) -> List[tuple]:
        """Получить список отношений с экипажем (name, status)"""
        return [
            (char.name, char.get_relationship_status())
            for char in self.crew_manager.get_all_crew()
            if char.role != Role.CAPTAIN and char.relationship > 0
        ]

    def get_top_relationship(self) -> Optional[tuple]:
        """Получить персонажа с наивысшими отношениями (name, status)"""
        crew = [
            char for char in self.crew_manager.get_all_crew()
            if char.role != Role.CAPTAIN and char.relationship > 0
        ]
        if not crew:
            return None
        top = max(crew, key=lambda c: c.relationship)
        return (top.name, f"{top.relationship}% ({top.get_relationship_status()})")

    def get_quest_manager(self) -> QuestManager:
        """Получить менеджер квестов"""
        return self.quest_manager

    def accept_quest(self, quest_id: str) -> bool:
        """Принять квест"""
        return self.quest_manager.accept_quest(quest_id)

    def complete_quest(self, quest_id: str):
        """
        Завершить квест и выдать награду.
        Возвращает награду если успешно.
        """
        reward = self.quest_manager.complete_quest(quest_id)
        if reward:
            self.add_credits(reward.credits)
            for item_data in reward.items:
                for item_id, qty in item_data.items():
                    self.add_item(item_id, qty)
            for char_id, amount in reward.relationship_changes.items():
                self.change_relationship(char_id, amount)
            logger.info(f"Квест {quest_id} завершён, награда: {reward.credits} кредитов")
        return reward

    def update_objective(self, quest_id: str, objective_id: str, amount: int = 1):
        """Обновить цель квеста"""
        self.quest_manager.update_objective(quest_id, objective_id, amount)

    # === НОВЫЕ МЕХАНИКИ ===
    
    def get_resonance_system(self) -> ResonanceSystem:
        """Получить систему Резонанса"""
        return self.resonance_system
    
    def get_path_system(self) -> PathSystem:
        """Получить систему Путей"""
        return self.path_system
    
    def get_ending_system(self) -> EndingSystem:
        """Получить систему Финалов"""
        return self.ending_system
    
    def get_romance_ending_system(self) -> RomanceEndingSystem:
        """Получить систему Романтических Концовок"""
        return self.romance_ending_system
    
    def choose_path(self, path_type: PathType) -> bool:
        """Выбрать Путь развития"""
        return self.path_system.choose_path(path_type)
    
    def check_ending_unlock(self, ending_type: EndingType) -> bool:
        """Проверить разблокировку Финала"""
        psychic = self.abilities_manager.get_tier(AbilityType.PSYCHIC).value * 25  # Примерный расчёт
        resonance_level = self.resonance_system.get_level_number()
        abilities = []  # TODO: Получить список способностей
        completed_quests = self.quest_manager.completed_quests
        
        return self.ending_system.check_unlock(
            ending_type, psychic, 0, resonance_level, abilities, completed_quests
        )
    
    def set_active_ending(self, ending_type: EndingType) -> bool:
        """Установить активный Финал"""
        return self.ending_system.set_active_ending(ending_type)
    
    def update_mental_state(self, health_change: int = 0, influence_change: int = 0):
        """Обновить ментальное состояние"""
        if health_change != 0:
            self.mental_state_system.change_mental_health(health_change)
        if influence_change != 0:
            self.mental_state_system.change_entity_influence(influence_change)

    def get_mental_state(self) -> dict:
        """Получить ментальное состояние"""
        return self.mental_state_system.to_dict()

    def get_mental_state_system(self) -> MentalStateSystem:
        """Получить систему ментального состояния"""
        return self.mental_state_system

    def get_romance_manager(self) -> RomanceSceneManager:
        """Получить менеджер романтических сцен"""
        return self.romance_manager

    def get_ending_manager(self) -> EndingSceneManager:
        """Получить менеджер финальных сцен"""
        return self.ending_manager
    
    def check_resonance_level_up(self):
        """Проверить повышение уровня Резонанса"""
        psychic = self.abilities_manager.get_tier(AbilityType.PSYCHIC).value * 25
        completed_chapters = [self.save_data.chapter] if self.save_data else [1]
        return self.resonance_system.check_level_up(psychic, completed_chapters)
