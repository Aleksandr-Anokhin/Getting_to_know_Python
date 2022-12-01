# 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

numbers = [2, 5, 5, 10, 3]
sum = 0
for i in range(len(numbers)):
    if i % 2 != 0:
        sum += numbers[i]
print(sum)

# 2. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

pair_of_numbers = [2, 3, 4, 5, 6]
sum_of_two = []

for i in range((len(pair_of_numbers) + 1)//2):
    sum_of_two.append(pair_of_numbers[i] * pair_of_numbers[len(pair_of_numbers)- 1 - i])
 
print(pair_of_numbers, '==>', sum_of_two) 

# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

real_numbers = [1.1, 1.2, 3.1, 5, 10.01]
fractional_part = []

for i in range(len(real_numbers)):
    fractional_part.append(real_numbers[i] % 1)
    result = max(fractional_part) - min(fractional_part)
print(result)

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

num = int(input("Введите десятичное число: "))
transform = ''
while num > 0:
    transform = str(num % 2) + transform
    num = num // 2
print(transform)    


# 5. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

'''
Сделал 2 варианта решения. 1 - й работает, но только для положительных чисел. 
Для отрицательных не получилось реализовать.
2 - й у меня вообще не работает, а у наставника как-то работает. 
'''
n = int(input("Введите число n: "))
Fibo_0 = [0, 1]
i = 2
while i <= n:
    Fibo_0.append(Fibo_0[i - 1] + Fibo_0[i - 2])
    i = i + 1
print(Fibo_0)
'''
def fibo(n):
    if n > 1:
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return (fibo(n - 1) + fibo(n - 2))
    if n <= - 2:
        return ((-1)**(n + 1)) + fibo(n + 2)
print(fibo(8))
'''

    


