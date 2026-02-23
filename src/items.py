"""
Система предметов и инвентаря
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Callable
from enum import Enum
import json


class ItemType(Enum):
    """Типы предметов"""
    CONSUMABLE = "consumable"      # Расходуемые
    EQUIPMENT = "equipment"        # Снаряжение
    MATERIAL = "material"          # Материалы
    QUEST = "quest"                # Квестовые
    ARTIFACT = "artifact"          # Артефакты
    WEAPON = "weapon"              # Оружие
    ARMOR = "armor"                # Броня


class Rarity(Enum):
    """Редкость предметов"""
    COMMON = "common"          # Обычное
    UNCOMMON = "uncommon"      # Необычное
    RARE = "rare"              # Редкое
    EPIC = "epic"              # Эпическое
    LEGENDARY = "legendary"    # Легендарное


class EquipmentSlot(Enum):
    """Слоты экипировки"""
    WEAPON = "weapon"
    ARMOR = "armor"
    ACCESSORY = "accessory"
    IMPLANT = "implant"


@dataclass
class ItemEffect:
    """Эффект предмета"""
    stat: str           # Какой стат изменяет
    value: int          # Значение изменения
    duration: int = 0   # Длительность (0 = мгновенный)
    is_buff: bool = True  # Бафф или дебафф


@dataclass
class Item:
    """Базовый предмет"""
    id: str
    name: str
    description: str
    item_type: ItemType
    rarity: Rarity = Rarity.COMMON
    value: int = 0      # Стоимость в кредитах
    weight: float = 0.0 # Вес
    
    # Эффекты
    effects: List[ItemEffect] = field(default_factory=list)
    
    # Использование
    is_consumable: bool = False
    is_stackable: bool = True
    max_stack: int = 99
    
    # Мета
    icon: str = "📦"
    lore: str = ""  # Описание в лоре
    
    def to_dict(self) -> dict:
        """Сериализация в словарь"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "item_type": self.item_type.value,
            "rarity": self.rarity.value,
            "value": self.value,
            "weight": self.weight,
            "effects": [
                {"stat": e.stat, "value": e.value, "duration": e.duration}
                for e in self.effects
            ],
            "is_consumable": self.is_consumable,
            "is_stackable": self.is_stackable,
            "max_stack": self.max_stack,
            "icon": self.icon,
            "lore": self.lore,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Item":
        """Десериализация из словаря"""
        effects = [
            ItemEffect(**e) for e in data.get("effects", [])
        ]
        return cls(
            id=data["id"],
            name=data["name"],
            description=data["description"],
            item_type=ItemType(data["item_type"]),
            rarity=Rarity(data["rarity"]),
            value=data["value"],
            weight=data["weight"],
            effects=effects,
            is_consumable=data.get("is_consumable", False),
            is_stackable=data.get("is_stackable", True),
            max_stack=data.get("max_stack", 99),
            icon=data.get("icon", "📦"),
            lore=data.get("lore", ""),
        )


@dataclass
class Consumable(Item):
    """Расходуемый предмет"""
    heal_amount: int = 0
    energy_amount: int = 0
    effect_text: str = ""


@dataclass
class Equipment(Item):
    """Предмет экипировки"""
    slot: EquipmentSlot = EquipmentSlot.ACCESSORY
    armor_value: int = 0
    damage: int = 0
    requirements: Dict[str, int] = field(default_factory=dict)


@dataclass
class Material(Item):
    """Материал для крафта"""
    category: str = "basic"  # basic, rare, exotic


@dataclass
class Artifact(Item):
    """Артефакт — уникальный предмет сюжета"""
    power_level: int = 0
    is_active: bool = False
    abilities_unlocked: List[str] = field(default_factory=list)


