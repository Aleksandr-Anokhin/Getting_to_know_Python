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
'''

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

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

with open('degree_k.txt', 'w', encoding='utf8') as file:
    file.write(f'{polynom_1}{polynom_2}')

