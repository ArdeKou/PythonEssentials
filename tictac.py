from random import randrange

def DisplayBoard(board):
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ',board[0][0],'  |  ',board[0][1],'  |  ',board[0][2],'  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ',board[1][0],'  |  ',board[1][1],'  |   ',board[1][2],' |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ',board[2][0],'  |  ',board[2][1],'  |   ',board[2][2],' |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    
def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    move = None
    while move not in range(1,10):
        move = int(input('Enter your move: '))
        if board[(move - 1) // 3][(move % 3) - 1] == 'X' or board[(move - 1) // 3][(move % 3) - 1] == 'O':
            move = None
            print('Illegal move')
    board[(move - 1) // 3][(move % 3) - 1] = 'O'
    return VictoryFor(board, 'O')


def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == sign:
            return True
        elif  board[0][i] == board[1][i] == board[2][i] == sign:
            return True
    if board[0][0] == board[1][1] == board [2][2] == sign:
        return True
    if board[2][0] == board[1][1] == board[0][2] == sign:
        return True
    return False

def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    freeSpaces = ()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 'X' and  board[i][j] != 'O':
                freeSpaces += (i, j)
    return freeSpaces
    
def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    move = None
    while move not in range(1,10):
        move = randrange(1,10)
        if board[(move - 1) // 3][(move % 3) - 1] == 'X' or board[(move - 1) // 3][(move % 3) - 1] == 'O':
            move = None
    board[(move - 1) // 3][(move % 3) - 1] = 'X'
    return VictoryFor(board, 'X')

board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
play = True
while play:
    DisplayBoard(board)
    if MakeListOfFreeFields(board) == ():
        print('Tie!')
        play = False
        continue
    if EnterMove(board):
        DisplayBoard(board)
        print('You won!')
        play = False
        continue
    if DrawMove(board):
        DisplayBoard(board)
        print('PC won!')
        play = False
        continue