#https://adventofcode.com/2017/day/2
list_data = [[int(j) for j in i.strip().split()] for i in open("input.txt")]


def get_solve(list_in):
    for idx_x, x in enumerate(list_in):
        list_not_x = list_in[:idx_x] + list_in[idx_x+1:]
        for y in list_not_x:
            if x % y == 0:
                return int(x/y)

print(f"Решение части 1: {sum([max(i)- min(i) for i in list_data])}")
print(f"Решение части 2: {sum([get_solve(i) for i in list_data])}")







