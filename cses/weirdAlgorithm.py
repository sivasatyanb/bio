n = int(input())
outputs = []

while n != 1:
    outputs.append(n)
    if n % 2 == 0:
        n //= 2
    else:
        n = (n * 3) + 1
outputs.append(1)

print(*outputs)

# 14 / 14 :)