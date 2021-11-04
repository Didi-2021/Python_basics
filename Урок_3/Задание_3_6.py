def int_func(arg):
    arg = arg.title()
    return arg


s1 = input('Введите слова :')
text = ''
index = s1.find(' ')
if index > 0:
    while index > 0:
        s2 = int_func(s1[:index])
        text = text + s2 + ' '
        s1 = s1[index + 1:]
        index = s1.find(' ')
text = text + int_func(s1)
print(text)
