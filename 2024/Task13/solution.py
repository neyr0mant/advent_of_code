#https://adventofcode.com/2024/day/5
list_str = [i.strip("\n ") for i in open("input.txt")]
from sympy import symbols, Eq, solve
list_avt_data = []
avt_data = []
for i in list_str:
    if "Button" in i:
        vx, vy = i.split(":")[1:][0].split(",")
        vx, vy = int(vx[3:]), int(vy[3:])
        avt_data.append((vx, vy))
    elif "Prize" in i:
        x, y = i.split(":")[1:][0].split(",")
        x, y = int(x[3:]), int(y[3:])
        avt_data = [(x, y)] + avt_data
    else:
        list_avt_data.append(avt_data)
        avt_data = []
def calculate_min_time(prize_x_y, v1, v2):
    x, y = prize_x_y
    v1x, v1y = v1
    v2x, v2y = v2
    tv1, tv2 = symbols('tv1 tv2')
    eq1 = Eq(v1x * tv1 + v2x * tv2, x)
    eq2 = Eq(v1y * tv1 + v2y * tv2, y)
    solutions = solve((eq1, eq2), (tv1, tv2))
    if solutions:
        tv1 = solutions[tv1]
        tv2 = solutions[tv2]
        if all(["/" not in str(tv1),  tv1 >= 0, "/" not in str(tv2), tv2 >= 0]):
            return tv1, tv2
        else:
            return None
def get_solve(part=1):
    if part ==1:
        return sum([sum([prize[0] * 3 + prize[1]]) for i in list_avt_data if
                    (prize := calculate_min_time(i[0], i[1], i[2]))])
    else:
        new_avt_data = []
        need_len = len("10000000000000")
        for avt_data in list_avt_data:
            prize_x, prize_y = str(avt_data[0][0]), str(avt_data[0][1])
            add_len_x, add_len_y = need_len - len(prize_x)-1, need_len - len(prize_y)-1
            prize_x, prize_y = (int(str('1' + '0' * add_len_x + prize_x)),
                                int(str('1' + '0' * add_len_y + prize_y)))
            new_avt_data.append([(prize_x, prize_y), avt_data[1], avt_data[2]])
        return sum([sum([prize[0] * 3 + prize[1]]) for i in new_avt_data if
                    (prize := calculate_min_time(i[0], i[1], i[2]))])
print(f"Решение части 1: {get_solve(part=1)}")
print(f"Решение части 2: {get_solve(part=2)}")


