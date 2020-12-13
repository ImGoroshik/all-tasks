print("             ДОБРО ПОЖАЛОВАТЬ")
print("         ========================")
a = "  В этой программе вы сможете посчитать\n    кол-во слов, пробелов и символов.\n  Если хотите закончить напишите 'stop' "
print(a)
print("-------------------------------------------")

while True:
    comm = input("Введите команду(probel, simvol, slova, или на русском пробел, символ, слова): ")
    if comm == "simvol":
        text = str(input("Введите текст: "))
        vivod = len(text)
        print("--------------------")
        print("Кол-во символов: ", vivod)
        print("--------------------")

    elif comm == "slova":
        text = str(input("Введите текст: ")).split(' ')
        vivod =len(text)
        print("--------------------")
        print("Кол-во слов: ", vivod)
        print("--------------------")

    elif comm == "probel":
        text = str(input("Введите текст: ")).split(' ')
        vivod = len(text) - 1
        print("--------------------")
        print("Кол-во пробелов: ", vivod)
        print("--------------------")

    elif comm == "stop":
        print("--------------------")
        print("Пока")
        print("--------------------")
        break


    if comm == "символ":
        text = str(input("Введите текст: "))
        vivod = len(text)
        print("--------------------")
        print("Кол-во символов: ", vivod)
        print("--------------------")

    elif comm == "слова":
        text = str(input("Введите текст: ")).split(' ')
        vivod =len(text)
        print("--------------------")
        print("Кол-во слов: ", vivod)
        print("--------------------")

    elif comm == "пробел":
        text = str(input("Введите текст: ")).split(' ')
        vivod = len(text) - 1
        print("--------------------")
        print("Кол-во пробелов: ", vivod)
        print("--------------------")

    elif comm == "стоп":
        print("--------------------")
        print("Пока")
        print("--------------------")
        break

    else:
        print("--------------------")
        print("Я не знаю такой команды =(")
        print("--------------------")



