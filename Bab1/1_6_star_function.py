from turtle import *
shape('turtle')
speed(1)
length_side = int(input("Masukkan panjang sisi bintang >>>"))


def star():
    for i in range(5):
        forward(length_side)
        right(144)


star()
