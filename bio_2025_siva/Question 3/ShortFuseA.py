f = int(input())
ts = input().split(' ')
times = []
for time in range(f):
    times.append(int(ts[time]))
# print(times)

poss = set()

if len(times) == 1:
    a = times[0]
    poss.add(0)
    poss.add(a)
    poss.add(a/2)

if len(times) == 2:
    a = times[0]
    b = times[1]
    
    poss.add(0)
    poss.add(a)
    poss.add(b)
    poss.add(a+b)
    poss.add(a/2)
    poss.add(b/2)
    poss.add(a+b/2)
    poss.add(b+a/2)
    if b/2 - a/4 > 0:
        poss.add((b/2 - a/4)+(b-a/2))
        poss.add((b/2 - a/4))
    if a/2 - b/4 > 0:
        poss.add((a/2 - b/4)+(a-b/2))
        poss.add((a/2 - b/4))

if len(times) == 3:
    a = times[0]
    b = times[1]
    c = times[2]
    
    poss.add(0)
    poss.add(a)
    poss.add(b)
    poss.add(c)
    poss.add(a+b)
    poss.add(a+c)
    poss.add(b+c)
    poss.add(a/2)
    poss.add(b/2)
    poss.add(c/2)
    poss.add(a+b/2)
    poss.add(b+a/2)
    poss.add(a+c/2)
    poss.add(c+a/2)
    poss.add(b+c/2)
    poss.add(c+b/2)
    
    if b/2 - a/4 > 0:
        poss.add((b/2 - a/4)+(b-a/2))
        poss.add((b/2 - a/4))
    if a/2 - b/4 > 0:
        poss.add((a/2 - b/4)+(a-b/2))
        poss.add((a/2 - b/4))
    
    if c/2 - a/4 > 0:
        poss.add((c/2 - a/4)+(c-a/2))
        poss.add((c/2 - a/4))
    if a/2 - c/4 > 0:
        poss.add((a/2 - c/4)+(a-c/2))
        poss.add((a/2 - c/4))
    
    if b/2 - c/4 > 0:
        poss.add((b/2 - c/4)+(b-c/2))
        poss.add((b/2 - c/4))
    if c/2 - b/4 > 0:
        poss.add((c/2 - b/4)+(c-b/2))
        poss.add((c/2 - b/4))

if len(times) == 4:
    a = times[0]
    b = times[1]
    c = times[2]
    d = times[3]
    
    poss.add(0)
    poss.add(a)
    poss.add(b)
    poss.add(c)
    poss.add(d)
    poss.add(a+b)
    poss.add(a+c)
    poss.add(a+d)
    poss.add(b+c)
    poss.add(b+d)
    poss.add(c+d)
    poss.add(a+b+c)
    poss.add(a+b+d)
    poss.add(a+c+d)
    poss.add(b+c+d)
    poss.add(a+b+c+d)
    
    poss.add(a/2)
    poss.add(b/2)
    poss.add(c/2)
    poss.add(d/2)
    poss.add(a+b/2)
    poss.add(b+a/2)
    poss.add(a+c/2)
    poss.add(c+a/2)
    poss.add(a+d/2)
    poss.add(d+a/2)
    poss.add(b+c/2)
    poss.add(c+b/2)
    poss.add(b+d/2)
    poss.add(d+b/2)
    poss.add(c+d/2)
    poss.add(d+c/2)
    
    if b/2 - a/4 > 0:
        poss.add((b/2 - a/4) + (b - a/2))
        poss.add(b/2 - a/4)
    if a/2 - b/4 > 0:
        poss.add((a/2 - b/4) + (a - b/2))
        poss.add(a/2 - b/4)

    if c/2 - a/4 > 0:
        poss.add((c/2 - a/4) + (c - a/2))
        poss.add(c/2 - a/4)
    if a/2 - c/4 > 0:
        poss.add((a/2 - c/4) + (a - c/2))
        poss.add(a/2 - c/4)

    if b/2 - c/4 > 0:
        poss.add((b/2 - c/4) + (b - c/2))
        poss.add(b/2 - c/4)
    if c/2 - b/4 > 0:
        poss.add((c/2 - b/4) + (c - b/2))
        poss.add(c/2 - b/4)
    
    if d/2 - a/4 > 0:
        poss.add((d/2 - a/4) + (d - a/2))
        poss.add(d/2 - a/4)
    if a/2 - d/4 > 0:
        poss.add((a/2 - d/4) + (a - d/2))
        poss.add(a/2 - d/4)

    if d/2 - b/4 > 0:
        poss.add((d/2 - b/4) + (d - b/2))
        poss.add(d/2 - b/4)
    if b/2 - d/4 > 0:
        poss.add((b/2 - d/4) + (b - d/2))
        poss.add(b/2 - d/4)

    if d/2 - c/4 > 0:
        poss.add((d/2 - c/4) + (d - c/2))
        poss.add(d/2 - c/4)
    if c/2 - d/4 > 0:
        poss.add((c/2 - d/4) + (c - d/2))
        poss.add(c/2 - d/4)
    
    

print(len(poss))
# print(poss)