import time
from copy import deepcopy


def execution_time(func):
    def wrapped(*args, **kwargs):
        time_start = time.time()
        res = func(*args, **kwargs)
        time_finish = time.time()
        execution_time = time_finish - time_start
        print("Script execution time: %s sec" % execution_time)
        return res

    return wrapped


class Matrix():
    def __init__(self, list_data: list):
        assert (len([i for i in list_data if len(i) == len(list_data[0])])
                == len(list_data)), "Это не матрица!Не все списки равны по длине!"
        self.list_data = list_data
        self.x_max, self.y_max = self.get_rank_matrix(self.list_data)

    @staticmethod
    def get_rank_matrix(matrix: list):
        return len(matrix[0]), len(matrix)

    def update_matrix(self, dict_elements: dict, revert_x_y = False):
        for elem, list_x_y in dict_elements.items():
            for x_y in list_x_y:
                x, y = x_y if not revert_x_y else x_y[::-1]
                self.list_data[y][x] = elem

    def __getitem__(self, x_y: tuple):
        return self.list_data[x_y[1]][x_y[0]]

    def find(self, elem: str):
        list_index = []
        for y, list_y in enumerate(self.list_data):
            for x, elem_ in enumerate(list_y):
                if elem_ == elem:
                    list_index.append((x, y))
        return list_index

    def print_matrix(self, dict_elements: dict = None):
        if not dict_elements:
            x_max, y_max, list_matrix = self.x_max, self.y_max, self.list_data
        else:
            new_matrix = self.get_matrix_with_change_elements(dict_elements)
            x_max, y_max = self.get_rank_matrix(new_matrix)
            list_matrix = new_matrix
        print(f"""Матрица размером {x_max}x{y_max}""")
        print(f"""Расположение осей""")
        print(f"""-- -- -- Y\n¦\n¦\n¦\nX""")
        res_matrix = "\n".join([" ".join([str(j) for j in i]) for i in list_matrix])
        print(res_matrix)
        return res_matrix

    def get_matrix_with_change_elements(self, dict_elements: dict):
        new_matrix = deepcopy(self.list_data)
        # изменяем элементы
        for elem, list_coordinate in dict_elements.items():
            for coordinate in list_coordinate:
                x, y = coordinate
                new_matrix[y][x] = elem
        return new_matrix
