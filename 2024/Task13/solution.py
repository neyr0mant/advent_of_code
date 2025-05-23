#https://adventofcode.com/2024/day/5
list_str = [i.strip("\n ") for i in open("input.txt")]
from sympy import symbols, Eq, solve
list_avt_data_v1, avt_data = [], []
for avt in list_str:
    if "Button" in avt:
        vx, vy = avt.split(":")[1:][0].split(",")
        vx, vy = int(vx[3:]), int(vy[3:])
        avt_data.append((vx, vy))
    elif "Prize" in avt:
        x, y = avt.split(":")[1:][0].split(",")
        x, y = int(x[3:]), int(y[3:])
        avt_data = [(x, y)] + avt_data
    else:
        list_avt_data_v1.append(avt_data)
        avt_data = []
list_avt_data_v2, need_len = [], len("10000000000000")
for av_data in list_avt_data_v1:
    prize_x, prize_y = str(av_data[0][0]), str(av_data[0][1])
    prize_x, prize_y = (int(str('1' + '0' * (need_len - len(prize_x)-1) + prize_x)),
                        int(str('1' + '0' * (need_len - len(prize_y)-1) + prize_y)))
    list_avt_data_v2.append([(prize_x, prize_y), av_data[1], av_data[2]])
def calculate_min_time(prize_x_y, v1, v2):
    prize_x, prize_y = prize_x_y
    v1x, v1y, v2x, v2y, tv1, tv2 = v1[0],  v1[1], v2[0], v2[1], symbols('tv1'), symbols('tv2')
    eq1, eq2 = Eq(v1x * tv1 + v2x * tv2, prize_x), Eq(v1y * tv1 + v2y * tv2, prize_y)
    solutions = solve((eq1, eq2), (tv1, tv2))
    if solutions:
        tv1, tv2 = solutions[tv1], solutions[tv2]
        if all(["/" not in str(tv1),  tv1 >= 0, "/" not in str(tv2), tv2 >= 0]):
            return tv1, tv2
def get_solve(part=1):
    solve_avt_data = list_avt_data_v1 if part==1 else list_avt_data_v2
    return sum([sum([prize[0] * 3 + prize[1]]) for i in solve_avt_data if
                (prize := calculate_min_time(i[0], i[1], i[2]))])
print(f"Решение части 1: {get_solve()}")
print(f"Решение части 2: {get_solve(part=2)}")


