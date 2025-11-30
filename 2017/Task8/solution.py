list_data = [i.strip().split() for i in open("input.txt")]
def get_solve(list_data_, part =1):
    dict_data, max_ = {}, 0
    for i in list_data_:
        arg1, arg2 = i[0], i[4]
        if arg1 not in globals():
            globals()[arg1], dict_data[arg1] = 0, 0
        if arg2 not in globals():
            globals()[arg2], dict_data[arg2] = 0, 0
        new_arg1 = eval(" ".join(i).replace("inc", "+").replace("dec", "-") + f" else {arg1}")
        globals()[arg1], dict_data[arg1] = new_arg1, new_arg1
        max_ = new_arg1 if new_arg1 > max_ else max_
    for i in dict_data:
        globals()[i] = 0
    return max(dict_data.values()) if part == 1 else max_

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 1: {get_solve(list_data, part=2)}")


""" f1 + f2 * f3 """


