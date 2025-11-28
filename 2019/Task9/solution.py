from collections import defaultdict
list_data = [i.strip() for i in open("input.txt")][0].split(",")
list_data = [int(i) for i in list_data]

class Intcode:
    def __init__(self, program, part=1):
        self.mem = defaultdict(int)
        for i, val in enumerate(program):
            self.mem[i] = val
        self.pc = 0
        self.relative_base = 0
        self.part = part
        self.outputs = []

    def get_param(self, offset, mode):
        addr = self.pc + offset
        if mode == 0:
            return self.mem[self.mem[addr]]
        elif mode == 1:
            return self.mem[addr]
        elif mode == 2:
            return self.mem[self.mem[addr] + self.relative_base]

    def get_write_addr(self, offset, mode):
        addr = self.mem[self.pc + offset]
        return addr + self.relative_base if mode == 2 else addr

    def run(self):
        while True:
            instruction = self.mem[self.pc]
            opcode = instruction % 100
            modes = instruction // 100

            mode1 = (modes // 1) % 10
            mode2 = (modes // 10) % 10
            mode3 = (modes // 100) % 10

            if opcode == 99:
                return self.outputs[-1] if self.outputs else None

            if opcode == 1:
                a = self.get_param(1, mode1)
                b = self.get_param(2, mode2)
                self.mem[self.get_write_addr(3, mode3)] = a + b
                self.pc += 4

            elif opcode == 2:
                a = self.get_param(1, mode1)
                b = self.get_param(2, mode2)
                self.mem[self.get_write_addr(3, mode3)] = a * b
                self.pc += 4

            elif opcode == 3:
                self.mem[self.get_write_addr(1, mode1)] = self.part
                self.pc += 2

            elif opcode == 4:
                val = self.get_param(1, mode1)
                self.outputs.append(val)
                self.pc += 2

            elif opcode == 5:
                if self.get_param(1, mode1) != 0:
                    self.pc = self.get_param(2, mode2)
                else:
                    self.pc += 3

            elif opcode == 6:
                if self.get_param(1, mode1) == 0:
                    self.pc = self.get_param(2, mode2)
                else:
                    self.pc += 3

            elif opcode == 7:
                a = self.get_param(1, mode1)
                b = self.get_param(2, mode2)
                self.mem[self.get_write_addr(3, mode3)] = 1 if a < b else 0
                self.pc += 4

            elif opcode == 8:  # equals
                a = self.get_param(1, mode1)
                b = self.get_param(2, mode2)
                self.mem[self.get_write_addr(3, mode3)] = 1 if a == b else 0
                self.pc += 4

            elif opcode == 9:
                self.relative_base += self.get_param(1, mode1)
                self.pc += 2

print(f"Решение части 1:{Intcode(list_data, part=1).run()}")
print(f"Решение части 2:{Intcode(list_data, part=2).run()}")