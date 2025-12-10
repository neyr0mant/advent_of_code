from pulp import *
list_data = [i for i in open("input.txt")]

def min_presses_part1(A, target):
    n = len(A)
    m = len(A[0]) if n else 0
    mat = [A[i][:] + [target[i]] for i in range(n)]
    col_to_row = [-1] * m
    rank = 0
    for col in range(m):
        pivot = -1
        for r in range(rank, n):
            if mat[r][col] == 1:
                pivot = r
                break
        if pivot == -1:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        col_to_row[col] = rank
        for r in range(n):
            if r != rank and mat[r][col] == 1:
                for c in range(col, m + 1):
                    mat[r][c] ^= mat[rank][c]
        rank += 1

    x0 = [0] * m
    for col in range(m - 1, -1, -1):
        if col_to_row[col] != -1:
            r = col_to_row[col]
            val = mat[r][m]
            for j in range(col + 1, m):
                if mat[r][j]:
                    val ^= x0[j]
            x0[col] = val

    free = [c for c in range(m) if col_to_row[c] == -1]
    kernel = []
    for f in free:
        v = [0] * m
        v[f] = 1
        for col in range(m - 1, -1, -1):
            if col_to_row[col] != -1:
                r = col_to_row[col]
                s = 0
                for j in range(col + 1, m):
                    if mat[r][j]:
                        s ^= v[j]
                v[col] = s
        kernel.append(v)

    best = float('inf')
    for mask in range(1 << len(kernel)):
        x = x0[:]
        for i in range(len(kernel)):
            if mask & (1 << i):
                for j in range(m):
                    x[j] ^= kernel[i][j]
        best = min(best, sum(x))
    return best

def min_presses_part2(buttons, target):
    n = len(target)
    m = len(buttons)
    prob = LpProblem("MinPresses", LpMinimize)
    x = [LpVariable(f"x{j}", lowBound=0, cat='Integer') for j in range(m)]
    prob += lpSum(x)
    for i in range(n):
        prob += lpSum(x[j] for j in range(m) if i in buttons[j]) == target[i]
    prob.solve(PULP_CBC_CMD(msg=0))
    if prob.status != 1:
        return -1  # no solution
    return int(value(prob.objective))

def get_solve(list_data_, part=1):
    count_all = 0
    for data in list_data_:
        l = data.find('[')
        r = data.find(']', l)
        pattern = data[l + 1:r]
        buttons = []
        pos = r
        while True:
            l = data.find('(', pos)
            if l == -1:
                break
            r = data.find(')', l)
            nums = [int(x) for x in data[l + 1:r].split(',') if x.isdigit()]
            if nums:
                buttons.append(nums)
            pos = r + 1
        l = data.find('{')
        r = data.find('}', l)
        powers = [int(x) for x in data[l + 1:r].split(',') if x.isdigit()]
        m = len(buttons)
        if part == 1:
            target = [1 if c == '#' else 0 for c in pattern]
            A = [[0] * m for _ in range(len(pattern))]
            for col, btn in enumerate(buttons):
                for idx in btn:
                    if idx < len(pattern):
                        A[idx][col] = 1
            count_all += min_presses_part1(A, target)
        else:
            count_all += min_presses_part2(buttons, powers)
    return count_all

print(f"Решение части 1: {get_solve(list_data, part =1)}")
print(f"Решение части 2: {get_solve(list_data, part =2)}")