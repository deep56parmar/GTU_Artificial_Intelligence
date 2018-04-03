from node import *

def DFS(start,goal):
    depth = 100
    stack = [start]
    visited = set()
    found = False
    while stack:
        state = stack.pop()
        if state == goal:
            found = state
            break

        if state in visited or state.step > depth:
            continue
        visited.add(state)
        for s in state.next():
            stack.append(s)
    if found:
        printPath(found)
        print("solution found")
    else:
        print("no solution found")
print("DFS for 8 puzzle")
start = Node([2,0,1,4,5,3,8,7,6])
goal = Node([1,2,3,4,5,6,7,8,0])
DFS(start,goal)
