#!/usr/bin/python3

# test input
# data = '''5 1 9 5
# 7 5 3
# 2 4 6 8'''
# file input
data = open('input.txt').read()

matrix = [[int(i) for i in row.split()] for row in data.splitlines()]
print(matrix)
result = sum([max(row) - min(row) for row in matrix])
print('result part one:', result)