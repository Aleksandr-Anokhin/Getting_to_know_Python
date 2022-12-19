

def write_a_task():
    number = int(input('Введите номер задания: '))
    text = input('Введите текст задания: ')
    new_list = [number, text]
    save_task(new_list)

def save_task(new_task):
    with open('task.csv', 'a') as bd:
        for i in range(len(new_task)):
            if i != len(new_task) - 1:
                bd.write(f'{new_task[i]};')
            else:
                bd.write(f'{new_task[i]}')
        bd.write('\n')
