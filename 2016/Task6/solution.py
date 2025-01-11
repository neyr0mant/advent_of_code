list_str = [i.strip() for i in open("input.txt")]

def get_solve(list_str, part =1):
    len_list_str = len(list_str[0])
    list_data = []
    for idx in range(len_list_str):
        list_data.append([j[idx] for j in list_str])
    list_out = [sorted(i, key=lambda x: i.count(x))[::-1] if part == 1 else sorted(i, key=lambda x: i.count(x))
                    for i in list_data]
    return "".join([i[0] for i in list_out])

print(f"Решение части 1: {get_solve(list_str)}")
print(f"Решение части 2: {get_solve(list_str, part=2)}")
