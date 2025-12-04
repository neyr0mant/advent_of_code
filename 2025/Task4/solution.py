from functions import *
list_data = [[j for j in i.strip()] for i in open("input.txt")]
grid = Matrix(list_data)
from functions import *
def get_solve_p1(grid_):
    count_all, vectors = 0, [[0,-1],[-1,-1],[-1, 0],[-1, 1], [0, 1], [1,1], [1, 0], [1, -1]]
    list_cor_possible = []
    for y in range(grid_.y_max):
        for x in range(grid_.x_max):
            if grid[x, y] == "@":
                count_neighbours = 0
                for vector in vectors:
                    x_n, y_n = x+vector[0], y+vector[1]
                    if 0 <= x_n <= grid_.x_max-1 and 0 <= y_n <= grid_.y_max-1:
                        neighbours = grid_[x_n, y_n]
                        if neighbours == "@":
                            count_neighbours += 1
                if count_neighbours < 4:
                    count_all += 1
                    list_cor_possible.append([x, y])
    return count_all, list_cor_possible
@execution_time
def get_solve_p2(grid_):
    count_all = 0
    count_possible, list_cor_possible = get_solve_p1(grid_)
    while count_possible:
        count_possible, list_cor_possible = get_solve_p1(grid_)
        for x,y in list_cor_possible:
            grid_[x, y] = "."
        count_all += count_possible
    return count_all

print(f"Решение части 1: {get_solve_p1(grid)[0]}")
print(f"Решение части 2: {get_solve_p2(grid)}")







