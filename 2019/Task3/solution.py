#Решения нет
list_data = [i.strip() for i in open("input.txt")]
from functions import execution_time

def get_cabling(list_rule, get_step_to_place =None):
    list_step, count_step_all = [(0,0)], 0
    for i in list_rule.split(","):
        old_place = list_step[-1]
        x_old, y_old = old_place[0], old_place[1]
        rule, count_step, new_place = i[0], int(i[1:]), None
        for j in range(1, count_step + 1):
            if rule == "R":
                new_place = (x_old+j,y_old)
            if rule == "L":
                new_place = (x_old-j,y_old)
            if rule == "U":
                new_place = (x_old,y_old+j)
            if rule == "D":
                new_place = (x_old, y_old-j)
            if get_step_to_place:
                if new_place == get_step_to_place:
                    count_step_all += j
                    return count_step_all
            list_step.append(new_place)
        count_step_all += count_step
    return set(list_step[1:])
@execution_time
def get_solve(list_data, part=1):
    wire_1, wire_2 = list_data[0], list_data[1]
    cabling_1, cabling_2 = get_cabling(wire_1), get_cabling(wire_2)
    list_assert_1, list_assert_2 = [i for i in cabling_1 if i in cabling_2], []
    if part == 2:
        list_assert_2 = [sum([get_cabling(j, i) for j in [wire_1,wire_2]]) for i in list_assert_1]
    return min([abs(i[0]) + abs(i[1]) for i in list_assert_1]) if part ==1 else min(list_assert_2)



print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")