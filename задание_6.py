a = 0  # Результат в первый день
b = 0  # Требуемый результат

i = True  # вспомогательная переменная
while i:
    try:
        a = input("Введите результат спортсмена в первый день: ")
        if (int(a) == float(a)) and (int(a) > 0):
            i = False
    except ValueError:
        i = True
i = True
while i:
    try:
        b = input("Введите требуемый результат спортсмена: ")
        if (int(b) == float(b)) and (int(b) > 0):
            i = False
    except ValueError:
        i = True
a = int(a)
b = int(b)
i = 1  # Счетчик дней

if a >= b:
    print('1-й день: {}'.format(a))
else:
    while a < b:
        i += 1
        a = round(a * 1.1, 2)
        print('{}-й день: {}'.format(i, a))

print('Ответ: на {}-й день спортсмен достиг результата - не менее {}'.format(i, b))

