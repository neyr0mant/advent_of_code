from functions import *
list_data = [i.strip() for i in open("input.txt")]
@execution_time
def get_solve(list_data_, n=2):
    summ_all = 0
    for num in list_data_:
        len_num = len(num)
        delete, acc = len_num - n, []
        for digit in num:
            while acc and delete > 0 and acc[-1] < digit:
                acc.pop()
                delete -= 1
            acc.append(digit)
        while delete > 0:
            acc.pop()
            delete -= 1
        summ_all += int("".join(acc[:n]))
    return summ_all

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, n=12)}")