n, i = input().split(' ')
n = int(n)
i = int(i)
n_str = str(n)
while len(n_str) < i:
    n += 1
    n_str += str(n)
    
# print(n_str)
print(n_str[i-1])