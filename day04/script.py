#!/usr/bin/python3
import math

# test input
# data = '''aa bb cc dd ee
# aa bb cc dd aa
# aa bb cc dd aaa'''
# data = '''abcde fghij
# abcde xyz ecdab
# a ab abc abd abf abj
# iiii oiii ooii oooi oooo
# oiii ioii iioi iiio'''
# file input
data = open('input.txt').read()


words_in_lines = [line.split() for line in data.splitlines()]
print("part one", sum(all(line.count(word) == 1 for word in line) for line in words_in_lines))

sortedletterarrays_in_words_in_lines = [[''.join(sorted(word)) for word in line.split()] for line in data.splitlines()]
print("part two", sum(all(line.count(word) == 1 for word in line) for line in sortedletterarrays_in_words_in_lines))