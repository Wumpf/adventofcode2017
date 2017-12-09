#!/usr/bin/python3
from namedlist import namedlist
import re

# test input
data = '''pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)'''
# file input
data = open('input.txt').read()

Program = namedlist('program', 'name parent weight children_str children')
programs = {}
regex = re.compile(r'(\D+) \((\d+)\)( \-> (\D+))?')
for line in data.splitlines():
    r = regex.match(line)
    name = r.group(1)
    programs[name] = Program(name=name, weight=int(r.group(2)), parent=None, children_str=r.group(4), children=[])

for _, program in programs.items():
    if program.children_str is not None:
        for child in program.children_str.split(','):
            program_child = programs[child.strip()]
            program_child.parent = program
            program.children.append(program_child)

root = next(filter(lambda x: x.parent is None, programs.values()))
print('result part one', root.name)

def weight_check(parent):
    weights = [weight_check(child) for child in parent.children]
    if len(weights) > 1:
        if weights[0] is not weights[1]:
            if len(weights) > 2:
                ref = weights[2]
            else:
                raise NotImplementedError
        else:
            ref = weights[0]
        for i, w in enumerate(weights):
            if w != ref:
                print('result part two', ref - (w - parent.children[i].weight))
                break
    return sum(weights) + parent.weight

weight_check(root)