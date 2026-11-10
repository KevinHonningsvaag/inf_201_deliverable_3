from game.character import Mage
from game.character import Warrior

def test_mage_initialization() -> None:
    """Test that a mage is initialized correctly."""

    mage = Mage("Harry")

    assert mage.name == "Harry"
    assert mage.hp == 100
    assert mage.mana == 30
    assert mage.is_alive

def test_mage_magic_attack() -> None:
    """Test that magical attacks consume mana and damage the enemy."""

    mage = Mage("Harry")
    enemy = Warrior("Orc")

    mage.attack(enemy)

    assert mage.mana == 20
    assert 80 <= enemy.hp <= 99

def test_mage_normal_attack() -> None:
    """Test that Mage uses a normal attack when mana is low."""

    mage = Mage("Harry", mana=5)
    enemy = Warrior("Orc")

    mage.attack(enemy)

    assert mage.mana == 10  # Fill in expected mana
    assert ...               # Check that enemy lost HP