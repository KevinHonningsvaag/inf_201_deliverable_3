import random


class Dice:
    def __init__(self, sides: int = 6) -> None:
        """
        Initialise the dice

        Args:
            sides (int) : how many sides does the dice have
        """
        if sides < 2:
            raise ValueError("Dice must have atleast 2 sides")
        self.sides = sides

    def roll(self) -> int:
        """Rolls the dice and makes it land on a random side"""
        return random.randint(1, self.sides)

    def __repr__(self) -> str:
        """Representation of dice object"""
        return f"Dice(sides = {self.sides})"

    def __call__(self) -> int:
        """Make the diceroll happen"""
        return self.roll()
