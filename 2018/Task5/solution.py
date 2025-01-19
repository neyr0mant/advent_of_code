data = [i.strip() for i in open("input.txt")][0]
from functions import execution_time, alphabet

def solve_p1(str_in):
    letter_out = []
    for letter in str_in:
        if letter_out:
            conditions = [letter.lower() == letter_out[-1].lower(),
                          ((letter.isupper() and letter_out[-1].islower())
                           or (letter.islower() and letter_out[-1].isupper()))]
            if all(conditions):
                letter_out = letter_out[:-1]
                continue
        letter_out += letter
    return len(letter_out)

@execution_time
def get_solve(str_in, part =1):
    if part ==1:
        solve = solve_p1(str_in)
    else:
        solve = min([solve_p1(str_in.replace(i, "").replace(i.upper(), "")) for i in alphabet["lower"]])
    return solve

print(f"Решение части 1: {get_solve(data)}")
print(f"Решение части 2: {get_solve(data, part=2)}")