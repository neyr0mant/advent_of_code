# Читаем входные координаты
list_data = [tuple(map(int, i.strip().split(', '))) for i in open("input.txt")]

def get_solve(list_data_, part =1):
    min_x = min(x for x, y in list_data_)
    max_x = max(x for x, y in list_data_)
    min_y = min(y for x, y in list_data_)
    max_y = max(y for x, y in list_data_)
    if part == 1:
        area_counts, infinite_points = {}, set()
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                distances = []
                for i, (cx, cy) in enumerate(list_data_):
                    dist = abs(x - cx) + abs(y - cy)
                    distances.append((dist, i))
                distances.sort()
                if len(distances) > 1 and distances[0][0] == distances[1][0]:
                    continue
                else:
                    closest_idx = distances[0][1]
                    if x == min_x or x == max_x or y == min_y or y == max_y:
                        infinite_points.add(closest_idx)
                    area_counts[closest_idx] = area_counts.get(closest_idx, 0) + 1
        for idx in infinite_points:
            if idx in area_counts:
                del area_counts[idx]
        result = max(area_counts.values())
    else:
        margin, region_size, threshold = 100, 0, 10000
        for x in range(min_x - margin, max_x + margin + 1):
            for y in range(min_y - margin, max_y + margin + 1):
                total_dist = 0
                for cx, cy in list_data_:
                    total_dist += abs(x - cx) + abs(y - cy)
                if total_dist < threshold:
                    region_size += 1
        result = region_size
    return result

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")