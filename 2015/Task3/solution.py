data_str = [i for i in open("input.txt")][0]
def get_count_house(track_list, part =1):
    houses = {"santa": [(0, 0)], "robot": [(0, 0)]}
    for idx, i in enumerate(track_list):
        key = "santa" if part == 1 else ("santa" if idx % 2 == 0 else "robot")
        last_house, last_list, new_house = houses[key][-1], houses[key], ()
        if i == "^":
            new_house = (last_house[0], last_house[1] + 1)
        elif i == "v":
            new_house = (last_house[0], last_house[1] - 1)
        elif i == ">":
            new_house = (last_house[0] + 1, last_house[1])
        elif i == "<":
            new_house = (last_house[0] - 1, last_house[1])
        houses[key] = last_list + [new_house]
    all_houses = houses["santa"] if part == 1 else houses["santa"] + houses["robot"]
    return len(set(all_houses))

print(f"Решение части 1: {get_count_house(data_str)}")
print(f"Решение части 2: {get_count_house(data_str, part=2)}")








