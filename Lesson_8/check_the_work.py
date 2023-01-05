import os
os.chdir(os.path.dirname(__file__))

import csv

def check_task_1():
    number = int(input('\nВведите номер задания: '))
    text = input('Введите текст решения: ')
    new_list = [number, text]
    save_task(new_list)

def save_task(new_task):
    with open('stud_1.csv', 'a') as bd:
        for i in range(len(new_task)):
            if i != len(new_task) - 1:
                bd.write(f'{new_task[i]};')
            else:
                bd.write(f'{new_task[i]}')
        bd.write('\n')

def check_task_2():
    number = int(input('\nВведите номер задания: '))
    text = input('Введите текст решения: ')
    new_list = [number, text]
    save_task(new_list)

def save_task(new_task):
    with open('stud_2.csv', 'a') as bd:
        for i in range(len(new_task)):
            if i != len(new_task) - 1:
                bd.write(f'{new_task[i]};')
            else:
                bd.write(f'{new_task[i]}')
        bd.write('\n')        

def read_task_1(unit = 1, file_name = 'stud_1.csv'):
    with open(file_name, newline = '') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if unit == 2:
                item = ', '.join(row)
                print(item)
            if unit == 1:
                for item in row:
                    print(item)
                print()

def read_task_2(unit = 1, file_name = 'stud_2.csv'):
    with open(file_name, newline = '') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            if unit == 2:
                item = ', '.join(row)
                print(item)
            if unit == 1:
                for item in row:
                    print(item)
                print()
