from datetime import datetime, timedelta
from collections import Counter

list_data = sorted([i.strip() for i in open("input.txt")],
                   key=lambda x: datetime.strptime(x[1:17], "%Y-%m-%d %H:%M"))
dict_data, id_guard = {}, None
for data in list_data:
    data_time, data_guard = datetime.strptime(data[1:17],"%Y-%m-%d %H:%M"), data[19:]
    if "#" in data_guard:
        id_guard = data_guard.split("#")[1].split()[0]
        if id_guard in dict_data.keys():
            dict_data[id_guard].append([])
        else:
            dict_data[id_guard] = [[]]
            continue
    else:
        dict_data[id_guard][-1].append(data_time.minute)

def get_solve(dict_data, part=1):
    id_guard, sum_sleep_max, max_minute_sleep, max_count_minute = None, 0, 0, 0
    for key, val in dict_data.items():
        list_sleep = [[(j, i[idx + 1]) for idx, j in enumerate(i) if all([idx + 1 < len(i), idx % 2 == 0])]
                      for i in dict_data[key]]
        list_range_sleep = []
        for duty in list_sleep:
            list_extend = [list(range(j[0], j[1])) for j in duty]
            [list_range_sleep.extend(i) for i in list_extend]
        counter = Counter(list_range_sleep)
        if counter:
            max_minute_sleep_, max_count_minute_ = counter.most_common(1)[0]
            if part == 1:
                sum_sleep = sum([sum([j[1] - j[0] for j in i]) for i in list_sleep])
                if sum_sleep > sum_sleep_max:
                    id_guard, max_minute_sleep, sum_sleep_max = key,max_minute_sleep_, sum_sleep
            else:
                if max_count_minute_>max_count_minute:
                    id_guard, max_count_minute, max_minute_sleep = key, max_count_minute_, max_minute_sleep_
    return int(id_guard)*max_minute_sleep

print(f"Решение части 1: {get_solve(dict_data)}")
print(f"Решение части 2: {get_solve(dict_data, part=2)}")