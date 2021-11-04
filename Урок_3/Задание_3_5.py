# На входе строка из чисел, разделенных пробелами. Для выхода спецсимвол "Е"
def my_func(arg):
    arg = str(arg)
    result_1 = 0
    result_2 = ''
    ext = True
    while ext:
        symbol_space = arg.find(' ')  # Индекс пробела в строке
        if symbol_space < 0:  # Проверить наличие следующего числа, с помощью наличия пробела
            if arg == 'E' or arg == 'Е':  # Проверка наличия спецсимвола 'Е' (ru/eng) завершения программы
                result_2 = 'E'
                break
            else:
                result_1 += int(arg)
                result_2 = ''
                break
        else:
            result_1 += int(arg[:symbol_space])  # Прибавить "ближайщее" число к сумме
            arg = arg[symbol_space + 1:]  # Удалить "ближайщее" число из строки
    return [result_1, result_2]  # Общая сумма функции, Индикатор спецсимвола


print('Сложение всеееееех чисел')
result = [0, '']  # Переменная для выходных данных функции
sum_num = 0  # Общая сумма программы
while result[1] == '':
    s = input('Введите числа (Устали? введите "Е") : ')
    result = my_func(s)
    sum_num += result[0]
    print(f'Текущая сумма чисел = {sum_num}.')
print(f'Конечная сумма чисел = {sum_num}.')
