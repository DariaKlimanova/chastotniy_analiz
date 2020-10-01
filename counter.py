def cnt_num(s):
    c = 0
    for i in s:
        if i.isdigit():
            c += 1
    return c


def cnt_w(s):
    c = 0
    for i in s:
        if i.isalpha():
            c += 1
    return c

def cnt(s):
    letters_ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    d = {}
    for i in s:
        if i.isalpha() and i not in d and i in letters_ru:
            d[i] = 1
        elif i.isalpha() and i in d and i in letters_ru:
            d[i] += 1
    return d


def cnt_tab(s):
    c = 0
    for i in s:
        if i == ' ':
            c += 1
    return c