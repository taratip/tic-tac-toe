#!/usr/bin/python
import random

# Display board
def display_board(board):
    for row in range(3):
        for column in range(3):
            if column < 2:
                print ' ' + board[row][column] + ' |',
            else:
                print ' ' + board[row][column]
        if row != 2:
            print '---|----|----'

# ask for player input position
def player_input(currentPlayer):
    print 'Enter position (1-9) for',
    print 'X' if currentPlayer == 0 else 'O'

    position = ''

    valid_value = '1 2 3 4 5 6 7 8 9'
    
    while True:
        try:
            data = raw_input()
            if data not in valid_value.split():
                print 'Invalid value. Please enter number between 1-9.'
                continue
            position = int(data)
            break
        except ValueError:
            print 'Invalid value. Please enter number between 1-9.'

    return position

# place marker on position
def place_marker(board, marker, position):
    row = get_row(position)
    column = get_column(position)

    if space_check(board, row, column):
        board[row][column] = marker
        return True
    else:
        return False

# check if win
def win_check(board,mark,position):
    x = get_row(position)
    y = get_column(position)

    # check column
    for column in range(3):
        if (board[x][column] != mark):
            break
        if (column == 2):
            return True

    # check row
    for row in range(3):
        if (board[row][y] != mark):
            break;
        if (row == 2):
            return True

    # check diag
    if (x == y):
        for i in range(3):
            if (board[i][i] != mark):
                break;
            if (i == 2):
                return True

    # check anti diag
    if (x + y == 2):
        for i in range(3):
            if (board[i][2-i] != mark):
                break;
            if (i == 2):
                return True
    return False

# get row for position
def get_row(position):
    if position % 3 == 0:
        return position/3 -1
    else:
        return position/3

# get column for position
def get_column(position):
    position_y = position % 3
    if (position_y == 1):
        y = 0
    elif (position_y == 2):
        y = 1
    elif (position_y == 0):
        y = 2
    return y

# choose the first player
def choose_first():
    return random.randint(0,2)

# check if position is taken
def space_check(board, row, column):
    return board[row][column] == ' '

# check if board is full
def full_board_check(board):
    for row in range(3):
        for col in range(3):
            if space_check(board, row, col):
                return False

    return True

# ask if want to replay
def replay():
    isReplay = ''

    while not (isReplay == 'y' or isReplay == 'n'):
        isReplay = raw_input('Do you want to play again (y/n): ').lower()

    if isReplay == 'y':
        return True
    else:
        return False

# clear a board
def clear_board(board):
    for x in range(3):
        for y in range(3):
            board[x][y] = ' '

#------------Game start------------------#
print('Welcome to Tic Tac Toe!')
board = [[' ' for x in range(3)] for y in range(3)]

currentPlayer = choose_first()
isGameOn = True

while True:
    while isGameOn:
        display_board(board)

        marker = 'X' if currentPlayer == 0 else 'O'
        position = player_input(currentPlayer)

        while True:
            if place_marker(board, marker, position):
                break
            else:
                print 'The position is already taken.'
                position = player_input(currentPlayer)

        if win_check(board,marker,position):
            display_board(board)
            print marker + ' is a Winner!'
            isGameOn = False
        else:
            if full_board_check(board):
                display_board(board)
                print 'It\'s a Draw!'
                isGameOn = False
            else:
                currentPlayer = 1 if currentPlayer == 0 else 0

    if not replay():
        print 'Game Over!'
        break
    else:
        clear_board(board)
        isGameOn = True
