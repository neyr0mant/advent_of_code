data = {j[1]:j[0] for i in open("input.txt") if (j := i.strip("\n").replace(" ", "").split("->"))}


def get_data_wires(data_in, data_replace=None):
    const_byte = 2 ** 16
    operators = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]
    data_not_digit, data_digit = {}, {}
    if not data_replace:
        [data_digit.update({key: val}) if val.isdigit() else data_not_digit.update({key: val}) for key, val in
         data_in.items()]
        return data_not_digit, data_digit
    for key, val in data_in.items():
        if val.isdigit():
            data_digit.update({key: val})
            continue
        operator = [i for i in operators if i in val]
        if not operator:
            data_digit.update({key: digit}) if (digit := data_replace.get(val)) else data_not_digit.update({key: val})
            continue
        operator, split_operator = operator[0], []
        for digit in val.split(operator):
            if digit_ := data_replace.get(digit):
                split_operator.append(digit_)
            elif digit.isdigit():
                split_operator.append(digit)
        if split_operator:
            len_split = len(split_operator)
            if len_split == 2:
                a, b = split_operator
                if operator == "AND":
                    val = str(int(a) & int(b))
                elif operator == "OR":
                    val = str(int(a) | int(b))
                elif operator == "LSHIFT":
                    val = str(int(a) << int(b))
                elif operator == "RSHIFT":
                    val = str(int(a) >> int(b))
            elif len_split == 1:
                if operator == "NOT":
                    val = ~ int(split_operator[0])
                else:
                    data_not_digit.update({key: val})
                    continue
            val = val if int(val) >= 0 else str(const_byte - abs(int(val)))
            data_digit.update({key: val})
        else:
            data_not_digit.update({key: val})
    return data_not_digit, data_digit

def get_data_digit(data_in):
    data_not_digit, data_digit = get_data_wires(data_in)
    while data_not_digit:
        data_not_digit, data_digit_ = get_data_wires(data_not_digit, data_replace=data_digit)
        data_digit.update(data_digit_)
    return data_digit
res = get_data_digit(data)
print(f"Решение части 1: {res['a']}")
data["b"] = res["a"]
res = get_data_digit(data)
print(f"Решение части 2: {res['a']}")
