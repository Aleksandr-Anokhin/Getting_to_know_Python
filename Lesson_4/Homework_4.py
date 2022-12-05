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


list_num = [1, 1, 2, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9, 9]
not_repeat = []

for i in list_num:
    if i not in not_repeat:
        not_repeat.append(i)
print(not_repeat)
'''