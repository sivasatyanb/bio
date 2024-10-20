def generateFibonacci():
    seq = [1, 2]
    for i in range(10):
        seq.append(seq[i] + seq[i+1])
    return seq

fib = generateFibonacci()
# print(fib)

n = int(input())
divisors = []
i = 0

while i < len(fib):
    if n == 0:
        break
    if fib[i] > n:
        divisors.append(fib[i-1])
        n -= fib[i-1]
        # print(n)
        i = 0
    else:
        i += 1

print(*divisors)