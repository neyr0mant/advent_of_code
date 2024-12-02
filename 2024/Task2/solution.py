#https://adventofcode.com/2024/day/2
list_data = [[int(j) for j in i.strip("\n ").split()] for i in open("input.txt")]
def get_good_report(report, part=1):
    list_diff = [(report[idx + 1] - i, idx) for idx, i in enumerate(report) if idx + 1 != len(report)]
    list_more = [i for i in list_diff if 3 >= i[0] > 0]
    list_less = [i for i in list_diff if -3 <= i[0] < 0]
    if len(list_more) == len(list_diff) or len(list_less) == len(list_diff):
        return True
print(f"Решение части 1: {len([i for i in list_data if get_good_report(i)])}")









