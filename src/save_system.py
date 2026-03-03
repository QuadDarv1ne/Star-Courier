"""
Система сохранений и загрузок игры
"""

import json
import os
from datetime import datetime
from typing import Dict, Any, Optional
from pathlib import Path

try:
    from .config import SAVE_DIR, DEFAULT_SAVE, GAME_TITLE, VERSION
    from .characters import CrewManager, Character, Role
    from .abilities import AbilitiesManager, AbilityType, AbilityTier
except ImportError:
    from config import SAVE_DIR, DEFAULT_SAVE, GAME_TITLE, VERSION
    from characters import CrewManager, Character, Role
    from abilities import AbilitiesManager, AbilityType, AbilityTier


class SaveData:
    """Данные сохранения"""
    
    def __init__(self):
        # Метаданные
        self.timestamp: str = ""
        self.game_version: str = VERSION
        self.chapter: int = 1
        self.scene: str = "start"
        
        # Статистика игрока
        self.stats: Dict[str, int] = {
            "alchemy": 0,
            "biotics": 0,
            "psychic": 0,
        }
        
        # Ресурсы
        self.credits: int = 0
        self.inventory: list = []
        
        # Отношения с персонажами
        self.relationships: Dict[str, int] = {}
        
        # Прогресс сюжета
        self.flags: Dict[str, bool] = {}  # Флаги событий
        self.completed_quests: list = []
        self.active_quests: list = []
        
        # История выборов
        self.choices_history: list = []
    
    def to_dict(self) -> Dict[str, Any]:
        """Сериализовать в словарь"""
        return {
            "meta": {
                "timestamp": self.timestamp,
                "game_version": self.game_version,
                "chapter": self.chapter,
                "scene": self.scene,
            },
            "player": {
                "stats": self.stats,
                "credits": self.credits,
                "inventory": self.inventory,
            },
            "relationships": self.relationships,
            "progress": {
                "flags": self.flags,
                "completed_quests": self.completed_quests,
                "active_quests": self.active_quests,
            },
            "history": {
                "choices": self.choices_history,
            }
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "SaveData":
        """Десериализовать из словаря"""
        save = cls()
        
        meta = data.get("meta", {})
        save.timestamp = meta.get("timestamp", "")
        save.game_version = meta.get("game_version", VERSION)
        save.chapter = meta.get("chapter", 1)
        save.scene = meta.get("scene", "start")
        
        player = data.get("player", {})
        save.stats = player.get("stats", save.stats)
        save.credits = player.get("credits", 0)
        save.inventory = player.get("inventory", [])
        
        save.relationships = data.get("relationships", {})
        
        progress = data.get("progress", {})
        save.flags = progress.get("flags", {})
        save.completed_quests = progress.get("completed_quests", [])
        save.active_quests = progress.get("active_quests", [])
        
        history = data.get("history", {})
        save.choices_history = history.get("choices", [])
        
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
            return True
        except Exception as e:
            print(f"Ошибка сохранения: {e}")
            return False
    
    def load_game(self, filename: str = None) -> Optional[SaveData]:
        """Загрузить игру"""
        if not filename:
            filename = DEFAULT_SAVE
        
        filepath = self.save_dir / filename
        if not filepath.exists():
            filepath = filepath.with_suffix(".json")
        
        if not filepath.exists():
            return None
        
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            self.current_save = SaveData.from_dict(data)
            return self.current_save
        except Exception as e:
            print(f"Ошибка загрузки: {e}")
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
    
    def __init__(self):
        self.save_manager = SaveManager()
        self.crew_manager = CrewManager()
        self.abilities_manager = AbilitiesManager()
        self.save_data: Optional[SaveData] = None
    
    def new_game(self):
        """Новая игра"""
        self.save_data = self.save_manager.create_new_save()
        self._sync_from_save()
    
    def load_game(self, filename: str = None) -> bool:
        """Загрузить игру"""
        loaded = self.save_manager.load_game(filename)
        if loaded:
            self.save_data = loaded
            self._sync_from_save()
            return True
        return False
    
    def save_game(self, filename: str = None) -> bool:
        """Сохранить игру"""
        self._sync_to_save()
        return self.save_manager.save_game(filename)
    
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
        
        # Отношения
        self.save_data.relationships = {}
        for char in self.crew_manager.get_all_crew():
            if char.role != Role.CAPTAIN:
                self.save_data.relationships[char.id] = char.relationship
    
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
    
    def set_flag(self, flag: str, value: bool = True):
        """Установить флаг сюжета"""
        if self.save_data:
            self.save_data.flags[flag] = value
    
    def get_flag(self, flag: str, default: bool = False) -> bool:
        """Получить флаг сюжета"""
        if self.save_data:
            return self.save_data.flags.get(flag, default)
        return default
    
    def add_item(self, item: str):
        """Добавить предмет в инвентарь"""
        if self.save_data and item not in self.save_data.inventory:
            self.save_data.inventory.append(item)
    
    def has_item(self, item: str) -> bool:
        """Проверить наличие предмета"""
        if self.save_data:
            return item in self.save_data.inventory
        return False
    
    def change_relationship(self, char_id: str, amount: int):
        """Изменить отношение с персонажем"""
        char = self.crew_manager.get_character(char_id)
        if char:
            char.change_relationship(amount)
