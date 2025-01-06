dict_data, count_elf = {}, 0
for str_ in open("input.txt"):
    str_ = str_.strip()
    if str_.isdigit():
        dict_data[count_elf] = dict_data.get(count_elf, 0) + int(str_)
    else:
        count_elf += 1
print(f"Решение части 1: {max(list(dict_data.values()))}")
list_values = [i for i in dict_data.values()]
list_values.sort(reverse=True)
print(f"Решение части 2: {list_values[0] + list_values[1] + list_values[2]}")


