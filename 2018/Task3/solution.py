from functions import Matrix, execution_time

list_str = [i.strip() for i in open("input.txt")]
dict_data = {}
for i in list_str:
    i_split = i.split("@")
    key = i_split[0].strip()[1:]
    split_val = i_split[1].split(":")
    start = [int(i) for i in split_val[0].split(",")]
    x_size, y_size = int(split_val[1].split("x")[0]), int(split_val[1].split("x")[1])
    dict_data.update({key: {"start": start, "x_size": x_size, "y_size": y_size}})

@execution_time
def get_solve(rank, dict_rule, part=1):
    grid = Matrix([[0 for _ in range(rank)] for _ in range(rank)])
    for idx, rule in dict_rule.items():
        coordinate_list = [[(rule["start"][0]+j, rule["start"][1]+i) for j in range(rule["x_size"])]
                           for i in range(rule["y_size"])]
        coordinate_change = []
        [coordinate_change.extend(i) for i in coordinate_list]
        if part == 2:
            dict_rule[idx].update({"coordinate_change": coordinate_change})
        for i in coordinate_change:
            grid[i[0], i[1]] += 1
    count, id_find = 0, 0
    for y, x_list in enumerate(grid.matrix):
        for x in x_list:
            if x >= 2:
                count += 1
    if part == 2:
        for id_rule, rule in dict_rule.items():
            bad_rule = False
            for x_y in rule["coordinate_change"]:
                if grid[x_y[0], x_y[1]] != 1:
                    bad_rule = True
                    break
            if not bad_rule:
                id_find = id_rule
    solve = count if part == 1 else id_find
    return solve

print(f"Решение части 1: {get_solve(1000,dict_data, part=1)}")
print(f"Решение части 2: {get_solve(1000,dict_data, part=2)}")
