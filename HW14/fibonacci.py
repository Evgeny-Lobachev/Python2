import doctest

num = int(input("Введите число: "))


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(fibonacci(num)))


def fibonacci(n):

    if n < 0:
        return []
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


if __name__ == "__main__":
    num = int(input("Введите число: "))
    result = list(fibonacci(num))
    print(result)

if __name__ == "__main__":
    doctest.testmod()