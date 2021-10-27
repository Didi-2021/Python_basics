print('Игра начинается...')
name = input('Как Вас зовут? ')
print('Приветствую, {}!'.format(name))
age = 0
a = True  # Проверка входных данных
while a:
    try:
        age = input("Сколько Вам лет? ")
        if (int(age) == float(age)) and (int(age) > 0):
            a = False
    except ValueError:
        a = True
age = int(age)
print('Как удивительно, отлично сохранились!\n')
if age <= 25:
    print('Теперь я загадаю загадку. Она непростая, будьте внимательны!\n')
    print('"Два конца, два кольца,\n Посредине гвоздик."\n')
    a = True
    while a:
        try:
            answer = input('Что это? \n Если сдаетесь так и напишите: "Сдаюсь"\n')
            if answer.lower() == "ножницы":
                a = False
            elif answer.lower() == "сдаюсь":
                print('Ответ на загадку: Ножницы')
                a = False
        except ValueError:
            a = True
    print('Вы молодец!')
else:
    print('Теперь я загадаю загадку. Она страшно сложная, будьте внимательны!\n')
    print('"Чем больше из неё берёшь,\n тем больше она становится."\n')
    a = True
    while a:
        try:
            answer = input('Что это? \n Если сдаетесь так и напишите: "Сдаюсь"\n')
            if answer.lower() == "яма":
                a = False
            elif answer.lower() == "сдаюсь":
                print('Ответ на загадку: Яма')
                a = False
        except ValueError:
            a = True
    print('Вы молодец!')
