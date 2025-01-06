
list_data = [int(i.strip()) for i in open('input.txt')]
def get_summ(list_num, part=1):
    for num_1 in list_num:
        num_2 = 2020 - num_1
        if part == 1:
            if num_2 in list_num:
                return num_1*num_2
        else:
            for num_2_ in list_num:
                num_3 = num_2 - num_2_
                if num_3 in list_num:
                    return num_2_*num_3*num_1

print(f"Решение части 1: {get_summ(list_data)}")
print(f"Решение части 1: {get_summ(list_data, part=2)}")


