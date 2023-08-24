"""
Задание №6
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
"""


class Rectangle:

    def __init__(self, side_a, side_b=0):
        self.side_a = side_a
        if side_b == 0:
            side_b = side_a
        self.side_b = side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

    def get_area(self):
        return self.side_a * self.side_b

    def __add__(self, other):
        res = self.get_perimeter() + other.get_perimeter()
        return Rectangle(res)

    def __sub__(self, other):
        res = abs(self.get_perimeter() - other.get_perimeter())
        return Rectangle(res)

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def print_info(self):
        print(f'Сторона a: {self.side_a}')
        print(f'Сторона b: {self.side_b}')
        print(f'Периметр: {self.get_perimeter()}')
        print(f'Площадь: {self.get_area()}')


if __name__ == '__main__':
    rectangle1 = Rectangle(7.3)
    rectangle1.print_info()

    rectangle2 = Rectangle(5.6, 10.2)
    rectangle2.print_info()

    print(f'({rectangle1.get_area():.2f} == {rectangle2.get_area():.2f}):', rectangle1 == rectangle2)
    print(f'({rectangle1.get_area():.2f} != {rectangle2.get_area():.2f}):', rectangle1 != rectangle2)
    print(f'({rectangle1.get_area():.2f} > {rectangle2.get_area():.2f}):', rectangle1 > rectangle2)
    print(f'({rectangle1.get_area():.2f} <= {rectangle2.get_area():.2f}):', rectangle1 <= rectangle2)
    print(f'({rectangle1.get_area():.2f} < {rectangle2.get_area():.2f}):', rectangle1 < rectangle2)
    print(f'({rectangle1.get_area():.2f} >= {rectangle2.get_area():.2f}):', rectangle1 >= rectangle2)