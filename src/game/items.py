# Game items
# Authors Kevin Honningsvåg and Herman Nordstrand


class Weapons:
    def __init__(self, name: str, damage: int) -> None:
        if damage < 2:
            raise ValueError("damage needs to be atleast two to avoid conflict with Dice")
        self.name = name
        self.damage = damage
