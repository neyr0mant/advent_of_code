from copy import deepcopy
list_data = [i.strip() for i in open('input.txt')]
def get_solve(list_data, part =1):
    res_1, res_2 = None, None
    if part == 1:
        sum_id_2, sum_id_3 = 0, 0
        for str_ in list_data:
            find_2, find_3 = False, False
            for idx, letter in enumerate(str_):
                if not find_2:
                    if str_.count(letter) == 2:
                        sum_id_2 += 1
                        find_2 = True
                if not find_3:
                    if str_.count(letter) == 3:
                        sum_id_3 += 1
                        find_3 = True
                if all([find_2, find_3]):
                    break
        res_1 = sum_id_2*sum_id_3
    else:
        idx_one_diff, box_one_dif = None, None
        for idx_box_1, box_1 in enumerate(list_data):
            for idx_box_2, box_2 in enumerate(list_data):
                if idx_box_1 == idx_box_2:
                    continue
                if box_one_dif:
                    break
                count_diff = 0
                for idx_letter_1, letter_1 in enumerate(box_1):
                    letter_2 = box_2[idx_letter_1]
                    if letter_1 != letter_2:
                        count_diff += 1
                        idx_one_diff = idx_letter_1
                    if count_diff > 1:
                        break
                if count_diff == 1:
                    box_one_dif = box_1
        res_2 = box_one_dif[:idx_one_diff] + box_one_dif[idx_one_diff+1:]
    return res_1 if part == 1 else res_2


print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")








