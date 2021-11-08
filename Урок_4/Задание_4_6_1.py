from itertools import count


start = int(input('Введите начальное значение : '))
for el in count(start):
    if el > start + 10000:
        break
    else:
        print(el, end=' ')
print('\nВыше выведены еще 10000 чисел после', start)
