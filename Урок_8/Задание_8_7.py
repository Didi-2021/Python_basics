import random


class MyComplexNum:
    def __init__(self, a, b):
        self.rl = a
        self.img = b
        if b < 0:
            self.sign = ''
        else:
            self.sign = '+'

    def __str__(self):
        if self.img == 0:
            res = f'{self.rl}'
        elif self.rl == 0:
            res = f'{self.img}i'
        else:
            res = f'{self.rl}{self.sign}{self.img}i'
        return res

    def __add__(self, other):
        rl = self.rl + other.rl
        img = self.img + other.img
        if img < 0:
            sign = ''
        else:
            sign = '+'

        if img == 0:
            res = f'{rl}'
        elif rl == 0:
            res = f'{img}i'
        else:
            res = f'{rl}{sign}{img}i'
        return res

    # (a+bi)(c+di) = (ac-bd)+(ad+cb)i
    def __mul__(self, other):
        rl = self.rl * other.rl - self.img * other.img
        img = self.rl * other.img + other.rl * self.img
        if (self.img + other.img) < 0:
            sign = ''
        else:
            sign = '+'

        if img == 0:
            res = f'{rl}'
        elif rl == 0:
            res = f'{img}i'
        else:
            res = f'{rl}{sign}{img}i'
        return res


a1 = random.randint(-100, 100)
b1 = random.randint(-100, 100)
a2 = random.randint(-100, 100)
b2 = random.randint(-100, 100)

x1 = MyComplexNum(a1, b1)
print('x1 =', x1)
x2 = MyComplexNum(a2, b2)
print('x2 =', x2)

print('x1 + x2 = ', x1 + x2)
print('x1 * x2 = ', x1 * x2)
