def my_func(arg1, arg2):
    res = arg1 ** arg2
    return res


x = float(input('Введите х = '))
y = int(input('Введите y = '))
print(f'{x} в степени {y} = ', my_func(x, y))
