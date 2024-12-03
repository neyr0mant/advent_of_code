#https://adventofcode.com/2024/day/3
list_data = [i for i in open("input.txt")]
data = "".join(list_data)
test_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

def get_multiplication(str_in, part=1):
    list_data = str_in.split("mul")
    summ = 0
    dont = False
    for i in list_data:
        list_i =[i.split(")") for i in i.split("(")]
        if len(list_i) < 2:
            continue
        if part ==2:
            if dont:
                if "do()" in i:
                    dont = False
                continue
        if list_i[0] == [""]:
            a_b_list = [int(i) for i in list_i[1][0].split(",") if i.isdigit()]
            if len(a_b_list) == 2:
                summ += a_b_list[0]*a_b_list[1]
        if part == 2:
            if "don't()" in i:
                dont = True
            if dont:
                if "do()" in i:
                    dont = False
    return summ
print(f"Решение части 1:{get_multiplication(data, part=1)}")
print(f"Решение части 1: {get_multiplication(data, part=2)}")










