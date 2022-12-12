# Д.з. № 3 задача 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Было так:
numbers = [2, 5, 5, 10, 3]
sum = 0
for i in range(len(numbers)):
    if i % 2 != 0:
        sum += numbers[i]
print(sum)

# Использовал list comprehension, но почему-то результат получается неверный.
numbers = [2, 5, 5, 10, 3]
sum = [i+i for i in range(len(numbers)) if i%2 != 0]
print(sum)

# Использовал map(), filter() и lambda() и всеравно результат не тот. Наверно вместо i % 2 != 0 надо что-то другое...
numbers = [2, 5, 5, 10, 3]
sum = map(lambda i: i+i, filter(lambda i: i % 2 != 0, numbers))
print(list(sum))

#*********************************************************************

# Д.з. № 3 задача 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# Было так:
real_numbers = [1.1, 1.2, 3.1, 5, 10.01]
fractional_part = []

for i in range(len(real_numbers)):
    fractional_part.append(real_numbers[i] % 1)
    result = max(fractional_part) - min(fractional_part)
print(result)

# Использовал map() и lambda().
real_numbers = [1.1, 1.2, 3.1, 5, 10.01]
fractional_part = list(map(lambda i: i%1, real_numbers))
result = max(fractional_part) - min(fractional_part)
print(result)


