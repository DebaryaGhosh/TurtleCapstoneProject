from turtle import Turtle
from colors import color_list
from player import Player
import random

SPEED = 10
CRASH_DISTANCE = 20

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(color_list))
        self.setheading(180)

    def set_starting_point(self):
        start_x = random.randint(300, 1000)
        start_y = random.randint(-280, 280)
        self.goto(start_x, start_y)

    def move(self):
        new_x = self.xcor() - SPEED
        self.goto(new_x, self.ycor())

    def random_location(self):
        x_pos = random.randint(-300, 300)
        y_pos = random.randint(-200, 240)
        self.goto(x_pos, y_pos)

    def check_game_over(self, player):
        if self.distance(player) < CRASH_DISTANCE:
            return True
        else:
            return False



