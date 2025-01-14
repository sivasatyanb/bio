# no feuds:

import math
import copy

# works
def claim(hive, colour, pos, facing):
    # init claim
    if colour == 'r':
        hive[pos-1][facing-1] = 'r'
    elif colour == 'b':
        hive[pos-1][facing-1] = 'b'
    
    # left
    if pos % 5 != 1 and facing == 5:
        hive[pos-1-1][2-1] = hive[pos-1][facing-1]
    # right
    if pos % 5 != 0 and facing == 2:
        hive[pos+1-1][5-1] = hive[pos-1][facing-1]
        
    # bottom left
    if (pos < 21 and str(pos)[-1] != '1') and facing == 4:
        if int(str(pos)[-1]) <= 5:
            hive[pos+4-1][1-1] = hive[pos-1][facing-1]
        elif int(str(pos)[-1]) > 5:
            hive[pos+5-1][1-1] = hive[pos-1][facing-1]
        
    # bottom right
    if (pos < 21 and str(pos)[-1] != '0') and facing == 3:
        if int(str(pos)[-1]) <= 5:
            hive[pos+5-1][6-1] = hive[pos-1][facing-1]
        elif int(str(pos)[-1]) > 5:
            hive[pos+6-1][6-1] = hive[pos-1][facing-1]
            
    # top left
    if (pos > 5 and str(pos)[-1] != '1') and facing == 6:
        if int(str(pos)[-1]) <= 5:
            hive[pos-6-1][3-1] = hive[pos-1][facing-1]
        elif int(str(pos)[-1]) > 5:
            hive[pos-5-1][3-1] = hive[pos-1][facing-1]
          
    # top right
    if (pos > 5 and str(pos)[-1] != '0') and facing == 1:
        if int(str(pos)[-1]) <= 5:
            hive[pos-5-1][4-1] = hive[pos-1][facing-1]
        elif int(str(pos)[-1]) > 5:
            hive[pos-4-1][4-1] = hive[pos-1][facing-1]
        
    return hive

# works
def countControl(hive):
    red_control = 0
    blue_control = 0
    for hex in hive:
        if hex.count('r') > hex.count('b'):
            red_control += 1
        elif hex.count('r') < hex.count('b'):
            blue_control += 1
    return red_control, blue_control

# works
def skirmish(hive, r_steps, b_steps, r_pos, b_pos, r_facing, b_facing):
    # change orientation
    if r_facing != 6:
        r_facing += 1
    else:
        r_facing = 1
    if b_facing != 1:
        b_facing -= 1
    else:
        b_facing = 6
        
    # change position
    if r_pos + r_steps > 25:
        r_pos = (r_pos + r_steps) - 25
    else:
        r_pos += r_steps
    if b_pos + b_steps > 25:
        b_pos = (b_pos + b_steps) - 25
    else:
        b_pos += b_steps
    
    # claim
    hive = claim(hive, 'r', r_pos, r_facing)
    hive = claim(hive, 'b', b_pos, b_facing)

    # print(hive, 'r_pos:', r_pos, 'b_pos:', b_pos, 'r_facing:', r_facing, 'b_facing:', b_facing)
    return hive, r_steps, b_steps, r_pos, b_pos, r_facing, b_facing

hive = []
for i in range(25):
    hive.append(['', '', '', '', '', ''])

# number of steps
r_steps, b_steps = input().split(' ')
r_steps = int(r_steps)
b_steps = int(b_steps)
# orientation
r_facing = 1
b_facing = 6
# position of drone (current hex)
r_pos = 1
b_pos = 25
# initial claims
hive = claim(hive, 'r', r_pos, r_facing)
hive = claim(hive, 'b', b_pos, b_facing)

skirms, feuds = input().split(' ')
skirms = int(skirms)
feuds = int(feuds)

for i in range(skirms-1):
    hive, r_steps, b_steps, r_pos, b_pos, r_facing, b_facing = skirmish(hive, r_steps, b_steps, r_pos, b_pos, r_facing, b_facing)

# print('after skirms:')
# print(hive, 'r_pos:', r_pos, 'b_pos:', b_pos, 'r_facing:', r_facing, 'b_facing:', b_facing)

r, b = countControl(hive)

print(r)
print(b)