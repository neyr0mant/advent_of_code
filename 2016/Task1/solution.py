list_move = [i.replace(" ", "").split(",") for i in open("input.txt")][0]
def get_answer(list_move_, part=1):
    x_santa, y_santa, direction, set_santa, double_place = 0, 0, (0, 1), set(), None
    for idx, data in enumerate(list_move_):
        rule = [i for i in ["L", "R"] if i in data][0]
        direction = (-direction[1], direction[0]) if rule == "L" \
            else (direction[1], -direction[0])
        count = int(data.split(rule)[1])
        x_santa_old, y_santa_old = x_santa, y_santa
        x_santa += count*direction[0]
        y_santa += count*direction[1]
        if part == 2:
            if dir_x := direction[0]:
                list_step = [(x_santa_old + i*dir_x, y_santa_old) for i in range(count)]
            else:
                dir_y = direction[1]
                list_step = [(x_santa_old, y_santa_old + i*dir_y) for i in range(count)]
            for step in list_step:
                if step in set_santa:
                    x_santa, y_santa = step
                    double_place = step
                    break
                else:
                    set_santa.add(step)
                if double_place:
                    break
    return abs(x_santa) + abs(y_santa)

print(f"Решение части 1: {get_answer(list_move)}")
print(f"Решение части 2: {get_answer(list_move, part=2)}")