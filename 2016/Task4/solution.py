#https://adventofcode.com/2016/day/3
list_data = [i.strip() for i in open("input.txt")]
List_dict_data = []
for data in list_data:
    data_split = data.split("[")
    data_card, control_summ = data_split[0], data_split[1][:-1]
    data_split_card = data_card.split("-")
    data_card, id_card = "".join(data_split_card[:-1]),  int(data_split_card[-1])
    List_dict_data.append({"data_card": data_card, "id_card": id_card, "control_summ": control_summ})

def get_solve(List_dict_data):
    summ_id = 0
    for card in List_dict_data:
        data_card = card["data_card"]
        dict_count = {i: data_card.count(i) for i in data_card}
        control_summ = card["control_summ"]
        list_assert_digit = [key for key, val in dict_count.items() if val != 1]
        list_assert_digit.sort(key=lambda x: dict_count[x], reverse=True)
        list_assert_altha = sorted([key for key, val in dict_count.items() if val == 1])
        assert_str = "".join(list_assert_digit)
        if len(assert_str) >= 5:
            if assert_str[:5] == control_summ:
                summ_id += card["id_card"]
            continue
        assert_str = assert_str + "".join(list_assert_altha[:5-len(assert_str)])
        if assert_str == control_summ:
            summ_id += card["id_card"]
    return summ_id

print(f"Решение части 1: {get_solve(List_dict_data)}")
# print(f"Решение части 2: {get_solve(list_data, part=2)}")







