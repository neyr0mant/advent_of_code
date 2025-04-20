list_str = [i.strip() for i in open("input.txt")]
dict_data = {}
for i in list_str:
    list_data = i.split()
    name = list_data[0]
    speed_fly = int(list_data[3])
    fly_sec = int(list_data[6])
    rest_sec = int(list_data[13])
    dict_data.update({name: [speed_fly,fly_sec,rest_sec]})
def calculate_distance(name, count_sec):
    list_data = dict_data[name]
    count_circle = count_sec//(list_data[1] + list_data[2])
    remainder = count_sec - count_circle*(list_data[1] + list_data[2])
    remainder = remainder if remainder <= list_data[1] else list_data[1]
    return list_data[0]*(count_circle*(list_data[1]) + remainder)
def get_solve(part =1):
    if part == 1:
        return max([calculate_distance(i, 2503) for i in dict_data])
    else:
        point_dict = {i: 0 for i in dict_data}
        for time_ in range(1, 2504):
            dict_distance = {name: calculate_distance(name, time_) for name in dict_data}
            max_val = max(list(dict_distance.values()))
            winner = [i for i in dict_distance if dict_distance[i] == max_val][0]
            point_dict[winner] +=1
        return max(point_dict.values())



print(f"Решение части 1: {get_solve()}")
print(f"Решение части 1: {get_solve(part=2)}")