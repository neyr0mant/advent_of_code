
from math import floor

def get_summ(num, all_summ = 0, part =1):
    new_num = floor(num / 3) - 2
    if part == 1:
        return new_num
    if new_num <= 0:
        return all_summ
    all_summ += new_num
    return get_summ(new_num, all_summ, part=part)

print(f"Решение части 1: {sum([get_summ(int(i)) for i in open('input.txt')])}")
print(f"Решение части 2: {sum([get_summ(int(i), part=2) for i in open('input.txt')])}")


