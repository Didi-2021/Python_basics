n = None
a = True  # Проверка входных данных
while a:
    try:
        n = input("Введите натуральное число: ")
        if (int(n) == float(n)) and (int(n) > 0):
            a = False
    except ValueError:
        a = True
n = int(n)
x = n
max_num = 1
while x > 0:
    if max_num < (x % 10):
        max_num = x % 10
    x = x // 10

print('В числе {} самая большая цифра : {}'.format(n, max_num))

