# -*- coding: utf-8 -*-
"""
Star Courier - Advanced Abilities System
Продвинутые способности 50-100 уровня
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from enum import Enum


class AdvancedAbilityTier(Enum):
    """Уровни продвинутых способностей"""
    TIER_50 = 50  # Базовый продвинутый
    TIER_60 = 60  # Улучшенный
    TIER_70 = 70  # Продвинутый
    TIER_80 = 80  # Экспертный
    TIER_90 = 90  # Мастерский
    TIER_100 = 100  # Легендарный


@dataclass
class AdvancedAbility:
    """Продвинутая способность"""
    id: str
    name: str
    description: str
    ability_type: str  # alchemy, biotics, psychic
    tier: AdvancedAbilityTier
    energy_cost: int
    cooldown: int = 0  # Ходов перезарядки
    damage: int = 0
    healing: int = 0
    duration: int = 0  # Длительность эффекта
    effects: Dict[str, int] = field(default_factory=dict)
    requirements: Dict[str, int] = field(default_factory=dict)


class AdvancedAbilitiesManager:
    """Менеджер продвинутых способностей"""

    def __init__(self):
        self.abilities: Dict[str, AdvancedAbility] = {}
        self.player_abilities: List[str] = []
        self._init_abilities()

    def _init_abilities(self):
        """Инициализировать все продвинутые способности"""
        self._init_alchemy_abilities()
        self._init_biotic_abilities()
        self._init_psychic_abilities()

    def _init_alchemy_abilities(self):
        """Алхимические способности 50-100 уровня"""
        # === УРОВЕНЬ 50 ===
        self.abilities["alchemy_50_1"] = AdvancedAbility(
            id="alchemy_50_1",
            name="Философский камень",
            description="Легендарный алхимический реагент, усиливающий все способности.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_50,
            energy_cost=50,
            cooldown=5,
            effects={"all_stats_boost": 25, "duration": 3},
            requirements={"alchemy": 50}
        )

        self.abilities["alchemy_50_2"] = AdvancedAbility(
            id="alchemy_50_2",
            name="Эликсир бессмертия",
            description="Временно делает неуязвимым к смертельному урону.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_50,
            energy_cost=60,
            cooldown=10,
            effects={"invulnerable": 1, "duration": 2},
            requirements={"alchemy": 50}
        )

        # === УРОВЕНЬ 60 ===
        self.abilities["alchemy_60_1"] = AdvancedAbility(
            id="alchemy_60_1",
            name="Трансмутация материи",
            description="Преобразует один материал в другой.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_60,
            energy_cost=40,
            cooldown=3,
            effects={"transmute": 1, "material_value": 50},
            requirements={"alchemy": 60}
        )

        self.abilities["alchemy_60_2"] = AdvancedAbility(
            id="alchemy_60_2",
            name="Алхимический взрыв",
            description="Создаёт мощную взрывную волну из химических реагентов.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_60,
            energy_cost=55,
            damage=80,
            cooldown=4,
            requirements={"alchemy": 60}
        )

        # === УРОВЕНЬ 70 ===
        self.abilities["alchemy_70_1"] = AdvancedAbility(
            id="alchemy_70_1",
            name="Золотой эликсир",
            description="Восстанавливает всё здоровье и энергию.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_70,
            energy_cost=70,
            healing=100,
            effects={"energy_restore": 100},
            cooldown=8,
            requirements={"alchemy": 70}
        )

        self.abilities["alchemy_70_2"] = AdvancedAbility(
            id="alchemy_70_2",
            name="Алхимическое оружие",
            description="Создаёт оружие из чистого алхимического огня.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_70,
            energy_cost=45,
            damage=60,
            effects={"burn_damage": 20, "duration": 3},
            cooldown=3,
            requirements={"alchemy": 70}
        )

        # === УРОВЕНЬ 80 ===
        self.abilities["alchemy_80_1"] = AdvancedAbility(
            id="alchemy_80_1",
            name="Вечный двигатель",
            description="Создаёт источник бесконечной энергии на короткое время.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_80,
            energy_cost=80,
            cooldown=12,
            effects={"infinite_energy": 1, "duration": 3},
            requirements={"alchemy": 80}
        )

        self.abilities["alchemy_80_2"] = AdvancedAbility(
            id="alchemy_80_2",
            name="Алхимическое превращение",
            description="Превращает врага в безобидное существо.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_80,
            energy_cost=90,
            cooldown=15,
            effects={"polymorph": 1, "duration": 2, "success_chance": 70},
            requirements={"alchemy": 80}
        )

        # === УРОВЕНЬ 90 ===
        self.abilities["alchemy_90_1"] = AdvancedAbility(
            id="alchemy_90_1",
            name="Древний рецепт",
            description="Активирует скрытые алхимические знания Древних.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_90,
            energy_cost=100,
            cooldown=10,
            effects={"all_abilities_boost": 50, "duration": 5},
            requirements={"alchemy": 90}
        )

        self.abilities["alchemy_90_2"] = AdvancedAbility(
            id="alchemy_90_2",
            name="Алхимический апокалипсис",
            description="Вызывает масштабную химическую реакцию.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_90,
            energy_cost=120,
            damage=150,
            cooldown=20,
            requirements={"alchemy": 90}
        )

        # === УРОВЕНЬ 100 ===
        self.abilities["alchemy_100_1"] = AdvancedAbility(
            id="alchemy_100_1",
            name="Божественная трансмутация",
            description="Изменяет саму реальность на квантовом уровне.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_100,
            energy_cost=150,
            cooldown=25,
            effects={"reality_warp": 1, "duration": 1},
            requirements={"alchemy": 100}
        )

        self.abilities["alchemy_100_2"] = AdvancedAbility(
            id="alchemy_100_2",
            name="Сердце вселенной",
            description="Позволяет создавать материю из чистой энергии.",
            ability_type="alchemy",
            tier=AdvancedAbilityTier.TIER_100,
            energy_cost=200,
            cooldown=30,
            effects={"create_matter": 1, "credits_gain": 1000},
            requirements={"alchemy": 100}
        )

    def _init_biotic_abilities(self):
        """Биотические способности 50-100 уровня"""
        # === УРОВЕНЬ 50 ===
        self.abilities["biotic_50_1"] = AdvancedAbility(
            id="biotic_50_1",
            name="Биотическая сингулярность",
            description="Создаёт гравитационную аномалию, захватывающую врагов.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_50,
            energy_cost=55,
            damage=40,
            cooldown=4,
            effects={"pull": 1, "duration": 2},
            requirements={"biotics": 50}
        )

        self.abilities["biotic_50_2"] = AdvancedAbility(
            id="biotic_50_2",
            name="Регенерация",
            description="Ускоряет естественное восстановление организма.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_50,
            energy_cost=40,
            healing=50,
            cooldown=3,
            requirements={"biotics": 50}
        )

        # === УРОВЕНЬ 60 ===
        self.abilities["biotic_60_1"] = AdvancedAbility(
            id="biotic_60_1",
            name="Биотический шторм",
            description="Высвобождает энергию в виде разрушительной волны.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_60,
            energy_cost=65,
            damage=70,
            cooldown=5,
            requirements={"biotics": 60}
        )

        self.abilities["biotic_60_2"] = AdvancedAbility(
            id="biotic_60_2",
            name="Усиление мышц",
            description="Временно увеличивает физическую силу.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_60,
            energy_cost=35,
            cooldown=3,
            effects={"strength_boost": 40, "duration": 4},
            requirements={"biotics": 60}
        )

        # === УРОВЕНЬ 70 ===
        self.abilities["biotic_70_1"] = AdvancedAbility(
            id="biotic_70_1",
            name="Биотический барьер",
            description="Создаёт защитное поле вокруг союзников.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_70,
            energy_cost=60,
            cooldown=6,
            effects={"shield": 100, "duration": 4, "aoe": 1},
            requirements={"biotics": 70}
        )

        self.abilities["biotic_70_2"] = AdvancedAbility(
            id="biotic_70_2",
            name="Нейротоксин",
            description="Вырабатывает яд, парализующий нервную систему.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_70,
            energy_cost=50,
            damage=50,
            cooldown=4,
            effects={"paralyze": 1, "duration": 2},
            requirements={"biotics": 70}
        )

        # === УРОВЕНЬ 80 ===
        self.abilities["biotic_80_1"] = AdvancedAbility(
            id="biotic_80_1",
            name="Эволюционный скачок",
            description="Временно активирует скрытые гены.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_80,
            energy_cost=80,
            cooldown=10,
            effects={"all_stats_boost": 35, "duration": 5},
            requirements={"biotics": 80}
        )

        self.abilities["biotic_80_2"] = AdvancedAbility(
            id="biotic_80_2",
            name="Биотическая левитация",
            description="Позволяет парить в воздухе и избегать атак.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_80,
            energy_cost=45,
            cooldown=5,
            effects={"levitate": 1, "dodge_boost": 50, "duration": 3},
            requirements={"biotics": 80}
        )

        # === УРОВЕНЬ 90 ===
        self.abilities["biotic_90_1"] = AdvancedAbility(
            id="biotic_90_1",
            name="Био-взрыв",
            description="Дестабилизирует биотическую энергию во враге.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_90,
            energy_cost=100,
            damage=120,
            cooldown=8,
            effects={"chain_explosion": 1},
            requirements={"biotics": 90}
        )

        self.abilities["biotic_90_2"] = AdvancedAbility(
            id="biotic_90_2",
            name="Улей",
            description="Временно контролирует разум нескольких существ.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_90,
            energy_cost=110,
            cooldown=15,
            effects={"mind_control": 3, "duration": 3},
            requirements={"biotics": 90}
        )

        # === УРОВЕНЬ 100 ===
        self.abilities["biotic_100_1"] = AdvancedAbility(
            id="biotic_100_1",
            name="Абсолютная форма",
            description="Достигает пика биотической эволюции.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_100,
            energy_cost=150,
            cooldown=20,
            effects={"max_stats": 1, "duration": 5},
            requirements={"biotics": 100}
        )

        self.abilities["biotic_100_2"] = AdvancedAbility(
            id="biotic_100_2",
            name="Биотическая сверхновая",
            description="Высвобождает всю накопленную энергию одновременно.",
            ability_type="biotics",
            tier=AdvancedAbilityTier.TIER_100,
            energy_cost=200,
            damage=200,
            cooldown=30,
            effects={"aoe_damage": 1, "self_damage": 50},
            requirements={"biotics": 100}
        )

    def _init_psychic_abilities(self):
        """Психические способности 50-100 уровня"""
        # === УРОВЕНЬ 50 ===
        self.abilities["psychic_50_1"] = AdvancedAbility(
            id="psychic_50_1",
            name="Психический удар",
            description="Атакует разум врага психической энергией.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_50,
            energy_cost=50,
            damage=60,
            cooldown=3,
            requirements={"psychic": 50}
        )

        self.abilities["psychic_50_2"] = AdvancedAbility(
            id="psychic_50_2",
            name="Ясновидение",
            description="Позволяет увидеть скрытые пути и предметы.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_50,
            energy_cost=40,
            cooldown=5,
            effects={"reveal_hidden": 1, "duration": 10},
            requirements={"psychic": 50}
        )

        # === УРОВЕНЬ 60 ===
        self.abilities["psychic_60_1"] = AdvancedAbility(
            id="psychic_60_1",
            name="Телекинез",
            description="Перемещает объекты силой мысли.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_60,
            energy_cost=55,
            cooldown=4,
            effects={"telekinesis": 1, "damage": 50},
            requirements={"psychic": 60}
        )

        self.abilities["psychic_60_2"] = AdvancedAbility(
            id="psychic_60_2",
            name="Психический щит",
            description="Защищает разум от ментальных атак.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_60,
            energy_cost=45,
            cooldown=6,
            effects={"mental_shield": 1, "duration": 5},
            requirements={"psychic": 60}
        )

        # === УРОВЕНЬ 70 ===
        self.abilities["psychic_70_1"] = AdvancedAbility(
            id="psychic_70_1",
            name="Ментальный контроль",
            description="Временно подчиняет волю врага.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_70,
            energy_cost=80,
            cooldown=10,
            effects={"mind_control": 1, "duration": 3, "success_chance": 60},
            requirements={"psychic": 70}
        )

        self.abilities["psychic_70_2"] = AdvancedAbility(
            id="psychic_70_2",
            name="Психическая буря",
            description="Высвобождает психическую энергию в радиусе.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_70,
            energy_cost=70,
            damage=80,
            cooldown=6,
            effects={"aoe": 1},
            requirements={"psychic": 70}
        )

        # === УРОВЕНЬ 80 ===
        self.abilities["psychic_80_1"] = AdvancedAbility(
            id="psychic_80_1",
            name="Предвидение",
            description="Позволяет видеть будущие ходы противника.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_80,
            energy_cost=60,
            cooldown=8,
            effects={"precognition": 1, "dodge_boost": 70, "duration": 4},
            requirements={"psychic": 80}
        )

        self.abilities["psychic_80_2"] = AdvancedAbility(
            id="psychic_80_2",
            name="Астральная проекция",
            description="Позволяет исследовать местность без тела.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_80,
            energy_cost=50,
            cooldown=5,
            effects={"invisible": 1, "scout": 1, "duration": 5},
            requirements={"psychic": 80}
        )

        # === УРОВЕНЬ 90 ===
        self.abilities["psychic_90_1"] = AdvancedAbility(
            id="psychic_90_1",
            name="Психическая тюрьма",
            description="Заключает разум врага в ментальную ловушку.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_90,
            energy_cost=100,
            cooldown=12,
            effects={"imprison": 1, "duration": 3},
            requirements={"psychic": 90}
        )

        self.abilities["psychic_90_2"] = AdvancedAbility(
            id="psychic_90_2",
            name="Массовый гипноз",
            description="Подчиняет несколько целей одновременно.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_90,
            energy_cost=120,
            cooldown=15,
            effects={"mass_hypnosis": 5, "duration": 4},
            requirements={"psychic": 90}
        )

        # === УРОВЕНЬ 100 ===
        self.abilities["psychic_100_1"] = AdvancedAbility(
            id="psychic_100_1",
            name="Вселенское сознание",
            description="Сливается с коллективным разумом вселенной.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_100,
            energy_cost=150,
            cooldown=20,
            effects={"omniscience": 1, "duration": 5},
            requirements={"psychic": 100}
        )

        self.abilities["psychic_100_2"] = AdvancedAbility(
            id="psychic_100_2",
            name="Психическая сингулярность",
            description="Создаёт разлом в реальности силой разума.",
            ability_type="psychic",
            tier=AdvancedAbilityTier.TIER_100,
            energy_cost=200,
            damage=250,
            cooldown=30,
            effects={"reality_tear": 1, "instant_kill_chance": 20},
            requirements={"psychic": 100}
        )

    def get_abilities_for_level(self, level: int) -> List[AdvancedAbility]:
        """Получить способности для уровня"""
        return [
            ability for ability in self.abilities.values()
            if ability.tier.value <= level
        ]

    def get_ability(self, ability_id: str) -> Optional[AdvancedAbility]:
        """Получить способность по ID"""
        return self.abilities.get(ability_id)

    def get_abilities_by_type(self, ability_type: str) -> List[AdvancedAbility]:
        """Получить способности по типу"""
        return [
            ability for ability in self.abilities.values()
            if ability.ability_type == ability_type
        ]

    def unlock_ability(self, ability_id: str) -> bool:
        """Разблокировать способность"""
        if ability_id not in self.abilities:
            return False
        if ability_id not in self.player_abilities:
            self.player_abilities.append(ability_id)
        return True

    def has_ability(self, ability_id: str) -> bool:
        """Проверить наличие способности"""
        return ability_id in self.player_abilities

    def get_unlocked_abilities(self) -> List[AdvancedAbility]:
        """Получить все разблокированные способности"""
        return [
            self.abilities[ability_id]
            for ability_id in self.player_abilities
            if ability_id in self.abilities
        ]


# Глобальный менеджер
advanced_abilities_manager = AdvancedAbilitiesManager()


def get_advanced_ability(ability_id: str) -> Optional[AdvancedAbility]:
    """Получить продвинутую способность по ID"""
    return advanced_abilities_manager.get_ability(ability_id)


def get_abilities_for_level(level: int) -> List[AdvancedAbility]:
    """Получить способности для уровня"""
    return advanced_abilities_manager.get_abilities_for_level(level)


def get_abilities_by_type(ability_type: str) -> List[AdvancedAbility]:
    """Получить способности по типу"""
    return advanced_abilities_manager.get_abilities_by_type(ability_type)
