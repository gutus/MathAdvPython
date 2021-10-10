from turtle import *
shape('turtle')
speed(100)


def starSpiral():
    length_side = int(input("Masukkan panjang sisi bintang >>>"))
    times = int(input("Berapa banyak bintang yang akan dibuat >>>"))
    for i in range(times):
        right(5)
        forward(length_side)
        right(144)
        forward(length_side)
        right(144)
        forward(length_side)
        right(144)
        forward(length_side)
        right(144)
        forward(length_side)
        right(144)
        length_side += 5


starSpiral()
