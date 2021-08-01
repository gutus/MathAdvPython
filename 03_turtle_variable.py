# SQUARE TURTLE WITH VARIABLE
from turtle import *

shape('turtle')
speed(1)


def square(sidelength):
    for i in range(60):
        right(5)  # geser 5 derajat
        forward(sidelength)
        right(90)


square(50)
