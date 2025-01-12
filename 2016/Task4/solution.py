#https://adventofcode.com/2016/day/3
list_data = [i.strip() for i in open("input.txt")]
List_dict_data = []
for idx, data in enumerate(list_data, start=1):
    data_split = data.split("[")
    data_card, control_summ = data_split[0], data_split[1][:-1]
    data_split_card = data_card.split("-")
    list_word, id_card = data_card.split("-")[:-1], int(data_split_card[-1])
    List_dict_data.append({"card": list_word, "id_card": id_card, "control_summ": control_summ})

def get_solve(List_dict_data):
    summ_id = 0
    for card in List_dict_data:
        print()




list_ = ["c", "b", "a"]
list_.sort()
print(list_)
print(f"Решение части 1: {get_solve(List_dict_data)}")
# print(f"Решение части 2: {get_solve(list_data, part=2)}")







