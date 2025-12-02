import re

list_data = [j.split("-") for j in [i.strip() for i in open("input.txt")][0].split(",")]

def get_solve(list_data_, part =1):
    summ_bad = 0
    for interval in list_data_:
        start, end = [int(i) for i in interval]
        for i in range(start, end+1):
            str_i = str(i)
            if not str_i.startswith("0"):
                len_i = len(str_i)
                if part == 1:
                    if not len_i % 2:
                        left, right = str_i[:len_i//2], str_i[len_i//2:]
                        if left == right:
                            summ_bad += i
                else:
                    pattern = r'^(.+?)\1+$'
                    res = re.findall(pattern, str_i)
                    if len(res) == 1:
                        if count := str_i.count(res[0]):
                            if count >= 2:
                                if res[0]*count == str_i:
                                    summ_bad += i
    return summ_bad



print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")