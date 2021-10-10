# Quadratic Formula
# Untuk menyelesaikan persamaan kuadrat a*x**2 + bx + c = 0 >>> ax kuadrat + bx + c = 0
# Menggunakan rumus x = (-b + sqrt(b**2 - 4*a*c))/(2*a)
# Menggunakan rumus x = (-b - sqrt(b**2 - 4*a*c))/(2*a)

from math import sqrt  # Mengimpor fungsi square root untuk mencari nilai akar kuadrat


def quad(a, b, c):
    x1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
    return x1, x2


a = int(input("Masukkan nilai a  dari persamaan ax**2 + bx + c = 0 >>> "))
b = int(input("Masukkan nilai b  dari persamaan ax**2 + bx + c = 0 >>> "))
c = int(input("Masukkan nilai c  dari persamaan ax**2 + bx + c = 0 >>> "))

print(quad(a, b, c))
x1 = {quad(a, b, c): 0}
print(f"Persamaan kuadrat dari {a}*{x1}**2 + {b} + {c} = 0")
