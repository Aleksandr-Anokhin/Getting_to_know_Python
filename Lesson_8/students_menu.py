import os
os.chdir(os.path.dirname(__file__))

from write_a_task import write_a_task
from check_the_work import check_task_1
from check_the_work import check_task_2

def students_menu():
    print("\nHello!")
    st_id = int(input('Введите Ваш id: '))
    if st_id == 1:
        student_1()
    elif st_id == 2:
        student_2()
    

def student_1():
    print('\n<<МЕНЮ>>')
    print('1. Посмотреть задание')
    print('2. Загрузить работу')
    st_1 = input('Выберите пункт меню: ')
    if st_1 == '1':
        write_a_task()
    elif st_1 == '2':
        check_task_1()
    else:
        print('Выберите необходимый пункт меню.')

def student_2():
    print('\n<<МЕНЮ>>')
    print('1. Посмотреть задание')
    print('2. Загрузить работу')
    st_2 = input('Выберите пункт меню: ')
    if st_2 == '1':
        write_a_task()
    elif st_2 == '2':
        check_task_2()
    else:
        print('Выберите необходимый пункт меню.')


