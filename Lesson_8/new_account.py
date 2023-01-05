import os
os.chdir(os.path.dirname(__file__))

from write_a_task import write_a_task

def new_account():
    nc = input('Выберите действие: ')
    print('1. Создать учетную запись преподавателя.')
    print('2. Создать учетную запись студента.')
    
    if nc == '1':
        make_account_teacher()
        print('Данные успешно сохранены')
    elif nc == '2':
        make_account_stud()
        print('Данные успешно сохранены')     

def make_account_teacher():
    first_name = input_firstname()
    last_name = input_lastname()
    id_number = input('Номер id: ')
    new_list_teacher = [first_name, last_name, id_number]
    write_a_task(new_list_teacher)
    

def make_account_stud():
    first_name = input_firstname()
    last_name = input_lastname()
    id_number = input('Номер id: ')
    new_list_stud = [first_name, last_name, id_number]
    write_a_task(new_list_stud)
       

def input_firstname():
    first = input('Имя: ')
    fi_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + fi_name

def input_lastname():
    first = input('Фамилия: ')
    la_name = first[1:]
    firstchar = first[0]
    return firstchar.upper() + la_name


    
    
    



