def my_func(arg1, arg2):
    res = 1 / arg1
    if arg2 != -1:
        for i in range(abs(arg2) - 1):
            res = res / arg1
    return res


x = float(input('Введите х = '))
y = int(input('Введите y = '))
print(f'{x} в степени {y} = ', my_func(x, y))
