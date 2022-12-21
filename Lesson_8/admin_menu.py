import os
os.chdir(os.path.dirname(__file__))

from export_data import csv_to_data
from ad_read_data import ad_read_data
from new_account import new_account

def admin_menu():
    print('<<МЕНЮ>>')
    print('1. Экспорт данных')
    print('2. Просмотр данных')
    print('3. Создание учетной записи')
    
    ad = input('Введите номер пункта меню: ')

    if ad == '1':
        csv_to_data()

    elif ad == '2':
        ad_read_data() 

    elif ad == '3':
        new_account()

    
        
