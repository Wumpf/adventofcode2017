#!/usr/bin/python3
from functools import reduce
import functools, operator

# test input
data = 'flqrgnkx'
# file input
data = 'ugkiagan'


def hash_rotate(times, lengths):
    cur = 0
    step = 0
    ring = [i for i in range(0, 256)]
    for _ in range(times):
        for l in lengths:
            old = ring[:]
            for i in range(cur + l-1, cur-1, -1):
                ring[cur % 256] = old[i % 256]
                cur += 1
            cur += step
            step += 1
    return ring

def knot_hash_bin(input):
    part2 = hash_rotate(64, [s for s in input.encode()] + [17, 31, 73, 47, 23])
    hashstring = ''
    for i in range(0,16):
        n = reduce(operator.xor, part2[i * 16 : (i+1)*16])
        hashstring += bin(n)[2:].zfill(8)
    return hashstring



field = []
num_used = 0
for i in range(128):
    knot_hash = knot_hash_bin(data + '-' + str(i))
    num_used += sum(1 if x=='1' else 0 for x in knot_hash)
    field.append(list(knot_hash))

print('result part one', num_used)


num_regions = 0

def flood_fill(x, y):
    if x < 0 or y < 0 or x >= 128 or y >= 128 or field[x][y] != '1':
        return False
    field[x][y] = '0'
    flood_fill(x+1, y)
    flood_fill(x-1, y)
    flood_fill(x, y+1)
    flood_fill(x, y-1)
    return True

for y, line in enumerate(field):
    for x, square in enumerate(line):
        if flood_fill(x, y):
            num_regions += 1

print('result part two', num_regions)