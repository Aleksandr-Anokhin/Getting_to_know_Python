import os
os.chdir(os.path.dirname(__file__))

def ad_read_data():
    print("1. Поиск в разделе Преподаватели")
    print("2. Поиск в разделе Студенты")
    ad_read = input('Введите номер пункта меню: ')

    if ad_read == '1':
        #read teacher file
        print('Введите фамилию для поиска среди записей: ')

    elif ad_read == '2':
        #read students file
        print('Введите фамилию для поиска среди записей: ')
    