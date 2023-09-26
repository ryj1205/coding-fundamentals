""" Dice App """
# Write a class called Dice
# When initialised the object will set how many faces the die has
# Create objects for 6, 20, 2 and 4 sided die.

# Import the random class:
import random

class Dice:

    """ Class for rolling the dice """

    def __init__(self, passedfaces):
        self.faces = passedfaces

    def roll(self):
        """ Return a random integer between 1 and how many faces the dice has """
        return random.randint(1, self.faces)

two_sides = Dice(2)
print("Two sided roll: {}".format(two_sides.roll()))

four_sides = Dice(4)
print("Four sided roll: {}".format(four_sides.roll()))

six_sides = Dice(6)
print("Six sided roll: {}".format(six_sides.roll()))

twenty_sides = Dice(20)
print("Twenty sided roll: {}".format(twenty_sides.roll()))
