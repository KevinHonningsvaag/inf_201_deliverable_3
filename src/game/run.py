from game.battle import Battle
from game.character import Mage, Warrior
from game.items import Weapons


def main() -> None:
    sword = Weapons("sword", 20)
    spear = Weapons("spear", 15)
    hero = Warrior("Hero", sword)
    enemy = Mage("Enemy", spear)
    Battle(hero, enemy).simulate_battle()


if __name__ == "__main__":
    main()
