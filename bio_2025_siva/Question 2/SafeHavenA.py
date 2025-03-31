# def checkGridFull(grid):
#     for row in grid:
#         for col in row:
#             if col == '':
#                 return False
#     return True

# def initialiseGame(n, r_steps, g_steps):
#     grid = []
#     for i in range(n):
#         row = []
#         for j in range(n):
#             row.append('')
#         grid.append(row)
        
#     grid[0][0] = 'r'
#     lastIndex = [0, 0]
#     # turn is odd for green, even for red
#     turn = 1
#     while not checkGridFull(grid):
#         if turn % 2 == 0:
#             colour = 'g'
#         else:
#             colour = 'r'
        
#         g_steps_rem = g_steps
#         r_steps_rem = r_steps
        
#         start = [0, 0]
        
#         if lastIndex == [n, n]:
#             start = [0, 0]
        
#         if lastIndex[1] % n == 0:
#             start[0] = lastIndex[0] + 1
#             start[1] = 0
        
#         for row in grid:
#             for square in row:
#                 if square == '':
#                     g_steps_rem -= 1


n, r, g = input().split(' ')
n = int(n)
r_steps = int(r)
g_steps = int(g)
print('2 1')