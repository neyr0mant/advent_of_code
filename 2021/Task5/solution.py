#Решения нет
from functions import Matrix, execution_time
list_data = [[[int(k) for k in j.split(",")] for j in i.strip().split("->")] for i in open("input.txt")]
@execution_time
def get_solve(rank, list_rule, part):
    grid = Matrix([[0 for _ in range(rank)] for _ in range(rank)])
    for rule in list_rule:
        x_1, y_1, x_2, y_2 = rule[0][0], rule[0][1], rule[1][0], rule[1][1]
        list_condition = [x_1 == x_2, y_1 == y_2, part == 2]
        if not any(list_condition):
            continue
        if list_condition[0]:
            y_min, y_max = min([y_1, y_2]), max([y_1, y_2])
            for y in range(y_min, y_max + 1):
                grid[x_1, y] += 1
        if list_condition[1]:
            x_min, x_max = min([x_1, x_2]), max([x_1, x_2])
            for x in range(x_min, x_max + 1):
                grid[x, y_1] += 1
        else:
            if not any(list_condition[:2]) and part == 2:
                count = abs(y_2 - y_1) + 1
                if y_2 > y_1:
                    if x_2 > x_1:
                        list_coordinate = [[x_1+i, y_1+i] for i in range(count)]
                    else:
                        list_coordinate = [[x_1 - i, y_1 + i] for i in range(count)]
                else:
                    if x_2 > x_1:
                        list_coordinate = [[x_1+i, y_1-i] for i in range(count)]
                    else:
                        list_coordinate = [[x_1 - i, y_1 - i] for i in range(count)]
                for coordinate in list_coordinate:
                    x, y = coordinate
                    grid[x, y] += 1
    return sum([sum([1 for x in x_list if x > 1]) for x_list in grid.matrix])

print(f"Решение части 1: {get_solve(1000,list_data, part=1)}")
print(f"Решение части 2: {get_solve(1000,list_data, part=2)}")