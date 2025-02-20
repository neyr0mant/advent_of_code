import sys
sys.setrecursionlimit(20000)
list_data = [[int(j) for j in i.strip().split()] for i in open("input.txt")][0]
def get_solve(list_data, count_iter, all_configuration):
    str_list = "-".join([str(i) for i in list_data])
    if str_list in all_configuration:
        return count_iter, list_data
    all_configuration.add(str_list)
    max_num, len_list = max(list_data), len(list_data)
    index_max = list_data.index(max_num)
    count_circle, remainder = max_num // len_list, max_num % len_list
    l_list, r_list = list_data[:index_max], list_data[index_max+1:]
    new_list = r_list + l_list + [0]
    new_list = [i+count_circle for i in new_list]
    if remainder:
        new_list = [i + 1 if idx < remainder else i for idx, i in enumerate(new_list)]
    l_list_new, r_list_new, new_num = (new_list[len(r_list): len_list-1],
                                       new_list[:len(r_list)], new_list[-1])
    new_list = l_list_new + [new_num] + r_list_new
    count_iter += 1
    return get_solve(new_list, count_iter=count_iter, all_configuration=all_configuration)


solve_1, list_data_v2 = get_solve(list_data, 0, set())
solve_2 = get_solve(list_data_v2, 0, set())[0]
print(f"Решение части 1: {solve_1}")
print(f"Решение части 2: {solve_2}")