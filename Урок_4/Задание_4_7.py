def generator(arg):
    res = 1
    for el_def in range(1, arg + 1):
        res = res * el_def
        yield res


res_2 = 0
n = int(input('Введите число : '))
g = generator(n)
for el in g:
    print(el)
    res_2 = el
print(f'\n{n}! = {res_2}')
