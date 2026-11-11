from game.battle import Battle
from game.character import Mage, Warrior


def test_enemy_does_not_attack_when_defeated() -> None:
    """Test that a defeated enemy cannot attack back."""

    hero = Character("Isildur")
    enemy = Character("Orc", hp_max=1)

    battle = Battle(hero, enemy)
    battle.play_round()

    assert enemy.hp == 0
    assert hero.hp == 100