#https://adventofcode.com/2016/day/3
list_data = [i.strip() for i in open("input.txt")]
List_dict_data = []
for data in list_data:
    data_split = data.split("[")
    data_room, control_summ = data_split[0], data_split[1][:-1]
    data_split_room = data_room.split("-")
    data_room_str, id_card = "".join(data_split_room[:-1]),  int(data_split_room[-1])
    List_dict_data.append({"data_room_str": data_room_str, "id_room": id_card, "control_summ": control_summ,
                           "data_room_list": data_split_room[:-1]})



def convert_str(str_in, count_step):
    altha = "abcdefghijklmnopqrstuvwxyz"
    str_out, remainder = "", count_step % len(altha)
    for i in str_in:
        new_index = altha.index(i) + remainder
        if new_index > len(altha) - 1:
            new_index -= len(altha)
        str_out += altha[new_index]
    return str_out


def get_solve(List_dict_data, part=1):
    solve = 0
    for room in List_dict_data:
        if part == 1:
            data_room_str, control_summ = room["data_room_str"], room["control_summ"]
            assert_dict = sorted({i: data_room_str.count(i) for i in data_room_str}.items(),
                                 key=lambda x: (-x[1], x[0]))
            assert_summ = "".join([i[0] for i in assert_dict[:5]])
            if assert_summ == control_summ:
                solve += room["id_room"]
        else:
            rule_list = ["northpole", "object", "storage"]
            data_room_list = room['data_room_list']
            if len(data_room_list) != len(rule_list):
                continue
            for idx, rule in enumerate(rule_list):
                if len(rule) != len(data_room_list[idx]):
                    continue
            list_convert = [convert_str(i, room["id_room"]) for i in room["data_room_list"]]
            if list_convert == rule_list:
                solve = room["id_room"]
    return solve
print(f"Решение части 1: {get_solve(List_dict_data)}")
print(f"Решение части 2: {get_solve(List_dict_data, part=2)}")







