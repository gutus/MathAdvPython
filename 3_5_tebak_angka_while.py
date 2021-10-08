# Tebak Angka dengan While
# Selama tebakan belumbenar, akan terus di loop, dan hanya break jika tebakannya benar

from random import randint


def salam():
    nama = input("Hai, nama kamu siapa? ")
    print(f"Hai {nama}, selamat datang di game tebak angka :D ")


salam()


number = randint(1, 100)  # angka acak antara 1 hingga 100
guess = int(
    input("Masukkan angka tebakan anda antara 1 hingga 100 >>>  "))
while guess:
    if guess == number:
        print(f"Tebakan {guess} benar!")
        break
    elif guess > number:
        print(f"Tebakanmu {guess} terlalu tinggi")
    else:
        print(f"Tebakanmu {guess} terlalu rendah")
    guess = int(
        input("Masukkan angka tebakan anda antara 1 hingga 100 >>>  "))
