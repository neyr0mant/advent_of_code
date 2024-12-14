#https://adventofcode.com/2024/day/11

def get_next_list_stones(num):
    if num == 0:
        return [1]
    str_num = str(num)
    len_num = len(str_num)
    return [int(str_num[:len_num // 2]), int(str_num[len_num // 2:])] if len_num % 2 == 0 else [num * 2024]
def get_count_stones(list_stones, count_iter):
    start_stones = {stone: 1 for stone in list_stones}
    for _ in range(count_iter):
        next_stones = {}
        for сur_stone, count in start_stones.items():
            new_stones = get_next_list_stones(сur_stone)
            for stone in new_stones:
                if stone in next_stones:
                    next_stones[stone] += count
                else:
                    next_stones[stone] = count
        start_stones = next_stones
    return sum(start_stones.values())
print(f"Решение части 1: {get_count_stones([2, 54, 992917, 5270417, 2514, 28561, 0, 990], 25)}")
print(f"Решение части 2: {get_count_stones([2, 54, 992917, 5270417, 2514, 28561, 0, 990], 75)}")
