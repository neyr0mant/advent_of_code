import os
from functions import execution_time
# link task https://adventofcode.com/2020/day/18
list_data = [i.strip("\n ") for i in open("input.txt")]

def get_sum(str_s, part):
    sum_all = 1
    list_s = str_s.split("*")
    if part == 1:
        for i in list_s:
          j = i.split("+")
          sum_all = sum_all*int(j[0]) + sum([int(i) for i in j[1:]])
    else:
        list_sum = [sum([int(j) for j in i.split("+")]) for i in list_s]
        for i in list_sum:
          sum_all = sum_all*i
    return sum_all


def get_sum_all_for_str(str_in, part):
    sum_all = 0
    while "(" in str_in:
        index_r = str_in.rindex("(")
        index_l = str_in[index_r + 1:].index(")") + index_r + 1
        str_new = str_in[index_r + 1:index_l]
        sum_str_new = get_sum(str_new, part)
        str_in = str_in[:index_r] + "%s" % sum_str_new + str_in[index_l + 1:]
        sum_all += sum_str_new
    return get_sum(str_in, part)


print(f"Решение части 1: {sum([get_sum_all_for_str(i,1) for i in list_data])}")
print(f"Решение части 2: {sum([get_sum_all_for_str(i, 2) for i in list_data])}")

