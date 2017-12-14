#!/usr/bin/python3
from namedlist import namedlist

# test input
data = '''0: 3
1: 2
4: 4
6: 4'''
# file input
data = open('input.txt').read()

firewall = [tuple([int(i) for i in line.split(':')]) for line in data.splitlines()]

collision = filter(lambda p: p[0] % (p[1]*2 - 2) == 0, firewall)
severity = sum(map(lambda p: p[0] * p[1], collision))
print('result part one', severity)


for delay in range(1, 99999999):
    collision = filter(lambda p: (p[0]+delay) % (p[1]*2 - 2) == 0, firewall)
    if not any(collision):
        print('result part two', delay)
        break
