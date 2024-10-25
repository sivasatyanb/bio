# part "../2024"a:

n, index = input().split(' ')

n = int(n)
index = int(index)
i = index

string = ''
string += str(n)
i -= len(str(n))

while True:
    n += 1
    string += str(n)
    i -= len(str(n))

    # print(string)
    # print(i)

    if i <= 0:
        print(string)
        print(int(string[index-1]))
        break