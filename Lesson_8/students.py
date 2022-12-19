from write_a_task import write_a_task

def main_students():

    st_id = int(input('Введите Ваш id: '))
    if st_id == 11:
        student_1()
    elif st_id == 12():
        student_2()
    elif st_id == 13():
        student_3()
    elif st_id == 14():
        student_4()

def student_1():
    print('<<МЕНЮ>>')
    print('1. Посмотреть задание')
    print('2. Загрузить работу')
    st_1 = input('Выберите пункт меню: ')
    if st_1 == '1':
        write_a_task()
    elif st_1 == '2':
        check_the_work()
    view_the_task