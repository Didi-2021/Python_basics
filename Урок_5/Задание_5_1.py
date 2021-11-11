file = open('./folder1/text1.txt', 'w', encoding='utf-8')
file.close()
file = open('./folder1/text1.txt', 'a', encoding='utf-8')
s = str
while s != '':
    s = input('Введите данные для записи в файл : ')
    file.write(s)
file.close()
