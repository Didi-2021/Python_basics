s = input('Введите несколько слов, разделенные пробелами\n')  # при условии что пробел один
len_s = len(s)
i = 1
print(s)
while len_s > 0:
    start = s.find(' ')
    if start == -1:
        if len(s) < 10:
            print(f'№{i} :', s)
        else:
            print(f'№{i} :', s[0:10])
        break
    if start < 10:
        print(f'№{i} :', s[0:start])
    else:
        print(f'№{i} :', s[0:10])
    s = s[start + 1: len_s]
    i += 1
