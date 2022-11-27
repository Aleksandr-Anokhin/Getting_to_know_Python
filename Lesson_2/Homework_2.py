# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    # Пример:
        # 6782 -> 23
        # 0.56 -> 11

numbers = input("Введите вещественное число: ")
sum_numbers = 0

for i in numbers:
    if i != ".":
        sum_numbers = sum_numbers + int(i)
print("Сумма цифр равна: ", sum_numbers)

# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input("Введите число N: "))
f = 1

for i in range(N):
    i = i + 1
    f = i * f
    
print(f, end = " ")


# 3. Задайте список из n чисел последовательности (1 + 1 / n)**n и выведите на экран их сумму.

n = int(input("Введите число n: "))
s = 0

for i in range(n):
    s += (1 + 1 / n)**n
    
print("Сумма чисел последовательности равна: ", s)

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.
from random import randint

A = int(input("Введите число N: "))
numbers = []
for i in range(A):
    numbers.append(randint(- A, A))
print(numbers)

B = int(input("Введите номер первой позиции: "))
C = int(input("Введите номер второй позиции: "))
for i in range(len(numbers)):
    mult = numbers[B -1]*numbers[C - 1]
print(mult)    

# 5. Реализуйте алгоритм перемешивания списка.

from random import Random, randint

M = int(input("Введите количество элементов массива: "))
numbers = []
for i in range(M):
    numbers.append(randint(- M, M))
print(numbers)

def mix(numbers):
    for i in range(len(numbers)):
        index = randint(0, len(numbers) - 1)
        temp = numbers[i]
        numbers[i] = numbers[index]
        numbers[index] = temp
    return numbers
print(mix(numbers))