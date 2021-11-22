class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


# a / b = c
try:
    a = int(input('Введите делимое '))
    b = int(input('Введите делитель '))
    res = a / b
except ZeroDivisionError:
    print('На НОЛЬ делить нельзя')
else:
    print(f'{a} / {b} = {res}')
finally:
    print('Программа завершена')
