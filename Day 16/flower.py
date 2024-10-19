import turtle

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.speed('slowest')


def is_even(n):
    return n % 2 == 0


for i in range(6):
    for j in range(360):
        if is_even(i):
            timmy.color("violet")
        else:
            timmy.color("coral")
        timmy.forward(1)
        timmy.left(1)
    timmy.left(60)
timmy.color("darkgreen")
timmy.right(90)
timmy.forward(300)
