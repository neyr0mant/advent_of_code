#https://adventofcode.com/2024/day/7
from functions import *
list_data = [[j for j in i if j != "\n"] for i in open("input.txt")]
matrix = Matrix(list_data)
@execution_time
def get_solve(part=1):
    count_p1 = 0
    list_start = []
    for x in range(matrix.x_max):
        for y in range(matrix.y_max):
            if matrix[x, y] == "S":
                list_start.append([x, y])
                break
        if list_start:
            break
    x_start, y_start = list_start[0]
    laser_matrix = Matrix([[0] * matrix.x_max for _ in range(matrix.y_max)])
    laser_matrix[x_start, y_start] = 1
    while list_start:
        new_list_start = []
        for x_y in list_start:
            x, y = x_y
            y_new = y + 1
            if y_new <= matrix.y_max - 1:
                if matrix[x, y_new] == "^":
                    count_p1 += 1
                    new_lasers = [[x + 1, y_new], [x - 1, y_new]]
                    for laser in new_lasers:
                        x_new = laser[0]
                        if 0 <= x_new <= matrix.x_max-1:
                            laser_matrix[x_new, y_new] += laser_matrix[x, y]
                            if laser not in new_list_start:
                                new_list_start.append([x_new, y_new])
                else:
                    laser_matrix[x, y_new] += laser_matrix[x, y]
                    if [x, y_new] not in new_list_start:
                        new_list_start.append([x, y_new])
        list_start = new_list_start
    return count_p1 if part == 1 else sum(laser_matrix.matrix[-1])


print(f"Решение части 1: {get_solve(part =1)}")
print(f"Решение части 2: {get_solve(part =2)}")















