#https://adventofcode.com/2024/day/5
from functions import execution_time
RULE_ST = {}
RULE_UPDATE = []
for i in open("input.txt"):
    x = i.strip("\n")
    if "|" in x:
        a, b = x.split("|")
        a, b = int(a), int(b)
        if res := RULE_ST.get(a, 0):
            res.append(b)
            RULE_ST[a] = res
        else:
            RULE_ST[a] = [b]
    if "," in x:
        list_str_rule = x.split(",")
        RULE_UPDATE.append([int(i) for i in list_str_rule])

def assert_rule(rule_list):
    len_list_rule = len(rule_list)
    for idx, key in enumerate(rule_list):
        if idx + 1 == len_list_rule:
            return True
        else:
            result = RULE_ST.get(key)
            if not result:
                return False
            else:
                next_key = rule_list[idx+1]
                if next_key not in result:
                    return False

def get_good_list(rule_list):
    dict_rule = {i: [j for j in RULE_ST.get(i, [0]) if j in rule_list] for i in rule_list}
    rule_list.sort(key=lambda key: len(dict_rule[key]), reverse=True)
    return rule_list

@execution_time
def get_summ(part=1):
    if part == 1:
        return sum([rule[int(len(rule)/2)] for rule in RULE_UPDATE if assert_rule(rule)])
    else:
        summ = 0
        for rule in RULE_UPDATE:
            res_assert = assert_rule(rule)
            if res_assert:
                continue
            else:
                good_list = get_good_list(rule)
                summ += rule[int(len(good_list)/2)]
    return summ
print(f"Решение части 1: {get_summ(part=1)}")
print(f"Решение части 2: {get_summ(part=2)}")










