#!/usr/bin/python3

# test input
data = 'ne,ne,ne'
ring_size = 5
# file input
data = open('input.txt').read()

pos = (0, 0, 0)
maxdist = 0
dirdict = { 'n':(1, 0, -1), 'ne':(0, 1, -1), 'se':(-1, 1, 0), 's':(-1, 0, 1), 'sw':(0, -1, 1), 'nw':(1, -1, 0) }
for dir in data.split(','):
    pos = tuple(pos[i]+dirdict[dir][i] for i in range(3))
    maxdist = max(maxdist, sum(abs(i) for i in pos) / 2)
print('result part one', sum(abs(i) for i in pos) / 2)
print('result part two', maxdist)
