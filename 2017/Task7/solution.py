dict_data = {}
for data in open("input.txt"):
    data = data.strip().replace("(", "").replace(")", "").replace(",", "")
    list_data = data.split()
    if "->" in data:
        tower, num_tower, list_tower = list_data[0], int(list_data[1]), list_data[3:]
        dict_data.update({tower: [num_tower, list_tower]})
    else:
        tower, num_tower = list_data
        dict_data.update({tower: [int(num_tower)]})

def get_summ(dict_data, key_start):
    data_list = dict_data[key_start]
    summ_weight = data_list[0]
    if len(data_list) == 1:
        return summ_weight
    for key_ in data_list[1]:
        summ_weight += get_summ(dict_data, key_)
    return summ_weight

def get_good_weight(dict_data, list_key_start, good_weight):
    for key_start in list_key_start:
        data_key = dict_data[key_start]
        if len(data_key) < 2:
            return good_weight
        key_list = data_key[1]
        data_summ_all = {i: get_summ(dict_data, i) for i in key_list}
        bad_key_data = {key: val for key, val in data_summ_all.items() if list(data_summ_all.values()).count(val) == 1}
        if not bad_key_data:
            return good_weight
        bad_key, bad_summ = list(bad_key_data.keys())[0], list(bad_key_data.values())[0]
        good_summ = [summ for summ in data_summ_all.values() if summ != bad_summ][0]
        weight_bad_key, list_bad_keys_new = dict_data[bad_key][0], dict_data[bad_key][1]
        good_weight = good_summ - bad_summ + weight_bad_key
        return get_good_weight(dict_data, list_bad_keys_new, good_weight)

def get_solve(dict_data, part=1):
    list_val = [i[1] for i in dict_data.values() if len(i) > 1]
    list_val = [i for sublist in list_val for i in sublist]
    key_main = list(set(dict_data.keys()) - set(list_val))[0]
    if part == 1:
        return key_main
    else:
        return get_good_weight(dict_data, [key_main], 0)


print(f"Решение части 1: {get_solve(dict_data)}")
print(f"Решение части 1: {get_solve(dict_data, part=2)}")
