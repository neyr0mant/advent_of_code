#https://adventofcode.com/2024/day/3
list_data = [i for i in open("input.txt")]
data = "".join(list_data)
test_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def get_solve(s, part=1):
    total = 0
    enabled = True
    for part_str in s.split("mul"):
        if len(part_str) < 3:
            continue
        if part_str[0] == "(" and ")" in part_str:
            args = part_str[1: part_str.index(")")].split(",")
            if len(args) == 2 and args[0].isdigit() and args[1].isdigit():
                a, b = int(args[0]), int(args[1])
                if part == 1 or enabled:
                    total += a * b
        if part == 2:
            if "don't()" in part_str:
                enabled = False
            if "do()" in part_str:
                enabled = True

    return total
print(f"Решение части 1:{get_solve(data, part=1)}")
print(f"Решение части 2: {get_solve(data, part=2)}")










