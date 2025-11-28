from itertools import permutations
list_data = [i.strip() for i in open("input.txt")][0].split(",")
list_data = [int(i) for i in list_data]
class Intcode:
    def __init__(self, program, inputs):
        self.mem = program[:]
        self.pc = 0
        self.inputs = inputs[:]
        self.outputs = []
        self.halted = False
    def run(self):
        while True:
            opcode = self.mem[self.pc] % 100
            modes = self.mem[self.pc] // 100
            mode = lambda n: (modes // (10 ** (n-1))) % 10
            if opcode == 99:
                self.halted = True
                return
            a = self.mem[self.pc + 1]
            b = self.mem[self.pc + 2] if opcode in [1,2,5,6,7,8] else None
            c = self.mem[self.pc + 3] if opcode in [1,2,7,8] else None
            param1 = self.mem[a] if mode(1) == 0 else a
            param2 = self.mem[b] if b is not None and mode(2) == 0 else b
            if opcode == 1:
                self.mem[c] = param1 + param2
                self.pc += 4
            elif opcode == 2:
                self.mem[c] = param1 * param2
                self.pc += 4
            elif opcode == 3:
                if not self.inputs:
                    return
                self.mem[a] = self.inputs.pop(0)
                self.pc += 2
            elif opcode == 4: # output
                self.outputs.append(param1)
                self.pc += 2
                return param1
            elif opcode == 5:
                self.pc = param2 if param1 != 0 else self.pc + 3
            elif opcode == 6:
                self.pc = param2 if param1 == 0 else self.pc + 3
            elif opcode == 7:
                self.mem[c] = 1 if param1 < param2 else 0
                self.pc += 4
            elif opcode == 8:
                self.mem[c] = 1 if param1 == param2 else 0
                self.pc += 4
def get_solve(list_data, part=1):
    max_signal = 0
    if part ==1:
        for phases in permutations([0, 1, 2, 3, 4]):
            signal = 0
            for phase in phases:
                amp = Intcode(list_data, [phase, signal])
                signal = amp.run()
            max_signal = max(max_signal, signal)
    else:
        for phases in permutations([5, 6, 7, 8, 9]):
            amps = [Intcode(list_data, [phase]) for phase in phases]
            signal = 0
            i = 0
            while not amps[4].halted:
                amps[i].inputs.append(signal)
                signal = amps[i].run()
                i = (i + 1) % 5
            max_signal = max(max_signal, amps[4].outputs[-1])
    return max_signal

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 1: {get_solve(list_data, part=2)}")