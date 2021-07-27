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
cars = []
start_cars = []
new_cars = []
game_is_on = True

def starting_cars():
    start_cars_list = []
    for i in range(10):
        start_cars_list.append(Car())

        for car in start_cars:
            car.random_location()
        return start_cars_list


cars += starting_cars()

screen.listen()
screen.onkey(player.move, "space")

while game_is_on:
    sleep(0.3)
    screen.update()

    for i in range(random.randint(0, 1)):
        new_cars.append(Car())
        new_cars[i].set_starting_point()

    cars += new_cars
    new_cars = []

    print(cars)

    for car in cars:
        car.move()

    for i in range(len(cars)):
        if cars[i].xcor() < -300:
            cars[i].clear()
            cars = cars[i:]
            break




screen.exitonclick()