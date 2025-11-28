data = [i.strip() for i in open("input.txt")][0]
def get_solve_p1(s: str) -> int:
    i = 0
    length = 0
    while i < len(s):
        if s[i] == '(':
            j = s.find(')', i)
            length_str, repeat_str = s[i + 1:j].split('x')
            length_to_take = int(length_str)
            repeat = int(repeat_str)
            i = j + 1 + length_to_take
            length += length_to_take * repeat
        else:
            length += 1
            i += 1
    return length


def get_solve_p2(s: str) -> int:
    def helper(start: int, end: int) -> int:
        total = 0
        i = start
        while i < end:
            if s[i] == '(':
                j = s.find(')', i)
                length_to_take, repeat = map(int, s[i + 1:j].split('x'))
                total += helper(j + 1, j + 1 + length_to_take) * repeat
                i = j + 1 + length_to_take
            else:
                total += 1
                i += 1
        return total

    return helper(0, len(s))

print(f"Решение части 1: {get_solve_p1(data)}")
print(f"Решение части 2: {get_solve_p2(data)}")