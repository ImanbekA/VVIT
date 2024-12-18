try:
    with open('l.txt', "r") as file:
    v = file.read()
    print(v)
except FileNotFoundError:
    print('Не существующий файл')