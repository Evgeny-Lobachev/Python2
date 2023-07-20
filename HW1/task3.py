number = int(input("Введите число в диапазоне от 0 до 100000: "))
count = 0

if number < 0 or number > 100000:
    print("Вы ввели некорректное число")
elif number == 0 or number == 1:
    print(f"Число {number} не является ни простым, ни составным")
else:
    for i in range(2, number + 1):
        if number % i == 0:
            count += 1
    if count == 1:
        print(f"Число {number} является простым")
    else:
        print(f"Число {number} является составным")