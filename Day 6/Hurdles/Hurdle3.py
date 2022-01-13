def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump_wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def jump():
    if front_is_clear():
        move()
    else:
        jump_wall()


while at_goal() != True:
    jump()
