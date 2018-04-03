from node import *

start = Node([2,0,1,4,5,3,8,7,6])
goal = Node([1,2,3,4,5,6,7,8,0])
print("welcome to 8 puzzle problem. . . . . .")
printPath(start)

while start != goal:
    action = input(" w s a d for up/down/left/right : ")
    number = start.board.index(0)
    if action == 'w':
        start = start.moveUp(number)
    elif action == 's':
        start = start.moveDown(number)
    elif action == 'a':
        start = start.moveLeft(number)
    elif action == 'd':
        start = start.moveRight(number)
    else:
        print("choose right option")
    print("Heuristic Value for current node is  ",start.manhattan_distance())
    print(start)
