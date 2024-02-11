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


at_goal() == False

while at_goal() == False:
    move()
    turn_left()
    move()
    jump()
    turn_right()

