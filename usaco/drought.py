def feed(cow1, cow2, corn):
    return cow1-1, cow2-1, corn + 2

t = int(input())
outputs = []

for i in range(t):
    
    # n = number of cows
    # h = list of the cows' hunger
    # mx = the index of the cow in the list h with the maximum hunger
    # mn = the index of the cow in the list h with the minimum hunger
    
    
    n = int(input())
    h = input().split(' ')
    h = [int(n) for n in h]
    corn = 0
    
    # cases where equal hunger for all cows is not possible:
    if len(h) == 2 and (h[0] % 2 == 0 and h[1] % 2 == 1) or ((h[0] % 2 == 1 and h[1] % 2 == 2)):
        outputs.append(-1)
        h = [1]
    
    # this means that every cow will have the same hunger level
    while len(set(h)) != 1:
        mx = h.index(max(h))  

        if mx == 0:
            mn = mx + 1
        elif mx == len(h) - 1:
            mn = mx - 1
        else:
            if h[mx - 1] == h[mx + 1]:
                mn = mx - 1
            else:
                mn = mx + 1
        
        h[mx], h[mn], corn = feed(h[mx], h[mn], corn)
        
        # print(*h, 'corn:', corn)
        
        if len(set(h)) == 2:
            c = []
            for hunger in h:
                c.append(h.count(hunger))
            if c[0] % 2 == 1 or c[0] % 2 == 1:
                outputs.append(-1)
                h = [1]
        
        for hunger in h:
            if hunger <= 0:
                outputs.append(-1)
                h = [1]
    
    if len(outputs) == i:
        outputs.append(corn)

for output in outputs:
    print(output)
            
# print(mx)

# print(h)