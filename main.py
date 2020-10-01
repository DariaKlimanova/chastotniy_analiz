from encryption import encrypt
from decryption import *
from counter import *
from bigram import *

with open('C:\\Users\\kalma\\Desktop\\voinaimir.txt', 'r', encoding='utf-8') as file:
    full_book = file.read().upper().replace(' ', '').replace('\n', '')

a = full_book
d_1 = cnt(a)

list_d = list(d_1.items())
list_d.sort(key=lambda i: i[1], reverse=True)

print('Кол-во символов в тексте:', str(len(a)) + '\n' +
      'Кол-во букв в тексте:', str(cnt_w(a))+'\n' +
      'Кол-во цифр в тексте:', str(cnt_num(a)))
for i in list_d:
    print('Символ ' + str(i[0]) + ' встречается ' + str(i[1]) + ' раз с частотой',
          round(i[1]/cnt_w(a)*100, 2), '%')

ru = []
for i in list_d[:4]:
    ru.append(i[0])


d_2 = bi(a)
list_d_2 = list(d_2.items())
list_d_2.sort(key=lambda i: i[1], reverse=True)
print()
for i in list_d_2[:21]:
    print('Сочетание ' + str(i[0]) + ' встречается ' + str(i[1]) + ' раз')

with open('C:\\Users\\kalma\\Desktop\\glava.txt', 'r', encoding='utf-8') as file:
    glava = file.read().upper().replace('\n', '')

print()
k = int(input("Ключ для шифрования главы = "))
encrypted_message = encrypt(glava, k)

f = open('C:\\Users\\kalma\\Desktop\\encr.txt', 'w', encoding='utf-8')
f.write(str(encrypted_message))
f.close()


d_1 = cnt(encrypted_message)
list_d = list(d_1.items())
list_d.sort(key=lambda i: i[1], reverse=True)

print('Кол-во символов в тексте:', str(len(encrypted_message)-cnt_tab(encrypted_message)) + '\n' +
      'Кол-во букв в тексте:', str(cnt_w(encrypted_message)) + '\n' +
      'Кол-во цифр в тексте:', cnt_num(encrypted_message))
for i in list_d:
    print('Символ ' + str(i[0]) + ' встречается ' + str(i[1]) + ' раз с частотой',
          round(i[1]/(cnt_w(encrypted_message))*100, 2), '%')
print()

d_3 = bi(encrypted_message)
list_d_3 = list(d_3.items())
list_d_3.sort(key=lambda i: i[1], reverse=True)

for i in list_d_3[:21]:
    print('Сочетание ' + str(i[0]) + ' встречается ' + str(i[1]) + ' раз')
print()

while True:
    print("Расшифровать текст по буквам? (да/нет)")
    z = input()
    if z == "нет":
        break
    else:
        content = ''
        content += str(decrypt(encrypted_message, list_d[0][0], ru, t=1))
        f = open('C:\\Users\\kalma\\Desktop\\decr_w.txt', 'w', encoding='utf-8')
        f.write(str(content))
        f.close()
        print()
        print('Если текст расшифрован верно, введите "да". '
              'Если требуется еще одна попытка, введите "нет".')
        z = input()
        if z == "да":
            break
        else:
            content = ''
            content += str(decrypt(encrypted_message, list_d[0][0], ru, t=2))
            f = open('C:\\Users\\kalma\\Desktop\\decr_w.txt', 'w', encoding='utf-8')
            f.write(str(content))
            f.close()
            print()
            print('Если текст расшифрован верно, введите "да". '
                  'Если требуется еще одна попытка, введите "нет".')
            z = input()
            if z == "да":
                break
            else:
                content = ''
                content += str(decrypt(encrypted_message, list_d[0][0], ru, t=3))
                f = open('C:\\Users\\kalma\\Desktop\\decr_w.txt', 'w', encoding='utf-8')
                f.write(str(content))
                f.close()
                print()
                print('Если текст расшифрован верно, введите "да". '
                      'Если требуется еще одна попытка, введите "нет".')
                if z == "да":
                    break
                else:
                    content = ''
                    content += str(decrypt(encrypted_message, list_d[0][0], ru, t=4))
                    f.write(str(content))
                    f.close()
                    break
while True:
    print("Расшифровать текст по биграммам (да/нет)")
    z = input()
    if z == "нет":
        break
    else:
        content = ''
        content += str(decrypt_bi(encrypted_message, list_d_2, list_d_3, t=1))
        f = open('C:\\Users\\kalma\\Desktop\\decr_bi.txt', 'w', encoding='utf-8')
        f.write(str(content))
        f.close()
        print('Если текст расшифрован верно, введите "да". '
              'Если требуется еще одна попытка, введите "нет".')
        z = input()
        if z == "да":
            break
        else:
            content = ''
            content += str(decrypt_bi(encrypted_message, list_d_2, list_d_3, t=2))
            f = open('C:\\Users\\kalma\\Desktop\\decr_bi.txt', 'w', encoding='utf-8')
            f.write(str(content))
            f.close()
            print('Если текст расшифрован верно, введите "да". '
                  'Если требуется еще одна попытка, введите "нет".')
            z = input()
            if z == "да":
                break
            else:
                content = ''
                content += str(decrypt_bi(encrypted_message, list_d_2, list_d_3, t=3))
                f = open('C:\\Users\\kalma\\Desktop\\decr_bi.txt', 'w', encoding='utf-8')
                f.write(str(content))
                f.close()
                print('Если текст расшифрован верно, введите "да". '
                      'Если требуется еще одна попытка, введите "нет".')
                z = input()
                if z == "да":
                    break


