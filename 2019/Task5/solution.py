list_data = [[int(j) for j in i.split(",")] for i in open("input.txt")][0]
from copy import deepcopy
def get_rule(rule):
    instruction_str = str(rule).zfill(5)  # Дополняем нулями слева до 5 цифр
    opcode = int(instruction_str[-2:])  # Последние две цифры — opcode
    modes = [int(instruction_str[-3]), int(instruction_str[-4]), int(instruction_str[-5])]  # Режимы параметров
    return opcode, modes

def get_param_value(list_data, index, mode):
    if mode == 0:
        return list_data[list_data[index]]
    elif mode == 1:
        return list_data[index]

def get_solve(list_data, input_value):
    i = 0
    list_data, list_out = deepcopy(list_data), []
    while i < len(list_data):
        opcode, modes = get_rule(list_data[i])
        if opcode == 99:
            break
        elif opcode == 1:
            param1 = get_param_value(list_data, i + 1, modes[0])
            param2 = get_param_value(list_data, i + 2, modes[1])
            result_addr = list_data[i + 3]
            list_data[result_addr] = param1 + param2
            i += 4
        elif opcode == 2:
            param1 = get_param_value(list_data, i + 1, modes[0])
            param2 = get_param_value(list_data, i + 2, modes[1])
            result_addr = list_data[i + 3]
            list_data[result_addr] = param1 * param2
            i += 4
        elif opcode == 3:
            result_addr = list_data[i + 1]
            list_data[result_addr] = input_value
            i += 2
        elif opcode == 4:
            param1 = get_param_value(list_data, i + 1, modes[0])
            list_out.append(param1)
            i += 2
        elif opcode == 5:
            param1 = get_param_value(list_data, i + 1, modes[0])
            param2 = get_param_value(list_data, i + 2, modes[1])
            if param1 != 0:
                i = param2
            else:
                i += 3
        elif opcode == 6:
            param1 = get_param_value(list_data, i + 1, modes[0])
            param2 = get_param_value(list_data, i + 2, modes[1])
            if param1 == 0:
                i = param2
            else:
                i += 3
        elif opcode == 7:
            param1 = get_param_value(list_data, i + 1, modes[0])
            param2 = get_param_value(list_data, i + 2, modes[1])
            result_addr = list_data[i + 3]
            list_data[result_addr] = 1 if param1 < param2 else 0
            i += 4
        elif opcode == 8:
            param1 = get_param_value(list_data, i + 1, modes[0])
            param2 = get_param_value(list_data, i + 2, modes[1])
            result_addr = list_data[i + 3]
            list_data[result_addr] = 1 if param1 == param2 else 0
            i += 4
    return list_out


print(f"Решение части 1: {get_solve(list_data, 1)[-1]}")
print(f"Решение части 2: {get_solve(list_data, 5)[-1]}")