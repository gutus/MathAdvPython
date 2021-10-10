# Equation Function
def equation(a, b, c, d):  # Penyelesaian persamaan ax + b = cx + d
    return (d-b)/(a-c)


a = int(input("Masukkan nilai a dari persamaan ax + b = cx + d >>> "))
b = int(input("Masukkan nilai b dari persamaan ax + b = cx + d >>> "))
c = int(input("Masukkan nilai c dari persamaan ax + b = cx + d >>> "))
d = int(input("Masukkan nilai d dari persamaan ax + b = cx + d >>> "))
print(
    f"Nilai x  {equation(a, b, c, d)}")
x = equation(a, b, c, d)
print("Persamaan  ax + b = cx + d >>> ")
print(f"\nPersamaan {a}*{x} + {b}= {c}*{x} + {d} ")
print(f"\nSehingga >>> {a*x} + {b}= {c*x} + {d} ")

# Periksa dengan memasukkan nilai equation (2,5,0,13) nilai x adalah 4.0
# Periksa dengan memasukkan nilai equation 12x+18= -34x +67 >>> (12,18,-34,67) nilai x adalah  1.065217391304348
