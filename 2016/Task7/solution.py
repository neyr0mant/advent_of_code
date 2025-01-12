import re
list_data = [i.strip() for i in open("input.txt")]


def assert_tsl(str_in):
    pattern = r'([\w])([\w])\2\1'
    tsl_list = [f"{ip[0]}{ip[1]}{ip[1]}{ip[0]}" for ip in re.findall(pattern, str_in) if ip[0] != ip[1]]
    if not tsl_list:
        return 0
    support_tsl = True
    for tsl in tsl_list:
        for tls_ in str_in.split(tsl):
            if tls_.count("[") != tls_.count("]"):
                support_tsl = False
                break
    return 1 if support_tsl else 0

def assert_ssl(str_in):
    pattern = r'([\w])([\w])\1'
    list_split = re.split(r'\[|\]', str_in)
    list_out, list_ins = list_split[::2], list_split[1::2]
    str_out, str_ins = "".join([i for i in list_out]), "".join([i for i in list_ins])
    set_out_aba, set_out_bab = set(), set()
    [[set_out_aba.add(f"{j[0]}{j[1]}{j[0]}") for j in re.findall(pattern, i)] for i in list_out]
    [[set_out_bab.add(f"{j[0]}{j[1]}{j[0]}") for j in re.findall(pattern, i)] for i in list_ins]
    for i in set_out_aba:
        bab = f"{i[1]}{i[0]}{i[1]}"
        if bab in str_ins:
            return 1
    for i in set_out_bab:
        aba = f"{i[1]}{i[0]}{i[1]}"
        if aba in str_out:
            return 1
    return 0


def get_solve(data_in, part=1):
    return sum([assert_tsl(i) for i in data_in] if part == 1 else [assert_ssl(i) for i in data_in])
print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")

