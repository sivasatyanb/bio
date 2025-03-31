# part "../2024"b:

# output = 12

n = 1
string = ''
while len(string) < 101:
    string += str(n)
    n += 1

if len(string) > 101:
    string = string[:101]

five = 0
for char in string:
    if char == '5':
        five += 1
print(five)