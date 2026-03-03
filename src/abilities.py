"""
Система способностей: алхимия, биотика, психика
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class AbilityType(Enum):
    """Тип способности"""
    ALCHEMY = "Алхимия"
    BIOTICS = "Биотика"
    PSYCHIC = "Психика"


class AbilityTier(Enum):
    """Уровень владения способностью"""
    NONE = 0       # Нет способности
    BASIC = 1      # Базовый
    ADVANCED = 2   # Продвинутый
    EXPERT = 3     # Эксперт
    MASTER = 4     # Мастер


@dataclass
class Ability:
    """Базовая способность"""
    id: str
    name: str
    description: str
    ability_type: AbilityType
    tier: AbilityTier = AbilityTier.NONE
    energy_cost: int = 0
    
    def is_available(self) -> bool:
        """Доступна ли способность"""
        return self.tier != AbilityTier.NONE


@dataclass
class AlchemyAbility(Ability):
    """Алхимическая способность"""
    effect: str = ""  # Описание эффекта
    materials_required: List[str] = field(default_factory=list)


@dataclass
class BioticAbility(Ability):
    """Биотическая способность"""
    field_type: str = ""  # Тип биотического поля
    duration: int = 0     # Длительность в ходах


@dataclass
class PsychicAbility(Ability):
    """Психическая способность"""
    target_type: str = ""  # Тип цели
    stability: float = 0.0  # Стабильность (0.0-1.0)


class AbilitiesManager:
    """Менеджер способностей"""
    
    def __init__(self):
        self.abilities: Dict[str, Ability] = {}
        self.player_tiers: Dict[AbilityType, AbilityTier] = {
            AbilityType.ALCHEMY: AbilityTier.NONE,
            AbilityType.BIOTICS: AbilityTier.NONE,
            AbilityType.PSYCHIC: AbilityTier.NONE,
        }
        self._init_default_abilities()
    
    def _init_default_abilities(self):
        """Инициализировать базовые способности"""
        
        # === АЛХИМИЯ ===
        self.abilities["healing_potion"] = AlchemyAbility(
            id="healing_potion",
            name="Лечебный эликсир",
            description="Восстанавливает здоровье, используя алхимические компоненты.",
            ability_type=AbilityType.ALCHEMY,
            tier=AbilityTier.BASIC,
            energy_cost=10,
            effect="Восстанавливает 25 HP",
            materials_required=["трава_исцеления", "чистая_вода"]
        )
        
        self.abilities["energy_amplifier"] = AlchemyAbility(
            id="energy_amplifier",
            name="Энергетический усилитель",
            description="Усиливает энергетические поля артефактов.",
            ability_type=AbilityType.ALCHEMY,
            tier=AbilityTier.ADVANCED,
            energy_cost=20,
            effect="+20% к силе способностей на 3 хода",
            materials_required=["кристалл_силы", "эфир"]
        )
        
        self.abilities["stabilizer"] = AlchemyAbility(
            id="stabilizer",
            name="Стабилизатор полей",
            description="Стабилизирует нестабильные энергетические поля.",
            ability_type=AbilityType.ALCHEMY,
            tier=AbilityTier.EXPERT,
            energy_cost=30,
            effect="Снимает негативные эффекты артефактов",
            materials_required=["стабилизатор", "редкий_минерал"]
        )
        
        # === БИОТИКА ===
        self.abilities["biotic_shield"] = BioticAbility(
            id="biotic_shield",
            name="Биотический щит",
            description="Создаёт защитное поле вокруг цели.",
            ability_type=AbilityType.BIOTICS,
            tier=AbilityTier.BASIC,
            energy_cost=15,
            field_type="protective",
            duration=3
        )
        
        self.abilities["mental_barrier"] = BioticAbility(
            id="mental_barrier",
            name="Ментальный барьер",
            description="Защищает от психических атак.",
            ability_type=AbilityType.BIOTICS,
            tier=AbilityTier.ADVANCED,
            energy_cost=20,
            field_type="mental",
            duration=5
        )
        
        self.abilities["biotic_pulse"] = BioticAbility(
            id="biotic_pulse",
            name="Биотический импульс",
            description="Высвобождает энергию для отталкивания врагов.",
            ability_type=AbilityType.BIOTICS,
            tier=AbilityTier.EXPERT,
            energy_cost=25,
            field_type="offensive",
            duration=1
        )
        
        # === ПСИХИКА ===
        self.abilities["mind_read"] = PsychicAbility(
            id="mind_read",
            name="Чтение мыслей",
            description="Позволяет читать поверхностные мысли цели.",
            ability_type=AbilityType.PSYCHIC,
            tier=AbilityTier.BASIC,
            energy_cost=15,
            target_type="single",
            stability=0.9
        )
        
        self.abilities["mind_influence"] = PsychicAbility(
            id="mind_influence",
            name="Влияние на сознание",
            description="Влияет на решение цели в диалоге.",
            ability_type=AbilityType.PSYCHIC,
            tier=AbilityTier.ADVANCED,
            energy_cost=30,
            target_type="single",
            stability=0.7
        )
        
        self.abilities["psychic_storm"] = PsychicAbility(
            id="psychic_storm",
            name="Психическая буря",
            description="Массовая атака на сознание всех врагов.",
            ability_type=AbilityType.PSYCHIC,
            tier=AbilityTier.MASTER,
            energy_cost=50,
            target_type="area",
            stability=0.4
        )
    
    def get_ability(self, ability_id: str) -> Optional[Ability]:
        """Получить способность по ID"""
        return self.abilities.get(ability_id)
    
    def get_available_abilities(self) -> List[Ability]:
        """Получить все доступные способности игрока"""
        return [ability for ability in self.abilities.values() 
                if self.can_use_ability(ability)]
    
    def set_tier(self, ability_type: AbilityType, tier: AbilityTier):
        """Установить уровень владения типом способности"""
        self.player_tiers[ability_type] = tier
    
    def get_tier(self, ability_type: AbilityType) -> AbilityTier:
        """Получить текущий уровень владения"""
        return self.player_tiers[ability_type]
    
    def can_use_ability(self, ability: Ability) -> bool:
        """Проверить, может ли игрок использовать способность"""
        if not ability.is_available():
            return False
        player_tier = self.player_tiers[ability.ability_type]
        return ability.tier.value <= player_tier.value
    
    def get_abilities_by_type(self, ability_type: AbilityType) -> List[Ability]:
        """Получить все способности типа"""
        return [a for a in self.abilities.values() 
                if a.ability_type == ability_type and self.can_use_ability(a)]


class CombatSystem:
    """Боевая система с использованием способностей"""
    
    def __init__(self, abilities_manager: AbilitiesManager):
        self.abilities = abilities_manager
        self.player_hp: int = 100
        self.player_max_hp: int = 100
        self.player_energy: int = 100
        self.player_max_energy: int = 100
        self.turn: int = 1
    
    def use_ability(self, ability: Ability) -> dict:
        """
        Использовать способность.
        Возвращает результат использования.
        """
        if not ability or not self.abilities.can_use_ability(ability):
            return {"success": False, "message": "Способность недоступна"}

        if ability.energy_cost < 0:
            return {"success": False, "message": "Некорректная стоимость энергии"}

        if self.player_energy < ability.energy_cost:
            return {"success": False, "message": "Недостаточно энергии"}

        self.player_energy -= ability.energy_cost
        
        result = {
            "success": True,
            "ability": ability.name,
            "energy_cost": ability.energy_cost,
            "effect": "",
            "message": ""
        }
        
        # Применение эффекта в зависимости от типа
        if isinstance(ability, AlchemyAbility):
            result["effect"] = ability.effect
            result["message"] = f"Вы использовали {ability.name}: {ability.effect}"
        
        elif isinstance(ability, BioticAbility):
            result["effect"] = f"{ability.field_type} поле на {ability.duration} ход(а)"
            result["message"] = f"Вы создали {ability.field_type} поле"
        
        elif isinstance(ability, PsychicAbility):
            result["effect"] = f"Влияние на {ability.target_type} цель"
            result["message"] = f"Вы использовали психическую способность на {ability.target_type}"
        
        return result
    
    def restore_energy(self, amount: int):
        """Восстановить энергию"""
        if amount <= 0:
            return
        self.player_energy = min(self.player_max_energy, self.player_energy + amount)

    def heal(self, amount: int):
        """Восстановить здоровье"""
        if amount <= 0:
            return
        self.player_hp = min(self.player_max_hp, self.player_hp + amount)

    def take_damage(self, amount: int) -> bool:
        """Получить урон"""
        if amount <= 0:
            return self.player_hp > 0
        self.player_hp = max(0, self.player_hp - amount)
        return self.player_hp > 0
    
    def is_alive(self) -> bool:
        """Жив ли игрок"""
        return self.player_hp > 0
