from copy import deepcopy
list_data = [[int(j) for j in i.split(",")] for i in open('input.txt')][0]


def get_solve_p1(list_data, noun=12, verb=2):
    list_data = deepcopy(list_data)
    code, idx = None, 0
    list_data[1] = noun
    list_data[2] = verb
    while True:
        code = list_data[idx]
        if code == 99:
            break
        position_a, position_b, position_c = list_data[idx+1], list_data[idx+2], list_data[idx+3]
        a, b = list_data[position_a], list_data[position_b]
        c = a + b if code == 1 else a * b
        list_data[position_c] = c
        idx += 4
    return list_data[0], noun, verb

def get_solve_p2(list_data):
    max_num = len(list_data)
    for noun in range(max_num):
        for verb in range(max_num):
            res = get_solve_p1(list_data, noun, verb)
            if res[0] == 19690720:
                return 100 * noun + verb



print(f"Решение части 1: {get_solve_p1(list_data)[0]}")
print(f"Решение части 2: {get_solve_p2(deepcopy(list_data))}")








