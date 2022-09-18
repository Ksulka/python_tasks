# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
print()
print('1.Задача: Удалить из текста все слова, содержащие ""абв""')
with open('text.txt', 'r', encoding = 'utf_8') as data:
    stroka = data.read().split()
print(f'В файле записано: {stroka}')
print('Удалили все слова с абв и получили: ')
print(' '.join([word for word in stroka if 'абв' not in word]))
print()
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

print('2.Задача: Игра 2021 конфета')
import random
def candy_game(k):
    summ_konf = 100
    if k == 0:
        name_1 = input('Игрок 1, введите ваше имя --> ')
        if name_1 == '':
            name_1 = 'Игрок №1'
        name_2 = input('Игрок 2, введите ваше имя --> ')
        if name_2 == '':
            name_2 = 'Игрок №2'
        print('''
        На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
        Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
        Все конфеты оппонента достаются сделавшему последний ход. 
        ''')
        print('Начинаем игру')
        hod = random.randint(1,2)
        if hod == 1:
            print(f'По жеребьевке 1 ход у {name_1}')
            while summ_konf > 0:
                print(f'На столе {summ_konf} кофет.')
                print(f'{name_1}, введите количество конфет, которое вы возьмете от 1 до 28 ')
                while True:
                    try:
                        gamer_1 = int(input("Введите число: "))
                        if 1 <= gamer_1 <= 28:
                            print('OK')
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Вы ввели не число или число не входит в указанный диапазаон. Попробуйте снова: ")
                summ_konf-=gamer_1
                if summ_konf <= 0:
                    print(f'Выйграл {name_1}! Поздравляем!')
                    break
                else:
                    print(f'Осталось {summ_konf} кофет.') 
                    print(f'{name_2}, введите количество конфет, которое возьмете вы от 1 до 28')
                    while True:
                        try:
                            gamer_2 = int(input("--> "))
                            if 1 <= gamer_2 <= 28:
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("Вы ввели не число или число не входит в указанный диапазаон. Попробуйте снова: ")
                summ_konf-=gamer_2
            else:
                print(f'Выйграл {name_2}! Поздравляем!')
        else:
            print(f'По жеребьевке 1 ход у {name_2}')
            while summ_konf > 0:
                print(f'На столе {summ_konf} кофет.')
                print(f'{name_2}, введите количество конфет, которое вы возьмете от 1 до 28 ')
                while True:
                    try:
                        gamer_2 = int(input("--> "))
                        if 1 <= gamer_2 <= 28:
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Вы ввели не число или число не входит в указанный диапазаон. Попробуйте снова: ")
                summ_konf-=gamer_2
                if summ_konf <= 0:
                    print(f'Выйграл {name_2}! Поздравляем!')
                    break
                else:
                    print(f'Осталось {summ_konf} кофет.')
                    print(f'{name_1}, введите количество конфет, которое возьмете вы от 1 до 28 ')
                    while True:
                        try:
                            gamer_1 = int(input("--> "))
                            if 1 <= gamer_1 <= 28:
                                print('OK')
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("Вы ввели не число или число не входит в указанный диапазаон. Попробуйте снова: ")
                summ_konf-=gamer_1
            else:
                print(f'Выйграл {name_1}! Поздравляем!')
    elif k == 1:
        name_1 = input('Игрок, введите ваше имя --> ')
        if name_1 == '':
            name_1 = 'Игрок №1'
        name_2 = 'Bot'
        
        print('''
        На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
        Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
        Все конфеты оппонента достаются сделавшему последний ход. 
        ''')
        print('Начинаем игру')
        hod = random.randint(1,2)
        if hod == 1:
            print(f'По жеребьевке 1 ход у {name_1}')
            while summ_konf > 0:
                print(f'На столе {summ_konf} кофет.')
                print(f'{name_1}, введите количество конфет, которое вы возьмете от 1 до 28')
                while True:
                    try:
                        gamer_1 = int(input("--> "))
                        if 1 <= gamer_1 <= 28:
                            print('OK')
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Вы ввели не число или число не входит в указанный диапазаон. Попробуйте снова: ")
                summ_konf-=gamer_1
                if summ_konf <= 0:
                    print(f'Выйграл {name_1}! Поздравляем!')
                    break
                else:
                    gamer_2 = random.randint(1,28)
                    print(f'Осталось {summ_konf} кофет. {name_2} берет {gamer_2} конфет(ы)')        
                    summ_konf-=gamer_2
            else:
                print(f'Выйграл {name_2}! Сожалеем, {name_1}...')
        else:
            print(f'По жеребьевке 1 ход у {name_2}')
            while summ_konf > 0:
                print(f'На столе {summ_konf} кофет.')
                gamer_2 = gamer_2 = random.randint(1,28)
                print(f'{name_2} взял {gamer_2} конфет(ы)')
                summ_konf-=gamer_2
                if summ_konf <= 0:
                    print(f'Выйграл {name_2}! Сожалеем {name_1}...')
                    break
                else:
                    print(f'Осталось {summ_konf} кофет. {name_1}, введите количество конфет, которое возьмете вы от 1 до 28  ')
                    while True:
                        try:
                            gamer_1 = int(input("--> "))
                            if 1 <= gamer_1 <= 28:
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("Вы ввели не число или число не входит в указанный диапазаон. Попробуйте снова: ")
                summ_konf-=gamer_1
            else:
                print(f'Выйграл {name_1}! Поздравляем!')
    elif k == 2:
        name_1 = input('Игрок, введите ваше имя --> ')
        if name_1 == '':
            name_1 = 'Игрок №1'
        name_2 = 'Super Bot'
        
        print('''
        На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
        Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
        Все конфеты оппонента достаются сделавшему последний ход. 
        ''')
        print('Начинаем игру')
        hod = random.randint(1,2)
        if hod == 1:
            print(f'По жеребьевке 1 ход у {name_1}')
            while summ_konf > 0:
                print(f'На столе {summ_konf} кофет.')
                print(f'{name_1}, введите количество конфет, которое вы возьмете от 1 до 28')
                while True:
                    try:
                        gamer_1 = int(input("--> "))
                        if 1 <= gamer_1 <= 28:
                            
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Вы ввели не число или число не входит в указанный диапазаон. Попробуйте снова: ")
                summ_konf-=gamer_1
                if summ_konf <= 0:
                    print(f'Выйграл {name_1}! Поздравляем!')
                    break
                else:
                    gamer_2 = summ_konf % 29
                    if gamer_2 == 0:
                        gamer_2 = random.randint(1,28)
                    print(f'Осталось {summ_konf} кофет. {name_2} берет {gamer_2} конфет(ы)')        
                    summ_konf-=gamer_2
            else:
                print(f'Выйграл {name_2}! Сожалеем, {name_1}...')
        else:
            print(f'По жеребьевке 1 ход у {name_2}')
            while summ_konf > 0:
                print(f'На столе {summ_konf} кофет.')
                gamer_2 = summ_konf % 29
                print(f'{name_2} взял {gamer_2} конфет(ы)')
                summ_konf-=gamer_2
                if summ_konf <= 0:
                    print(f'Выйграл {name_2}! Сожалеем {name_1}...')
                    break
                else:
                    print(f'Осталось {summ_konf} кофет.')
                    print(f'{name_1}, введите количество конфет, которое возьмете вы от 1 до 28  ')
                    while True:
                        try:
                            gamer_1 = int(input("--> "))
                            if 1 <= gamer_1 <= 28:
                                break
                            else:
                                raise ValueError
                        except ValueError:
                            print("Вы ввели не число или число не входит в указанный диапазаон. Попробуйте снова: ")
                summ_konf-=gamer_1
            else:
                print(f'Выйграл {name_1}! Поздравляем!')

