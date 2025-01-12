#https://adventofcode.com/2016/day/3
list_data = [i.strip() for i in open("input.txt")]
List_dict_data = []
for data in list_data:
    data_split = data.split("[")
    data_room, control_summ = data_split[0], data_split[1][:-1]
    data_split_room = data_room.split("-")
    data_room_str, id_card = "".join(data_split_room[:-1]),  int(data_split_room[-1])
    List_dict_data.append({"data_room_str": data_room_str, "id_room": id_card, "control_summ": control_summ,
                           "data_card_list": data_split_room[:-1]})

def get_solve(List_dict_data):
    summ_id = 0
    for room in List_dict_data:
        data_room_str = room["data_room_str"]
        control_summ = room["control_summ"]
        assert_dict = sorted({i: data_room_str.count(i) for i in data_room_str}.items(),
                             key=lambda x: (-x[1], x[0]))
        assert_summ = "".join([i[0] for i in assert_dict[:5]])
        if assert_summ == control_summ:
            summ_id += room["id_room"]
    return summ_id

print(f"Решение части 1: {get_solve(List_dict_data)}")
# print(f"Решение части 2: {get_solve(list_data, part=2)}")







