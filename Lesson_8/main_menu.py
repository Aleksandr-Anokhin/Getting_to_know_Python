from main_teacher import main_teacher



def greeting():
    print('<<УЧЕБНЫЙ ПОРТАЛ>>')

def main_menu():
    while True:
        
        print('1. Войти как Преподаватель')
        print('2. Войти как Студент') 
        n = input('Выберите пункт меню: ')

        if n == '1':
            main_teacher()
        elif n == '2':
            #student()
            print('<<МЕНЮ>>')
            enter = input('Нажмите Enter для выхода в главное меню ')
            main_menu()

        elif n == '0':
            print('Administrator')
            #admin()
