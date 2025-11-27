list_data = [int(i.strip()) for i in open("input.txt")]
def get_solve(list_data_, part=1):
    sort_data = sorted(list_data_)
    data = [0] + sort_data + [sort_data[-1] +3]
    if part == 1:
        diff_count = {1: 0, 2: 0, 3: 0}
        for i in range(1, len(data)):
            diff = data[i] - data[i - 1]
            if diff in diff_count:
                diff_count[diff] += 1
        return diff_count[1] * diff_count[3]
    else:
        ways = {adapter: 0 for adapter in sort_data}
        ways[0] = 1
        for adapter in data[1:]:
            ways[adapter] = (
                    ways.get(adapter - 1, 0) +
                    ways.get(adapter - 2, 0) +
                    ways.get(adapter - 3, 0)
            )
        return ways[data[-1]]

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 1: {get_solve(list_data, part=2)}")