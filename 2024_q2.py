# 2b) 2
# 2c) 

# # initialising lists

e = []
o = []
t = []

for i in range(1, 100):
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
    for j in range(i):
        t.append(i)
        
# print(e)
# print(o)
# print(t)
        
# merging lists
        
string = 'TT'

one = string[0]
two = string[1]   

if one == 'O':
    one = o
elif one == 'E':
    one = e
else:
    one = t
    
if two == 'O':
    two = o
elif two == 'E':
    two = e
else:
    two = t
    
new = []

for i in range(2):
    
    n = i
    n = two[n]
    print(n)
    n = one[n-1]
    print(n)
    n = two[n-1]
    print(n)
    new.append(n)
        
print(new)
























# string, index = input().split(' ')

# closing_bracket_indexes = []

# for i in range(len(string) -1, -1, -1):
    
#     # print(string[i])
    
#     if string[i] == ')':
#         closing_bracket_indexes.append(i)

# number_of_brackets = len(closing_bracket_indexes)

