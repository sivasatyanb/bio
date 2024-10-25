n = 1
index = 101
string = ''
five = 0

for i in range(index):
    string += str(n)
    n += 1
    if '5' in str(n):
        for letter in str(n):
            if letter == '5':
                five += 1
    if len(string) > index:
        break

print(five)