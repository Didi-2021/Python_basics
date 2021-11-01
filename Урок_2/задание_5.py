rating = []
result = input('Введите элемент рейтинга :')
i = True
while i:
    try:
        if (int(result) == float(result)) and (int(result) > 0):
            result = int(result)
            rating.append(result)
            rating.sort(reverse=True)
            print(f'Вы ввели число {result}. Результат{rating}')
            result = input('Введите элемент рейтинга или -1 ("минус один") для завершения ввода :')
            if result == '-1':
                i = False
                break
            i = True
        else:
            result = input('Введите элемент рейтинга или -1 ("минус один") для завершения ввода :')
            if result == '-1':
                i = False
                break
    except ValueError:
        result = input('Введите натуральное число или -1 ("минус один") для завершения ввода :')
        if result == '-1':
            i = False
            break
        i = True
rating.sort(reverse=True)
print(f'Результат{rating}')
