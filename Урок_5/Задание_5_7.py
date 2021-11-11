import json


file = open('folder1/text7_1.txt', 'r', encoding='utf-8')
text_list = file.readlines()  # Список текст
file.close()
line_list = []  # Список строка
dict_1 = {}  # Словарь - прибыль
dict_2 = {}  # Словарь - убыток
dict_3 = {}  # Словарь - средняя прибыль
average_profit = 0
for line in text_list:
    for el in line.split(' '):
        line_list.append(el)
    profit = int(line_list[2]) - int(line_list[3])
    if profit > 0:
        dict_1[line_list[0]] = profit
        average_profit += profit
    else:
        dict_2[line_list[0]] = profit
    profit = 0
    line_list = []
dict_3['average_profit'] = average_profit
res_list = [dict_1, dict_2, dict_3]
json_var = json.dumps(res_list)
with open('folder1/text7_2.json', 'w', encoding='utf-8') as write_f:
    json.dump(json_var, write_f)
