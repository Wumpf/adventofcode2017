#!/usr/bin/python3

# file input
data = open('input.txt').read()


class Program:
    def __init__(self, parttwo):
        self.registers = { 'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0 }
        self.prog_pos = 0
        self.mul_count = 0
        if parttwo:
            self.registers['a'] = 1

    def set(self, reg, val):
        self.registers[reg] = val
    def sub(self, reg, val):
        self.registers[reg] -= val
    def mul(self, reg, val):
        self.registers[reg] *= val
        self.mul_count += 1
    def jnz(self, reg, val):
        try:
            regval = self.registers[reg]
        except:
            regval = int(reg)
        if regval != 0:
            self.prog_pos += val - 1

    def execute_next_line(self, code):
        line = code[self.prog_pos].split()
        instr = line[0]
        reg = line[1]
        val = reg if len(line) == 2 else line[2]
        try:
            val = int(val)
        except:
            val = self.registers[val]
        getattr(self, instr)(reg, val)
        self.prog_pos += 1
        return len(code) == self.prog_pos




code = data.splitlines()

# partone = Program(False)
# while not partone.execute_next_line(code):
#     pass
# print('result part one', partone.mul_count)

partone = Program(True)
while not partone.execute_next_line(code):
    pass
print('result part two', partone.registers['h'])