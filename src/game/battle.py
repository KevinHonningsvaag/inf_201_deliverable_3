from game.character import Character

class Battle:
    """Represents a battle between two characters"""

    def __init__(
        self,
        hero: Character,
        enemy: Character
    ) -> None:
        """
        choose two characters to battle each other
        """
        self.hero = hero
        self.enemy = enemy
    
    def play_round(self)->None:
        """simulates one round of battle between hero and enemy"""

        if self.hero.is_alive and self.enemy.is_alive:
            enemy_hp_before = self.enemy.hp
            self.hero.attack(self.enemy)

            print(f"{self.hero.name} attacks {self.enemy.name}!")

            damage_dealt = enemy_hp_before - self.enemy.hp

            print(f"{self.hero.name} deals {damage_dealt} damage to {self.enemy.name}!")
            print(f"{self.enemy.name} has {self.enemy.hp} HP remaining.")

            if self.enemy.is_alive:
                hero_hp_before = self.hero.hp
                self.enemy.attack(self.hero)
                damage_dealt = hero_hp_before - self.hero.hp

                print(f"{self.enemy.name} deals {damage_dealt} damage to {self.hero.name}!")
                print(f"{self.hero.name} has {self.hero.hp} HP remaining.")

    def simulate_battle(self) -> None:
    """Simulate a battle until one character dies."""

    round_number = 1

    print(f"\nBattle: {self.hero.name} vs {self.enemy.name}")

    while self.hero.is_alive and self.enemy.is_alive:
        print(f"\n========== Round {round_number} ==========")

        self.play_round()
        round_number += 1

    if self.hero.is_alive:
        print(f"\n{self.hero.name} wins the battle!")
    elif self.enemy.is_alive:
        print(f"\n{self.enemy.name} wins the battle!")
    else:
        print("\nNo winner!")

