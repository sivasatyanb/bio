initialState = ['12', '', '3', '4']
initialState = [[int(digit) for digit in n] if n else [] for n in initialState]

finalState = ['1', '32', '4', '']
finalState = [[int(digit) for digit in n] if n else [] for n in finalState]

# we will treat all pegs like a stack, so a state compremises of four stacks (where some could be empty)

def generateMoves(state):
    validMoves = []
    # this is each peg
    for i in range(len(state)):
        if len(state[i]) != 0:
            ball = state[i][-1]
            # this is each ball
            for j in range(len(state)): 
                if i != j:
                    # copy old state
                    newState = [peg for peg in state]
                    # copy bottom of stack
                    newState[i] = newState[i][:-1]
                    # change top of stack
                    newState[j] = newState[j] + [ball]
                    validMoves.append(newState)
    return validMoves

# recursive function
def findMinimumMoves(currentState, finalState, depth):
    if currentState == finalState:
        return depth
    
    for nextState in generateMoves(currentState):
        moves = min(findMinimumMoves(nextState, finalState, depth + 1))
    
    return moves

moves = findMinimumMoves(initialState, finalState, 0)

print(moves)

# moves = generateMoves(initialState)

# print(len(moves))

# for move in moves:
#     print(*move, '\n')

