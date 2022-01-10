name = input("Введите ваше имя: ")
if len(name) < 5:
    surname = input("Введите фамилию: ")
    print((name+surname).upper())
else:
    print(name.lower())


