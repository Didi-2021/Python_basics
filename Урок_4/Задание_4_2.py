import random

my_list = []
new_list = []
size_list = input('Введите количество элементов в списке : ')
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
    el = random.randint(-1000, 1000)  # Для примера числа из диапазона
    my_list.append(el)
    i += 1
print('Начальный список : ', my_list)
new_list = [my_list[i + 1] for i in range(size_list - 1) if my_list[i] < my_list[i + 1]]
print('Конечный список :', new_list)
