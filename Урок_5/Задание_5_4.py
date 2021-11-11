file = open('./folder1/text4_1.txt', 'r', encoding='utf-8')
line_list = []
while True:
    line = file.readline()
    if not line:
        break
    line_list.append(line)
file.close()
s = ''
for el in line_list:
    if el.find('One') != -1:
        s = s + 'Один' + el[3:]
    if el.find('Two') != -1:
        s = s + 'Два' + el[3:]
    if el.find('Three') != -1:
        s = s + 'Три' + el[5:]
    if el.find('Four') != -1:
        s = s + 'Четыре' + el[4:]
print(line_list)
print(s)
file_2 = open('folder1/text4_2.txt', 'w', encoding='utf-8')
file_2.write(str(s))
file_2.close()
