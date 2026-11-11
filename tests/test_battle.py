from game.battle import Battle
from game.character import Mage, Warrior


hero = Warrior("Isildur")
enemy = Mage("Sauron")

battle = Battle(hero, enemy)
battle.simulate_battle()
