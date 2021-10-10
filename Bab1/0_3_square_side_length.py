from turtle import *
shape('turtle')
speed(2)


# 100 sebagai default value jika kita lupa memanggil square tanpa memasukkan value
def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)


panjang_sisi = int(input("Masukkan panjang sisi persegi >>> "))
square(panjang_sisi)
