# Tebak Angka

from random import randint


def tebakAngka():
    tebakan = int(
        input("Masukkan angka tebakan anda antara 1 hingga 100 >>>  "))
    angkaAcak = randint(1, 100)  # angka acak antara 1 hingga 100
    print(f"Angka acak pilihan komputer {angkaAcak}\n")
    print(f"Angka pilihanmu {tebakan}\n")
    if tebakan == angkaAcak:
        print("Tebakan kamu benar!")
    elif tebakan > angkaAcak:
        print("Tebakanmu terlalu tinggi")
    else:
        print("Tebakanmu terlalu rendah")


tebakAngka()
