# Quadratic Formula
# Untuk menyelesaikan persamaan kuadrat a*x**2 + bx + c = 0 >>> ax kuadrat + bx + c = 0
# Menggunakan rumus x = (-b + sqrt(b**2 - 4*a*c))/(2*a)
# Menggunakan rumus x = (-b - sqrt(b**2 - 4*a*c))/(2*a)

from math import sqrt  # Mengimpor fungsi square root untuk mencari nilai akar kuadrat


def quad(a, b, c):
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return [x1, x2]  # Supaya gampang dislice kita return sebagai list


a = int(input("Masukkan nilai a  dari persamaan ax**2 + bx + c = 0 >>> "))
b = int(input("Masukkan nilai b  dari persamaan ax**2 + bx + c = 0 >>> "))
c = int(input("Masukkan nilai c  dari persamaan ax**2 + bx + c = 0 >>> "))

print(quad(a, b, c))
# Buffer variabel untuk menyimpan sementara hasil list menjadi variabel hasil
hasil = quad(a, b, c)
x1 = hasil[0]  # Slicing indeks 0 untuk mendapat x pertama >> x1
x2 = hasil[1]  # Slicing indeks 1 untuk mendapat x kedua >> x2
print(f"Untuk nilai x1 = {x1} adalah sbb >>")
print(f"Persamaan kuadrat dari {a}*{x1}**2 + ({b}*{x1}) + ({c}) = 0")
print(f"Persamaan kuadrat dari {a*x1**2 + b*x1 + c } = 0")
print(f"Sedangkan untuk nilai x2 = {x2} adalah sbb >>")
print(f"Persamaan kuadrat dari {a}*{x2}**2 + ({b}*{x2}) + ({c}) = 0")
print(f"Persamaan kuadrat dari {a*x2**2 + b*x2 + c } = 0")
