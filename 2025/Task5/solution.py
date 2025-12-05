list_data = [i.strip() for i in open('input.txt', 'r')]
dict_data = {"ranges": [], "list_id": []}
for i in list_data:
    if i:
        if "-" in i:
            cur_data = dict_data["ranges"]
            dict_data["ranges"].append([int(j) for j in i.split("-")])
        else:
            dict_data["list_id"].append(int(i))

def get_solve(dict_data_, part=1):
    count_id = 0
    if part == 1:
        for id_ in dict_data_["list_id"]:
            for range_ in dict_data["ranges"]:
                start, end = range_
                if id_ in range(start, end + 1):
                    count_id += 1
                    break
    else:
        ranges = dict_data["ranges"]
        ranges.sort(key=lambda x: x[0])
        count_id, parse_range = 0, []
        for cur in ranges:
            if not parse_range:
                parse_range.append(cur)
            else:
                last = parse_range[-1]
                if cur[0] <= last[1] + 1:
                    last[1] = max(last[1], cur[1])
                else:
                    parse_range.append(cur)
        count_id = 0
        for start, end in parse_range:
            count_id += end - start + 1
    return count_id


print(f"Решение части 1: {get_solve(dict_data)}")
print(f"Решение части 2: {get_solve(dict_data, part=2)}")