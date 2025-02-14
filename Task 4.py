# Условие задания КИМ 15.2:
'''
Напишите программу, которая в последовательности натуральных чисел определяет минимальное число, кратное 7 и не кратное 2.
Программа получает на вход натуральные числа, количество введенных чисел неизвестно, последовательность чисел заканчивается числом 0 (0 – признак окончания ввода, не входит в последовательность).
Количество чисел не превышает 1000. Введенные числа не превышают 30000.
Программа должна вывести одно число - минимальное число, кратное 7 и не кратное 2.
'''

minimum = 10**20 # Создаём переменную для минимума (сначала присваиваем очень большое значение (10 в 20 степени), чтобы первое же число было меньше, чем этот минимум)
x = int(input("Введите число: ")) # Получаем первое число
while x != 0: # Пока число не равно 0 (то есть это не конец последовательности), делаем ...
    if x % 7 == 0 and x % 2 != 0:  # Проверяем, кратно ли число 7 (если остаток при делении на 7 равен 0, то число кратно 7) И не кратно ли число 2 (если остаток при делении на 2 не равен 0, то число не кратно 2)
        minimum = min(minimum, x)  # Данная команда сверяет 2 числа (текущий минимум и текущее введённое число) и выбирает минимальное
    x = int(input("Введите число: ")) # Получаем следующее число
print("Ответ: ", minimum)  # Выводим ответ