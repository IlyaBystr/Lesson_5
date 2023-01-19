#38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)

# text = input("Введите текст через пробел:\n")
# print(f"Исходный текст: {text}")
# find_txt = "абв"
# lst = [i for i in text.split() if find_txt not in i]
# print(f'Результат: {" ".join(lst)}')


#40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# def encode(s):
 
#     encoding = ""
 
#     i = 0
#     while i < len(s):
#         count = 1
 
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
 
#         encoding += str(count) + s[i]
#         i = i + 1
 
#     return encoding

# if __name__ == '__main__':
 
#     s = '222223333332222211100'
#     print(encode(s))


#39(2). Создайте программу для игры в ""Крестики-нолики"". 

board = list(range(1,10))

def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print ("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("Эта клеточка уже занята")
        else:
            print ("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
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
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)