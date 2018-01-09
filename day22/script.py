#!/usr/bin/python3
import copy

data = '''..#
#..
...'''
# file input
data = open('F:/Development/current_development/adventofcode2017/day22/input.txt').read()

target_gridsize = 501   # enough for all tasks
memory = [list(s) for s in data.splitlines()]
to_add_left_right = int((target_gridsize - len(memory)) / 2)
for i in range(len(memory)):
    memory[i] = ['.'] * to_add_left_right  + memory[i] + ['.'] * to_add_left_right
memory = [['.'] * target_gridsize for _ in range(to_add_left_right)] + memory + [['.'] * target_gridsize for _ in range(to_add_left_right)]
original_memory = copy.deepcopy(memory)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]   # +1 to rotate right

curdiri = 3
curpos = (int(len(memory) / 2), int(len(memory) / 2))
total_infections = 0
for _ in range(10000):
    cur_is_infected = memory[curpos[1]][curpos[0]] == '#'
    curdiri = (curdiri + int(cur_is_infected) * 2 - 1) % 4
    memory[curpos[1]][curpos[0]] = '.' if cur_is_infected else '#'
    curpos = (curpos[0] + dirs[curdiri][0], curpos[1] + dirs[curdiri][1])
    total_infections += not cur_is_infected
print('result part one', total_infections)


# state encodes direction we need to rotate
# clean        3
# weakend      0
# infected     1
# flagged      2
memory = [[(3 if elem == '.' else 1) for elem in line] for line in original_memory]
curdiri = 3
curpos = (int(len(memory) / 2), int(len(memory) / 2))
total_infections = 0

for _ in range(10000000):
    oldstate = memory[curpos[1]][curpos[0]]
    curdiri = (curdiri + oldstate) % 4
    memory[curpos[1]][curpos[0]] = (oldstate + 1) % 4
    curpos = (curpos[0] + dirs[curdiri][0], curpos[1] + dirs[curdiri][1])
    total_infections += (oldstate == 0)
print('result part two', total_infections)