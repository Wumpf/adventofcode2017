#!/usr/bin/python3

data = '''../.# => ##./#../...
.#./..#/### => #..#/..../..../#..#'''
# file input
data = open('input.txt').read()


rule_list_pattern = []
rule_list_results = []
for line in data.splitlines():
    left, right = line.split('=>')
    rule_list_pattern += [left.strip().split('/')]
    rule_list_results += [right.strip().split('/')]

def ressolve_pattern(subblock):
    for i, comp in enumerate(rule_list_pattern):
        if comp == subblock:
            return rule_list_results[i]
    return None

def enhance(subblock):
    for _ in range(4):
        newpattern = ressolve_pattern(subblock)
        if newpattern != None:
            return newpattern
        # flip to right
        newpattern = ressolve_pattern([x[::-1] for x in subblock])
        if newpattern != None:
            return newpattern

        # rotate 90 deg to right
        subblock = [''.join(subblock[x][len(subblock) - 1 - y] for x in range(len(subblock))) for y in range(len(subblock))]
    print('no pattern matched any version. should never happen')
    return None

def iteration(last_pattern):
    subblock = []
    divisor = 2 if len(last_pattern) % 2 == 0 else 3
    newpattern = [""] * (len(last_pattern) + int(len(last_pattern) / divisor))
    for y in range(0, len(last_pattern), divisor):
        for x in range(0, len(last_pattern), divisor):
            subblock = [last_pattern[y + i][x:(x+divisor)] for i in range(divisor)]
            subblock_enhanced = enhance(subblock)
            for newy, line in enumerate(subblock_enhanced):
                newpattern[int(y/divisor)*(divisor + 1) + newy] += line
    return newpattern

def count_on(pattern):
    return sum(sum(l == '#' for l in line) for line in last_pattern)

last_pattern = '''.#.
..#
###'''.splitlines()

for i in range(5):
    last_pattern = iteration(last_pattern)
    print(i)
print('result part one', count_on(last_pattern))

for i in range(5, 18):
    last_pattern = iteration(last_pattern)
    print(i)
print('result part two', count_on(last_pattern))
