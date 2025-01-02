data_str = [i for i in open("input.txt")][0]

def position_basement(str_in):
    basement = 0
    for idx, i in enumerate(str_in):
        basement = basement + 1 if i == "(" else basement - 1
        if basement < 0:
            return idx+1
print(f"Решение части 1: {data_str.count('(') - data_str.count(')')}")
print(f"Решение части 2: {position_basement(data_str)}")

