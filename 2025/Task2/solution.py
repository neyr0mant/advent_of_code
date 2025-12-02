from functions import execution_time
list_data = [j.split("-") for j in [i.strip() for i in open("input.txt")][0].split(",")]

@execution_time
def get_solve(list_data_, part=1):
    total_sum = 0
    for interval in list_data_:
        start, end = int(interval[0]), int(interval[1])
        for i in range(start, end + 1):
            str_i = str(i)
            len_i = len(str_i)
            if part == 1:
                if len_i % 2 == 0:
                    half = len_i // 2
                    if str_i[:half] == str_i[half:]:
                        total_sum += i
            else:
                max_sub_len = len_i // 2
                for sub_len in range(1, max_sub_len + 1):
                    if len_i % sub_len == 0:
                        sub_str = str_i[:sub_len]
                        if sub_str * (len_i // sub_len) == str_i:
                            total_sum += i
                            break
    return total_sum

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")