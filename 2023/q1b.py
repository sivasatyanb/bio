def generateFibonacci():
    seq = [1, 2]
    for i in range(30):
        if (seq[i] + seq[i+1]) > 1000000:
            break
        seq.append(seq[i] + seq[i+1])
    return seq

print(max(generateFibonacci()))
# >>> 832040