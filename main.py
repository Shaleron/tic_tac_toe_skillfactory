import random
import copy

'''
Функция регистрации игрока
'''
def playerIntroduce(player):
    name = input('Enter your name, Player: ')
    player["Name"] = name
    print(f'Ok, {name}, you are in the game')
    pass

'''
Функция розыгрыша крестика (первый ход) между игроками
'''
def markChoose(player1, player2):
    if random.randint(0, 1):
        player1["Mark"] = 'O'
        player2['Mark'] = 'X'
        tmp_str = f'{player2["Name"]} has the right to make the first move in the game'
        current_player = player2
    else:
        player1["Mark"] = 'X'
        player2['Mark'] = 'O'
        tmp_str = f'{player1["Name"]} has the right to make the first move in the game'
        current_player = player1
#    print('\n')
    print(f'{player1["Name"]}, your mark is {player1["Mark"]}')
    print(f'{player2["Name"]}, your mark is {player2["Mark"]}')
    print(tmp_str)
    return current_player

'''
Функция хода игрока
'''
def gameMove(player, gmatrix):
    print(f'{player["Name"]} move.')
    possibleRow = False
    while not(possibleRow):
        str_num = int(input(f'{player["Name"]}, specify the number of the row you want to put the mark:'))
        while not (str_num in [1, 2, 3]):
            str_num = int(input(f'{player["Name"]}, the number of the line must be 1,2 or 3. Please, try again: '))
        possibleRow = not(all(gmatrix[str_num - 1]))
        if not(possibleRow):
            print(f'The {str_num} row is totally occupied. Choose other row.')
            str_num = None
    possibleColumn = True
    while possibleColumn:
        col_num = int(input(f'{player["Name"]}, specify the number of the column you want to put the mark:'))
        while not(col_num in [1, 2, 3]):
            col_num = int(input(f'{player["Name"]}, the number of the line must be 1,2 or 3. Please, try again: '))
        possibleColumn = gmatrix[str_num - 1][col_num - 1]
        if possibleColumn:
            print(f'The position of {str_num} row and {col_num} column is occupied. Select another column')
            col_num = None
    gmatrix[str_num - 1][col_num - 1] = player["Mark"]
    pass

'''
Функция проверки выигрыша
'''
def check_is_win(player, gmatrix):
    mark = player["Mark"]
    return (check_rows_to_win(mark, gmatrix) or check_columns_to_win(mark, gmatrix) or
            check_diagonals_to_win(mark, gmatrix))


'''
Функция проверки того, что в списке содержатся одинаковые элементы и они равны искомому
'''
def check_list_to_win(mark, glist):
    gset = set(glist)
    if (len(gset) == 1) and (mark in gset):
        return True
    else:
        return False

'''
Проверка строк на наличие выигравшей
'''
def check_rows_to_win(mark, gmatrix):
    check = False
    for L in gmatrix:
        check = check or check_list_to_win(mark, L)
    return check

'''
Проверка столбцов на наличие выигравшего
'''
def check_columns_to_win(mark, gmatrix):
    check = False
    for j in range(0,3):
        column = [gmatrix[i][j] for i in range(0,3)]
        check = check or check_list_to_win(mark, column)
    return check

'''
Проверка диагоналей на наличие выигравшей
'''
def check_diagonals_to_win(mark, gmatrix):
    check = False
    diag1 = [gmatrix[i][i] for i in range(0, 3)]
    diag2 = [gmatrix[i][2-i] for i in range(0, 3)]
    return check_list_to_win(mark, diag1) or check_list_to_win(mark, diag2)


'''
Функция смены текущего игрока (перехода хода)
'''
def change_curPlayer(curPlayer, player1, player2):
    if curPlayer is player1:
        return player2
    else:
        return player1

def analize_list_to_finish(L):
    aset = set(L)
    if len(aset) == 3:
        return False
    else:
        if len(aset) == 2 and not ('' in aset):
            return False
        else:
            return True

def analize_rows_to_finish(gmatrix):
    check = False
    for L in gmatrix:
        check = check or analize_list_to_finish(L)
    return check

def analize_columns_to_finish(gmatrix):
    check = False
    for j in range(0,3):
        column = [gmatrix[i][j] for i in range(0,3)]
        check = check or analize_list_to_finish(column)
    return check

def analize_diagonals_to_finish(gmatrix):
    check = False
    diag1 = [gmatrix[i][i] for i in range(0, 3)]
    diag2 = [gmatrix[i][2-i] for i in range(0, 3)]
    return analize_list_to_finish(diag1) or analize_list_to_finish(diag2)

def check_is_finish(gmatrix):
    return analize_rows_to_finish(gmatrix) or analize_columns_to_finish(gmatrix) or analize_diagonals_to_finish(gmatrix)


'''
Функция прорисовки игрового поля
'''
def print_game_field(gmatrix):
    print('   ║ 1 | 2 | 3 ║')
    print(16 * '═')
    for i in range(0, 3):
        temp_s = ' ' + str(i + 1) + ' ║'
        for j in range(0, 3):
            if gmatrix[i][j] == '':
                s = ' '
            elif gmatrix[i][j] == 'X':
                s = '𝐗'
            else:
                s = '𝐎'
            if j != 2:
                temp_s = temp_s + ' ' + s + ' |'
            else:
                temp_s = temp_s + ' ' + s + ' ║'
        print(temp_s)
        if i != 2:
            print(16 * '\u2014')
        else:
            print(16 * '═')
    pass


        # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Player1 = {"Name": None, "Mark": None}
    Player2 = {"Name": None, "Mark": None}
    print("Let's register the players\n")
    playerIntroduce(Player1)
    playerIntroduce(Player2)
    game_continue = 'Y'
    while game_continue == 'Y':
        gameMatrix = [['', '', ''], ['', '', ''], ['', '', '']]
        print('Game starts.....')
        curPlayer = markChoose(Player1, Player2)
        for i in range(0, 9):
            gameMove(curPlayer, gameMatrix)
            print(f"This is game field after {curPlayer['Name']}'s move.")
            print_game_field(gameMatrix)
            if i >= 4:
                if check_is_win(curPlayer, gameMatrix):
                    print(f'Congradulations!!!!! {curPlayer["Name"]} is winner!!! This game is complete')
                    break
                elif not check_is_finish(gameMatrix):
                    print('There is no possibilities to win for players. Draw! The game is complete.')
                    break
                if i == 8:
                    print('Draw! The game is complete.')
            curPlayer = change_curPlayer(curPlayer, Player1, Player2)
        game_continue = input('Do you want to get another game? (Y/N): ')


