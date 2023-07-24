from fractions import Fraction

fr1 = input("Введите первую дробь: ")
fr2 = input("Введите вторую дробь: ")

numer1, dmin1 = map(int, fr1.split("/"))
numer2, dmin2 = map(int, fr2.split("/"))

f1 = Fraction(numer1, dmin1)
f2 = Fraction(numer2, dmin2)
print(f"\n*ПРОВЕРКА* Сумма дробей: {f1 + f2}, Произведение дробей: {f1 * f2} \n")

if dmin1 != dmin2:
    numer_sum = numer1 * dmin2 + numer2 * dmin1
    dmin_sum = dmin1 * dmin2
else:
    numer_sum = numer1 + numer2
    dmin_sum = dmin1

numer_prod = numer1 * numer2
dmin_prod = dmin1 * dmin2

print(f"Сумма дробей: {numer_sum}/{dmin_sum}")
print(f"Произведение дробей: {numer_prod}/{dmin_prod}")