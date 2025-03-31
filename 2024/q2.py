e = [n*2 for n in range(1, 100)]
o = [2*n+1 for n in range(0, 100)]
t = [n for n in range(1, 10+1) for _ in range(n)]

def combine(list1, list2):
    newList = []
    for i in range(100):
        newList.append(list2[list1[list2[i]]])
    return newList