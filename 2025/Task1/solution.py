list_data = [i.strip().replace("L", "-").replace("R", "+") for i in open("input.txt")]

def get_solve(list_data_, part=1):
    pos, count_zero = 50, 0
    for cmd in list_data_:
        steps = eval(cmd)
        new_pos = (pos + steps) % 100
        if part == 1:
            if new_pos == 0:
                count_zero += 1
        else:
            count_circle = abs(steps) // 100
            count_zero += count_circle
            rem_steps = abs(steps) - count_circle * 100
            if steps > 0 and rem_steps + pos > 99:
                count_zero += 1
            elif steps < 0 and pos - rem_steps <= 0 and pos != 0:
                count_zero += 1
        pos = new_pos
    return count_zero

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")
