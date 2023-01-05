import os
os.chdir(os.path.dirname(__file__))

from teacher_menu import teacher_menu
from students_menu import students_menu
from admin_menu import admin_menu

def greeting():
    print('\n<<УЧЕБНЫЙ ПОРТАЛ>>')

def main_menu():
    while True:
        
        print('1. Войти как Преподаватель')
        print('2. Войти как Студент') 
        n = input('Выберите пункт меню: ')

        if n == '1':
            teacher_menu()
            
        elif n == '2':
            students_menu()
            
        elif n == '0':
            print('\nAdministrator')
            admin_menu()

greeting()
main_menu()
