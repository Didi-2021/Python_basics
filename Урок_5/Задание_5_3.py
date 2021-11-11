file = open('folder1/text3.txt', 'r', encoding='utf-8')
list_1 = [['Фамилия', 'Оклад']]
while True:
    line = file.readline()
    if not line:
        break
    space_index = line.find(' ')
    f_name = line[:space_index]
    salary = int(line[space_index + 1:])
    list_1.append([f_name, salary])
file.close()
print(list_1)
list_2 = [[el2 for el2 in el1 if int(el1[1]) < 20000] for el1 in list_1[1:]]
# list_2 = [el for el in list_1[1:] for el2 in el if int(el2[1]) < 20000]
# list_2 = [el for el in list_1[1:] if int(el2[1]) < 20000 for el2 in el]
list_2 = [el[0] for el in list_2 if el]
print('Оклад меньше 20000 :', list_2)
average_salary = 0
for el in list_1[1:]:
    average_salary += int(el[1])
print('Средняя зарплата = ', average_salary)
