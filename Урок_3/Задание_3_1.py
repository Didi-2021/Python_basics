def division(arg):
    try:
        result = str(arg[0]) + ' / ' + str(arg[1]) + ' = ' + str(arg[0] / arg[1])
    except ZeroDivisionError:
        result = 'Ошибка. На ноль делить нельзя.'
    return result


lst_args = [int(input('Введите делимое : ')), int(input('Введите делитель : '))]
print(division(lst_args))
