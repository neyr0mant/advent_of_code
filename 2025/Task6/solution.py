#https://adventofcode.com/2024/day/6
import sys
from functions import *
sys.setrecursionlimit(10000)
laboratory_data = [[j for j in i.strip("\n ").split()[0]] for i in open("input.txt")]
matrix = Matrix(laboratory_data)
def get_answer():
    x_max, y_max, start_symbol = matrix.x_max, matrix.y_max, "^"
    data_move = {'^': [0, -1, '>'], '>': [1, 0, 'v'], 'v': [0, 1, '<'], '<': [-1, 0, '^']}
    start_coordinate = matrix.find(start_symbol)[0]
    x_security, y_security = start_coordinate

    def walk_security(x_start, y_start, symbol=start_symbol, set_dot = set(), set_square_position = set(),
                      dict_all_position = {}, prison = 0):
        set_dot.add((x_start, y_start))
        set_square_position.add(symbol)
        if not all([0 < x_start + 1 < x_max, 0 < y_start + 1 < y_max]):
            return len(set_dot), prison
        x_next, y_next = x_start + data_move[symbol][0], y_start + data_move[symbol][1]
        next_symbol = matrix[x_next, y_next]
        if next_symbol == "#":
            symbol = data_move[symbol][2]
            x_next, y_next = x_start + data_move[symbol][0], y_start + data_move[symbol][1]
            # matrix.print_matrix(dict_all_position)
        if len(set_square_position) == 4:
            all_coordinate = []
            [all_coordinate.extend(i) for i in list(dict_all_position.values())]
            if (x_start, y_start) in all_coordinate:
                # matrix.print_matrix(dict_all_position)
                set_square_position = set(symbol)
                prison += 1
                # matrix.print_matrix({"O": [(x_next, y_next)]})
        cur_position = dict_all_position.get(symbol, [])
        cur_position.extend([(x_start, y_start)])
        dict_all_position[symbol] = cur_position
        return walk_security(x_next, y_next, symbol=symbol, set_square_position=set_square_position,
                             dict_all_position=dict_all_position, prison=prison)
    return walk_security(x_security, y_security)

res_walk = get_answer()

print(f"Решение части 1: {res_walk[0]}")
print(f"Решение части 2: {res_walk[1]}")











