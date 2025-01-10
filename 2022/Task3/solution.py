#https://adventofcode.com/2016/day/3
list_data = [i.strip() for i in open("input.txt")]

start_num = 347991
def get_solve(list_data_, part=1):
    dict_weight = {i: idx for idx, i in enumerate("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", start=1)}
    if part == 1:
        all_summ = 0
        for bag in list_data_:
            len_bag = int(len(bag)/2)
            dep1, dep2 = bag[:len_bag], bag[len_bag:]
            for letter in dep1:
                if letter in dep2:
                    all_summ += dict_weight[letter]
                    break
    else:
        all_summ = 0
        list_group = [list_data_[i * 3: i * 3 + 3] for i in range(len(list_data_) // 3)]
        for group in list_group:
            bag1, bag2, bag3 = group
            for letter in bag1:
                if all([letter in bag2, letter in bag3]):
                    all_summ += dict_weight[letter]
                    break
    return all_summ
print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 1: {get_solve(list_data, part=2)}")







