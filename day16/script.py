#!/usr/bin/python3

# test input
data = 's1,x3/4,pe/b'
programs_original = list('abcde')
# file input
data = open('input.txt').read()
programs_original = list('abcdefghijklmnop')

def dance():
    global programs
    for instr in data.split(','):
        if instr[0] == 's':
            spinmove = len(programs) - int(instr[1:])
            programs = programs[spinmove:] + programs[:spinmove]
        elif instr[0] == 'x':
            swappositions = instr[1:].split('/')
            posA = int(swappositions[0])
            posB = int(swappositions[1])
            programs[posA], programs[posB] = programs[posB], programs[posA]
        elif instr[0] == 'p':
            swapnames = instr[1:].split('/')
            posA = programs.index(swapnames[0])
            posB = programs.index(swapnames[1])
            programs[posA], programs[posB] = programs[posB], programs[posA]

programs = programs_original.copy()
dance()
print('result part one', ''.join(programs))




programs = programs_original.copy()
total_num_dances = 1000000000
patterns = [''.join(programs)]
for i in range(total_num_dances):
    dance()
    newpattern = ''.join(programs)
    if patterns[0] != newpattern:
        patterns.append(newpattern)
    else:
        break
print('pattern repeats every ', len(patterns), ' dances')
print('result part two', patterns[total_num_dances % len(patterns)])