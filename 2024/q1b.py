n = 1
n_str = str(n)
while len(n_str) < 101:
    n += 1
    n_str += str(n)
    
print(n_str)
print(n_str[:101].count('5'))