
filename = 'phonebook.txt'
myfile = open(filename, 'a+')
myfile.close


def greeting():
    print('<<ТЕЛЕФОННЫЙ СПРАВОЧНИК>>')

def menu():
    print('\nМЕНЮ')
    print('1. Добавить новую запись')
    print('2. Вывод записей на экран')
    print('3. Импорт')
    print('4. Экспорт')
    print('5. Поиск')
    print('6. Выход\n') 
    n = input('Выберите пункт меню: ')

    if n == '1':
        new_contact()
        enter = input('Нажмите Enter для завершения')
        menu()
    elif n == '2':
        myfile = open(filename, 'r+')
        filecontents = myfile.read()
        if len(filecontents) == 0:
            print('Записей нет')
        else:
            print(filecontents)
        myfile.close
        enter = input('Нажмите Enter для завершения')
        menu()
    elif n == '5':
        searchcontact()
        enter = input('Нажмите Enter для завершения')
        menu()
    elif n == '6':
        print('Спасибо за просмотр')
    else:
        print('Пожалуста, введите номер пункта меню')
        enter = input('Нажмите Enter для завершения')
        menu()
    
def new_contact():
    first_name = input('Имя: ')
    last_name = input('Фамилия: ')
    patronymic = input('Отчество: ')
    date_of_birth = input('Дата рождения: ')
    phone_number = input('Номер телефона: ')
    mail = input('Эл. почта: ')
    contact_details = ('[' + first_name + ' ' + last_name + ' ' + patronymic + '; ' + date_of_birth + '; ' + phone_number + '; ' + mail)
    myfile = open(filename, 'a')
    myfile.write(contact_details)
    print('Данные успешно сохранены')

#def searchcontact():
greeting()
menu()

        
            








