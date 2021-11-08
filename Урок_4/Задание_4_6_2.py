from itertools import cycle


finish = input('Введите Ваше любимое число : ')
c = 0
for el in cycle(finish):
    if c % 100 == 0:
        print()
    if c > 9999:
        break
    else:
        print(el, end=' ')

    c += 1
print('Все эти числа для Вас :')
