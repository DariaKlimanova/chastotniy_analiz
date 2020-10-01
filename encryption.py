def encrypt(a, k):
    s = ""
    letters_ru = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    for el in a:
        if el.isalpha() and el in letters_ru:
            b = el.replace(a[a.index(el)], letters_ru[(letters_ru.index(el) + k) % 33])
            s += b
        else:
            b = el
            s += b
    return s