# Условие задания КИМ 15.2:
'''
Напишите программу для решения следующей задачи.
На контрольной работе по алгебре ученикам 9 класса было предложено 10 примеров.
Неудовлетворительная оценка выставляется, если правильно решено менее половины примеров.
Сколько неудовлетворительных оценок было получено учениками?
Если хотя бы один из учеников правильно решил все задачи, выведите «YES», иначе выведите «NO».
Программа получает на вход количество учеников в классе N (1 ≤ N ≤ 30), затем для каждого ученика вводится количество правильно решённых примеров.
'''

n = int(input("Введите количество учеников: "))
count = 0
all_right = False
for i in range(n):
    x = int(input("Введите количество решённых задач: "))
    if x < 5:
        count += 1
    if x == 10:
        all_right = True
if all_right:
    print(f"Ответ: {count}; YES.")
else:
    print(f"Ответ: {count}; NO.")