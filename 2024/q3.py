def calculateScore(string):
    total = 0
    for letter in string:
        score = ord(letter) - 64
        total += score
    return total

def validateString(string):
    valid = True
    for i in range(len(string) - 1):
        if string[i] == string[i+1]:
            valid = False
        else:
            continue
    return valid

def generateStrings(score):
    # for i in range(26):
    #     letters.append(chr(i+65))
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    length = 1
    strings = []
    start = 0
    end = 1
    
    # this works for adj letters - now we can think about duplicating
    for i in range(26):
        for j in range(26-i):
            string = letters[start:end]
            print(string, start, end)
            if (validateString(string)) and (calculateScore(string) == score) and (string not in strings):
                strings.append(string)
            elif calculateScore(string) > score:
                break
            end += 1
        start += 1
        end = start + 1
        
    strings.sort()
    return strings

# print(calculateScore('ZZAZ'))

# print(validateString('ABABB'))

print(generateStrings(20))

# print('abcde'[3:0:-1])

def main():
    string = input()

    score = calculateScore(string)

    strings = generateStrings(score)
    
    print(strings)

    print(strings.index([string]) + 1)

# if __name__ == '__main__':
#     main()