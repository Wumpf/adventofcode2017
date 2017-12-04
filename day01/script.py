#!/usr/bin/python3

# test input
#data = '1122'
#data = '1111'
#data = '1234'
#data = '91212129'
# file input
data = open('input.txt').read()


data = list(data)
print(data)

# part one
out_count = 0
for index, item in enumerate(data):
    if item == data[(index+1) % len(data)]:
        out_count = out_count + int(item)

print('result part one:', out_count)


# part two
out_count = 0
for index, item in enumerate(data):
    if item == data[(index+int(len(data)/2)) % len(data)]:
        out_count = out_count + int(item)

print('result part two:', out_count)
