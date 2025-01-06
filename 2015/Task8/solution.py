list_str = [i.strip() for i in open("input.txt", 'r')]
import re

def get_solve(list_str, part =1):
    all_count, hex_count, repr_count = 0, 0, 0
    for str_ in list_str:
        all_count += len(str_)
        hex_count += len(str_[1:-1].encode().decode('unicode-escape'))
        repr_count += len(re.sub('"', r'\"', repr(str_)))
    return all_count - hex_count if part == 1 else repr_count - all_count

print(f"Решение части 1: {get_solve(list_str)}")
print(f"Решение части 2: {get_solve(list_str, part=2)}")