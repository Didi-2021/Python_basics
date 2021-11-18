class Clothes:
    title = str


class Coat(Clothes):
    title = 'Пальто'
    v = int

    def __init__(self, arg):
        self.v = arg

    def expense(self):
        print(f'Расход ткани на пальто: {self.v / 6.5 + 0.5}.')


class Suit(Clothes):
    title = 'Костюм'
    h = int

    def __init__(self, arg):
        self.h = arg

    def expense(self):
        print(f'Расход ткани на костюм: {self.h * 2 +0.3}.')


a_1 = Suit(180)
a_1.expense()
a_2 = Coat(60)
a_2.expense()
