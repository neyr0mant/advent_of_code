list_data = [i.strip().split(":") for i in open('input.txt')]

list_dict_data = []
for i in list_data:
    rule = i[0].split()
    letter = rule[1]
    min_, max_ = rule[0].split("-")
    min_, max_ = int(min_), int(max_)
    list_dict_data.append({"min_": min_, "max_": max_, "letter": letter, "str_assert": i[1].split()[0]})


def get_solve(list_data, part=1):
    count_good = 0
    for pas_assert in list_data:
        rule = pas_assert[0].split()
        letter = rule[1]
        min_, max_ = rule[0].split("-")
        min_, max_ = int(min_), int(max_)
        str_assert = pas_assert[1].split()[0]
        if part == 1:
            count = str_assert.count(letter)
            if all([count >= min_, count <= max_]):
                count_good += 1
        else:
            assertion_list = [str_assert[min_-1] == letter, str_assert[max_-1] ==letter]
            if all(assertion_list):
                continue
            if any(assertion_list):
                count_good += 1
    return count_good


print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")








