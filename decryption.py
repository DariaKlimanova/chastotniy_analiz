def decrypt(a, m, ru, t):
    letters_ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    if t == 1:
        if m.isalpha() and m in letters_ru:
            k = int(letters_ru.index(m)) - int(letters_ru.index(ru[0]))

    elif t == 2:
        if m.isalpha() and m in letters_ru:
            k = int(letters_ru.index(m)) - int(letters_ru.index(ru[1]))

    elif t == 3:
        if m.isalpha() and m in letters_ru:
            k = int(letters_ru.index(m)) - int(letters_ru.index(ru[2]))

    elif t == 4:
        if m.isalpha() and m in letters_ru:
            k = int(letters_ru.index(m)) - int(letters_ru.index(ru[3]))
    s = ''
    for el in a:
        if el.isalpha() and el in letters_ru:
            b = el.replace(a[a.index(el)], letters_ru[(letters_ru.index(el) - k) % 33])
            s += b
        else:
            b = el
            s += b
    return s


def decrypt_bi(a, l_1, l_2, t):
    letters_ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    s = ''
    a = str(a)
    x = []
    z = []
    for i in l_1:
        x.append(i[0])
    for i in l_2:
        z.append(i[0])
    while True:
        if t == 1:
            if z[0][0] in letters_ru and z[0][1] in letters_ru:
                k_1 = int(letters_ru.index(z[0][0])) - int(letters_ru.index(x[0][0]))
                k_2 = int(letters_ru.index(z[0][1])) - int(letters_ru.index(x[0][1]))
                if k_1 == k_2:
                    k = k_1
                    break
                else:
                    t = 2
        elif t == 2:
            if z[1][0] in letters_ru and z[1][1] in letters_ru:
                k_1 = int(letters_ru.index(z[1][0])) - int(letters_ru.index(x[1][0]))
                k_2 = int(letters_ru.index(z[1][1])) - int(letters_ru.index(x[1][1]))
                if k_1 == k_2:
                    k = k_1
                    break
                else:
                    t = 3
        elif t == 3:
            if z[2][0] in letters_ru and z[2][1] in letters_ru:
                k_1 = int(letters_ru.index(z[2][0])) - int(letters_ru.index(x[2][0]))
                k_2 = int(letters_ru.index(z[2][1])) - int(letters_ru.index(x[2][1]))
                if k_1 == k_2:
                    k = k_1
                    break
                else:
                    break

    for el in a:
        if el.isalpha() and el in letters_ru:
            b = el.replace(a[a.index(el)], letters_ru[(letters_ru.index(el) - k) % 33])
            s += b
        else:
            b = el
            s += b
    return s


