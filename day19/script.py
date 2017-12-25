#!/usr/bin/python3

# test input
data = '''     |          
     |  +--+    
     A  |  C    
 F---|----E|--+ 
     |  |  |  D 
     +B-+  +--+ 
                
'''
# file input
data = open('input.txt').read()

word = ''
board = [[c for c in line] for line in data.splitlines()]
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

# look for starting point
pos = tuple()
dir = dirs[2]
for i, c in enumerate(board[0]):
    if c == '|':
        pos = (i, 0)
        break

def eva(p):
    return board[p[1]][p[0]]

def addp(p, d):
    return (p[0] + d[0], p[1] + d[1])

def walk():
    global word
    global dir
    global pos
    pos = addp(pos, dir)
    cur = eva(pos)
    if cur == '+':
        for d in dirs:
            if eva(addp(pos, d)) != ' ' and d[0] != -dir[0] and d[1] != -dir[1]:
                dir = d
                break
    elif cur == ' ':
        return False
    elif cur != '|' and cur != '-':
        word += cur

    return True


stepcount = 1
while walk():
    stepcount += 1
    pass


print('result part one', word)
print('result part two', stepcount)