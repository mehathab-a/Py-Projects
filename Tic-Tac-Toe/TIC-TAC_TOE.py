# Create the Game TIC-TAC_TOE
# Computer Randomizes one of the player is user requires

# --------

# Part-1:
import random

board = [' '] * 9


def draw_board(board):
    row1 = f'{board[0]}|{board[1]}|{board[2]}'
    row2 = f'{board[3]}|{board[4]}|{board[5]}'
    row3 = f'{board[6]}|{board[7]}|{board[8]}'
    print(row1 + '\n' + row2 + '\n' + row3)


def win(pos, play):
    if play == '2':
        play = 'Player 2'
    if play == '1':
        play == "Computer"
    posx = board.index(pos)
    if posx == 0 or posx == 3 or posx == 6:
        if board[posx] == pos and board[posx + 1] == pos and board[posx + 2] == pos:
            print(f"{play} Wins\n\tGame Over")
            return True
        elif posx == 0 or posx == 1 or posx == 2:
            if board[posx] == pos and board[posx + 3] == pos and board[posx + 6] == pos:
                print(f"{play} Wins\n\tGame Over")
                return True
    return False


def inp(player, x_o):
    if board.count(' ') > 0:
        if player == 'Player 1' or str(player) == '2':
            usr = int(input(f'Enter {player} Position:'))
            while ' ' not in board[usr - 1]:
                usr = int(input("Re-Enter Position: "))
        else:
            usr = int(random.randint(1, 9))
            while ' ' not in board[usr - 1]:
                usr = int(random.randint(1, 9))
        board[usr - 1] = x_o
        draw_board(board)


draw_board(board)
print("Select Player 2:")
player = int(input("1 Play with Computer\n2 play with Friend\n Enter: "))
while 1 == 1:
    inp("Player 1", 'X')
    if win('X', 'Player 1'):
        break
    inp(player, 'O')
    if win('O', f'{player}'):
        break
    if board.count(' ') == 0:
        print("Game Over")
        break
