import random


def jump():
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()


def turn_right():
    turn_left()


for x in range(1, 7):
    move()
    turn_left()
    move()
    jump()
    turn_right()

