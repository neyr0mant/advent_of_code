data_task = [int(i.strip()) for i in open("input.txt")]
def get_solve(list_measure, part=1):
    count_increased, summ_old = 0, 0
    if part == 1:
        for idx, measure in enumerate(list_measure[1:]):
            old_measure = list_measure[idx]
            if old_measure < measure:
                count_increased += 1
        return count_increased
    else:
        for idx, measure in enumerate(list_measure[2:]):
            old_measure_1, old_measure_2 = list_measure[idx], list_measure[idx+1]
            summ_new = measure + old_measure_1 + old_measure_2
            if summ_new > summ_old:
                count_increased += 1
            summ_old = summ_new
        return count_increased - 1

print(f"Решение части 1: {get_solve(data_task)}")
print(f"Решение части 2: {get_solve(data_task, part=2)}")

