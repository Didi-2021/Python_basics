import random

my_list = []  # Исходные список
new_list = []  # Конечный список
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
    el = random.randint(1, 10)  # Для примера числа из диапазона
    my_list.append(el)
    i += 1

print('Начальный список    : ', my_list)
my_2_list = list(set(my_list))  # Вспомогательный список
# print('Уникальные значения : ', my_2_list)
count_1_list = [my_list.count(el) for el in my_2_list]  # Список с количеством повторений
count_2_list = []  # Список с количеством повторений измененный
for el in count_1_list:
    if el == 1:
        count_2_list.append(el)
    else:
        count_2_list.append(0)
# print('Все повторения      : ', count_1_list)
# print('Уникльные повторения: ', count_2_list)
my_3_list = []  # Список без повторяющихся элементов
for i in range(len(my_2_list)):
    if count_2_list[i] == 1:
        my_3_list.append(my_2_list[i])
# print('Уникальные значения : ', my_3_list)
new_list = [el for el in my_list if el in my_3_list]
print('Конечный список     : ', new_list)