print('''
Выберите режим игры:
0 - игра с другом
1 - игра с Ботом
2 - игра с Супер-Ботом
''')
while True:
    try:
        mode = int(input("--> "))
        if 0 <= mode <= 2:
            break
        else:
            raise ValueError
    except ValueError:
        print("Вы ввели не число или число не входит в указанный диапазон. Попробуйте снова: ")
candy_game(mode)
print()


# Создайте программу для игры в ""Крестики-нолики"".
print('3.Задача: игра в Крестики-нолики')

board = list(range(1,10))

def draw_board(board):
    
    for i in range(3):
        print("", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "")
        print("-" * 10)
        

def take_input(player_token):
   valid = False
   while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if(str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def take_input_bot(player_token):
    valid = False
    while not valid:
        player_answer = random.randint(1,9) 
        if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
            print("Поле после хода бота:")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def check_can_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
        if board[each[0]] == board[each[1]] and str(board[each[2]]) not in 'XO': 
            return board[each[2]]
        elif board[each[2]] == board[each[0]] and str(board[each[1]]) not in 'XO':
            return board[each[1]]
        elif board[each[1]] == board[each[2]] and str(board[each[0]]) not in 'XO':
            return board[each[0]]
   return False

def take_input_super_bot(player_token):
    valid = False
    while not valid:
        tmp = check_can_win(board)
        if tmp:
            player_answer = tmp
            board[player_answer-1] = player_token
            valid = True
            print("Поле после хода бота:") 
        else:
            player_answer = random.randint(0,9)
            if(str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
                print("Поле после хода бота:")

def game(board,mode):
    if mode == 0:
        counter = 0
        win = False
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                take_input("X")
            else:
                take_input("O")
            counter += 1
            if counter > 4:
                tmp = check_win(board)
                if tmp:
                    print(tmp, "выиграл!")
                    win = True
                    break
            if counter == 9:
                print("Ничья!")
                break
        return draw_board(board)
    elif mode == 1:
        counter = 0
        win = False
        print('Бот играет за 0')
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                take_input("X")
            else:
                take_input_bot("O")
            counter += 1
            if counter > 4:
                tmp = check_win(board)
                if tmp:
                    print(tmp, "выиграл!")
                    win = True
                    break
            if counter == 9:
                print("Ничья!")
                break   
        return draw_board(board)
    elif mode ==2:
        counter = 0
        win = False
        print('Бот играет за 0')
        while not win:
            draw_board(board)
            if counter % 2 == 0:
                take_input("X")
            else:
                take_input_super_bot("O")
            counter += 1
            if counter > 4:
                tmp = check_win(board)
                if tmp:
                    print(tmp, "выиграл!")
                    win = True
                    break
            if counter == 9:
                print("Ничья!")
                break   
        return draw_board(board)

print('''
Выберите режим игры:
0 - игра с другом
1 - игра с Ботом
2 - игра с Супер-Ботом
''')
while True:
    try:
        mode = int(input("--> "))
        if 0 <= mode <= 2:
            break
        else:
            raise ValueError
    except ValueError:
        print("Вы ввели не число или число не входит в указанный диапазон. Попробуйте снова: ")
game(board,mode)


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
print('4.Задача: RLE алгоритм.')

def write_file(name,st):
    with open(name, 'w') as data:
        data.write(st)

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

with open('tekst_old.txt', 'r') as data:
    text_bez_szhatiya = data.read()
szhatiy_text = coding(text_bez_szhatiya)
write_file('tekst_new.txt',szhatiy_text)
print(f'Текст из файла: {text_bez_szhatiya}')
print(f'Сжатый текст: {szhatiy_text}')
print(f'Дешифрованный текст {decoding(szhatiy_text)}')
print()


