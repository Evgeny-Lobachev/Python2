class Matrix:


    def __init__(self, matrix):

        self.matrix = matrix

    def __str__(self):

        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __eq__(self, other):

        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return False

    def __add__(self, other):

        if isinstance(other, Matrix):
            if len(self.matrix) == len(other.matrix) and len(self.matrix[0]) == len(other.matrix[0]):
                result = [[0 for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))]
                for i in range(len(self.matrix)):
                    for j in range(len(self.matrix[0])):
                        result[i][j] = self.matrix[i][j] + other.matrix[i][j]
                return Matrix(result)
            else:
                raise ValueError("Матрицы должны иметь одинаковые размеры!")
        else:
            raise TypeError("Можно складывать только две матрицы!")

    def __mul__(self, other):
       
        if isinstance(other, Matrix):
            if len(self.matrix[0]) == len(other.matrix):
                result = [[0 for j in range(len(other.matrix[0]))] for i in range(len(self.matrix))]
                for i in range(len(self.matrix)):
                    for j in range(len(other.matrix[0])):
                        for k in range(len(other.matrix)):
                            result[i][j] += self.matrix[i][k] * other.matrix[k][j]
                return Matrix(result)
            else:
                raise ValueError("Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы!")
        else:
            raise TypeError("Можно умножать только две матрицы!")



A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])


print("A:")
print(A)
print("B:")
print(B)


print("A == B:", A == B)
print("A == A:", A == A)


C = A + B
print("C = A + B:")
print(C)

D = A * B
print("D = A * B:")
print(D)