#!/usr/bin/python3

# data = '''0/2
# 2/2
# 2/3
# 3/4
# 3/5
# 0/1
# 10/1
# 9/10'''
# file input
data = open('input.txt').read()

partdict = {}
parts = []
for part in data.splitlines():
    stra, strb = part.split('/')
    a, b = int(stra), int(strb)
    part = [False, a, b]
    parts.append(part)
    for i in [a, b]:
        if i in partdict:
            partdict[i].append(part)
        else:
            partdict[i] = [part]


strongestbridge = 0
longestbridge_strength = 0
longestbridge_length = 0

def find_strongest_rec(current_connector, score, length):
    global strongestbridge
    global longestbridge_length
    global longestbridge_strength

    strongestbridge = max(score, strongestbridge)
    if longestbridge_length < length:
        longestbridge_strength = score
        longestbridge_length = length
    elif longestbridge_length == length:
        longestbridge_strength = max(score, longestbridge_strength)

    usable_parts = partdict.get(current_connector, None)
    if usable_parts is not None:
        score += current_connector
        for part in filter(lambda x: not x[0], usable_parts):
            part[0] = True
            new_connector = part[1] + part[2] - current_connector
            find_strongest_rec(new_connector, score + new_connector, length + 1)
            part[0] = False

find_strongest_rec(0, 0, 0)


print('result part one', strongestbridge)
print('result part two', longestbridge_strength)