#Решения нет
list_data = [i.strip() for i in open("input.txt")][0]
def get_solve(data_, w = 25, h =6, part=1):
    index_l, mim_zero, list_layer, solve = 0, float("inf"), [], 0
    while index_l < len(data_):
        layer = []
        for i in range(h):
            s = data_[index_l:index_l + w]
            layer.append(s)
            index_l = index_l + w
        if part == 1:
            count_zero = sum([i.count("0") for i in layer])
            if count_zero < mim_zero:
                solve = sum([i.count("1") for i in layer])*sum([i.count("2") for i in layer])
                mim_zero = count_zero
        list_layer.append(layer)
    if part == 2:
        out_layer = []
        for idx_down, str_up in enumerate(list_layer[0]):
            out_str = ""
            list_str_down = [i[idx_down] for i in list_layer[1:]]
            for idx_pixel, pixel in enumerate(str_up):
                pixel_find = pixel
                if pixel == "2":
                    idx_layer = 0
                    while pixel_find == "2":
                        pixel_find = list_str_down[idx_layer][idx_pixel]
                        idx_layer += 1
                pixel_find = "#" if pixel_find == "1" else " "
                out_str += pixel_find
            out_layer.append(out_str)
        solve = "\n".join(out_layer)
    return solve

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2:\n{get_solve(list_data, part=2)}")