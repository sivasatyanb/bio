n = int(input())
inputs = input().split(' ')

total = (n * (n + 1)) // 2

for number in inputs:
    number = int(number)
    total -= number

print(total)

# 14 / 14 :)