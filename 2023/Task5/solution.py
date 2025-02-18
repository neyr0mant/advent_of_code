from functions import execution_time
def get_data():
    list_str = [i.strip().split('\n')[0] for i in open("input.txt")]
    list_seeds, all_maps, cur_map = list(map(int, list_str[0].split(': ')[1].split())), [], []
    for str_ in list_str[2:]:
        if str_.endswith(':'):
            continue
        elif str_ == '':
            if cur_map:
                all_maps.append(cur_map)
                cur_map = []
        else:
            cur_map.append(list(map(int, str_.split())))
    if cur_map:
        all_maps.append(cur_map)
    return list_seeds, all_maps

def apply_map(value, map_data):
    for dest_start, src_start, length in map_data:
        if src_start <= value < src_start + length:
            return dest_start + (value - src_start)
    return value

def apply_map_to_range(start, length, map_data):
    ranges = [(start, start + length)]
    result_ranges = []
    for dest_start, start, len_range in map_data:
        new_ranges = []
        for r_start, r_end in ranges:
            intersect_start = max(r_start, start)
            intersect_end = min(r_end, start + len_range)
            if intersect_start < intersect_end:
                offset = dest_start - start
                result_ranges.append((intersect_start + offset, intersect_end + offset))
                if r_start < intersect_start:
                    new_ranges.append((r_start, intersect_start))
                if intersect_end < r_end:
                    new_ranges.append((intersect_end, r_end))
            else:
                new_ranges.append((r_start, r_end))
        ranges = new_ranges
    result_ranges.extend(ranges)
    return result_ranges
@execution_time
def get_solve(list_seed, all_maps, part =1):
    if part == 1:
        for map_data in all_maps:
            list_seed = [apply_map(place, map_data) for place in list_seed]
        return min(list_seed)
    else:
        list_range = []
        for i in range(0, len(list_seed), 2):
            start, len_range = list_seed[i], list_seed[i + 1]
            list_range.append((start, len_range))
        cur_ranges = [(start, start + length) for start, length in list_range]
        for map_data in all_maps:
            new_ranges = []
            for start, end in cur_ranges:
                mapped_ranges = apply_map_to_range(start, end - start, map_data)
                new_ranges.extend(mapped_ranges)
            cur_ranges = new_ranges
        return min(start for start, end in cur_ranges)

list_seeds, all_maps = get_data()
print(f"Решение задания 1:{get_solve(list_seeds,all_maps, part=1)}")
print(f"Решение задания 2:{get_solve(list_seeds,all_maps, part=2)}")
