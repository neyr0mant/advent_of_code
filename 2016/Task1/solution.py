list_move = [i.replace(" ", "").split(",") for i in open("input.txt")][0]
def get_answer(list_move_, part=1):
    x_santa, y_santa, direction, set_santa = 0, 0, (0, 1), set(),
    for idx, data in enumerate(list_move_):
        rule = [i for i in ["L", "R"] if i in data][0]
        direction = (-direction[1], direction[0]) if rule == "L" \
            else (direction[1], -direction[0])
        count = int(data.split(rule)[1])
        x_santa_old, y_santa_old = x_santa, y_santa
        x_santa += count*direction[0]
        y_santa += count*direction[1]
        if part == 2:
            for i in range(count):
                if dir_ := direction[0]:
                    step = (x_santa_old + i*dir_, y_santa_old)
                else:
                    dir_ = direction[1]
                    step = (x_santa_old, y_santa_old + i*dir_)
                if step in set_santa:
                    x_santa, y_santa = step
                    break
                else:
                    set_santa.add(step)
    return abs(x_santa) + abs(y_santa)

print(f"Решение части 1: {get_answer(list_move)}")
print(f"Решение части 2: {get_answer(list_move, part=2)}")