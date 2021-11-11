file = open('folder1/text6.txt', 'r', encoding='utf-8')
line_list = []
while True:
    line = file.readline()
    if not line:
        break
    line_list.append(line)
file.close()
print(line_list)
num_sum = 0
subj_dict = {}
for line in line_list:
    index = line.find(':')
    subj_name = line[:index]  # Название предмета
    line = line[index + 2:]  # Сокращаем строчку
    while len(line) > 0:
        if line[0] == '-':
            line = line[2:]
        else:
            index = line.find('(')
            num = line[:index]
            num_sum = num_sum + int(num)
            index = line.find(')')
            line = line[index + 2:]
    subj_dict[subj_name] = num_sum
    num_sum = 0
print(subj_dict)
