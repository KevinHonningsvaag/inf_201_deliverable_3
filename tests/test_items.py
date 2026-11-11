from game.items import Weapons


def test_weapon_initialization() -> None:
    sword = Weapons("sword", 20)

    assert sword.name == "sword"
    assert sword.damage == 20
