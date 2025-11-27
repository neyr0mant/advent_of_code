from copy import deepcopy
dict_data = {idx: i.strip() for idx, i in enumerate(open("input.txt"))}



def get_solve(data, part=1, index_find=None):
    global_acc, index_instruction, set_instruction = 0, 0, set()
    while True:
        if index_instruction in set_instruction:
            return global_acc, False
        name_instruction, data_instruction = data[index_instruction].split()
        data_instruction_int = int(data_instruction)
        if index_instruction == index_find:
            if name_instruction == "acc":
                global_acc += data_instruction_int
            return global_acc, True
        name_instruction, data_instruction = data[index_instruction].split()
        data_instruction_int = int(data_instruction)
        set_instruction.add(index_instruction)
        if name_instruction == "nop":
            if part == 2:
                new_data = deepcopy(data)
                new_data[index_instruction] = f'jmp {data_instruction_int}'
                res = get_solve(new_data,part=1,  index_find=index_find)
                if res[1]:
                    return res
            index_instruction += 1
        if name_instruction == "acc":
            index_instruction += 1
            global_acc += data_instruction_int
        if name_instruction == "jmp":
            if part == 2:
                new_data = deepcopy(data)
                new_data[index_instruction] = f'nop {data_instruction_int}'
                res = get_solve(new_data,part=1, index_find=index_find)
                if res[1]:
                    return res
            index_instruction += data_instruction_int

print(f"Решение части 1: {get_solve(dict_data)[0]}")
print(f"Решение части 2: {get_solve(dict_data, part=2, index_find=max(dict_data.keys()))[0]}")


