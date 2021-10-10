# Brute Force Guess Number
# Menggunakan while untuk mencoba satusatu sampai didapat value yg sesuai dengan persamaan

print("Persamaan yang akan dicari nilaix nya >>> 2x+5=13")


def tebak():
    x = -100  # Angka awal yg diiterate dari -100
    while x < 100:
        if 2*x + 5 == 13:  # Detail persamaan 2x = 2*x
            print(f"Nilai x adalah >>> {x}")
        x += 1  # Ditambahkan 1 untuk diiterate dengan nilai baru sampai ditemukan nilai x yg pas


tebak()  # Memanggil  fungsi tebak
