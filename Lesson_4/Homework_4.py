# 1. Вычислить число Pi c заданной точностью *d* (d = 0.001)
'''
from math import fabs  # для вычисления абсолютного значения числа
from math import pi

d = float(input('Введите значение точности: '))
sum = 0
a = 0
n = 0

while True:
    a = float((-1) ** n) / float(2 * n + 1)
    sum += a
    n += 1
    result = sum * 4

    if fabs(a) < d:
        break

print('Результат вычисления pi: ', result)
print('pi для сравнения: ', pi)

# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

N = int(input("Введите число N: "))
j = 2
multipliers = []

while j * j <= N:
    while N % j == 0:
        multipliers.append(j)
        N //= j
    j = j + 1
if N > 1:
    multipliers.append(N)
print(multipliers)

# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

list_num = [1, 1, 2, 2, 3, 3, 4, 5, 7, 8, 8, 9]
not_repeat = []

for i in list_num:
    if list_num.count(i) == 1:
        not_repeat.append(i)
print(not_repeat)


# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# ариант 1. Был сделан до 5-го урока.

import random

k = int(input("Введите число k: "))
a = int(random.randint(0,100))
b = int(random.randint(0,100))

if a != 0:
    polynom_1 = (str(a) + "x^" + str(k) + " + ")
else:
    polynom_1 = (str())

if b != 0:
    polynom_2 = (str(b) + " = 0")
else:
    polynom_2 = (str())
print(f'{polynom_1}{polynom_2}')

with open('g:/Prog/Python/Getting_to_know_Python/Lesson_4/number_k.txt', 'w', encoding='utf8') as file:
    file.write(f'{polynom_1}{polynom_2}')

# Запись в файл и его создание работает только если прописать полный путь к файлу. пробовал писать адрес по разному, ничего не помогло.    

# Вариант 2. Сделан после 5-го урока, когда увидел подсказку и понял, что условие невнимательно прочитал. 
from random import randint

k = int(input("Введите число k: "))
a = int(randint(0,100))
b = int(randint(0,100))
c = int(randint(0,100))
lst_polynom = []

for i in range(k, -1, -1):
    lst_polynom.append(f'{a}x**{i} + {b}x + {c} = 0')
print(lst_polynom)

with open('g:/Prog/Python/Getting_to_know_Python/Lesson_4/polynom_k.txt', 'w') as file:
    file.write(f'{lst_polynom}')
'''
