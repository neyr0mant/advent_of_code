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
            step = 1 if steps > 0 else -1
            count_zero += abs(steps) // 100 # полное количество кругов
            for _ in range(abs(steps) % 100): # допровряем остаток
                pos = (pos + step) % 100
                if pos == 0:
                    count_zero += 1
        pos = new_pos
    return count_zero

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")
