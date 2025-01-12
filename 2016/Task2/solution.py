#https://adventofcode.com/2016/day/2
list_data = [i.strip() for i in open("input.txt")]
from functions import execution_time
@execution_time
def get_solve(list_rule, part=1):
    rule_move = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}
    rule_phone_p1 = {1: (0,2), 2: (1, 2), 3: (2, 2), 4: (0,1), 5: (1, 1), 6: (2, 1), 7: (0,0), 8: (1, 0), 9: (2, 0)}
    rule_phone_invert_p1 = {val: key for key, val in rule_phone_p1.items()}
    rule_phone_p2 = {1: (2, 4), 2: (1, 3), 3: (2, 3), 4: (3, 3), 5:(0, 2), 6: (1, 2), 7: (2, 2),
                     8: (3, 2), 9: (4, 2), "A": (1, 1), "B": (2, 1), "C": (3, 1), "D": (2, 0)}
    rule_phone_invert_p2 = {val: key for key, val in rule_phone_p2.items()}
    rule_phone, rule_phone_invert = (rule_phone_p1, rule_phone_invert_p1) if \
        (part == 1) else (rule_phone_p2, rule_phone_invert_p2)
    start_num, num_out = 5, ""
    for rule in list_rule:
        for str_rule in rule:
            start_place = rule_phone[start_num]
            move = rule_move[str_rule]
            new_place = (start_place[0]+move[0], start_place[1] + move[1])
            if new_num := rule_phone_invert.get(new_place):
                start_num = new_num
            else:
                continue
        num_out += str(start_num)
    return num_out

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")







