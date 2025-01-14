from collections import deque

# initialState = ['12', '', '3', '4']

initialState = input().split(' ')

global finalState
finalState = input().split(' ')

initialState = [[int(digit) for digit in n] if n != '0' else [] for n in initialState]
finalState = [[int(digit) for digit in n] if n != '0' else [] for n in finalState]

# print(finalState)

# print(initialState)

def generateMoves(state):
    validMoves = []
    # this is each peg
    for i in range(len(state)):
        if len(state[i]) != 0:
            # this is the ball at the top of each peg
            ball = state[i][-1]
            # this is every peg that the selected ball can move to
            for j in range(len(state)): 
                # only move if current peg != new peg
                if i != j:
                    # copy old state
                    newState = [peg for peg in state]
                    # remove ball from current peg
                    newState[i] = state[i][:-1]
                    # add ball to new peg
                    newState[j] = state[j] + [ball]
                    validMoves.append(newState)
    return validMoves

def breadthFirstSearch(initialState):
    visited = set()
    queue = deque([(initialState, 0)])
    
    while queue:
        currentState, depth = queue.popleft()
        hash = tuple(tuple(peg) for peg in currentState)
        # print(hash)
        
        if hash in visited:
            continue
        
        visited.add(hash)

        if currentState == finalState:
            return depth

        for nextState in generateMoves(currentState):
            queue.append((nextState, depth + 1))

result = breadthFirstSearch(initialState)
print(result)

# moves = generateMoves(initialState)

# print(len(moves))

# for move in moves:
#     print(*move)