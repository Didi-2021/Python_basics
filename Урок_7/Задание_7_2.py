import random


class Clothes:
    title = str
    coat_count = 0  # Общее число пальто
    suit_count = 0  # Общее число комтюмов
    costs_list = []  # Лист с пальто
    suits_list = []  # Лист с пальто


class Coat(Clothes):
    title = 'Пальто'
    number = 0  # Порядковый номер
    v = int  # Размер

    def __init__(self, arg):
        Coat.number += 1
        self.v = arg
        Clothes.coat_count += 1
        temp_expense = self.v / 6.5 + 0.5
        Clothes.costs_list.append([Coat.number, arg, temp_expense])

    def expense(self):
        print(f'Расход ткани на данное пальто: {Coat.costs_list[self.number - 1][2]}.')


class Suit(Clothes):
    title = 'Костюм'
    number = 0  # Порядковый номер
    h = int  # Рост

    def __init__(self, arg):
        Suit.number += 1
        self.h = arg
        Clothes.coat_count += 1
        temp_expense = self.h * 2 + 0.3
        Clothes.suits_list.append([Coat.number, arg, temp_expense])

    def expense(self):
        print(f'Расход ткани на данный костюм: {Coat.suits_list[self.number - 1][2]}.')


def coat_expense():
    summa = 0
    for i in range(len(Clothes.costs_list)):
        summa += Clothes.costs_list[i][2]
    print(f'Расходы все пальто : {summa} ед.')
    return summa


def suit_expense():
    summa = 0
    for i in range(len(Clothes.suits_list)):
        summa += Clothes.suits_list[i][2]
    print(f'Расход на все костюмы : {summa} ед.')
    return summa


c_1 = Coat(random.randint(40, 100))
print(f'{c_1.title} {c_1.number} ', end='. ')
c_1.expense()

c_2 = Coat(random.randint(40, 100))
print(f'{c_2.title} {c_2.number} ', end='. ')
c_2.expense()

# Ткань на все пальто
res_coat_exp = coat_expense()
print()

s_1 = Suit(random.randint(100, 210))
print(f'{s_1.title} {s_1.number} ', end='. ')
s_1.expense()

s_2 = Suit(random.randint(100, 210))
print(f'{s_2.title} {s_2.number} ', end='. ')
s_2.expense()

s_3 = Suit(random.randint(100, 210))
print(f'{s_3.title} {s_3.number} ', end='. ')
s_3.expense()

# Ткань на все костюмы
res_suit_exp = suit_expense()
print()

print(f'Всего трани затрачено : {res_suit_exp + res_coat_exp} ед.')
