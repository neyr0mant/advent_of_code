data_str = [i for i in open("input.txt")][0]

def get_solve(data_str, part = 1):
    summ_all = 0
    start_num, old_num, len_str = data_str[0], data_str[0], len(data_str)
    for idx, new_num in enumerate(data_str[1:]):
        if part == 1:
            if old_num == new_num:
                summ_all += int(new_num)
        else:
            new_num_p2 = data_str[int(len_str/2) + idx]
            if old_num == new_num_p2:
                summ_all += 2*int(old_num)
            if idx == int(len_str / 2) - 1:
                break
        old_num = new_num
    if part == 1:
        if start_num == old_num:
            summ_all += int(start_num)
    return summ_all
print(f"Решение части 1: {get_solve(data_str)}")
print(f"Решение части 2: {get_solve(data_str, part=2)}")



