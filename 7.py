import os

turn = 'X'
win = False
spaces = 9

def draw(board):
    for i in range(6, -1, -3): 
        print(' ' + board[i] + '|' + board[i+1] + '|' + board[i+2])

def takeinput(board, spaces, turn):
    pos = -1
    print(turn + "'s turn:")
    while pos == -1:
        try:
            print("Pick position 1-9:")
            pos = int(input())
            if pos < 1 or pos > 9:
                pos = -1
            elif board[pos - 1] != ' ':
                pos = -1
        except:
            print("Enter a valid position")
            spaces -= 1
    board[pos - 1] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
    return board, spaces, turn

def checkwin(board):
    # Check rows
    for i in range(0, 3):
        r = i * 3
        if board[r] != ' ' and board[r] == board[r+1] == board[r+2]:
            return board[r]

    # Check columns
    for i in range(0, 3):
        if board[i] != ' ' and board[i] == board[i+3] == board[i+6]:
            return board[i]

    # Check diagonals
    if board[0] != ' ' and board[0] == board[4] == board[8]:
        return board[0]

    if board[2] != ' ' and board[2] == board[4] == board[6]:
        return board[2]

    return 0

board = [' ']*9

while not win and spaces:
    draw(board)
    board, spaces, turn = takeinput(board, spaces, turn)
    win = checkwin(board)
    os.system('cls')  # Use 'clear' on Linux/MacOS, 'cls' on Windows
    draw(board)

if not win and not spaces:
    print("Draw")
elif win:
    print(f'{win} wins')

input()
