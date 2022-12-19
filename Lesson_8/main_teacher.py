from write_a_task import write_a_task


def main_teacher():
    
    t_id = int(input('Введите Ваш id: '))
    if t_id == 1:
        teacher_1()

    elif t_id == 2:
        teacher_2()

    else:
        print("Вы не зарегистрированы или ввели некорректно id.")

def teacher_1():
    print('<<МЕНЮ>>')
    print('1. Написать задание')
    print('2. Проверить работу')
    t_1 = input('Выберите пункт меню: ')
    if t_1 == '1':
        write_a_task()
    elif t_1 == '2':
        check_the_work()

def teacher_2():
    print('<<МЕНЮ>>')
    print('1. Написать задание')
    print('2. Проверить работу')


