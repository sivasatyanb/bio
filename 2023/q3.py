# initialState = input().split(' ')
initialState = ['12', '0', '3', '4']
initialState = [[int(digit) for digit in n] for n in initialState]

# print(initialState)

# finalState = input().split(' ')
finalState = ['1', '32', '4', '0']
finalState = [[int(digit) for digit in n] for n in finalState]

# print(finalState[0][0])

# we will treat all pegs like a stack, so a state compremises of four stacks (where some could be empty)

def generateMoves(state):
    validMoves = []
    
    for i in range(len(state)):
        if state[i]:
            data = state[i][-1]
            
            for j in range(len(state)):
                if i != j:
                    newState = [list(peg) for peg in state]
                    newState[i].pop()
                    newState[j].append(data)
                    validMoves.append(newState)
    
    return validMoves

moves = generateMoves(initialState)

for move in moves:
    print(move)
    
print(len(moves))
