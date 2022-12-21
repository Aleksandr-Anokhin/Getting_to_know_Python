import os
os.chdir(os.path.dirname(__file__))

import csv
file_name = 'all_data.csv'

def csv_to_data(file_name = 'all_data.csv'):
    with open(file_name, newline='') as f:
        csv_f = csv.reader(f, delimiter=';')
        data = []
        for row in csv_f:
            data.append(row)
    return data

def export_to_xml(data = csv_to_data()):
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<account_data>\n'
    for row in data:
        first_name, last_name, id_number = row
        xml += '    <contact>\n'
        xml += '        <Name>{}</Name>\n' \
            .format(first_name)
        xml += '        <Last_name>{}</Last_name>\n' \
            .format(last_name)
        xml += '        <id_number>{}</id_number>\n' \
            .format(id_number)
        
    xml += '</account_data>'
    with open('all_data.xml', 'w') as page:
        page.write(xml)
    return data