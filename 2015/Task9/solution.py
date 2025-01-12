data_str = [[j.strip() for j in i.split("=")] for i in open("input.txt")]
import itertools
dict_data = {}

for i in data_str:
    t1t2 = i[0].split()
    town_1, town_2 = t1t2[0], t1t2[2]
    dict_data.update({(town_1,town_2): int(i[1])})

def get_solve(data_in):

    towns, distance = set(data_in.keys()), list(data_in.values())
    return 1

print(f"Решение части 1: {get_solve(dict_data)}")