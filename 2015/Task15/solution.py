import math
import itertools
from functions import execution_time
list_str = [i.strip() for i in open("input.txt")]
list_data = []
for i in list_str:
    list_split = i.replace(",", "").split()
    list_data.append([int(list_split[2]),  int(list_split[4]), int(list_split[6]),int(list_split[8]),
                      int(list_split[10])])


def generate_combinations(target_sum, num_count, current_combination=[], start=1):
    combinations = []
    if len(current_combination) == num_count:
        if sum(current_combination) == target_sum:
            combinations.append(current_combination)
        return combinations
    for i in range(start, target_sum):
        combinations.extend(generate_combinations(target_sum, num_count, current_combination + [i], i))
    return combinations


@execution_time
def get_solve(part = 1):
    all_combinations = generate_combinations(100, len(list_data))
    max_prod, combination_max,list_prod_max = 0, [], []
    for combination in all_combinations:
        for combination_ in itertools.permutations(combination):
            list_prod = [0, 0, 0,0] if part ==1 else [0, 0, 0, 0, 0]
            for idx, i in enumerate(combination_):
                data = list_data[idx][:4] if part ==1 else list_data[idx]
                for idx_, data_ in enumerate(data):
                    list_prod[idx_] += i*data_
            if all([i > 0 for i in list_prod]):
                cur_prod = math.prod(list_prod) if part == 1 else math.prod(list_prod[:4])
                if cur_prod >= max_prod:
                    if part == 1:
                        max_prod = cur_prod
                    else:
                        if list_prod[-1] == 500:
                            max_prod = cur_prod
    return max_prod



print(f"Решение части 1: {get_solve()}")
print(f"Решение части 2: {get_solve(part=2)}")

