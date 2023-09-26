""" Goal: """
# Create a lottery ball, or Hat, that takes a variable number of arguments that specify the number
# of balls of each color that are in the hat. Give the object the ability to pick a random number
# of balls from the hat which will then be used to compute the probability of picking a certain
# distribution of balls over a large number of experiments.

import random

class LotteryBall:

    """ This class is a random lottery ball drawer, outputting numbers and their color ball. """

    def __init__(self, balls_list):
        self.balls = balls_list

    def draw(self, num_balls):

        """ Create a list of color-number pairs to draw from randomly """

        draw_list = []
        for color, number in self.balls.items():
            draw_list.extend([(color, number)] * number)
        drawn_balls = random.sample(draw_list, min(num_balls, len(draw_list)))
        return drawn_balls

balls = {"blue": 5, "green": 3, "orange": 2}
ball_drawer = LotteryBall(balls)

lottery_draw = ball_drawer.draw(8)
print(lottery_draw)
