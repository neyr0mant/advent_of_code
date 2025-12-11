#https://adventofcode.com/2024/day/11
dict_data = {i.strip().split(":")[0]: i.strip().split(":")[1].split() for i in open("input.txt")}
def get_solve(dict_data_, part = 1):
    solve = 0
    if part == 1:
        start, end = 'you', 'out'
        list_start = [(start, [start])]
        all_paths = []
        while list_start:
            cur, path = list_start.pop()
            if cur == end:
                all_paths.append(path)
                continue
            if cur in dict_data_:
                for neighbor in dict_data_[cur]:
                    if neighbor not in path:
                        new_path = path + [neighbor]
                        list_start.append((neighbor, new_path))
        solve = len(all_paths)
    return solve
print(f"Решение части 1: {get_solve(dict_data)}")
# print(f"Решение части 2: {get_solve()}")
