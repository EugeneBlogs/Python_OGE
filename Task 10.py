# Условие задания КИМ 15.2:
'''
Напишите программу, которая в последовательности натуральных чисел определяет наибольший из делителей числа 2200.
Программа получает на вход количество чисел в последовательности, а затем сами числа.
В последовательности всегда имеется число, являющееся делителем 2200.
Количество чисел не превышает 1000, а сами числа не превышают 30000.
Программа должна вывести одно число — наибольший из делителей числа 2200.
'''

n = int(input("Введите количество делителей: "))
maximum = -10**20
for i in range(n):
    x = int(input("Введите делитель: "))
    if 2200 % x == 0:
        maximum = max(maximum, x)
print("Ответ: ", maximum)