from copy import deepcopy
list_data = [int(i.strip()) for i in open("input.txt")]
from functions import execution_time

@execution_time
def get_solve(list_data, part=1):
    list_data = deepcopy(list_data)
    start_index, count = 0, 0
    while True:
        bounce = list_data[start_index]
        new_index = start_index+bounce
        if new_index < 0 or new_index > len(list_data)-1:
            count += 1
            break
        if part == 1:
            list_data[start_index] += 1
        else:
            list_data[start_index] += -1 if bounce >= 3 else 1
        count += 1
        start_index = new_index
    return count

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")