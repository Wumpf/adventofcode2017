#!/usr/bin/python3

# test input
data = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
data = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
data = '<{o"i!a,<{i<a>'
# file input
data = open('input.txt').read()

group_depth = 0
score = 0
garbage_amount = 0
garbage = False
it = iter(data)
for c in it:
    if c == '!':
        next(it)
    elif garbage:
        if c == '>':
            garbage = False
        else:
            garbage_amount += 1
    else:
        if c == '<':
            garbage = True
        elif c == '{':
            group_depth += 1
            score += group_depth
        elif c == '}':
            group_depth -= 1

print('result part one', score)
print('result part two', garbage_amount)