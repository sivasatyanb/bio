# note that this doesn't really work

def generateFibonacci():
    seq = [1, 2]
    for i in range(30):
        if (seq[i] + seq[i+1]) > 53316291173:
            break
        seq.append(seq[i] + seq[i+1])
    return seq

fib = generateFibonacci()

total = 0
for number in range(1, 53316291173):
    rem = number
    divs = 0
    for i in range(len(fib)-1, -1, -1):
        f = fib[i]
        if f <= rem:
            rem -= f
            divs += 1
        if divs > 3:
            break
    if divs == 3:
        print(number)
        total += 1

print(total)