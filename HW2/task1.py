from math import sqrt

a, b, c = 1, -6, 13

d = b ** 2 - 4 * a * c
if d < 0:
    sqrt_d = sqrt(abs(d))
    print(f"Дискриминант: {d}; x1 = {-b / (2 * a)} + {sqrt_d / (2 * a)}i; x1 = {-b / (2 * a)} - {sqrt_d / (2 * a)}i")
elif d == 0:
    x = -b / (2 * a)
    print(f"Дискриминант: {d}; x = {x}")
else:
    x1 = (-b + d ** (1 / 2)) / (2 * a)
    x2 = (-b - d ** (1 / 2)) / (2 * a)
    print(f"Дискриминант: {d}; x1 = {x1}; x2 = {x2}")