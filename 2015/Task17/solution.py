import itertools
list_data = [int(i.strip()) for i in open("input.txt")]
def get_solve(part = 1):
    res = 0
    for i in range(1, len(list_data)+1):
        data = [i for i in list(itertools.combinations(list_data, i)) if sum(i) == 150]
        res += len(data)
        if part != 1 and data:
            return len(data)
    return res

print(f"Решение части 1: {get_solve()}")
print(f"Решение части 2: {get_solve(part=2)}")
