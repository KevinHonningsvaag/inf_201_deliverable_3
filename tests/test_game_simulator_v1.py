from inf_201_deliverable_3.game_simulator_v1 import Character


def test_take_damage():
    character = Character("Hero", hp_max=100)
    character.take_damage(30)

    assert character.hp == 70


def test_hp_cannot_be_negative():
    character = Character("Hero", hp_max=100)
    character.take_damage(150)

    assert character.hp == 0


def test_heal():
    character = Character("Hero", hp_max=100)
    character.take_damage(50)
    character.heal(20)

    assert character.hp == 70


def test_heal_cannot_exceed_hp_max():
    character = Character("Hero", hp_max=150)
    character.take_damage(10)
    character.heal(50)

    assert character.hp == 150


def test_attack_only_damages_target():
    attacker = Character("Attacker", damage=20)
    target = Character("Target")

    attacker.attack(target)

    assert target.hp == 80
    assert attacker.hp == 100
