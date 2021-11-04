def my_func():
    name = input('Ввведите имя :')
    lname = input('Ввведите фимилию :')
    bday = input('Ввведите день рождения :')
    city = input('Ввведите город проживания :')
    email = input('Ввведите e-mail :')
    phone = input('Ввведите номер телефона :')
    res = name + ' ' + lname + ' ' + bday + ' ' + city + ' ' + email + ' ' + phone
    return res


print(my_func())
