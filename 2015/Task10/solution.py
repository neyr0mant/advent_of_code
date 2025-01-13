from functions import execution_time
def split_number_string(number_string):
    result = []
    current_number = ""
    for char in number_string:
        current_number += char
        if len(current_number) > 1 and (len(current_number) == 1 or char != current_number[-2]):
            if current_number:
                result.append(current_number[:-1])
            current_number = char
    if current_number:
        result.append(current_number)
    return result
@execution_time
def get_solve(num_start, count_iter_need=0):
    solve, count_iter = 0, 0
    while count_iter != count_iter_need:
        new_str = ""
        groups = split_number_string(num_start)
        for group in groups:
            num_group = group.count(group[0])
            new_str += f"{num_group}{group[0]}"
        num_start = new_str
        count_iter += 1
    return len(num_start)


print(f"Решение части 1: {get_solve('3113322113', 40)}")
print(f"Решение части 2: {get_solve('3113322113', 50)}")