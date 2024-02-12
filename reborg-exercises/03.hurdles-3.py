import random


def jump():
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()


def turn_right():
    turn_left()


while at_goal() == False:
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
