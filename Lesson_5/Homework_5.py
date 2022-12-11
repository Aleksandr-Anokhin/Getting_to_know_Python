
# 1. Напишите программу, удаляющую из файла все слова, содержащие "абв".

text_in_file = 'g:/Prog/Python/Getting_to_know_Python/Lesson_5/text_abv.txt'
f = open(text_in_file, 'r', encoding = 'utf8')
text_list = f.read() + ' '
f.close()
print(text_list)

text_list = list(filter(lambda x: 'абв' not in x, text_list.split()))
print(text_list)

# 2. Создайте программу для игры с конфетами человек против человека.

# Игра против робота работает, а вот человек против человека нет:(

from random import randint as numbers

take_sweet = 0
player_sweet = 0
bot_sweet = 0
total_sweet = 0
player_1 = None
player_2 = None

def start_game():
    global total_sweet
    print(" <<НАСТРОЙКА ИГРЫ>>")
    print("1. Player vs Player\n2. Player vs Bot")
    variant_game = int(input("Какой вариант игры Вы выбираете? 1 или 2: "))
    total_sweet = int(input("\nВведите количество конфет от 0 до 2021:  "))
    print("Игра началась!")
    if variant_game == 1:
        player_vs_player()
    else:
        who_is_first()
   
def player_vs_player():
    global total_sweet
    global player_1
    global player_2    
    player_1 = input('\nИгрок 1, введите имя: ')
    player_2 = input('\nИгрок 2, введите имя: ')    
    print('\nКомпьютер опеределил кто первый начнет игру.\n')

    random_number = numbers(1, 2)
    if random_number == 1:        
        play_count_1 = 0        
        print(f"Сейчас на столе {total_sweet} конфет")    
        take_sweet = int(input(f"{player_1}, Сколько конфет Вы хотите взять? "))
        if take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet:
            take_sweet = int(input(f"{player_1}, Вы берёте слишком много конфет! Попробуйте снова: "))
        total_sweet -= take_sweet
        play_count_1 += take_sweet
        if total_sweet > 0:
            random_number == 2
        else:
            print(f"Ура! {player_1}, Вы победили!") 


    else:        
        play_count_2 = 0         
        print(f"Сейчас на столе {total_sweet} конфет")     
        take_sweet = int(input(f"{player_2}, Сколько конфет Вы хотите взять? "))
        if take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet:
            take_sweet = int(input(f"{player_2}, Вы берёте слишком много конфет! Попробуйте снова: "))
        total_sweet -= take_sweet
        play_count_2 += take_sweet
        if total_sweet > 0:
            random_number == 1
        else:
            print(f"Ура! {player_2}, Вы победили!")        
   
      

def who_is_first():
    random_number = numbers(1, 2)
    if random_number == 1:
        player_turn()
    else:
        bot_turn()

def player_turn():
    global total_sweet
    global take_sweet
    global player_sweet
    print(f"Ваш ход, сейчас на столе {total_sweet} конфет")
    take_sweet = int(input("Сколько конфет Вы хотите взять? "))
    while take_sweet > 28 or take_sweet < 0 or take_sweet > total_sweet:
        take_sweet = int(input("Вы берёте слишком много конфет! Попробуйте снова: "))
    total_sweet -= take_sweet
    player_sweet += take_sweet
    if total_sweet > 0:
        bot_turn()
    else:
        print("Вы победили!")

def bot_turn():
    global total_sweet
    global take_sweet
    global bot_sweet
    take_sweet = total_sweet % 29 if total_sweet % 29 != 0 else numbers(1, 28)
    total_sweet -= take_sweet
    bot_sweet += take_sweet
    print(f"Бот взял {take_sweet} конфет. На столе осталось {total_sweet} конфет")
    if total_sweet > 0:
        player_turn()
    else:
        print("Бот победил!")
start_game()



# 3. Создайте программу для игры в "Крестики-нолики".

print('Сыграем в Крестики Нолики!\n')

board = list(range(1,10))

def victory_check(board):
    victory = [(1,2,3),(4,5,6),(7,8,9),
               (1,4,7),(2,5,8),(3,6,9),
               (1,5,9),(3,5,7)]
    for i in victory:
        if (board[i[0] - 1]) == (board[i[1] - 1]) == (board[i[2] - 1]):
            return board[i[0] - 1]
    else:
        return False

def design_board(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)

# design_board(board)

def choice(tic_tac):
    valid = False
    while not valid:
        player_index = input('Ваш ход, выберите ячейку ' + tic_tac + ' --> ')
        try:
            player_index = int(player_index)
        except:
            print('Что-то не то нажали')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index - 1]) not in 'XO'):
                board[player_index - 1] = tic_tac
                valid = True
            else:
                print('Занято')
        else:
            print('Еще раз попробуйте')

def game(board):
    counter = 0
    vic = False
    while not vic:
        design_board(board)
        if counter % 2 == 0:
            choice('X')
        else:
            choice('0')
        
        if counter > 4:
            tt_win = victory_check(board)
            if tt_win:
                print(tt_win,'Победа!')
                vic = True
                break
        counter += 1
    
        if counter > 8:
            design_board(board)
            print('Победила, ДРУЖБА)')
            break
        
game(board)



# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaasssdddwwwwwwwwwwwweeeffffff -> 4a3s3d9w3w3e6f
# 4a3s3d9w3w3e6f-> aaaasssdddwwwwwwwwwwwweeeffffff

with open('g:/Prog/Python/Getting_to_know_Python/Lesson_5/decoded.txt', 'r') as data:
    dec_txt = data.read()

def encoded_rle(alg):
    str_code = ''
    prev_char = ''
    count = 1
    for char in alg:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

str_code = encoded_rle(dec_txt)
print(str_code)

with open('g:/Prog/Python/Getting_to_know_Python/Lesson_5/encoded.txt', 'r') as data:
    dec_txt2 = data.read()

def decoded_rle(alg:str):
    count = ''
    str_decode = ''
    for char in alg:
        if char.isdigit():
            count += char 
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode

str_decode = decoded_rle(dec_txt2)
print(str_decode)


