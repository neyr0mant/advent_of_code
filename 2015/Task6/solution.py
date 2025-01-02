from functions import Matrix, execution_time

list_str = [i.strip() for i in open("input.txt")]


def generate_test_data(rank, count_rule = 5):
    import random
    list_index = [i for i in range(rank)]
    return [f"{random.choice(['turn on', 'turn off', 'toggle'])} {random.choice(list_index)},{random.choice(list_index)}"
            f" through {random.choice(list_index)},{random.choice(list_index)}" for _ in range(count_rule)]

@execution_time
def get_count_lamp(rank, list_rule, print_all=False, out_file= False, part=1):
    grid = Matrix([[0 for _ in range(rank)] for _ in range(rank)])
    msg = 'Зажжены' if part == 1 else "Яркость"
    if print_all:
        print("Начальная сетка")
        print(f"{msg}: {sum([sum([x for x in x_list]) for x_list in grid.list_data])} лампочек")
        grid.print_matrix()

    def get_rule_for_str(rule_str_):
        for type_rule in ["toggle", "turn off", "turn on"]:
            if type_rule in rule_str_:
                list_coordinate = [[int(j) for j in i.split(",")] for i in
                                   rule_str_.split(type_rule)[1].split("through")]
                return {type_rule: list_coordinate}

    def get_list_coordinate_for_change(list_coordinate_):
        list_out = []
        list_x, list_y = [i[1] for i in list_coordinate_], [i[0] for i in list_coordinate_]
        x_min, y_min, x_max, y_max = min(list_x), min(list_y), max(list_x), max(list_y)
        for y in range(y_min, y_max+1):
            for x in range(x_min, x_max+1):
                if (0 <= x <= rank-1) and (0 <= y <= rank-1):
                    list_out.append([x, y])
        return list_out

    for idx, rule_str in enumerate(list_rule):
        rule = get_rule_for_str(rule_str)
        list_coordinate_for_change = get_list_coordinate_for_change(list(rule.values())[0])
        rule_key = list(rule.keys())[0]
        if rule_key == "turn on":
            if part == 1:
                grid.update_matrix({1: list_coordinate_for_change}, revert_x_y=True)
            else:
                for x_y in list_coordinate_for_change:
                    y, x = x_y
                    grid.update_matrix({grid[x, y] + 1: [[x, y]]})
        elif rule_key == "turn off":
            if part == 1:
                grid.update_matrix({0: list_coordinate_for_change}, revert_x_y=True)
            else:
                for x_y in list_coordinate_for_change:
                    y, x = x_y
                    cur_bright = grid[x, y]
                    bright = 0 if cur_bright - 1 < 0 else cur_bright - 1
                    grid.update_matrix({bright: [[x, y]]})
        elif rule_key == "toggle":
            for x_y in list_coordinate_for_change:
                y, x = x_y
                if part == 1:
                    grid.update_matrix({1: [[x, y]]}) if grid[x, y] == 0 else grid.update_matrix({0: [[x, y]]})
                else:
                    grid.update_matrix({grid[x, y] + 2: [[x, y]]})
        if print_all:
            print(f"Правило {idx+1}: {rule_str}")
            print(f"Список точек: {list_coordinate_for_change}")
            print(f"{msg}: {sum([sum([x for x in x_list]) for x_list in grid.list_data])} лампочек")
            res = grid.print_matrix()
            with open("out.txt", "w") as file:
                file.write(res)
        if all([out_file, idx+1 == len(list_rule), not print_all]):
            res = grid.print_matrix()
            with open("out.txt", "w") as file:
                file.write(res)
    return sum([sum([x for x in x_list if x > 0]) for x_list in grid.list_data])


# print(f"Решение части 1: {get_count_lamp(10,generate_test_data(10, 5),part=2, print_all=True)}")
print(f"Решение части 1: {get_count_lamp(1000,list_str)}")
print(f"Решение части 2: {get_count_lamp(1000,list_str, part=2)}")
#341389 - слишком мало
