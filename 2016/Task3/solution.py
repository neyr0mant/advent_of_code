#https://adventofcode.com/2016/day/3
list_data = [[int(j) for j in i.strip().split()] for i in open("input.txt")]
def get_solve(list_triangle, part=1):
    count = 0
    if part == 2:
        list_convert = []
        len_all = len(list_triangle)
        for idx_data, data in enumerate(list_triangle):
            if idx_data + 3 > len_all:
                break
            if idx_data % 3 == 0:
                t1, t2 ,t3 = ([data[0], list_triangle[idx_data+1][0], list_triangle[idx_data+2][0]],
                              [data[1], list_triangle[idx_data+1][1], list_triangle[idx_data+2][1]],
                              [data[2], list_triangle[idx_data+1][2], list_triangle[idx_data+2][2]])
                list_convert.extend([t1, t2, t3])
        list_triangle = list_convert
    for triangle in list_triangle:
        a, b, c = triangle
        if all([a < b+c, b < a+c, c < a+b]):
            count += 1
    return count
print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")







