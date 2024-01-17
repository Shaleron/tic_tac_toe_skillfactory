import random

def playerIntroduce(player):
    name = input('Enter your name, Player: ')
    player["Name"] = name
    print(f'Ok, {name}, you are in the game')
    pass

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
    print('\n')
    print(f'{player1["Name"]}, your mark is {player1["Mark"]}')
    print(f'{player2["Name"]}, your mark is {player2["Mark"]}')
    print(tmp_str)
    return current_player

def gameMove(player, gmatrix):
    print('\n')
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


def change_curPlayer(curPlayer, player1, player2):
    print(id(curPlayer))
    print(id(player1))
    print(id(player2))
    if curPlayer is player1:
        return player2
    else:
        return player1





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Player1 = {"Name": None, "Mark": None}
    Player2 = {"Name": None, "Mark": None}
    gameMatrix = [['','',''], ['','',''], ['','','']]
    print("Let's register the players\n")
    playerIntroduce(Player1)
    playerIntroduce(Player2)
    curPlayer = markChoose(Player1, Player2)
    print(gameMatrix)
    gameMove(curPlayer, gameMatrix)
    print(gameMatrix)
    curPlayer = change_curPlayer(curPlayer, Player1, Player2)
    gameMove(curPlayer, gameMatrix)
    print(gameMatrix)
    curPlayer = change_curPlayer(curPlayer, Player1, Player2)
    gameMove(curPlayer, gameMatrix)
    print(gameMatrix)
    cur_Player = change_curPlayer(curPlayer, Player1, Player2)
    gameMove(curPlayer, gameMatrix)
    print(gameMatrix)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
