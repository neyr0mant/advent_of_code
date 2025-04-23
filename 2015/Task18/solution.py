from functions import Matrix, execution_time
from copy import deepcopy
list_str = [[0 if j == "." else 1 for j in i.strip()] for i in open("input.txt")]
grid_main = Matrix(list_str)
def get_count_neighbour(coordinate, grid):
    count = 0
    for i in [[0,1],[1,1],[1,0], [1, -1], [0, -1], [-1,-1], [-1, 0], [-1, 1]]:
        x, y = coordinate[0] + i[0], coordinate[1] + i[1]
        if all([x >= 0, y >= 0, x <= len(list_str[0])-1, y <= len(list_str)-1]):
            if grid[x, y] == 1:
                count += 1
    return count

@execution_time
def get_solve(count_iter, part=1):
    grid = deepcopy(grid_main)
    if part != 1:
        for x_y in [[0,0], [0, grid.y_max-1], [grid.x_max-1, 0], [grid.x_max-1,grid.y_max-1]]:
            x,y = x_y
            grid[x, y] = 1
    for i in range(count_iter):
        dict_update = {0:[], 1:[]}
        for y in range(0, len(list_str)):
            for x in range(0, len(list_str[0])):
                cur_elem, count_neighbour = grid[x, y], get_count_neighbour([x,y], grid)
                if cur_elem == 1:
                    if count_neighbour not in [2,3]:
                        dict_update[0].extend([[x,y]])
                else:
                    if count_neighbour == 3:
                        dict_update[1].extend([[x,y]])
        for key, val in dict_update.items():
            for x_y in val:
                key_update = key
                if part != 1 and x_y in [[0,0], [0, grid.y_max-1], [grid.x_max-1, 0], [grid.x_max-1,grid.y_max-1]]:
                    key_update = 1
                grid[x_y[0], x_y[1]] = key_update
        grid.draw(factor=4)
    grid.get_gif(name_gif=f"Гифка {part}")
    return sum([sum([x for x in x_list]) for x_list in grid.matrix])


print(f"Решение части 1: {get_solve(100)}")
print(f"Решение части 2: {get_solve(100, part=2)}")