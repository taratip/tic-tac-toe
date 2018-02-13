#!/usr/bin/python
currentPlayer = 0
symbol = 'x'
moveCount = 0

#initialize each row to null
Matrix = [[' ' for x in range(3)] for y in range(3)]

isWin = False

while not isWin:
    if currentPlayer == 0:
        print ('enter position for x')
        symbol = 'x'
    else:
        print('enter position for o: ')
        symbol = 'o'

    position_x = raw_input('row: ')
    position_y = raw_input('column: ')

    while True:
        if Matrix[int(position_x)-1][int(position_y)-1] == ' ':
            Matrix[int(position_x)-1][int(position_y)-1] = symbol
            moveCount+=1;
            break
        else:
            print 'This position is taken. Enter a new position:'
            position_x = raw_input('row: ')
            position_y = raw_input('column: ')

    x = int(position_x)-1
    y = int(position_y)-1

    for row in range(3):
        for column in range(3):
            if column < 2:
                print ' ' + Matrix[row][column] + ' |',
            else:
                print ' ' + Matrix[row][column]
        if row <> 2:
            print '---|----|----'

    # check column
    for column in range(3):
        if (Matrix[x][column] != symbol):
            break
        if (column == 2):
            isWin = True

    # check row
    for row in range(3):
        if (Matrix[row][y] != symbol):
            break;
        if (row == 2):
            isWin = True

    # check diag
    if (x == y):
        for i in range(3):
            if (Matrix[i][i] != symbol):
                break;
            if (i == 2):
                isWin = True

    # check anti diag
    if (x + y == 2):
        for i in range(3):
            if (Matrix[i][2-i] != symbol):
                break;
            if (i == 2):
                isWin = True

    if (moveCount == (3**2)):
        break

    if isWin:
        break

    currentPlayer = 0 if currentPlayer == 1 else 1

if not isWin:
    print 'Draw'
else:
    if currentPlayer == 0:
        print 'Player X wins!'
    else:
        print 'Player O wins!'
