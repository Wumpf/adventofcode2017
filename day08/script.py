#!/usr/bin/python3

# test input
data = '''b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10'''
# file input
data = open('input.txt').read()

registers = {}
highest = 0
for line in data.splitlines():
    parts = line.split()
    target, op, amount, = parts[0], parts[1], int(parts[2])
    cond_var, cond, cond_ref = parts[4], parts[5], parts[6]

    if target not in registers:
        registers[target] = 0
    if cond_var not in registers:
        registers[cond_var] = 0

    if eval(''.join(['registers[\'', cond_var, '\'] ', cond, ' ', cond_ref])):
        if op == 'inc':
            registers[target] += amount
            highest = max(highest, registers[target])
        else:
            registers[target] -= amount

print('result part one', max(registers.values()))
print('result part two', highest)