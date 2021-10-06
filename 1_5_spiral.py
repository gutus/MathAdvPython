from turtle import *
shape('turtle')
speed(100)


def square():
    initial_length = 5
    for i in range(180):
        right(5)
        forward(initial_length)
        right(90)
        forward(initial_length)
        right(90)
        forward(initial_length)
        right(90)
        forward(initial_length)
        right(90)

        initial_length += 5


square()
