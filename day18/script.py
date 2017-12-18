#!/usr/bin/python3
from string import ascii_lowercase
from queue import Queue

# test input
data = '''snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d'''
# file input
data = open('input.txt').read()


class SndException(Exception):
    def __init__(self, val):
        self.val = val
class RcvException(Exception):
    def __init__(self, reg):
        self.reg = reg

class Program:
    def __init__(self, index):
        self.index = index
        self.registers = {}
        for c in ascii_lowercase:
            self.registers[c] = 0
        self.registers['p'] = index
        self.prog_pos = -1
        self.queue = Queue()

    def snd(self, reg, val):
        raise SndException(val)
    def set(self, reg, val):
        self.registers[reg] = val
    def add(self, reg, val):
        self.registers[reg] += val
    def mul(self, reg, val):
        self.registers[reg] *= val
    def mod(self, reg, val):
        self.registers[reg] %= val   # here be dragons
    def rcv(self, reg, val):
        raise RcvException(reg)
    def jgz(self, reg, val):
        try:
            regval = self.registers[reg]
        except:
            regval = int(reg)
        if regval > 0:
            self.prog_pos += val - 1

    def execute_next_line(self, code):
        self.prog_pos = (self.prog_pos + 1) % len(code)
        line = code[self.prog_pos].split()
        instr = line[0]
        reg = line[1]
        val = reg if len(line) == 2 else line[2]
        try:
            val = int(val)
        except:
            val = self.registers[val]
        getattr(self, instr)(reg, val)






code = data.splitlines()


def part1():
    prog0 = Program(0)
    sound_freq = 0
    while True:
        try:
            prog0.execute_next_line(code)
        except RcvException as rcv:
            if prog0.registers[rcv.reg] != 0:
                print('result part one', sound_freq)
                break
        except SndException as snd:
            sound_freq = snd.val

part1()




def part2():
    class DeadlockException(Exception):
        pass

    prog0 = Program(0)
    prog1 = Program(1)
    prog1_send_count = 0
    try:
        while True:
            try:
                prog0.execute_next_line(code)
            except RcvException as prog0Rcv:
                while True:
                    try:
                        prog1.execute_next_line(code)
                    except RcvException as prog1Rcv:
                        if prog1.queue.empty():
                            raise DeadlockException()
                        prog1.registers[prog1Rcv.reg] = prog1.queue.get()
                    except SndException as prog1Snd:
                        prog0.registers[prog0Rcv.reg] = prog1Snd.val
                        prog1_send_count += 1
                        break
            except SndException as prog0Snd:
                prog1.queue.put(prog0Snd.val)
    except DeadlockException:
        print('result part two', prog1_send_count)

part2()