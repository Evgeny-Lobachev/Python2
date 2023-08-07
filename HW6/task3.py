from random import randint


def valid_queens(positions):
    for i in range(8):
        for j in range(i + 1, 8):
            if positions[i] == positions[j] \
                    or positions[i] - i == positions[j] - j \
                    or positions[i] + i == positions[j] + j:
                return False
    return True


pos_x = [el for el in range(1, 9)]
pos_y = [randint(1, 9) for el in range(1, 9)]
pos_y_exist = [2, 5, 7, 1, 3, 8, 6, 4]  

if __name__ == '__main__':
    print(f"{pos_x} - Расстановка по Х \n{pos_y} - Расстановка по Y")
    dct = sorted({pos_x[el-1]: pos_y[el-1] for el in range(1, 9)}.items())
    print(dct)
    print(valid_queens(pos_y))