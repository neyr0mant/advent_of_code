def get_solve(data_in, part =1):
    list_range = [int(i) for i in data_in.split('-')]
    list_pass = []
    for password in range(list_range[0], list_range[1]+1):
        password = str(password)
        dict_count = {i: password.count(i) for i in "0123456789"}
        condition_1 = any([i >= 2 for i in dict_count.values()])
        sorted_password = "".join(sorted([i for i in password]))
        condition_2 = sorted_password == password
        if part == 1:
            list_conditions = [condition_1, condition_2]
        else:
            condition_3 = any([i == 2 for i in dict_count.values()])
            list_conditions = [condition_1, condition_2, condition_3]
        if all(list_conditions):
            list_pass.append(password)
    return len(list_pass)


print(f"Решение части 1: {get_solve('156218-652527')}")
print(f"Решение части 2: {get_solve('156218-652527', part=2)}")
