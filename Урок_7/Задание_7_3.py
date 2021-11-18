class Cell:
    numbers = int

    def __init__(self, arg):
        self.numbers = arg

    def __add__(self, other):
        return Cell(self.numbers + other.numbers)


c_1 = Cell(10)
print(f'Ячеек в клетке {c_1.numbers}')
c_2 = Cell(5)
print(f'Ячеек в клетке {c_2.numbers}')
print('Сумма клеток : ', (c_1 + c_2).numbers)
