import time
from copy import deepcopy
import threading


def execution_time(func):
    def wrapped(*args, **kwargs):
        time_start = time.time()
        res = func(*args, **kwargs)
        time_finish = time.time()
        print(f"Script execution time: {round(time_finish - time_start, 3)} sec.")
        return res

    return wrapped


class Matrix:
    def __init__(self, list_data: list):
        assert (len([i for i in list_data if len(i) == len(list_data[0])])
                == len(list_data)), "Это не матрица!Не все списки равны по длине!"
        self.matrix = list_data
        self.x_max, self.y_max = self.get_rank_matrix(self.matrix)

    @staticmethod
    def get_rank_matrix(matrix: list):
        return len(matrix[0]), len(matrix)

    def update_matrix_element(self, elem, x_y):
        x, y = x_y
        self.matrix[y][x] = elem

    def update_matrix_list_data(self, data_for_change: dict):
        for elem, list_x_y in data_for_change.items():
            for x_y in list_x_y:
                self.update_matrix_element(elem, x_y)

    def __getitem__(self, x_y: tuple):
        return self.matrix[x_y[1]][x_y[0]]

    def find(self, elem: str):
        list_index = []
        for y, list_y in enumerate(self.matrix):
            for x, elem_ in enumerate(list_y):
                if elem_ == elem:
                    list_index.append((x, y))
        return list_index

    def print_matrix(self, dict_elements: dict = None):
        if not dict_elements:
            x_max, y_max, list_matrix = self.x_max, self.y_max, self.matrix
        else:
            new_matrix = self.get_matrix_with_change_elements(dict_elements)
            x_max, y_max = self.get_rank_matrix(new_matrix)
            list_matrix = new_matrix
        print(f"""Матрица размером {x_max}x{y_max}""")
        print(f"""Расположение осей""")
        print(f"""-- -- -- X\n¦\n¦\n¦\nY""")
        res_matrix = "\n".join([" ".join([str(j) for j in i]) for i in list_matrix])
        print(res_matrix)

    def get_matrix_with_change_elements(self, dict_elements: dict):
        new_matrix = deepcopy(self.matrix)
        # изменяем элементы
        for elem, list_coordinate in dict_elements.items():
            for coordinate in list_coordinate:
                x, y = coordinate
                new_matrix[y][x] = elem
        return new_matrix


