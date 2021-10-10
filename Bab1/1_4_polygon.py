from turtle import *
shape('turtle')
speed(2)
side_number = int(input("Masukkan jumlah sisi polygon >>> "))


def polygon():
    for i in range(side_number):
        forward(200)
        right(360/side_number)


polygon()
