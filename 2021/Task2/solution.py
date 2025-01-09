list_data = [i.strip().split() for i in open('input.txt')]


def get_solve(list_data, part=1):
    start, aim = (0, 0), 0
    for rule_count in list_data:
        rule, count = rule_count
        count = int(count)
        if part == 1:
            if rule == "forward":
                start = (start[0] + count, start[1])
            elif rule == "down":
                start = (start[0], start[1] + count)
            else:
                start = (start[0], start[1] - count)
        else:
            if rule == "forward":
                start = (start[0] + count, start[1] + count*aim)
            elif rule == "down":
                aim += count
            else:
                aim -= count
    return abs(start[0]) * abs(start[1])


print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")








