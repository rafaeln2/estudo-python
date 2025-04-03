import random

class Dice:
    def roll(self):
        diceroll = (random.randint(1, 6), random.randint(1, 6))
        return diceroll

dice = Dice()
print("Rolling the dice...")
print(f"You rolled: {dice.roll()}")
