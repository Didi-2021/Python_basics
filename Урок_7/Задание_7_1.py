import random


class Matrix:
    m = []
    r = int
    c = int

    def __init__(self, rows, columns):
        self.r = rows
        self.c = columns
        mat_c = []
        mat = []
        for i in range(self.r):
            for k in range(self.c):
                mat_c.append(random.randint(-90, 100))
            mat.append(mat_c)
            mat_c = []
        self.m = mat

    def __str__(self):
        for i in range(self.r):
            for k in range(self.c):
                s = str(self.m[i][k])
                print(s.center(5), end=' ')  # 5 взято для выравнивания при небольших значениях
            print()

    def __add__(self, other):
        temporary_matrix = Matrix(self.r, self.c)
        for i in range(self.r):
            for k in range(self.c):
                temporary_matrix.m[i][k] = self.m[i][k] + other.m[i][k]
        return temporary_matrix


mat_1 = Matrix(5, 10)
print(type(mat_1))
mat_1.__str__()
print()

mat_2 = Matrix(5, 10)
print(type(mat_2))
mat_2.__str__()
print()

mat_3 = mat_1 + mat_2
print(type(mat_3))
mat_3.__str__()
