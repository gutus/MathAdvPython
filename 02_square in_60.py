from turtle import *
shape('turtle')
speed(10)


def square():
    for i in range(160):
        forward(100)
        right(90)
        forward(100)
        right(90)
        right(5)


square()
