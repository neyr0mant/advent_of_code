from functions import *
list_data = [i.strip() for i in open("input.txt")]

def sort_str(str_, n):
    len_num = len(str_)
    delete, acc = len_num - n, []
    for digit in str_:
        while acc and delete > 0 and acc[-1] < digit:
            acc.pop()
            delete -= 1
        acc.append(digit)
    return acc
@execution_time
def get_solve(list_data_, part=1):
    n = 2 if part == 1 else 12
    summ_all = 0
    for num in list_data_:
        summ_all += int("".join(sort_str(num, n)[:n]))
    return summ_all

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")