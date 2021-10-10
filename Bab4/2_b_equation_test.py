# Equation Function

from fractions import Fraction  # untuk mengkonversi fraction 1/2 menjadi float


def equation(a, b, c, d):  # Penyelesaian persamaan ax + b = cx + d
    return (d-b)/(a-c)


a = float(Fraction(input("Masukkan nilai a dari persamaan ax + b = cx + d >>> ")))
b = float(Fraction(input("Masukkan nilai b dari persamaan ax + b = cx + d >>> ")))
c = float(Fraction(input("Masukkan nilai c dari persamaan ax + b = cx + d >>> ")))
d = float(Fraction(input("Masukkan nilai d dari persamaan ax + b = cx + d >>> ")))
print(
    f"Nilai x  {equation(a, b, c, d)}")
x = equation(a, b, c, d)
print("Persamaan  ax + b = cx + d >>> ")
print(
    f"\nPersamaan {Fraction(a)}*{x} + {Fraction(b)m}= {Fraction(c)}*{x} + {Fraction(d)} ")
print(f"\nSehingga >>> {a*x} + {b}= {c*x} + {d} ")

# Periksa dengan memasukkan nilai equation (1/2,2/3,1/5,7/8) nilai x adalah 0.6944444444444446
# Rieuuuut.... :D
