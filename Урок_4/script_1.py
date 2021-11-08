from sys import argv

script_name, first_param, second_param, third_param = argv
print('Заработная плата сотрудника равна : ', int(first_param) * int(second_param) + int(third_param), ' руб.')
