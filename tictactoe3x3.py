theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
row = ['top', 'mid', 'low']
col = ['L', 'M', 'R']


def printboard():
    for i in row:
        for j in col:
            target = i + '-' + j
            print(theBoard[target], end=" | ")

        print('\n-   -   -')


def startGame():
    printboard()
    turn = 'X'
    for i in range(9):
        while True:
            message = 'It is the turn of ' + turn
            print(message)
            keyIn = input()
            if keyIn not in theBoard or checkLocked(keyIn) == False:
                print('Invalid move. Please try again')
            else:
                theBoard[keyIn] = turn
                break
        printboard()  # updated
        if checkFinish(turn) == True:
            return turn

        if checkTied() == True:
            return 0

        # reset move for next player
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    # END GAME

# Check if a move is already played


def checkLocked(move):
    if theBoard[move] == 'X' or theBoard[move] == 'O':
        return False


def checkFinish(turn):
    # check if winning in a row
    for i in row:
        done = True
        for j in col:
            temp = i + '-' + j
            if theBoard[temp] != turn:
                done = False
        if done == True:
            return winning(turn)

    # check if winning in a col
    for j in col:
        done = True
        for i in row:
            temp = i + '-' + j
            if theBoard[temp] != turn:
                done = False
        if done == True:
            return winning(turn)

    # check if winning in a diagonal
    done = True
    for i, j in zip(row, col):
        temp = i + '-' + j
        if theBoard[temp] != turn:
            done = False
            break
    if done == True:
        return winning(turn)


# check if the game ended up tied
def checkTied():
    for i in row:
        for j in col:
            temp = i + '-' + j
            if theBoard[temp] == ' ':
                return False
    return True


# Display winning message


def winning(turn):
    print('Player of ' + turn + ' won this round !')
    return True


def play():
    print('-----------------------------------------')
    print('       WELCOME TO TIC TAC TOE 3 X 3      ')
    print('-----------------------------------------')
    X_Score = Y_Score = TiedGame = 0
    while True:
        # reset the board
        turn = 'X'
        for key in theBoard:
            theBoard[key] = ' '

        result = startGame()
        if result == 'X':
            X_Score = X_Score + 1
        elif result == 'Y':
            Y_Score = Y_Score + 1
        else:
            TiedGame = TiedGame + 1

        print('So far, player X scored: ' + str(X_Score))
        print('Player Y Scored: ' + str(Y_Score))
        print('Number of tied game: ' + str(TiedGame))
        print('Do you wanna continue playing? Anything other than Yes means No')
        choice = input()
        if choice == 'Yes':
            print('Starting a new game...')
        else:
            announcement(X_Score, Y_Score, TiedGame)
            break


def announcement(X_Score, Y_Score, tiedNo):
    space = '                  '
    print('Player X' + space + 'Player Y' + space + 'Number of Tied Game')
    print(str(X_Score) + space + str(Y_Score) + space + str(tiedNo))

    if X_Score == Y_Score:
        print('2 players have the same score!')
    elif X_Score > Y_Score:
        print('CONGRATULATION. THE WINNER IS PLAYER X')
    else:
        print('CONGRATULATION. THE WINNER IS PLAYER Y')


play()
