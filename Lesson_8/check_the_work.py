import csv

def read_task(unit = 1, file_name = 'task.csv'):
    with open(file_name, newline = '') as f:
        reader = csv.reader(f, delimiter='; ')
        for row in reader:
            if unit == 2:
                item = ', '.join(row)
                print(item)
            if unit == 1:
                for item in row:
                    print(item)
                print()