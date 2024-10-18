from random import *

class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_dice(self):
        return randint(1,self.sides)
        


dice = Die(6)
for i in range(10):
    print(f"Roll dice {dice.roll_dice()}")

dice2 = Die(10)
for i in range(20):
    print(f"Roll dice {dice2.roll_dice()}")


