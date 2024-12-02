#https://adventofcode.com/2024/day/2
list_data = [[int(j) for j in i.strip("\n ").split()] for i in open("input.txt")]
from copy import deepcopy
def get_good_report(report, part=1):
    list_diff = [(report[idx + 1] - i) for idx, i in enumerate(report) if idx + 1 != len(report)]
    list_more = [i for i in list_diff if 3 >= i > 0]
    list_less = [i for i in list_diff if -3 <= i < 0]
    if any([len(list_more) == len(list_diff), len(list_less) == len(list_diff)]):
        return True
    if part == 2:
        for i in range(len(report)):
            copy_report = deepcopy(report)
            copy_report.pop(i)
            if get_good_report(copy_report, part=1):
                return True
        return False

print(f"Решение части 1: {len([i for i in list_data if get_good_report(i)])}")
print(f"Решение части 2: {len([i for i in list_data if get_good_report(i, part=2)])}")









