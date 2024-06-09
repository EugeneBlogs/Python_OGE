while True:
    try:
        print("")
        number = input("Введите число: ")
        print("")
        print("Что нужно сделать?")
        print("Перевести из 10 в другую - 1")
        print("Перевести из другой в 10 - 2")
        print("Выход из программы - 0")
        choose = int(input("Выбор: "))
        print("")
        if choose == 1:
            print("В какую систему счисления переводим? Напишите 2, 8 или 16.")
            system = int(input("Система счисления: "))
            print("")
            number = int(number)
            if system == 2:
                result = bin(number)[2:]
                print(f"{number} в двоичной системе счисления {result}.")
            elif system == 8:
                result = oct(number)[2:]
                print(f"{number} в восьмеричной системе счисления {result}.")
            elif system == 16:
                result = hex(number)[2:]
                print(f"{number} в шестнадцатеричной системе счисления {result}.")
            else:
                print("Некорректная система счисления.")
        elif choose == 2:
            print("Из какой системв счисления переводим?")
            system = int(input("Система счисления: "))
            print("")
            result = int(number, system)
            print(f"{number} в десятичной системе счисления {result}.")
        elif choose == 0:
            raise SystemExit(0)
        else:
            print("Команда не распознана.")
    except:
        print("")
        print("Ой! Что-то пошло не так. Возможно, вы ввели некорректные данные.")