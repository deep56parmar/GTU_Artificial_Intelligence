import random

def drawBoard(board):
    print("   ")
    print(board[9]," ",board[8]," ",board[7])
    print("   ")
    print(".........")
    print("   ")
    print(board[6]," ",board[5]," ",board[4])
    print("   ")
    print(".........")
    print(board[3]," ",board[2]," ",board[1])
    print("   ")
    print(".........")

def inputPlayerLetter():
    letter = ""
    while not(letter == 'X' or letter == '0'):
        letter = input("Chose your symbol (0/X) : ").upper()
    if letter == 'X':
        return ["X","0"]
    else:
        return ["0","X"]

def whoGoesFirst():
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

def makeMove(board,letter,move):
    board[move] = letter

def isWinner(bo,le):
    return ((bo[7] == le and bo[8] == le and bo[9]== le) or
    (bo[4] == le and bo[5] == le and bo[6]== le) or
    (bo[1] == le and bo[2] == le and bo[3]== le) or
    (bo[7] == le and bo[4] == le and bo[1]== le) or
    (bo[8] == le and bo[5] == le and bo[2]== le) or
    (bo[9] == le and bo[6] == le and bo[3]== le) or
    (bo[7] == le and bo[5] == le and bo[3]== le) or
    (bo[9] == le and bo[5] == le and bo[1]== le) )

def getBoardCopy(board):
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board,move):
    return board[move] == ''

def getPlayerMove(board):
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        move = input("What is your next move ? (1-9) : ")
    return int(move)

def 
