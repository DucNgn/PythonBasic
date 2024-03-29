import os

# The basic board of a 3x3 tictactoe game
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
row = ['top', 'mid', 'low']
col = ['L', 'M', 'R']
LtoR_Diago = ['top-L', 'mid-M', 'low-R']
RtoL_Diago = ['top-R', 'mid-M', 'low-L']

#Banner generated by figlet
def welcome():
    os.system('clear')
    os.system('figlet Tic Tac Toe 3 x 3')


# A method prints the tic tac toe board when being requested
def printboard(divideLine):
    welcome()
    for i in row:
        for j in col:
            target = i + '-' + j
            print('| ' + theBoard[target], end =" ")

        print(divideLine)


def startGame():
    welcome()
    divideLine = '|\n-------------'
    printboard(divideLine)
    turn = 'X'
    for i in range(9):
        makeMove(turn)
        printboard(divideLine) 

        if isFinish(turn) == True:
            return turn

        if isTied() == True:
            return -1

        # reset move for next player
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


#Ask user to make a move
def makeMove(turn):
    while True:
            print('It is the turn of ' + turn)
            keyIn = input()
            if keyIn not in theBoard or isLocked(keyIn) is True:
                print('Invalid move. Please try again')
            else:
                theBoard[keyIn] = turn
                break


#-----------------------------------SUPPORT METHODS FOR THE GAME----------------
# Check if a move is already played
def isLocked(move):
    if theBoard[move] == 'X' or theBoard[move] == 'O':
        return True

# Check if a person won the game by checking row, col, and diagonal
def isFinish(turn):
    # check if winning in a row
    listOfLoc = []
    for i in row:
        for j in col:
            temp = i + '-' + j
            listOfLoc.append(temp)
        if isWinLine(listOfLoc, turn) is True:
            return winning(turn)
        else:
            listOfLoc.clear()
    
    # Check if winning in a col
    for j in col:
        for i in row:
            temp = i + '-' + j
            listOfLoc.append(temp)
        if isWinLine(listOfLoc, turn) is True:
            return winning(turn)
        else:
            listOfLoc.clear()

    # Check if winning in a diagonal
    if isWinLine(LtoR_Diago, turn) is True or isWinLine(RtoL_Diago, turn) is True:
        return winning(turn)
    
# Check if the game ends up tied
def isTied():
    for i in row:
        for j in col:
            temp = i + '-' + j
            if theBoard[temp] == ' ':
                return False
    return True

#--------SUPPORT METHODS TO FIND A WINNER --------------------
#A method to check if a list of location is valid for a win
def isWinLine(potentialList, turn):
    for i in potentialList:
        if theBoard[i] != turn:
            return False
    return True

# Highlight the move of the winner.
def highLightWinner(turn):
    for key, value in theBoard.items():
        if value == turn:
            theBoard[key] = '[' + turn + ']'
        else:
            theBoard[key] = " " + value + " "

# Display winning message
def winning(turn):
    print('Player of ' + turn + ' won this round !')
    highLightWinner(turn)

    divideLine = '|\n-------------------'
    printboard(divideLine)
    return True

#-----------------------------------END OF SUPPORT METHODS FOR THE GAME---------------------

# Main method to start the game
def play():
    X_Score = O_Score = TiedGame = 0
    while True:
        # Reset the board
        turn = 'X'
        for key in theBoard:
            theBoard[key] = ' '

        result = startGame()
        if result == 'X':
            X_Score = X_Score + 1
        elif result == 'O':
            O_Score = O_Score + 1
        else:
            TiedGame = TiedGame + 1

        print('So far, player X scored: ' + str(X_Score))
        print('Player O Scored: ' + str(O_Score))
        print('Number of tied game: ' + str(TiedGame))
        print('Do you want to continue playing? Anything other than Yes means No')
        choice = input()
        if choice.lower() == 'yes':
            print('Starting a new game...')
        else:
            announcement(X_Score, O_Score, TiedGame)
            break

# Display an announcement sums up the game
def announcement(X_Score, O_Score, tiedNo):
    space = '                  '
    print('Player X' + space + 'Player O' + space + 'Number of Tied Game')
    print(str(X_Score) + space + str(O_Score) + space + str(tiedNo))

    if X_Score == O_Score:
        print('2 players have the same score!')
    elif X_Score > O_Score:
        print('CONGRATULATION. THE WINNER IS PLAYER X')
    else:
        print('CONGRATULATION. THE WINNER IS PLAYER O')

play() #Start the game session.