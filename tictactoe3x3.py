# The basic board of a 3x3 tictactoe game
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
row = ['top', 'mid', 'low']
col = ['L', 'M', 'R']
LtoRDiago = ['top-L', 'mid-M', 'low-R']
RtoLDiago = ['top-R', 'mid-M', 'low-L']

# A method prints the Sudoku board when requested
def printboard(divideLine):
    for i in row:
        for j in col:
            target = i + '-' + j
            print('| ' + theBoard[target], end =" ")

        print(divideLine)


def startGame():
    divideLine = '|\n-------------'
    printboard(divideLine)
    turn = 'X'
    for i in range(9):
        while True:
            print('It is the turn of ' + turn)
            keyIn = input()
            if keyIn not in theBoard or checkLocked(keyIn) == False:
                print('Invalid move. Please try again')
            else:
                theBoard[keyIn] = turn
                break
        printboard(divideLine)  # updated board

        if checkFinish(turn) == True:
            return turn

        if checkTied() == True:
            return -1

        # reset move for next player
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

#-----------------------------------SUPPORT METHODS FOR THE GAME----------------------------
# Check if a move is already played
def checkLocked(move):
    if theBoard[move] == 'X' or theBoard[move] == 'O':
        return False

# Check if a person won the game by checking row, col, and diagonal
def checkFinish(turn):
    # check if winning in a row
    listOfLoc = []
    for i in row:
        for j in col:
            temp = i + '-' + j
            listOfLoc.append(temp)
        if checkLocs(listOfLoc, turn) == True:
            return winning(turn)
        else:
            listOfLoc.clear()
    
    # Check if winning in a col
    for j in col:
        for i in row:
            temp = i + '-' + j
            listOfLoc.append(temp)
        if checkLocs(listOfLoc, turn) == True:
            return winning(turn)
        else:
            listOfLoc.clear()

    # Check if winning in a left-> right diagonal
    if checkLocs(LtoRDiago, turn) == True or checkLocs(RtoLDiago, turn) == True:
        return winning(turn)
    
# Check if the game ended up tied
def checkTied():
    for i in row:
        for j in col:
            temp = i + '-' + j
            if theBoard[temp] == ' ':
                return False
    return True

#--------SUPPORT METHODS TO FIND A WINNER --------------------
#A method to check if a list of location is valid for a win
def checkLocs(aList, turn):
    for i in aList:
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
    print('-----------------------------------------')
    print('       WELCOME TO TIC TAC TOE 3 X 3      ')
    print('-----------------------------------------')
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