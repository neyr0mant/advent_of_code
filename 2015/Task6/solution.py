from functions import Matrix, execution_time

list_str = [i.strip() for i in open("input.txt")]

def generate_test_data(rank, count_rule=5):
    import random
    list_index = [i for i in range(rank)]
    return [f"{random.choice(['turn on', 'turn off', 'toggle'])} {random.choice(list_index)},{random.choice(list_index)}"
            f" through {random.choice(list_index)},{random.choice(list_index)}" for _ in range(count_rule)]

@execution_time
def get_solve(rank, list_rule, part):
    grid = Matrix([[0 for _ in range(rank)] for _ in range(rank)])
    for rule_str in list_rule:
        rule_key = [i for i in ["toggle", "turn off", "turn on"] if i in rule_str][0]
        coordinate = [[int(j) for j in i.split(",")] for i in rule_str.split(rule_key)[1].split("through")]
        for y in range(coordinate[0][1], coordinate[1][1] + 1):
            for x in range(coordinate[0][0], coordinate[1][0] + 1):
                bright, key = grid[x, y], None
                if rule_key == "turn on":
                    key = 1 if part == 1 else bright + 1
                elif rule_key == "turn off":
                    key = 0 if part == 1 else bright - 1 if bright >= 1 else 0
                elif rule_key == "toggle":
                    if part == 1:
                        key = 0 if bright == 1 else 1
                    else:
                        key = bright + 2
                grid.update_element(key, x, y)
    return sum([sum([x for x in x_list]) for x_list in grid.matrix])


print(f"Решение части 1: {get_solve(1000,list_str, part=1)}")
print(f"Решение части 2: {get_solve(1000,list_str, part=2)}")

