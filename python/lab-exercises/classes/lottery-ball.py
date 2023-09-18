## !! PLEASE NOTE THIS IS UNFINISHED !!

# Import the random class:
import random

###################################################################
# Goal: 
# Create a lottery ball, or Hat, that takes a variable number of arguments that specify 
# the number of balls of each color that are in the hat. 
# Give the object the ability to pick a random number of balls from the hat
# which will then be used to compute the probability of picking a certain distribution 
# of balls over a large number of experiments
###################################################################

class LotteryBall:

    def __init__(self):

        self.balls = []

    def select_balls(self, num_of_picks):

        picked_balls = random.sample(self.balls, num_of_picks)

###################################################################

hat = LotteryBall()

picked_balls = hat.pick_balls(10)

###################################################################

