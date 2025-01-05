from functions import Matrix, execution_time

list_str = [i.strip() for i in open("input.txt")]


def generate_test_data(rank, count_rule = 5):
    import random
    list_index = [i for i in range(rank)]
    return [f"{random.choice(['turn on', 'turn off', 'toggle'])} {random.choice(list_index)},{random.choice(list_index)}"
            f" through {random.choice(list_index)},{random.choice(list_index)}" for _ in range(count_rule)]

@execution_time
def get_solve(rank, list_rule, part):
    grid = Matrix([[0 for _ in range(rank)] for _ in range(rank)])

    def update_grid(list_coordinate, key, part_):
        if part_ == 1:
            if key == "turn on":
                grid.update_matrix_list_data({1: list_coordinate})
            elif key == "turn off":
                grid.update_matrix_list_data({0: list_coordinate})
            elif key == "toggle":
                for x, y in list_coordinate:
                    elem = 1 if grid[x, y] == 0 else 0
                    grid.update_matrix_element(elem, [x, y])
        else:
            for x, y in list_coordinate:
                cur_bright = grid[x, y]
                if key == "turn on":
                    cur_bright += 1
                elif key == "turn off":
                    cur_bright -= 1 if cur_bright >= 1 else 0
                elif key == "toggle":
                    cur_bright += 2
                grid.update_matrix_element(cur_bright, [x, y])

    for rule_str in list_rule:
        rule_key = [i for i in ["toggle", "turn off", "turn on"] if i in rule_str][0]
        start_coordinate = [[int(j) for j in i.split(",")] for i in rule_str.split(rule_key)[1].split("through")]
        a, b = [start_coordinate[0][0], start_coordinate[1][0]], [start_coordinate[0][1], start_coordinate[1][1]]
        x_min, x_max, y_min, y_max = min(a), max(a), min(b), max(b)
        coordinate_for_change = []
        if x_max != x_min:
            if y_max != y_min:
                [[coordinate_for_change.append([x, y]) for x in range(x_min, x_max+1)] for y in range(y_min, y_max+1)]
            else:
                coordinate_for_change.extend([[x, y_max] for x in range(x_min, x_max+1)])
        else:
            coordinate_for_change.extend([[x_max, y] for y in range(y_min, y_max+1)])
        update_grid(coordinate_for_change, rule_key, part)
    return sum([sum([x for x in x_list if x > 0]) for x_list in grid.matrix])


print(f"Решение части 1: {get_solve(1000,list_str, part=1)}")
print(f"Решение части 2: {get_solve(1000,list_str, part=2)}")
