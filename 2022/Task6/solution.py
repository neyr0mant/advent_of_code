data = [i.strip() for i in open("input.txt")][0]


def get_solve(str_data, len_marker=4):
    for idx, letter in enumerate(str_data):
        if idx <= len(str_data) - len_marker-1:
            if len(set([j for j in str_data[idx:idx+len_marker]])) == len_marker:
                return idx+len_marker

print(f"Решение части 1: {get_solve(data)}")
print(f"Решение части 2: {get_solve(data, len_marker=14)}")