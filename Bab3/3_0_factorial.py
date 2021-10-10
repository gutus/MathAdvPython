# FACTORIAL


def factorial(num):
    """ Menampilkan list faktorial dari sebuah angka"""
    factorList = []
    for i in range(1, num+1):
        if num % i == 0:
            factorList.append(i)
    return factorList


angka = int(input("Masukkan angka yang ingin didapatkan faktorialnya >> "))
d = factorial(angka)
print(
    f"Angka yang anda masukkan untuk diperiksa faktorialnya adalah >>> {angka}")
print(f"Faktorialnya >> > {d}")
