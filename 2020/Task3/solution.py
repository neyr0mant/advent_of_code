from functions import Matrix
import math
list_data = [[j for j in i.strip()] for i in open('input.txt')]

def get_solve(list_data, vectors):
    list_count = []
    matrix, start_place = Matrix(list_data), (0, 0)
    for vector in vectors:
        x_v, y_v = vector
        count = 0
        for y in range(0, matrix.y_max, y_v):
            x = start_place[0] + x_v
            y = start_place[1] + y_v
            if x >= matrix.x_max:
                x -= matrix.x_max
            if y >= matrix.y_max:
                break
            start_place = (x, y)
            if matrix[x, y] == "#":
                count += 1
        if count:
            list_count.append(count)
        start_place = (0, 0)
    return math.prod(list_count)


print(f"Решение части 1: {get_solve(list_data, [[3,1]])}")
print(f"Решение части 2: {get_solve(list_data, [[1,1], [3,1], [5,1], [7,1], [1,2]] )}")








