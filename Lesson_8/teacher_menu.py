import os
os.chdir(os.path.dirname(__file__))

from write_a_task import write_a_task
from check_the_work import read_task_1
from check_the_work import read_task_2

def teacher_menu():
    
    t_id = int(input('Введите Ваш id: '))
    if t_id == 1:
        teacher_1()

    elif t_id == 2:
        teacher_2()

    else:
        print("Вы не зарегистрированы или ввели некорректно id.")

def teacher_1():
    print('\n<<МЕНЮ>>')
    print('1. Написать задание')
    print('2. Проверить работу')
    t_1 = input('Выберите пункт меню: ')
    if t_1 == '1':
        write_a_task()
    elif t_1 == '2':
        st_id = input('Введите id студента: ')
        if st_id == '1':
            read_task_1()
        elif st_id == '2':
            read_task_2()

def teacher_2():
    print('\n<<МЕНЮ>>')
    print('1. Написать задание')
    print('2. Проверить работу')
    t_1 = input('Выберите пункт меню: ')
    if t_1 == '1':
        write_a_task()
    elif t_1 == '2':
        st_id = input('Выберите пункт меню: ')
        if st_id == '1':
            read_task_1()
        elif st_id == '2':
            read_task_2()

