import random


count = 10000  # Задание количества чисел
s = ''  # Строка с числами, разделенные пробелами
for i in range(count):  # Генерация случайных целых чисел на промежутке [1; 100]
    s = s + str(random.randint(1, 100)) + ' '
file = open('folder1/text5.txt', 'w', encoding='utf-8')
file.write(s)
file.close()
file = open('folder1/text5.txt', 'r', encoding='utf-8')
num_sum = 0
s = file.read()
space_index = s.find(' ')
while space_index > 0:
    num_sum = num_sum + int(s[:space_index])
    s = s[space_index + 1:]
    space_index = s.find(' ')
file.close()
print(f'Сумма всех чисел в файле равна = {num_sum}')
