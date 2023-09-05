import doctest

a = int(input("Введите длину стороны треугольника а: "))

b = int(input("Введите длину стороны треугольника b: "))

c = int(input("Введите длину стороны треугольника c: "))
if a + b > c and a + c > b and b + c > a:
    print("Такой треугольник существует: ")
    if a == b == c:
        print("Равносторонний.")
    if a == b or a == c or b == c:
        print("Равнобедренный.")
    else:
        print("Разносторонний.")
else:
    print("Такой треугольник не существует.")


def is_triangle(a, b, c):
   
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return 'Равносторонний.'
        elif a == b or a == c or b == c:
            return 'Равнобедренный.'
        else:
            return 'Разносторонний.'
    else:
        return 'Такой треугольник не существует.'


if __name__ == "__main__":
    a = int(input("Введите длину стороны треугольника а: "))
    b = int(input("Введите длину стороны треугольника b: "))
    c = int(input("Введите длину стороны треугольника c: "))
    result = is_triangle(a, b, c)
    print(result)

# Добавим следующий код в конец файла для запуска doctest:
if __name__ == "__main__":
    doctest.testmod()