# Д.з. № 4 задача 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

# Было так:
list_num = [1, 1, 2, 2, 3, 3, 4, 5, 7, 8, 8, 9]
not_repeat = []

for i in list_num:
    if list_num.count(i) == 1:
        not_repeat.append(i)
print(not_repeat)

# Применил: filter() и lambda().
list_num = [1, 1, 2, 2, 3, 3, 4, 5, 7, 8, 8, 9]
not_repeat = list(filter(lambda i: list_num.count(i) == 1, list_num))
print(not_repeat)

