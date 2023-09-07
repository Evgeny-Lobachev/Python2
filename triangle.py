import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('HW15//triangle_app.log', encoding='utf-8')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def check_triangle(a, b, c):

    if a + b <= c or a + c <= b or b + c <= a:
        logger.error("Треугольник не существует")
    elif a <= 0 or b <= 0 or c <= 0:
        logger.error("Стороны треугольника должны быть больше нуля")
    else:
        logger.info("Треугольник существует")
        if a == b == c:
            print("Равносторонний")
        elif a == b or a == c or b == c:
            print("Равнобедренный")
        else:
            print("Разносторонний")


def main():
    parser = argparse.ArgumentParser(description="Проверка типа треугольника")
    parser.add_argument("a", type=int, help="Длина стороны a")
    parser.add_argument("b", type=int, help="Длина стороны b")
    parser.add_argument("c", type=int, help="Длина стороны c")
    args = parser.parse_args()

    check_triangle(args.a, args.b, args.c)


if __name__ == "__main__":
    main()