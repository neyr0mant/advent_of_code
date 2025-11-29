from functions import alphabet, execution_time
import re
alphabet = alphabet['lower']
triple_letter_list_all = [letter+alphabet[idx+1] + alphabet[idx+2] for idx, letter in
                          enumerate(alphabet) if idx+2 < len(alphabet)]
dict_alphabet = {}
for idx, i in enumerate(alphabet):
    if idx+1 < len(alphabet):
        dict_alphabet.update({i: alphabet[idx+1]})
    else:
        dict_alphabet.update({i: alphabet[0]})

def assert_pass(pas):
    triple_letter_list = [letter+pas[idx+1] + pas[idx+2] for idx, letter in
                          enumerate(pas) if idx+2 < len(pas)]
    rule_1 = [i for i in triple_letter_list if i in triple_letter_list_all]
    rule_2 = not [i for i in ["i", "o", "l"] if i in pas]
    rule_3 = len(set(re.findall(r"(.)\1", pas))) >= 2
    return True if all([rule_1, rule_2,rule_3]) else False

def get_new_pass(pas, pas_add = ""):
    if not pas:
        return pas_add
    next_letter = dict_alphabet[pas[-1]]
    pas_add = next_letter if not pas_add else next_letter+pas_add
    if next_letter == "a":
        return get_new_pass(pas[:-1], pas_add=pas_add)
    else:
        return pas[:-1] + pas_add


@execution_time
def get_solve(password):
    while True:
        new_pass = get_new_pass(password)
        if not assert_pass(new_pass):
            password = new_pass
        else:
            return new_pass
res_1 = get_solve("hxbxwxba")
res_2 = get_solve(res_1)
print(f"Решение части 1: {res_1}")
print(f"Решение части 2: {res_2}")