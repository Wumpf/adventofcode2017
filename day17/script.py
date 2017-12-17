#!/usr/bin/python3

# test input
data = 3
# file input
data = 354

num_inserts = 2018
buffer = [0]
pos = 0
for i in range(1, num_inserts):
    insertpos = (pos + data) % len(buffer) + 1
    buffer.insert(insertpos, i)
    pos = insertpos
print('result part one', buffer[(insertpos + 1) % len(buffer)])



num_inserts = 50000000
pos = 1
value = 0
for i in range(1, num_inserts):
    insertpos = (pos + data) % i + 1
    pos = insertpos
    if pos == 1:
        value = i
print('result part two', value)

# too high: 49998922