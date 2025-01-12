list_str = [i.strip() for i in open("input.txt", 'r')]
import re

def get_solve(list_str, part =1):
    all_count = sum(len(str_) for str_ in list_str)
    hex_count = sum(len(str_[1:-1].encode().decode('unicode-escape')) for str_ in list_str)
    repr_count = sum(len(re.sub('"', r'\"', repr(str_))) for str_ in list_str)
    return all_count - hex_count if part == 1 else repr_count - all_count

print(f"Решение части 1: {get_solve(list_str)}")
print(f"Решение части 2: {get_solve(list_str, part=2)}")