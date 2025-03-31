from collections import deque

def generateStates(state):
    pass

def breadthFirstSearch(state, finalState):
    visited = set()
    distance  = 0
    hash = tuple(tuple(peg for peg in state))
    
    visited.add(hash)
    
    queue = deque([distance, state])
    
    while queue:
        nextStates = generateStates(state)
        for state in nextStates:
            if state in visited:
                pass
            if state == finalState:
                return distance
            else:
                queue.add()