#https://adventofcode.com/2024/day/6
from functions import *
list_data = [[j for j in i if j != "\n"] for i in open("input.txt")]
matrix = Matrix(list_data)
matrix.print_matrix()
operators = ["*", "+"]
data_index_operator = {i: [] for i in operators}
operators_list = matrix.matrix[-1]
start_index = min([operators_list.index(i) for i in operators])
while start_index < matrix.x_max:
    operator = operators_list[start_index]
    next_list = [operators_list[start_index + 1:].index(i) for i in operators if i in operators_list[start_index + 1:]]
    end_index = min(next_list) + start_index if next_list else matrix.x_max
    data_index_operator[operator].append([start_index, end_index])
    start_index = end_index + 1
num_data = matrix.matrix[:-1]
@execution_time
def get_solve(part = 1):
    sum_all = 0
    for operator_, list_cor in data_index_operator.items():
        for cor in list_cor:
            start, end = cor
            if part == 1:
                num_list = ["".join([j for j in x_list[start:end] if j not in [" ", "x"]]) for x_list in num_data]
            else:
                num_list = []
                for x in range(start, end):
                    num = ""
                    for y in range(matrix.y_max):
                        digit = matrix[x, y]
                        if digit.isdigit():
                            num = num + digit
                    num_list.append(num)
            cmd = f"{operator_}".join(num_list)
            sum_all += eval(cmd)
    return sum_all


print(f"Решение части 1: {get_solve()}")
print(f"Решение части 2: {get_solve(part = 2)}")











