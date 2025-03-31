# def generatePalindromicNumbers(limit):
#     palins = []
#     for i in range(1, limit+1):
#         string = str(i)
#         if string[::-1] == string:
#             palins.append(i)
#     return palins

# limit = 1000000
# palins = generatePalindromicNumbers(limit)

# print(len(palins))

def findSum(n):
    seqs = []
    palins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44]

    # length 2
    for p1 in palins:
        for p2 in palins:
            if p1 + p2 == n:
                seqs.append([p1, p2, p3])

    # length 3
    for p1 in palins:
        for p2 in palins:
            for p3 in palins:
                if p1 + p2 + p3 == n:
                    seqs.append([p1, p2, p3])
    
    return seqs


n = 54
# print(sorted(findSum(n)))

print([1, 9, 44], [2, 8, 44], [3, 7, 44], [4, 6, 44], [5, 5, 44])