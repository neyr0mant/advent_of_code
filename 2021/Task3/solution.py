#https://adventofcode.com/2021/day/3
list_data = [i.strip() for i in open("input.txt")]

start_num = 347991
def get_solve(list_data_, part=1):
    if part == 1:
        v_gamma, v_epsilon = "", ""
        for i in range(len(list_data_[0])):
            list_bit = [j[i] for j in list_data_]
            count_0, count_1 = list_bit.count("0"), list_bit.count("1")
            if count_0 > count_1:
                v_gamma += "0"
                v_epsilon += "1"
            else:
                v_gamma += "1"
                v_epsilon += "0"
        solve = int(v_gamma, 2)*int(v_epsilon,2)
    else:
        id_oxi = get_id_oxi_c02(list_data_)
        id_co2 = get_id_oxi_c02(list_data_, oxi= False)
        solve = id_co2*id_oxi
    return solve


def get_id_oxi_c02(list_num, oxi=True, position= 0):
    if len(list_num) == 1:
        return int(list_num[0], 2)
    list_position = [i[position] for i in list_num]
    count_0, count_1 = list_position.count("0"), list_position.count("1")
    if oxi:
        assert_num = "1" if count_1 >= count_0 else "0"
    else:
        assert_num = "0" if count_0 <= count_1 else "1"
    list_num_new = [i for i in list_num if i[position] == assert_num]
    position += 1
    return get_id_oxi_c02(list_num_new, oxi=oxi,position=position)


print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")







