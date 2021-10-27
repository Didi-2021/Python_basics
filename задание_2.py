time = 0
a = True  # Проверка входных данных
while a:
    try:
        time = input("Введите количество секунд: ")
        if (int(time) == float(time)) and (int(time) > 0):
            a = False
    except ValueError:
        a = True

time = int(time)
hh = time // 3600
mm = (time - hh * 3600) // 60
ss = time % 60

print('{hour}:{minute}:{second}'.format(hour=hh, minute=mm, second=ss))

