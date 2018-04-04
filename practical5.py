from node import *

def astar(start,goal):
    depth = 75
    priotity_queue = PriorityQueue()
    h_val = start.manhattan_distance() + start.hamming_distance()

    f_val = h_val + start.step
    priotity_queue.push(start, f_val)
    visited = set()
    found = False
    while not priotity_queue.isEmpty():
        state = priotity_queue.pop()
        if state == goal:
            found = state
            break

        if state in visited or state.step > depth:
            continue

        visited.add(state)

        for s in state.next():
            h_val_s = s.manhattan_distance() + s.hamming_distance()
            f_val_s = h_val_s + s.step
            priotity_queue.push(s, f_val_s)

    if found:
        printPath(found)
        print("Find solution")
    else:
        print("No solution found")

print("8-puzzle solution using A*")
start = Node([2,0,1,4,5,3,8,7,6])
goal = Node([1,2,3,4,5,6,7,8,0])
astar(start,goal)
