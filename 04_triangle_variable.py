# TRIANGLE TURTLE WITH VARIABLE
from turtle import *

shape('turtle')
speed(1)


def triangle(sidelength):
    for i in range(6):
        forward(sidelength)
        right(120)


triangle(200)
