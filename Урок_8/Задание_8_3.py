print('Заполнение списка числами.')
s = ''
lst = []
while s != 'stop':
    s = input('Введите очередное число : ')
    if s == 'stop':
        break
    try:
        s = float(s)
        lst.append(s)
    except ValueError:
        print('Вы ввели не число. Введите число или "stop" для завершения ввода.')
print(lst)
