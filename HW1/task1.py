import math

print("Введите коэффициенты для квадратного уравнения")
print("Формат квадратного уравнения: ax^2 - bx - c = 0 ")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

disc = b ** 2 - 4 * a * c
print(disc)

if disc > 0:
    x1 = ((-b + math.sqrt(disc)) / (2 * a))
    x2 = ((-b - math.sqrt(disc)) / (2 * a))
    print(f"x1 = {x1}, x2 = {x2}")
elif disc == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    print("В этом квадратном уравнении корней нет")