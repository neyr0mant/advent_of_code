list_data = [i.strip() for i in open("input.txt")][0].split(",")
list_data = [int(i) for i in list_data]
from functions import execution_time
@execution_time
def get_solve(list_data_, part=1):
    min_summ = float('inf')
    for i in range(max(list_data_)):
        summ = sum([abs(int(j)-int(i)) for j in list_data_]) if part ==1 else \
            sum([int(abs(int(j)-int(i))*(abs(int(j)-int(i))+1)/2) for j in list_data_])
        if summ < min_summ:
            min_summ = summ
    return int(min_summ)

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data,part=2)}")