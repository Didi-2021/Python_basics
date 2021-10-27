revenue = 0  # Выручка
costs = 0  # Издержки
number = 0  # Численность
profitability = 0  # Рентабельность
prof_num = 0  # Прибыль на сотрудника

a = True  # Ввод выручки
while a:
    try:
        revenue = input("Введите выручку Вашей фирмы: ")
        if (int(revenue) == float(revenue)) and (int(revenue) > 0):
            a = False
    except ValueError:
        a = True
a = True  # Ввод издержек
while a:
    try:
        costs = input("Введите издержки Вашей фирмы: ")
        if (int(costs) == float(costs)) and (int(costs) > 0):
            a = False
    except ValueError:
        a = True
revenue = int(revenue)
costs = int(costs)

# Результат работы фирмы
if revenue < costs:
    print('Ваша фирма приносит убытки')
elif revenue == costs:
    print('Ваша фирма не приносит прибыль и убытки')
else:
    print('Ваша фирма приносит прибыль')
    profitability = (revenue - costs) / revenue
    print('Рентабельность Вашей фирмы = {}'.format(profitability))
    a = True
    while a:
        try:
            number = input("Введите численность Вашей фирмы: ")
            if (int(number) == float(number)) and (int(number) > 0):
                a = False
        except ValueError:
            a = True
    number = int(number)
    prof_num = (revenue - costs) / number
    print('Прибыль на одного сотрудника = {}'.format(prof_num))

