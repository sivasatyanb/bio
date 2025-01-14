def generateRows():
    combs = set()
    row = ['R'] * 9
    for j in range(9):
        row[j] = 'G'
        for k in range(9):
            row[k] = 'K'
            string = ''
            for l in row:
                string += l
            combs.add(string)
    
    return combs

print(generateRows())
                

# row = list(input())
    
# currentRow = row
# for i in range(len(row)-1):
#     newRow = []
#     for j in range(len(currentRow)-1):
#         items = [currentRow[j], currentRow[j+1]]
#         if items[0] == items[1]:
#             newRow.append(items[0])
#         else:
#             if 'R' not in items:
#                 newRow.append('R')
#             elif 'G' not in items:
#                 newRow.append('G')
#             elif 'B' not in items:
#                 newRow.append('B')
#     currentRow = newRow

# print(currentRow[0])