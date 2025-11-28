#Решения нет
list_data = [i.strip() for i in open("input.txt")]
dict_data = {}
for i in list_data:
    key, val = i.split(")")
    cur_data = dict_data.get(key, [])
    dict_data[key] = cur_data + [val]


def get_solve(data_, part =1):
    if part == 1:
        data_orb = {i: 0 for i in data_}
        key_start_list = ["COM"]
        set_orb = set(key_start_list)
        while set_orb != set(data_.keys()):
            new_key_start_list = []
            for key_start in key_start_list:
                if new_orb_list := data_.get(key_start):
                    new_key_start_list.extend(new_orb_list)
                    for new_orb in new_orb_list:
                        data_orb[new_orb] = data_orb[key_start] + 1
                    set_orb.add(key_start)
            key_start_list = new_key_start_list
        result = sum(data_orb.values())
    else:
        start_list, finish, count, find, all_set = ["YOU"], "SAN", -3, False, set()
        while not find:
            count += 1
            new_list = []
            all_set.update(start_list)
            for key_start in start_list:
                if res_1 := data_.get(key_start):
                    res_1 = [i for i in res_1 if i not in all_set]
                    new_list.extend(res_1)
                if res_2 := [key for key, val in data_.items() if key_start in val]:
                    res_2 = [i for i in res_2 if i not in all_set]
                    new_list.extend(res_2)
                if key_start == finish:
                    find = True
                    break
            start_list = new_list
        result = count
    return result


print(f"Решение части 1: {get_solve(dict_data)}")
print(f"Решение части 1: {get_solve(dict_data, part=2)}")