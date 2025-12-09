from math import gcd
from functions import *
list_data = [[int(j) for j in i.strip().split(",")] for i in open("input.txt")]
@execution_time
def get_solve(list_data_, part=1):
    max_area = 0
    n = len(list_data_)
    if part == 1:
        for i in range(n):
            for j in range(i + 1, n):
                dx = abs(list_data_[i][0] - list_data_[j][0]) + 1
                dy = abs(list_data_[i][1] - list_data_[j][1]) + 1
                max_area = max(max_area, dx * dy)
        return max_area
    else:
        def clip_to_halfplane(poly, line_value, is_vertical, is_min):
            if not poly:
                return []
            output = []
            prev = poly[-1]
            prev_val = prev[0] if is_vertical else prev[1]
            prev_inside = prev_val >= line_value if is_min else prev_val <= line_value
            for curr in poly:
                curr_val = curr[0] if is_vertical else curr[1]
                curr_inside = curr_val >= line_value if is_min else curr_val <= line_value
                if curr_inside:
                    if not prev_inside:
                        inter = (line_value, prev[1]) if is_vertical else (prev[0], line_value)
                        output.append(inter)
                    output.append(curr)
                elif prev_inside:
                    inter = (line_value, prev[1]) if is_vertical else (prev[0], line_value)
                    output.append(inter)
                prev = curr
                prev_inside = curr_inside
            return output
        def is_full_covered(min_x, min_y, max_x, max_y):
            clipped = list_data_[:]
            clipped = clip_to_halfplane(clipped, min_x, True, True)
            clipped = clip_to_halfplane(clipped, max_x, True, False)
            clipped = clip_to_halfplane(clipped, min_y, False, True)
            clipped = clip_to_halfplane(clipped, max_y, False, False)
            if len(clipped) < 3:
                return False
            a = 0
            for i in range(len(clipped)):
                x1, y1 = clipped[i]
                x2, y2 = clipped[(i + 1) % len(clipped)]
                a += x1 * y2 - x2 * y1
            a = abs(a) // 2
            b = 0
            v = len(clipped)
            for i in range(v):
                x1, y1 = clipped[i]
                x2, y2 = clipped[(i + 1) % v]
                dx = abs(x2 - x1)
                dy = abs(y2 - y1)
                g = gcd(dx, dy)
                b += g + 1
            b -= v
            total = a + (b // 2) + 1
            rect_count = (max_x - min_x + 1) * (max_y - min_y + 1)
            return total == rect_count
        pairs = []
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = list_data_[i]
                x2, y2 = list_data_[j]
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                pairs.append((area, i, j))
        pairs.sort(reverse=True)
        for area, i, j in pairs:
            if area <= max_area:
                break
            min_x = min(list_data_[i][0], list_data_[j][0])
            max_x = max(list_data_[i][0], list_data_[j][0])
            min_y = min(list_data_[i][1], list_data_[j][1])
            max_y = max(list_data_[i][1], list_data_[j][1])
            if is_full_covered(min_x, min_y, max_x, max_y):
                max_area = area
    return max_area


print(f"Решение части 1: {get_solve(list_data, part =1)}")
print(f"Решение части 2: {get_solve(list_data, part =2)}")