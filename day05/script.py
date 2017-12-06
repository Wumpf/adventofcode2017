#!/usr/bin/python3
import math

# test input
data = '''0
3
0
1
-3'''
# file input
data = open('input.txt').read()

# part 1
instructions = [int(instr) for instr in data.split()]
pos = 0
num_steps = 0
while pos < len(instructions):
    instructions[pos] += 1
    pos += instructions[pos] - 1
    num_steps += 1
print('result part one', num_steps)

# part 2
instructions = [int(instr) for instr in data.split()]
pos = 0
num_steps = 0
while pos < len(instructions):
    oldpos = pos
    pos += instructions[pos]
    instructions[oldpos] += 1 if instructions[oldpos] < 3 else -1
    num_steps += 1
print('result part two', num_steps)