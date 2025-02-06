from functions import Matrix, execution_time
dict_data, table = {}, []
for i in open("input.txt"):
    i = i.strip()
    if "," in i:
        dict_data["list_num"] = [int(j) for j in i.split(",")]
        continue
    if i == "":
        cur_data = dict_data.get("list_table", [])
        if table:
            cur_data.append(Matrix(table))
            dict_data["list_table"] = cur_data
            table = []
    else:
        table.append([{int(j): 1} for j in i.split()])
def get_sum_table(table):
    summ = 0
    for i in table.matrix:
        for j in i:
            key, val = list(j.items())[0]
            if val == 1:
                summ += key
    return summ
@execution_time
def get_solve(dict_data):
    list_win = []
    for num in dict_data["list_num"]:
        list_win_idx = []
        for idx, table in enumerate(dict_data["list_table"]):
            rank = table.x_max
            find_coordinate = table.find({num: 1})
            if find_coordinate:
                x, y = find_coordinate[0]
                table[x, y] = {num: 2}
                horizontal = table.matrix[y]
                vertical = [j[x] for j in table.matrix]
                val_vertical = [list(i.values())[0] for i in vertical]
                val_horizontal = [list(i.values())[0] for i in horizontal]
                if val_vertical.count(2) == rank or val_horizontal.count(2) == rank:
                    summ = get_sum_table(table)
                    list_win_idx.append(idx)
                    list_win.append(num*summ)
        if list_win_idx:
            list_win_idx.sort(reverse=True)
            for win_idx in list_win_idx:
                del dict_data["list_table"][win_idx]
    return list_win

result = get_solve(dict_data)
print(f"Решение части 1: {result[0]}")
print(f"Решение части 2: {result[-1]}")