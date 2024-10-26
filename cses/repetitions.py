string = input()

count = 0
counts = []

for i in range(len(string)):
    if string[i] != string[-1]:
        if string[i] == string[i+1]:
            count += 1
        elif count > 0:
            counts.append(count)
            # count = 0
        else:
            count = 0
    else:
        if string[i] == string[i-1]:
            count += 1
            counts.append(count)
    print(count, *counts)

if len(counts) == 0:
    print(1)
else:
    print(max(counts))

# 8/14 :( (for now)