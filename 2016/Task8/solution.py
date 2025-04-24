from functions import Matrix
import re
list_str = [i.strip() for i in open("input.txt")]
matrix = Matrix([[" " for _ in range(50)] for _ in range(6)])
def get_solve():
    for data in list_str:
        data_digit = [int(i) for i in re.findall(r'\d+', data)]
        if "rect" in data:
            list_coordinate_update = [[j, i] for j in range(data_digit[0]) for i in range(data_digit[1])]
            for coordinate in list_coordinate_update:
                matrix[coordinate[0], coordinate[1]] = "#"
        else:
            rotate_row = "rotate row" in data
            reminder = data_digit[1] // matrix.x_max if rotate_row else data_digit[1] // matrix.y_max
            reminder = reminder if reminder else data_digit[1]
            list_data = matrix.matrix[data_digit[0]] if rotate_row else [i[data_digit[0]] for i in matrix.matrix]
            new_list_data = [list_data[idx-reminder] for idx, i in enumerate(list_data)]
            if rotate_row:
                matrix.matrix[data_digit[0]] = new_list_data
            else:
                for idx, x_list in enumerate(matrix.matrix):
                    x_list[data_digit[0]] = new_list_data[idx]
    return sum([len([x for x in x_list if x == "#"]) for x_list in matrix.matrix])
print(f"Решение части 1: {get_solve()}")
print(f"Решение части 2: \n{matrix.print_matrix(only_res=True)}")