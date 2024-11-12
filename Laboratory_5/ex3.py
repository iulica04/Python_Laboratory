# Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization.
# The class should provide methods to access elements (get and set methods) and some mathematical functions such as transpose,
# matrix multiplication and a method that allows iterating through all elements from a matrix an apply a
# transformation over them (via a lambda function).


class Matrix:
    def __init__(self, n, m):
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]
        self.n = n
        self.m = m

    def get(self, i, j):
        return self.matrix[i][j]

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def transpose(self):
        self.matrix = [[self.matrix[j][i] for j in range(self.n)] for i in range(self.m)]
        self.n, self.m = self.m, self.n

    def multiply(self, matrix):
        if self.m != matrix.n:
            print("Matrix multiplication is not possible: n and m must to be equal.")
            return None

        result = Matrix(self.n, matrix.m)

        for i in range(self.n):
            for j in range(matrix.m):
                result.set(i, j, sum(self.get(i, k) * matrix.get(k, j) for k in range(self.m)))

        return result

    def apply(self, transformation):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i, j, transformation(self.get(i, j)))

    def __str__(self):
        return '\n'.join([' '.join([str(self.get(i, j)) for j in range(self.m)]) for i in range(self.n)])

if __name__ == '__main__':
    matrix = Matrix(2, 2)
    matrix.set(0, 0, 10)
    matrix.set(0, 1, 20)
    matrix.set(1, 0, 30)
    matrix.set(1, 1, 40)
    print("Matrix 1:")
    print(matrix)
    print()


    matrix.transpose()
    print("Transpose of matrix 1:")
    print(matrix)
    print()


    matrix2 = Matrix(2, 2)
    matrix2.set(0, 0, 1)
    matrix2.set(0, 1, 2)
    matrix2.set(1, 0, 3)
    matrix2.set(1, 1, 4)
    print("Matrix 2:")
    print(matrix2)

    print("Matrix 1 * Matrix 2:")
    print(matrix.multiply(matrix2))
    print()


    matrix.apply(lambda x: x * 2)
    print("Matrix 1 * 2:")
    print(matrix)
    print()

    matrix.apply(lambda x: x + 1)
    print("Matrix 1 + 1:")
    print(matrix)
    print()

    matrix.apply(lambda x: x - 1)
    print("Matrix 1 - 1:")
    print(matrix)
    print()