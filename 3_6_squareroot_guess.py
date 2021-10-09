# Square Root Guess

def rata_rata(a, b):
    return (a+b)/2


def squareRoot(num, lo, hi):
    for i in range(20):
        tebak = rata_rata(lo, hi)
        if tebak ** 2 == num:
            print(tebak)
        elif tebak ** 2 > num:
            hi = tebak
        else:
            lo = tebak
    print(tebak)


angka = int(input("Masukkan angka bulat yang akan dicari akar kuadratnya >>>  "))
bawah = int(input("Masukkan angka tebakan perkiraan kuadrat sisi rendah >>>  "))
atas = int(input("Masukkan angka tebakan perkiraan kuadrat sisi tinggi >>>  "))
squareRoot(angka, bawah, atas)
