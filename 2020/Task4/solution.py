list_data = [i.strip() for i in open("input.txt")]

dict_data = {}
key = 1
for data in list_data:
    if not data:
        key += 1
    else:
        for i in data.split():
            i_split = i.split(":")
            pole, value = i_split[0], i_split[1]
            if dict_data.get(key):
                dict_data[key].update({pole: value})
            else:
                dict_data[key] = {pole: value}

def asser_data_pass(data_pass):
    min_max_rule = {"byr":(1920, 2002),"iyr":(2010, 2020), "eyr": (2020, 2030), "cm": (150, 193), "in":(59, 76)}
    for key, val in data_pass.items():
        if key in ["byr", "iyr", "eyr"]:
            min_, max_ = min_max_rule[key]
            if not val.isdigit() or len(val) != 4:
                return 0
            if int(val) > max_ or int(val) < min_:
                return 0
        elif key in ["hgt","hcl"]:
            letter, digit = (val[-2:], val[:-2]) if key == "hgt" else (val[0], val[1:])
            condition_hgt = [letter in ["cm","in"], digit.isdigit()]
            condition_hcl = [letter == "#", all([i in "abcdef0123456789" for i in digit]),
                             len(digit) == 6]
            condition_assert = condition_hgt if key == "hgt" else condition_hcl
            if not all(condition_assert):
                return 0
            if key == "hgt":
                min_, max_ = min_max_rule[letter]
                if not min_ <= int(digit) <= max_:
                    return 0
        elif key == "ecl":
            if val not in ['amb', 'blu','brn','gry','grn','hzl','oth']:
                return 0
        elif key == "pid":
            if not val.isdigit() or len(val) != 9:
                return 0
    return 1

def get_solve(dict_data, part=1):
    count = 0
    key_st = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
    for kye, val in dict_data.items():
        list_key_pass = list(val.keys())
        if len(list_key_pass) == len(key_st):
            count += 1 if part == 1 else asser_data_pass(val)
        else:
            if len(list_key_pass) + 1 != len(key_st):
                continue
            else:
                if "cid" in list_key_pass:
                    continue
                else:
                    count += 1 if part == 1 else asser_data_pass(val)
    return count


print(f"Решение части 1: {get_solve(dict_data)}")
print(f"Решение части 2: {get_solve(dict_data, part=2)}")