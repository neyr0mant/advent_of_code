list_data = [(i.strip()[:7], i.strip()[7:]) for i in open("input.txt")]


def get_num_for_rule(rule):
    list_range = [i for i in range(2 ** len(rule))]
    for idx, i in enumerate(rule, start=1):
        if i in ["F", "L"]:
            list_range = list_range[:int(len(list_range) / 2)]
        else:
            list_range = list_range[int(len(list_range) / 2):]
    return list_range[0]


def get_solve(list_place, part=1):
    list_count = []
    for place in list_place:
        str_, column = get_num_for_rule(place[0]), get_num_for_rule(place[1])
        list_count.append(str_ * 8 + column)
    res = [i for i in range(8*128) if all([i not in list_count, (i+1) in list_count, (i-1) in list_count])]
    solve = max(list_count) if part == 1 else res[0]
    return solve

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")
