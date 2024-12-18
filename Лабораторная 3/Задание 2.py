#запись в пустой файл
a = input('Введите текст:')
with open('lb2.txt', 'w', encoding='utf-8') as file:
    file.write(a)
#дозапись
a = input('Введите текст:')
with open('lb2.txt', 'a', encoding='utf-8') as file:
    file.write(a)


