# Object-oriented game simulator
# Kevin Honningsvåg and Herman Nordstrand, NMBU, 2026
# Credits to Turid Torheim

from __future__ import annotations

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
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        if weapon is None:
            self.damage = base_damage
        else:
            self.damage = weapon.damage

    def attack(self, target: Character) -> None:
        """Attack and deal damage to target character"""
        target.take_damage(self.damage)

    def take_damage(self, damage: int) -> None:
        self._hp -= Dice(damage).roll()
        self._hp = max(self._hp, 0)  # Target hp cannot end up lower than 0

    def heal(self, heal: int) -> None:
        """Character recovers hitpoints from healing"""
        self._hp += heal
        self._hp = min(self._hp, self.hp_max)  # Target hp cannot end up higher than hp_max

    def introduce(self) -> None:
        """Creates string that introduces character"""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>)"

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
        self, name: str, weapon: Weapons | None = None, hp_max: int = 150, base_damage: int = 10, armor: int = 5
    ) -> None:
        super().__init__(name=name, weapon=weapon, hp_max=hp_max, base_damage=base_damage)
        self.armor = armor

    def take_damage(self, damage: int) -> None:
        """Reduce incoming damage by armor."""

        if damage <= 0:
            return

        if damage == 1:
            rolled_damage = 1
        else:
            rolled_damage = Dice(damage).roll()

        reduced_damage = max(rolled_damage - self.armor, 0)
        self._hp = max(self._hp - reduced_damage, 0)


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
        self.base_damage = base_damage
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target: Character) -> None:
        """Use magic if enough mana is available, otherwise attack normally."""
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(self.base_damage * 2)  # Mana attack deals double damage

        else:
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)  # Regenerates mana when using base attack
