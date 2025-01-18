list_data = [[j for j in i.strip().split(",")] for i in open("input.txt")]
list_data = [[[int(k) for k in j.split("-")] for j in i] for i in list_data]

def get_solve(list_data, part=1):
    count_double = 0
    for i in list_data:
        condition_1 = i[0][0] <= i[1][0] and i[0][1] >= i[1][1]
        condition_2 = i[1][0] <= i[0][0] and i[1][1] >= i[0][1]
        list_condition = [condition_1, condition_2]
        if part == 2:
            condition_1 = i[0][1] >= i[1][0] >= i[0][0]
            condition_2 = i[0][1] >= i[1][1] >= i[0][0]
            condition_3 = i[1][1] >= i[0][0] >= i[1][0]
            condition_4 = i[1][1] >= i[0][1] >= i[1][0]
            list_condition = [condition_1,condition_2, condition_3,condition_4]
        if any(list_condition):
            count_double += 1
    return count_double

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")
