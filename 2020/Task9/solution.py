from itertools import combinations
list_data = [int(i.strip()) for i in open("input.txt")]
def get_solve_p1(list_data_, len_preamble =5):
    iteration = 0
    while iteration+len_preamble <= len(list_data_):
        index_l, index_r = iteration, len_preamble+iteration
        sum_preamble = {a + b for a, b in combinations(list_data_[index_l:index_r], 2)}
        num = list_data_[iteration+len_preamble]
        if num not in sum_preamble:
            return num
        iteration += 1
    return None

def get_solve_p2(list_data_, target):
    start, cur_sum = 0, list_data_[0]
    for end in range(1, len(list_data_)):
        cur_sum += list_data_[end]
        while cur_sum > target and start < end - 1:
            cur_sum -= list_data_[start]
            start += 1
        if cur_sum == target and (end - start + 1) > 1:
            contiguous_range = list_data_[start:end+1]
            return min(contiguous_range) + max(contiguous_range)

    return None

solve_1 = get_solve_p1(list_data, len_preamble=25)
print(f"Решение части 1: {solve_1}")
print(f"Решение части 1: {get_solve_p2(list_data, target=solve_1)}")


