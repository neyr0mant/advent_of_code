from functions import *
import math
list_str = [[int(j) for j in i.strip()] for i in open("input.txt")]
matrix = Matrix(list_str)

def get_solve(part=1):
    vectors, low_points = [(1, 0), (0, 1), (-1, 0), (0, -1)], []
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
        visited, stack, sq = set(), [(start_x, start_y)], 0
        while stack:
            x, y = stack.pop()
            if any([(x, y) in visited, matrix[x, y] == 9]):
                continue
            visited.add((x, y))
            sq += 1
            for dx, dy in vectors:
                nx, ny = x + dx, y + dy
                if (0 <= nx < matrix.x_max and
                        0 <= ny < matrix.y_max and
                        (nx, ny) not in visited and
                        matrix[nx, ny] != 9):
                    stack.append((nx, ny))
        return sq
    return math.prod(sorted([pool_sq(i[0], i[1]) for i in low_points], reverse=True)[:3])



print(f"Решение части 1: {get_solve()}")
print(f"Решение части 2: {get_solve(2)}")