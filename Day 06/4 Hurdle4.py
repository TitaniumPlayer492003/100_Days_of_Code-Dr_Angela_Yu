def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif not front_is_clear():
        turn_left()