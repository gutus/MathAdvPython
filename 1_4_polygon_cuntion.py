# POLYGON FUNCTION


from turtle import *

shape('turtle')
speed(1)

sisi = int(input("Masukkan jumlah sisi poligon yg anda inginkan>>> \t"))
panjang = int(input("Masukkan panjang sisi yg anda inginkan>>> \t"))

print("Berikut adalah contoh polygon yang anda inginkan: \n")


def polygon(sisi):
    for i in range(sisi):
        forward(panjang)
        right((360/int(sisi)))
        forward(panjang)


polygon(sisi)
