def sum_two_max(arg):
    arg.remove(min(arg))
    return arg[0] + arg[1]


lst_args = []
print('Введите 3 числа.')
for i in range(3):
    lst_args.append('')
    lst_args[i] = int(input(f'{i + 1} число = '))
print('Вы ввели : ', lst_args)
print('Сумма наибольших двух = ', sum_two_max(lst_args))
