#!/usr/bin/python3

# test input
data = '''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''
# file input
data = open('input.txt').read()

lines = data.splitlines()

nodes = [[] for i in range(len(lines))]
for i, line in enumerate(lines):
    for edge in line.split()[2:]:
        target = int(edge.strip(','))
        nodes[i].append(target)
        nodes[target].append(i)

def visit(node, visted):
    for child in node:
        if child not in visited:
            visited.add(child)
            visit(nodes[child], visited)

visited = set()
visit(nodes[0], visited)
print('result part one', len(visited))
#print(nodes)


num_groups = 1
for node in range(len(nodes)):
    if node not in visited:
        visit(nodes[node], visited)
        num_groups += 1
print('result part two', num_groups)
