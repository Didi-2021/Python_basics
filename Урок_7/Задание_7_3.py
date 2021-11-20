import random


class Cell:
    numbers = int
    s = str

    def __init__(self, arg):
        self.numbers = arg

    def __str__(self):
        print(f'ЯКлетка.{self.numbers}')

    def __add__(self, other):
        return Cell(self.numbers + other.numbers)

    def __sub__(self, other):
        if self.numbers > other.numbers:
            res = Cell(self.numbers - other.numbers)
        else:
            print('Нельзя вычитать')
            res = None
        return res

    def __mul__(self, other):
        return Cell(self.numbers * other.numbers)

    def __truediv__(self, other):
        return Cell(self.numbers // other.numbers)

    def make_order(self, row_cells):
        num = self.numbers
        while num > 0:
            if num - row_cells > 0:
                print('*' * row_cells + '\\n', end='')
                num -= row_cells
            elif num - row_cells == 0:
                print('*' * row_cells)
                num -= row_cells
            else:
                print('*' * num)
                num -= row_cells


def rnd():
    return random.randint(1, 100)


print('1 клетка  : ', end='')
c_1 = Cell(rnd())
c_1.__str__()

print('2 клетка  : ', end='')
c_2 = Cell(rnd())
c_2.__str__()

print('Сложение  : ', end='')
c_1add2 = c_1 + c_2
c_1add2.__str__()

print('Вычитание : ', end='')
c_1sub2 = c_1 - c_2
c_1sub2.__str__()

print('Умножение : ', end='')
c_1sub2 = c_1 * c_2
c_1sub2.__str__()

print('Деление   : ', end='')
c_1sub2 = c_1 / c_2
c_1sub2.__str__()

r_c = 6  # row_cells ячеек в ряду
print(f'\nКлетка под лупой (x{r_c}) ', end='')
print('1 клетка  : ', end='')
c_1.__str__()
c_1.make_order(r_c)
