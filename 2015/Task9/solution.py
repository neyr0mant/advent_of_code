data_str = [[j.strip() for j in i.split("=")] for i in open("input.txt")]
import itertools
dict_data = {}
from functions import execution_time

for i in data_str:
    t1t2 = i[0].split()
    town_1, town_2 = t1t2[0], t1t2[2]
    dict_data.update({(town_1,town_2): int(i[1])})
@execution_time
def get_solve(data_in, part=1):
    list_keys = list(data_in.keys())
    list_distance = []
    town_start, town_finish = [i[0] for i in list_keys],[i[1] for i in list_keys]
    towns = set(town_start + town_finish)
    list_route = list(itertools.permutations(towns,len(towns)))
    for route in list_route:
        rout_distance = 0
        for idx, town1 in enumerate(route):
            if idx + 1 == len(route):
                break
            else:
                town2 = route[idx+1]
                distance = res if (res := data_in.get((town1, town2))) else data_in.get((town2, town1))
                rout_distance += distance
        list_distance.append(rout_distance)
    return min(list_distance) if part == 1 else max(list_distance)


print(f"Решение части 1: {get_solve(dict_data)}")
print(f"Решение части 2: {get_solve(dict_data, part=2)}")