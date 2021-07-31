# Python for Math
# Python untuk menyelesaikan persamaan matematis dengan memanfaatkan library python
# Diambil dari buku MATH ADVENTURES WITH PYTHON
# AN ILLUSTRATED GUIDE TO EXPLORING MATH WITH CODE
# BY PETER FARRELL

import math


def f(x):
    return math.sqrt(x+3)-x+1


# iterate f(x) when f(0), f(1), f(math.sqrt(2)), f(math.sqrt(2)-1)
for x in [0, 1, math.sqrt(2), math.sqrt(2)-1]:
    print("f({: .3f})={: .3f}".format(x, f(x)))


print("\n\n\n\t Dengan Iterasi range f(x) dengan range x (1-5), kita bisa menggunakan lebih banyak sample point")
for x in range(0, 5):
    print("f({: .3f})={: .3f}".format(x, f(x)))
