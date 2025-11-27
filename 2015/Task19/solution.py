import re
dict_data = {"convert_data": {}}
for data in open("input.txt"):
    data = data.strip()
    if "=>" in data:
        data_split = data.split("=>")
        key, val = data_split[0][:-1], data_split[1][1:]
        cur_data = dict_data["convert_data"].get(key, [])
        cur_data.append(val)
        dict_data["convert_data"][key] = cur_data
    else:
        dict_data["data"] = data

def get_solve(part =1):
    data = dict_data["data"]
    if part == 1:
        set_data = set()
        for key, val in dict_data["convert_data"].items():
            indexes_replace = [m.start() for m in re.finditer(re.escape(key), data)]
            for key_replace in val:
                for index in indexes_replace:
                    new_data = data[:index] + key_replace + data[index+len(key):]
                    set_data.add(new_data)
        result = len(set_data)
    else:
        total_elements = len(re.findall(r'[A-Z]', data))
        result = total_elements - data.count('Rn') - data.count('Ar') - 2 * data.count('Y') - 1
    return result

print(f"Решение части 1: {get_solve()}")
print(f"Решение части 2: {get_solve(part=2)}")