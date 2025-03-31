import sys

def calculateScore(string):
    total = 0
    for letter in string:
        score = ord(letter) - 64
        total += score
    return total

def validateString(string):
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True

def generateCombinations(length, string, currentScore, score, strings):
    letters = [chr(i + 65) for i in range(26)]
    if currentScore > score:
        return
    if length == 0:
        if currentScore == score and validateString(string):
            strings.append(string)
            # print(string)
        return

    for letter in letters:
        newScore = currentScore + (ord(letter) - 64)
        generateCombinations(length - 1, string + letter, newScore, score, strings)

def generateStrings(score):
    
    strings = []

    for length in range(1, 13):
        generateCombinations(length, '', 0, score, strings)

    strings.sort()
    return strings

def main():
    string = sys.stdin.readline()[:-1]
    # string = input().strip().upper()
    
    # print(string)

    score = calculateScore(string)

    strings = generateStrings(score)
    
    print(len(strings))

    position = strings.index(string) + 1

    print(position)

if __name__ == '__main__':
    main()

# b) 16
# c) 