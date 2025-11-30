from functions import *
list_str = [[int(j) for j in i.strip()] for i in open("input.txt")]
matrix = Matrix(list_str)
import math


def get_solve(part=1):
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    low_points = []
    for y in range(matrix.y_max):
        for x in range(matrix.x_max):
            cur = matrix[x, y]
            is_low = True
            for dx, dy in vectors:
                nx, ny = x + dx, y + dy
                if 0 <= nx < matrix.x_max and 0 <= ny < matrix.y_max:
                    if matrix[nx, ny] <= cur:
                        is_low = False
                        break
            if is_low:
                low_points.append((x, y))

    if part == 1:
        return sum(matrix[x, y] + 1 for x, y in low_points)
    def pool_sq(start_x, start_y):
        visited = set()
        stack = [(start_x, start_y)]
        size = 0
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if matrix[x, y] == 9:
                continue
            size += 1
            for dx, dy in vectors:
                nx, ny = x + dx, y + dy
                if (0 <= nx < matrix.x_max and
                        0 <= ny < matrix.y_max and
                        (nx, ny) not in visited and
                        matrix[nx, ny] != 9):
                    stack.append((nx, ny))
        return size
    pool_sq_list = []
    for x, y in low_points:
        pool_sq_list.append(pool_sq(x, y))
    pool_sq_list.sort(reverse=True)
    return math.prod(pool_sq_list[:3])



print(f"Решение части 1: {get_solve()}")
print(f"Решение части 2: {get_solve(2)}")