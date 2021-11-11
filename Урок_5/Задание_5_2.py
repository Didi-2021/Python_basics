file = open('folder1/text2.txt', 'r', encoding='utf-8')
num_lines = 0  # Количество строк
num_words = 0  # Количество слов
list_1 = [['Номер строки', 'Количество слов']]  # Лист с Номером строки, Количеством слов
while True:
    line = file.readline()
    if not line:
        break
    num_lines += 1
    line.strip()
    num_words = len(line.split())
    print(f'{num_lines} строка:\nСимволов = {len(line)}; Слов = {num_words}.')
    list_1.append([num_lines, num_words])
print(f'\nВсего строк в файле : {num_lines}')
print(list_1)
file.close()
