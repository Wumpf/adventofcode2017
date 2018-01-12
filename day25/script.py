#!/usr/bin/python3

# Hardcoding the state using example data is much easier than parsing the whole thing programmatically...

# preallocate band, hopefully large enough
band = [0] * 999999
band_pos = int(len(band) / 2)
state = 'A'

def execute(instr):
    global band_pos
    global state
    band[band_pos] = instr[0]
    band_pos += instr[1]
    state = instr[2]
    
states = {
    'A': ((1, 1, 'B'), (0, 1, 'F')),
    'B': ((0, -1, 'B'), (1, -1, 'C')),
    'C': ((1, -1, 'D'), (0, 1, 'C')),
    'D': ((1, -1, 'E'), (1, 1, 'A')),
    'E': ((1, -1, 'F'), (0, -1, 'D')),
    'F': ((1, 1, 'A'), (0, -1, 'E')),
}
for _ in range(12425180):
    state = states[state]
    execute(state[0] if band[band_pos] == 0 else state[1])

print('result part one', sum(band))
print('result part two', 0)