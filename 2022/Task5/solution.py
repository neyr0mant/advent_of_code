#https://adventofcode.com/2022/day/3
from copy import deepcopy
data_box, list_data, rule_list = {}, [], []
for i in open("input.txt"):
    if i != "\n":
        if "[" in i:
            list_data.append(i)
            continue
        if i[1].isdigit():
            list_num_box, old_idx = [int(j) for j in i.strip().split()], 0
            for box in list_num_box:
                idx_box = box if box == 1 else old_idx + 4
                old_idx = idx_box
                box_data = [box[idx_box] for box in list_data[::-1] if idx_box <= len(box)-1 and box[idx_box] != " "]
                data_box.update({box: box_data})
        else:
            rule_list.append(i.split())

def get_solve(dict_data,rule_list, part=1):
    dict_data = deepcopy(dict_data)
    for rule in rule_list:
        box_from, box_to, count_box = int(rule[3]), int(rule[5]), int(rule[1])
        from_data, to_data = dict_data[box_from], dict_data[box_to]
        from_new = from_data[:len(from_data)-count_box]
        data_move = from_data[::-1][:count_box]
        to_data.extend(data_move) if part == 1 else to_data.extend(data_move[::-1])
        dict_data[box_from], dict_data[box_to] = from_new, to_data
    key_sort = sorted(list(dict_data.keys()))
    return "".join([dict_data[key][-1] for key in key_sort])

print(f"Решение части 1: {get_solve(data_box, rule_list)}")
print(f"Решение части 2: {get_solve(data_box, rule_list, part=2)}")







