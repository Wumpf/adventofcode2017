#!/usr/bin/python3
import math

# test input
#data = '''0 2 7 0'''
# file input
data = open('input.txt').read()

cur_bank = tuple(int(i) for i in data.split())
oldstates = { cur_bank: 0 }
num_banks = len(cur_bank)

def get_extra(index, num_extra, max_index, n, add):
    dist = (index - max_index) % num_banks
    extra = 0 if dist > num_extra else 1
    return add if index == max_index else (n + add + extra)

num_steps = 0
while True:
    max_index, max_val = max(enumerate(cur_bank), key=lambda x: x[1])
    add = int(max_val / num_banks)
    num_extra = max_val % num_banks
    num_steps += 1
    cur_bank = tuple(get_extra(index, num_extra, max_index, n, add) for index, n in enumerate(cur_bank))
    if cur_bank in oldstates:
        print('result part one', num_steps)
        print('result part two', num_steps - oldstates[cur_bank])
        break
    oldstates[cur_bank] = num_steps
