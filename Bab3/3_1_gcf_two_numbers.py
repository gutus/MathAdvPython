# Gratest Commn factor/ FPB (Faktor Persekutuan Besar)

def gcf(a, b):
    if(b == 0):
        return a
    else:
        return gcf(b, a % b)


a = int(input("Masukkan bilangan pertama >>> "))
b = int(input("Masukkan bilangan kedua >>> "))

fpb = gcf(a, b)
print(f"Angka pertama {a}, angka kedua {b} \nFPB kedua angka adalah {fpb}")
