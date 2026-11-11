# Object-oriented game simulator
# Kevin Honningsvåg and Herman Nordstrand, NMBU, 2026
# Credits to Turid Torheim

from __future__ import annotations

from typing import override

from game.dice import Dice
from game.items import Weapons


class Character:
    """Represents a character in the RPG"""

    def __init__(
        self,
        name: str,
        weapon: Weapons | None = None,
        hp_max: int = 100,
        base_damage: int = 10,
    ) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
        """
        self.name: str = name
        self._hp: int = hp_max  # Note: _hp indicated private attribute
        self.hp_max: int = hp_max
        if weapon is None:
            self.damage: int = base_damage
        else:
            self.damage = weapon.damage

        if base_damage < 2:
            raise ValueError("base_damage needs to be atleast 2 to avoid Dice conflict")
        if hp_max <= 0:
            raise ValueError("hp_max needs to be above 0")

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(Dice(self.damage).roll())

    def take_damage(self, damage: int) -> None:
        if damage < 0:
            raise ValueError("cannot take negative damage")
        self._hp -= damage
        self._hp = max(self._hp, 0)  # Target hp cannot end up lower than 0

    def heal(self, heal: int) -> None:
        """Character recovers hitpoints from healing"""
        if heal < 0:
            raise ValueError("heal cannot be negative")
        self._hp += heal
        self._hp = min(self._hp, self.hp_max)  # Target hp cannot end up higher than hp_max

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    @override
    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

    @override
    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp

    @property
    def is_alive(self) -> bool:
        """Returns if the character is alive or not"""
        return self._hp > 0


class Warrior(Character):
    """Represents a warrior character."""

    def __init__(
        self,
        name: str,
        weapon: Weapons | None = None,
        hp_max: int = 150,
        base_damage: int = 10,
        armor: int = 5,
    ) -> None:
        super().__init__(name=name, weapon=weapon, hp_max=hp_max, base_damage=base_damage)
        self.armor: int = armor
        if armor < 0:
            raise ValueError("armor need to be positive")

    @override
    def take_damage(self, damage: int) -> None:
        """Reduce incoming damage by armor."""
        if damage < 0:
            raise ValueError("cannot take negative damage")

        reduced_damage = max(damage - self.armor, 0)
        super().take_damage(reduced_damage)


class Mage(Character):
    """Represents a mage character."""

    def __init__(
        self,
        name: str,
        weapon: Weapons | None = None,
        hp_max: int = 100,
        base_damage: int = 10,
        mana: int = 30,
        mana_max: int = 30,
    ) -> None:
        super().__init__(name, weapon, hp_max, base_damage)
        self.base_damage: int = base_damage
        self.mana: int = mana
        self.mana_max: int = mana_max

        if not 0 <= mana <= mana_max:
            raise ValueError("mana requirement: 0 <= mana <= mana_max")

    @override
    def attack(self, target: Character) -> None:
        """Use magic if enough mana is available, otherwise attack normally."""
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(Dice(self.base_damage).roll() * 2)  # Mana attack deals double damage

        else:
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)  # Regenerates mana when using base attack
