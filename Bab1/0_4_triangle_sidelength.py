from turtle import *
shape('turtle')
speed(1)


def triangle(sidelength=120):
    for i in range(3):
        forward(sidelength)
        right(180-60)


panjang_sisi_segitiga = int(input("Masukkan panjang sisi segitiga >>>  "))
triangle(panjang_sisi_segitiga)
