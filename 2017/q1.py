row = list(input())
    
currentRow = row
for i in range(len(row)-1):
    newRow = []
    for j in range(len(currentRow)-1):
        items = [currentRow[j], currentRow[j+1]]
        if items[0] == items[1]:
            newRow.append(items[0])
        else:
            if 'R' not in items:
                newRow.append('R')
            elif 'G' not in items:
                newRow.append('G')
            elif 'B' not in items:
                newRow.append('B')
    currentRow = newRow

print(currentRow[0])