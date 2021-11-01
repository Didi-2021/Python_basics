import random

# Задать режима ввода элементов списка
print('Заполните список элементами.\nЗаполнить список "В ручную"/"Автоматически"?')
mode = input('"В ручную" - введите цифру 1 / "Автоматически" - введите цифру 2 :')
if (mode == '1') or (mode == '2'):
    mode = int(mode)
else:
    i = True  # Вспомогательная переменная для проверки входных данных
    while i:
        try:
            mode = input("Введите цифру 1 или 2 :")
            if (mode == '1') or (mode == '2'):
                mode = int(mode)
                i = False
        except ValueError:
            i = True

my_list = []

if mode == 1:  # Ввод элементов в ручную
    # Задать количество элементов в списке
    size_list = input('Введите количество элементов в списке :')
    i = True
    while i:
        try:
            if (int(size_list) == float(size_list)) and (int(size_list) > 0):
                size_list = int(size_list)
                i = False
        except ValueError:
            size_list = input("Введите натуральное число :")
            i = True

    for i in range(size_list):
        el = input(f'Введите {i + 1}-ый элемент списка :')  # Для примера только строки
        my_list.append(el)
        i += 1

else:  # Ввод элементов автоматически
    size_list = input('Введите количество элементов в списке :')
    i = True
    while i:
        try:
            if (int(size_list) == float(size_list)) and (int(size_list) > 0):
                size_list = int(size_list)
                i = False
        except ValueError:
            size_list = input("Введите натуральное число  :")
            i = True

    for i in range(size_list):
        el = random.randint(-10, 10)  # Для примера числа из диапазона
        my_list.append(el)
        i += 1
print('Начальный список :', my_list)
n = int(size_list / 2)  # Вспомогательная переменная
for i in range(n):
    my_list[2 * i], my_list[2 * i + 1] = my_list[2 * i + 1], my_list[2 * i]
print('Конечный список :', my_list)
