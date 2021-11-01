month = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
my_dict = {
    12: 'Зима', 3: 'Весна', 6: 'Лето', 9: 'Осень',
    1: 'Зима', 4: 'Весна', 7: 'Лето', 10: 'Осень',
    2: 'Зима', 5: 'Весна', 8: 'Лето', 11: 'Осень'
}
num_month = input('Введите номер месяца от 1 до 12 :')
i = True  # Вспомогательная переменная для проверки входных данных
while i:
    try:
        if int(num_month) in month:
            num_month = int(num_month)
            i = False
        else:
            num_month = input("Введите число от 1 до 12 :")
            continue
    except ValueError:
        num_month = input("Введите число от 1 до 12 :")
        i = True
print('Время года :', my_dict.get(num_month))
