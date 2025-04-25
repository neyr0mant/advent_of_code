from functions import execution_time
list_str = [i.strip() for i in open("input.txt")]
dict_data = {}
for data in list_str:
    list_split = data.replace(".", "").split(" contain")
    contain, internal = list_split[0], list_split[1][1:]
    name_contain = " ".join(contain.split()[:-1])
    data_internal = {name_contain: {}}
    for internal_ in internal.split(","):
        if internal_ == "no other bags":
            break
        list_internal = [] if internal_ == "internal_" else internal_.split()
        name_internal = " ".join(list_internal[1:3])
        count_internal = int(list_internal[0])
        data_internal[name_contain].update({name_internal: count_internal})
    dict_data.update(data_internal)

def get_solve_p1(name_start):
    dict_name = {key:val for key, val in dict_data.items() if val.get(name_start)}
    dict_name_new = {}
    if not dict_name:
        return {}
    for name_start_ in dict_name:
        dict_name_new.update(get_solve_p1(name_start_))
    dict_name.update(dict_name_new)
    return dict_name

def get_solve_p2(name_start):
    dict_name = dict_data[name_start]
    count = sum(dict_name.values())
    if not dict_name:
        return count
    for name_start_, count_start in dict_name.items():
        count += count_start*get_solve_p2(name_start_)
    return count


print(f"Решение части 1: {len(get_solve_p1('shiny gold'))}")
print(f"Решение части 2: {get_solve_p2('shiny gold')}")