#!/usr/bin/python3

# test input
# data = '''5 9 2 8
# 9 4 7 3
# 3 8 6 5'''
# file input
data = open('input.txt').read()

def find_evenly_divisible_result(row):
    for index, elem0 in enumerate(row):
        for elem1 in row[(index+1):]:
            if elem0 % elem1 == 0:
                return int(elem0 / elem1)
            if elem1 % elem0 == 0:
                return int(elem1 / elem0)
    return float('nan')

matrix = [[int(i) for i in row.split()] for row in data.splitlines()]
result = sum([find_evenly_divisible_result(row) for row in matrix])
print('result part two:', result)