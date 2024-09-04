'''
i.

The substring 11111 will appear between the integers 111 and 112:
between positions/digits 223 and 227 inclusive

'''

n = 1
string = ''
while n < 987654321:
    string += str(n)
    n += 1

print(len(string) - 1)

