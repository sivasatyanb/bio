n, index = input().split(' ')
n = int(n)
index = int(index)
string = ''

for i in range(index):
    string += str(n)
    n += 1
    if len(string) > index:
        break

print(string[index-1])