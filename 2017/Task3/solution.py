#https://adventofcode.com/2017/day/3

num = 347991
def get_solve(num, part =1):
    i, count_step, start, start_vector, step_x, step_y, dict_coordinate, summ = (1, 1, [0, 0], (1,0),
                                                                                 0, 0, {(0, 0): 1}, 0)
    while i < num if part == 1 else summ < num:
        if step_x >= count_step or step_y >= count_step:
            start_vector = (-start_vector[1], start_vector[0])
            if start_vector[0]:
                count_step += 1
                step_y = 0
            else:
                step_x = 0
        i += 1
        if start_vector[0]:
            step_x += 1
        else:
            step_y += 1
        start = (start[0] + start_vector[0], start[1] + start_vector[1])
        if part == 2:
            neighbours = [(start[0] + 1, start[1]), (start[0] - 1, start[1]),
                          (start[0], start[1] + 1), (start[0], start[1] - 1),
                          (start[0] + 1, start[1] + 1), (start[0] - 1, start[1]+1),
                          (start[0] - 1, start[1] - 1), (start[0]+1, start[1] - 1)]
            new_summ = sum([dict_coordinate.get(i,0) for i in neighbours])
            if new_summ > summ:
                summ = new_summ
            dict_coordinate.update({start: summ})
    return abs(start[0]) + abs(start[1]) if part == 1 else summ

print(f"Решение части 1: {get_solve(347991)}")
print(f"Решение части 2: {get_solve(347991, part=2)}")
