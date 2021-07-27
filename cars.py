from turtle import Turtle
from colors import color_list
import random

SPEED = 5

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(color_list))
        self.setheading(180)
        self.set_starting_point()

    def set_starting_point(self):
        start_x = 300
        start_y = random.randint(-280, 280)
        self.goto(start_x, start_y)

    def move(self):
        new_x = self.xcor() - SPEED
        self.goto(new_x, self.ycor())



