list_data = [[int(j) for j in i.split(",")] for i in open("input.txt")][0]
def get_solve(count_day):
    data_dict = {i: list_data.count(i) for i in range(9)}
    for _ in range(count_day):
        new_dict = {i: 0 for i in range(9)}
        for i, k in data_dict.items():
            if i != 0:
                new_dict[i-1] += k
            else:
                new_dict[8] = k
                new_dict[6] += k
        data_dict = new_dict
    return sum(data_dict.values())

print(f"Решение части 1: {get_solve(80)}")
print(f"Решение части 2: {get_solve(256)} ")