@dataclass
class ItemStack:
    """Стак предметов в инвентаре"""
    item: Item
    quantity: int = 1
    
    def is_full(self) -> bool:
        """Проверить, полон ли стак"""
        return self.quantity >= self.item.max_stack
    
    def add(self, amount: int) -> int:
        """
        Добавить предметы.
        Возвращает количество не поместившихся.
        """
        space = self.item.max_stack - self.quantity
        if amount <= space:
            self.quantity += amount
            return 0
        else:
            self.quantity = self.item.max_stack
            return amount - space
    
    def remove(self, amount: int) -> int:
        """
        Удалить предметы.
        Возвращает количество удалённых.
        """
        removed = min(amount, self.quantity)
        self.quantity -= removed
        return removed
    
    def is_empty(self) -> bool:
        """Проверить, пуст ли стак"""
        return self.quantity <= 0


class Inventory:
    """Инвентарь игрока"""
    
    def __init__(self, max_slots: int = 20):
        self.slots: List[Optional[ItemStack]] = [None] * max_slots
        self.max_slots = max_slots
        self.credits: int = 0
    
    def get_empty_slot(self) -> int:
        """Найти пустой слот"""
        for i, slot in enumerate(self.slots):
            if slot is None:
                return i
        return -1
    
    def get_slot_for_item(self, item: Item) -> int:
        """
        Найти слот для предмета (существующий стак или пустой).
        Возвращает -1 если нет места.
        """
        if item.is_stackable:
            # Ищем существующий стак
            for i, slot in enumerate(self.slots):
                if slot and slot.item.id == item.id and not slot.is_full():
                    return i
        
        # Ищем пустой слот
        return self.get_empty_slot()
    
    def add_item(self, item: Item, quantity: int = 1) -> bool:
        """
        Добавить предмет в инвентарь.
        Возвращает True если успешно.
        """
        remaining = quantity
        
        while remaining > 0:
            slot_idx = self.get_slot_for_item(item)
            
            if slot_idx == -1:
                return False  # Нет места
            
            if self.slots[slot_idx]:
                # Добавляем в существующий стак
                remaining = self.slots[slot_idx].add(remaining)
            else:
                # Создаём новый стак
                stack_size = min(remaining, item.max_stack)
                self.slots[slot_idx] = ItemStack(item, stack_size)
                remaining -= stack_size
        
        return True
    
    def remove_item(self, item_id: str, quantity: int = 1) -> bool:
        """
        Удалить предмет из инвентаря.
        Возвращает True если успешно.
        """
        removed = 0
        
        for slot in self.slots:
            if slot and slot.item.id == item_id:
                removed += slot.remove(quantity - removed)
                if removed >= quantity:
                    break
        
        # Очищаем пустые стаки
        self.slots = [slot if slot and not slot.is_empty() else None for slot in self.slots]
        
        return removed >= quantity
    
    def has_item(self, item_id: str, quantity: int = 1) -> bool:
        """Проверить наличие предмета"""
        total = sum(
            slot.quantity for slot in self.slots
            if slot and slot.item.id == item_id
        )
        return total >= quantity
    
    def get_item_count(self, item_id: str) -> int:
        """Получить количество предмета"""
        return sum(
            slot.quantity for slot in self.slots
            if slot and slot.item.id == item_id
        )
    
    def get_item(self, item_id: str) -> Optional[Item]:
        """Получить предмет по ID (первый найденный)"""
        for slot in self.slots:
            if slot and slot.item.id == item_id:
                return slot.item
        return None
    
    def use_item(self, item_id: str, target=None) -> Optional[dict]:
        """
        Использовать предмет.
        Возвращает результат использования.
        """
        if not self.has_item(item_id):
            return None
        
        item = self.get_item(item_id)
        if not item or not item.is_consumable:
            return None
        
        result = {"success": True, "item": item.name, "effects": []}
        
        # Применяем эффекты
        for effect in item.effects:
            result["effects"].append({
                "stat": effect.stat,
                "value": effect.value,
            })
        
        # Удаляем предмет
        self.remove_item(item_id, 1)
        
        return result
    
    def get_all_items(self) -> List[ItemStack]:
        """Получить все предметы"""
        return [slot for slot in self.slots if slot is not None]
    
    def get_items_by_type(self, item_type: ItemType) -> List[ItemStack]:
        """Получить предметы по типу"""
        return [
            slot for slot in self.slots
            if slot and slot.item.item_type == item_type
        ]
    
    def get_total_weight(self) -> float:
        """Получить общий вес"""
        return sum(
            slot.item.weight * slot.quantity
            for slot in self.slots if slot
        )
    
    def get_free_slots(self) -> int:
        """Получить количество свободных слотов"""
        return sum(1 for slot in self.slots if slot is None)
    
    def to_dict(self) -> dict:
        """Сериализация"""
        return {
            "slots": [
                {"item": slot.item.to_dict(), "quantity": slot.quantity}
                if slot else None
                for slot in self.slots
            ],
            "credits": self.credits,
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Inventory":
        """Десериализация"""
        inv = cls()
        inv.credits = data.get("credits", 0)
        
        slots_data = data.get("slots", [])
        for i, slot_data in enumerate(slots_data):
            if slot_data:
                item = Item.from_dict(slot_data["item"])
                inv.slots[i] = ItemStack(item, slot_data["quantity"])
        
        return inv


class ItemDatabase:
    """База данных предметов"""
    
    def __init__(self):
        self.items: Dict[str, Item] = {}
        self._init_default_items()
    
    def _init_default_items(self):
        """Инициализировать базовые предметы"""
        
        # === РАСХОДУЕМЫЕ ===
        self.items["healing_potion"] = Consumable(
            id="healing_potion",
            name="Лечебный эликсир",
            description="Восстанавливает 25 единиц здоровья.",
            item_type=ItemType.CONSUMABLE,
            rarity=Rarity.COMMON,
            value=50,
            weight=0.2,
            is_consumable=True,
            heal_amount=25,
            effects=[ItemEffect("hp", 25)],
            icon="🧪"
        )
        
        self.items["energy_cell"] = Consumable(
            id="energy_cell",
            name="Энергоячейка",
            description="Восстанавливает 30 единиц энергии.",
            item_type=ItemType.CONSUMABLE,
            rarity=Rarity.COMMON,
            value=40,
            weight=0.1,
            is_consumable=True,
            energy_amount=30,
            effects=[ItemEffect("energy", 30)],
            icon="🔋"
        )
        
        self.items["biotic_stim"] = Consumable(
            id="biotic_stim",
            name="Биотический стимулятор",
            description="Временно усиливает биотические способности.",
            item_type=ItemType.CONSUMABLE,
            rarity=Rarity.UNCOMMON,
            value=150,
            weight=0.15,
            is_consumable=True,
            effects=[
                ItemEffect("biotics_power", 20, duration=3),
            ],
            icon="💉"
        )
        
        self.items["psychic_amplifier"] = Consumable(
            id="psychic_amplifier",
            name="Психический усилитель",
            description="Увеличивает силу психических способностей.",
            item_type=ItemType.CONSUMABLE,
            rarity=Rarity.RARE,
            value=300,
            weight=0.1,
            is_consumable=True,
            effects=[
                ItemEffect("psychic_power", 35, duration=2),
            ],
            icon="🔮"
        )
        
        # === МАТЕРИАЛЫ ===
        self.items["herb_healing"] = Material(
            id="herb_healing",
            name="Трава исцеления",
            description="Редкая трава с целебными свойствами.",
            item_type=ItemType.MATERIAL,
            rarity=Rarity.UNCOMMON,
            value=25,
            weight=0.05,
            category="basic",
            icon="🌿"
        )
        
        self.items["pure_water"] = Material(
            id="pure_water",
            name="Чистая вода",
            description="Дистиллированная вода для алхимии.",
            item_type=ItemType.MATERIAL,
            rarity=Rarity.COMMON,
            value=10,
            weight=0.5,
            category="basic",
            icon="💧"
        )
        
        self.items["power_crystal"] = Material(
            id="power_crystal",
            name="Кристалл силы",
            description="Энергетический кристалл с древней станции.",
            item_type=ItemType.MATERIAL,
            rarity=Rarity.RARE,
            value=200,
            weight=0.3,
            category="rare",
            icon="💎"
        )
        
        self.items["ether"] = Material(
            id="ether",
            name="Эфир",
            description="Мистическая субстанция из глубин космоса.",
            item_type=ItemType.MATERIAL,
            rarity=Rarity.EPIC,
            value=500,
            weight=0.1,
            category="exotic",
            icon="✨"
        )
        
        # === ОРУЖИЕ ===
        self.items["plasma_pistol"] = Equipment(
            id="plasma_pistol",
            name="Плазменный пистолет",
            description="Стандартное оружие экипажа.",
            item_type=ItemType.WEAPON,
            rarity=Rarity.COMMON,
            value=500,
            weight=1.5,
            slot=EquipmentSlot.WEAPON,
            damage=15,
            icon="🔫"
        )
        
        self.items["biotic_blade"] = Equipment(
            id="biotic_blade",
            name="Биотический клинок",
            description="Клинок, усиленный биотическим полем.",
            item_type=ItemType.WEAPON,
            rarity=Rarity.RARE,
            value=1500,
            weight=1.0,
            slot=EquipmentSlot.WEAPON,
            damage=30,
            requirements={"biotics": 2},
            icon="⚔️"
        )
        
        # === БРОНЯ ===
        self.items["light_armor"] = Equipment(
            id="light_armor",
            name="Лёгкая броня",
            description="Стандартная защита экипажа.",
            item_type=ItemType.ARMOR,
            rarity=Rarity.COMMON,
            value=400,
            weight=5.0,
            slot=EquipmentSlot.ARMOR,
            armor_value=10,
            icon="🦺"
        )
        
        self.items["psi_shield"] = Equipment(
            id="psi_shield",
            name="Пси-щит",
            description="Генератор психического защитного поля.",
            item_type=ItemType.ARMOR,
            rarity=Rarity.EPIC,
            value=2000,
            weight=3.0,
            slot=EquipmentSlot.ARMOR,
            armor_value=25,
            requirements={"psychic": 2},
            icon="🛡️"
        )
        
        # === АРТЕФАКТЫ ===
        self.items["main_artifact"] = Artifact(
            id="main_artifact",
            name="Загадочный артефакт",
            description="Древний объект неизвестного происхождения. "
                       "Излучает странную энергию.",
            item_type=ItemType.ARTIFACT,
            rarity=Rarity.LEGENDARY,
            value=0,  # Бесценен
            weight=2.0,
            power_level=100,
            is_stackable=False,
            icon="🔷"
        )
        
        self.items["alien_data_chip"] = Artifact(
            id="alien_data_chip",
            name="Чип с данными",
            description="Инопланетный носитель информации. "
                       "Содержит зашифрованные данные.",
            item_type=ItemType.ARTIFACT,
            rarity=Rarity.EPIC,
            value=0,
            weight=0.01,
            is_stackable=False,
            icon="💾"
        )
        
        # === КВЕСТОВЫЕ ===
        self.items["captain_badge"] = Item(
            id="captain_badge",
            name="Значок капитана",
            description="Символ власти капитана «Элеи».",
            item_type=ItemType.QUEST,
            rarity=Rarity.UNCOMMON,
            value=0,
            weight=0.05,
            is_stackable=False,
            icon="🎖️"
        )
        
        self.items["pirate_key"] = Item(
            id="pirate_key",
            name="Ключ пирата",
            description="Электронный ключ с пиратского фрегата.",
            item_type=ItemType.QUEST,
            rarity=Rarity.UNCOMMON,
            value=0,
            weight=0.1,
            is_stackable=False,
            icon="🔑"
        )
    
    def get_item(self, item_id: str) -> Optional[Item]:
        """Получить предмет по ID"""
        return self.items.get(item_id)
    
    def get_all_items(self) -> List[Item]:
        """Получить все предметы"""
        return list(self.items.values())
    
    def get_items_by_rarity(self, rarity: Rarity) -> List[Item]:
        """Получить предметы по редкости"""
        return [i for i in self.items.values() if i.rarity == rarity]
    
    def get_items_by_type(self, item_type: ItemType) -> List[Item]:
        """Получить предметы по типу"""
        return [i for i in self.items.values() if i.item_type == item_type]
    
    def create_item(self, item_id: str, quantity: int = 1) -> Optional[ItemStack]:
        """Создать стак предмета"""
        item = self.get_item(item_id)
        if item:
            return ItemStack(item, quantity)
        return None
