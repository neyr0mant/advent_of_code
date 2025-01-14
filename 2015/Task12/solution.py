import json

json_data = json.load(open('input.txt', 'r'))


def get_solve(data_in, summ=0, part=1):
    if isinstance(data_in, int):
        return summ + data_in
    if isinstance(data_in, list):
        return sum([get_solve(i, part=part) for i in data_in])
    if isinstance(data_in, str):
        return 0
    if part == 2:
        if isinstance(data_in, dict):
            if "red" in data_in.values():
                return 0
    for key, val in data_in.items():
        if isinstance(val, dict):
            summ += get_solve(val, part=part)
        elif isinstance(val, list):
            for i in val:
                summ += get_solve(i, part=part)
        elif isinstance(val, int):
            summ += val
    return summ


print(f"Решение части 1: {get_solve(json_data)}")
print(f"Решение части 2: {get_solve(json_data, part=2)}")
