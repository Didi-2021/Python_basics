n = None
a = True  # Проверка входных данных
while a:
    try:
        n = input("Введите целое число: ")
        if int(n) == float(n):
            a = False
    except ValueError:
        a = True

nn = n + n
nnn = n + n + n
s = int(n) + int(nn) + int(nnn)
print('{} + {} + {}  = {}'.format(n, nn, nnn, s))

