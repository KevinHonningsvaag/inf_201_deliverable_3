import pytest

from game.battle import Battle
from game.character import Character, Mage, Warrior


def test_warrior_vs_mage() -> None:
    """Test that a warrior and mage can complete a battle."""
    hero = Warrior("Isildur")
    enemy = Mage("Sauron")

    battle = Battle(hero, enemy)
    battle.simulate_battle()

    assert not (hero.is_alive and enemy.is_alive)


def test_battle_initialization() -> None:
    """Test that a battle stores both characters."""
    hero = Character("Isildur")
    enemy = Character("Sauron")

    battle = Battle(hero, enemy)

    assert battle.hero is hero
    assert battle.enemy is enemy


def test_enemy_does_not_attack_when_defeated() -> None:
    """Test that a defeated enemy cannot attack back."""

    hero = Character("Isildur")
    enemy = Character("Orc", hp_max=1)

    battle = Battle(hero, enemy)
    battle.play_round()

    assert enemy.hp == 0
    assert hero.hp == 100


def test_battle_ends_when_one_character_dies() -> None:
    """Test that the battle ends when one character dies."""
    hero = Character("Isildur")
    enemy = Character("Orc", hp_max=1)

    battle = Battle(hero, enemy)
    battle.simulate_battle()

    assert hero.is_alive
    assert not enemy.is_alive


def test_battle_ends_after_100_rounds(capsys: pytest.CaptureFixture[str]) -> None:
    """A battle ends in a draw when both are alive after 100 turns"""
    hero = Warrior("Isildur", armor=100)
    enemy = Warrior("Orc", armor=100)

    Battle(hero, enemy).simulate_battle()

    output = capsys.readouterr().out
    assert output.count("========== Round ") == 100
    assert "Round 100" in output
    assert "turn limit reached" in output
    assert hero.is_alive and enemy.is_alive
