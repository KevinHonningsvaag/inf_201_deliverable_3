from game.character import Warrior


def test_warrior_initialization() -> None:
    """Test that a warrior is initialized correctly."""

    warrior = Warrior("Gimli")

    assert warrior.name == "Gimli"
    assert warrior.hp == 150
    assert warrior.armor == 5
    assert warrior.is_alive

def test_warrior_armor() -> None:
    """Test that armor protects against damage."""

    warrior = Warrior("Gimli", armor=5)

    warrior.take_damage(4)

    assert warrior.hp == 150