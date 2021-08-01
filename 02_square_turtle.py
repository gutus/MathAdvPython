# SQUARE TURTLE
from turtle import *

shape('turtle')
speed(2)


def square():
    for i in range(60):
        right(5)  # geser 5 derajat
        forward(200)
        right(90)


square()
