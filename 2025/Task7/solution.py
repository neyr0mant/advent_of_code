#https://adventofcode.com/2024/day/7
list_data = [[int(j.replace(":", "")) for j in i.strip("\n ").split()] for i in open("input.txt")]
from functions import execution_time
def get_good_calibration(n, list_num, part=1):
    def assert_list_num(index, cur_num):
        if index == len(list_num):
            return cur_num == n
        next_num = list_num[index]
        assert_list =[assert_list_num(index + 1, cur_num + next_num), assert_list_num(index + 1, cur_num * next_num)]
        if part == 2:
            assert_list.append(assert_list_num(index + 1, int(f"{cur_num}{next_num}")))
        if any(assert_list):
            return True
        return False
    return assert_list_num(1, list_num[0])

@execution_time
def get_solve(part):
    return sum([i[0] for i in list_data if get_good_calibration(i[0],i[1:], part=part)])


print(f"Решение части 1: {get_solve(1)}")
print(f"Решение части 2: {get_solve(2)}")















