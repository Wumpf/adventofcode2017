#!/usr/bin/python3
import math

# test input
data = 1024
# file input
data = 265149

class Found(Exception): pass

square = math.ceil(math.sqrt(data))
if square % 2 == 0:
    square = square + 1

print('square', square)
dist0 = math.ceil(square / 2) - 1
print('dist0', dist0)

nums_step = [5, 3, 1, 7]
nums = [6, 4, 2, 8]
for d in range(dist0-1):
    for i in range(4):
        nums_step[i] = nums_step[i] + 8
        nums[i] = nums[i] + nums_step[i]
print('nums', nums)

dist1 = min(abs(num - data) for num in nums)

print('dist1', dist1)
print('result part one', dist1 + dist0)

