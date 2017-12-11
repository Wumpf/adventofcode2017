#!/usr/bin/python3
from functools import reduce
import functools, operator

# test input
data = '3, 4, 1, 5'
ring_size = 5
# file input
data = open('input.txt').read()
ring_size = 256


def hash_rotate(times, lengths):
    cur = 0
    step = 0
    ring = [i for i in range(0, ring_size)]
    for _ in range(times):
        for l in lengths:
            old = ring[:]
            for i in range(cur + l-1, cur-1, -1):
                ring[cur % ring_size] = old[i % ring_size]
                cur += 1
            cur += step
            step += 1
            #print(ring)
    return ring

part1 = hash_rotate(1, [int(s) for s in data.split(',')])
print('result part one', part1[0] * part1[1])

part2 = hash_rotate(64, [s for s in data.encode()] + [17, 31, 73, 47, 23])
hashstring = ''
for i in range(0,16):
    n = reduce(operator.xor, part2[i * 16 : (i+1)*16])
    hashstring += '%0.2x' % n
print('result part two', hashstring)