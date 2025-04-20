list_str = [i.strip() for i in open("input.txt")]
import itertools

dict_data = {}
for i in list_str:
    list_data = i.split()
    name = list_data[0]
    next_name = list_data[-1][:-1]
    count = int(list_data[3])
    if 'gain' in list_data:
        if cur_data := dict_data.get(name):
            dict_data[name] = cur_data | {next_name:count}
        else:
            dict_data[name] = {next_name: count}
    else:
        if cur_data := dict_data.get(name):
            dict_data[name] = cur_data | {next_name: -count}
        else:
            dict_data[name] = {next_name: -count}
def calculate_index_happiness(list_name, dict_data):
    index_happiness = 0
    for idx, name in enumerate(list_name):
        if idx == 0:
            next_door_1, next_door_2 = list_name[-1], list_name[1]
        elif idx == len(list_name) - 1:
            next_door_1, next_door_2 = list_name[idx-1], list_name[0]
        else:
            next_door_1, next_door_2 = list_name[idx - 1], list_name[idx + 1]
        index_happiness += dict_data[name][next_door_1] + dict_data[name][next_door_2]
    return index_happiness

def get_solve(part =1):
    if part == 1:
        permutations = itertools.permutations(list(dict_data.keys()))
        return max([calculate_index_happiness(i, dict_data) for i in permutations])
    else:
        dict_data_p2 = {i: k | {"Me": 0} for i,k in dict_data.items()}
        dict_data_p2.update({"Me": {name: 0 for name in list(dict_data.keys())}})
        permutations = itertools.permutations(list(dict_data_p2.keys()))
        return max([calculate_index_happiness(i,dict_data_p2) for i in permutations])


print(f"Решение части 1: {get_solve()}")
print(f"Решение части 2: {get_solve(part=2)}")


