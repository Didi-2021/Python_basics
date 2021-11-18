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
                mat_c.append(random.randint(0, 100))
            mat.append(mat_c)
            mat_c = []
        self.m = mat

    def __str__(self):
        for i in range(self.r):
            print(self.m[i])

    def __add__(self, other):
        mat_c = []
        mat = []
        for i in range(self.r):
            for k in range(self.c):
                mat_c.append(self.m[i][k] + other.m[i][k])
            mat.append(mat_c)
            mat_c = []
        return mat


mat_1 = Matrix(3, 5)
mat_1.__str__()
print()
mat_2 = Matrix(3, 5)
mat_2.__str__()
print()
print(mat_1 + mat_2)
