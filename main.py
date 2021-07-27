from turtle import Screen
from player import Player
from cars import Car
from time import sleep
import random

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Cross")
screen.tracer(0)

player = Player()
car = Car()
cars = []
game_is_on = True

screen.listen()
screen.onkey(player.move, "space")

while game_is_on:
    sleep(0.3)
    screen.update()

    # for i in range(random.randint(0, 4)):
    #     cars.append(Car())
    car.move()


screen.exitonclick()