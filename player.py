from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_Y = -200


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(self.xcor(), STARTING_Y)
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

