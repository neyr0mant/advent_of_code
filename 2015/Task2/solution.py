list_data = [list(map(int, i.strip("\n").split("x"))) for i in open("input.txt")]

def get_sum_prise(size_list, part =1):
    if part ==1:
        square_list = [size_list[0]*size_list[1], size_list[1]*size_list[2], size_list[0]*size_list[2]]
        return 2*(sum(square_list)) + min(square_list)
    else:
        import math
        size_list.sort()
        return 2*(size_list[0] + size_list[1]) + math.prod(size_list)
print(f"Решение части 1: {sum([get_sum_prise(i) for i in list_data])}")
print(f"Решение части 2: {sum([get_sum_prise(i, part=2) for i in list_data])}")








