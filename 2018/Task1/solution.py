list_freq_str = [i.strip() for i in open('input.txt')]


from functions import execution_time
@execution_time
def get_solve(list_data, part = 1):
    if part == 1:
        return eval(''.join([i.strip() for i in open('input.txt')]))
    else:
        set_freq, last_freq,  double_freq = {0}, 0, 0
        list_rule = []
        for rule in list_data:
            operator = [i for i in ["+", "-"] if i in rule][0]
            rule_int = int(rule.split(operator)[1]) if operator == "+" else -int(rule.strip().split(operator)[1])
            list_rule.append(rule_int)
        while True:
            for rule in list_rule:
                new_freq = last_freq + rule
                if new_freq in set_freq:
                    double_freq = new_freq
                    break
                set_freq.add(new_freq)
                last_freq = new_freq
            if double_freq:
                break
        return double_freq


print(f"Решение части 1: {get_solve(list_freq_str)}")
print(f"Решение части 2: {get_solve(list_freq_str, part=2)}")
