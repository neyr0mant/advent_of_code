import time
from copy import deepcopy
from PIL import Image, ImageDraw
import uuid


def execution_time(func):
    def wrapped(*args, **kwargs):
        time_start = time.time()
        res = func(*args, **kwargs)
        time_finish = time.time()
        print(f"Метод {func.__name__} отработал за {round(time_finish - time_start, 3)} с.")
        return res
    return wrapped


alphabet = {"lower": "abcdefghijklmnopqrstuvwxyz", "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}


class Matrix:
    def __init__(self, list_data: list):
        assert (len([i for i in list_data if len(i) == len(list_data[0])])
                == len(list_data)), "Это не матрица!Не все списки равны по длине!"
        self.matrix = list_data
        self.x_max, self.y_max = self.get_rank_matrix(self.matrix)
        self.streams = []

    @staticmethod
    def get_rank_matrix(matrix: list):
        return len(matrix[0]), len(matrix)

    def update_list_elements(self, data_for_change: dict):
        for elem, list_x_y in data_for_change.items():
            for x_y in list_x_y:
                x, y = x_y
                self.matrix[y][x] = elem

    def __setitem__(self, x_y, val):
        x, y = x_y
        self.matrix[y][x] = val

    def __getitem__(self, x_y):
        x, y = x_y
        return self.matrix[y][x]

    def find(self, elem: str):
        list_index = []
        for y, list_y in enumerate(self.matrix):
            for x, elem_ in enumerate(list_y):
                if elem_ == elem:
                    list_index.append((x, y))
        return list_index

    def print_matrix(self, dict_elements: dict = None, only_res=False):
        if not dict_elements:
            x_max, y_max, list_matrix = self.x_max, self.y_max, self.matrix
        else:
            new_matrix = self.get_matrix_with_change_elements(dict_elements)
            x_max, y_max = self.get_rank_matrix(new_matrix)
            list_matrix = new_matrix
        res_matrix = "\n".join([" ".join([str(j) for j in i]) for i in list_matrix])
        if only_res:
            return res_matrix
        print(f"""Матрица размером {x_max}x{y_max}\nРасположение осей: X-→, Y↓""")
        print(res_matrix)

    def get_matrix_with_change_elements(self, dict_elements: dict):
        new_matrix = deepcopy(self.matrix)
        # изменяем элементы
        for elem, list_coordinate in dict_elements.items():
            for coordinate in list_coordinate:
                x, y = coordinate
                new_matrix[y][x] = elem
        return new_matrix


    def draw(self, factor=3, symbol_dif = 1):
        size_x = factor * self.x_max
        size_y = factor * self.y_max
        im = Image.new('RGB', (size_x, size_y), '#1a1a1a')
        draw = ImageDraw.Draw(im)
        for y in range(self.y_max):
            for x in range(self.y_max):
                x_size = x * factor
                y_size = y * factor
                if self.matrix[x][y] == symbol_dif:
                    draw.point([(x_size, y_size)], '#ffa126')
        self.streams.append(im)

    def get_gif(self, name_gif=None):
        name_gif = name_gif if name_gif else f'{uuid.uuid4()}.gif'
        self.streams[0].save(name_gif, save_all=True,
                             append_images=self.streams[1:])


