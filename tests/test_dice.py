from game.dice import Dice


def test_default_sides():
    dice = Dice()
    assert dice.sides == 6


def test_custom_sides():
    dice = Dice(20)
    assert dice.sides == 20


def test_roll_within_range():
    dice = Dice(6)

    for _ in range(100):
        result = dice.roll()
        assert isinstance(result, int)
        assert 1 <= result <= 6
