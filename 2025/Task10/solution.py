from pulp import *
list_data = []
for data in [i for i in open("input.txt")]: # парсим данные
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
    list_data.append([buttons, pattern, powers])

def min_presses_part1(A, target):
    n = len(A)
    m = len(A[0]) if n else 0
    # Создаём расширенную матрицу [A | target] для Гауссова исключения
    mat = [A[i][:] + [target[i]] for i in range(n)]
    col_to_row = [-1] * m
    rank = 0
    # Прямой ход Гаусса над GF(2) — приводим матрицу к ступенчатому виду
    for col in range(m):
        pivot = -1
        for r in range(rank, n):
            if mat[r][col] == 1:
                pivot = r
                break
        if pivot == -1: # Этот столбец нулевой — кнопка "свободная"
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank] # Меняем строки местами, чтобы 1 стояла на диагонали
        col_to_row[col] = rank
        for r in range(n): # Обнуляем все остальные элементы в этом столбце (XOR)
            if r != rank and mat[r][col] == 1:
                for c in range(col, m + 1):
                    mat[r][c] ^= mat[rank][c]
        rank += 1

    x0 = [0] * m # Находим одно частное решение (все свободные переменные = 0)
    for col in range(m - 1, -1, -1):
        if col_to_row[col] != -1:
            r = col_to_row[col]
            val = mat[r][m]  # правая часть уравнения
            for j in range(col + 1, m):
                if mat[r][j]:
                    val ^= x0[j] # вычитаем уже найденные переменные (по модулю 2)
            x0[col] = val

    free = [c for c in range(m) if col_to_row[c] == -1] # Находим все свободные переменные (те кнопки, которые не стали ведущими)
    kernel = [] # Строим базис ядра (все решения вида "частное + линейная комбинация ядра")
    for f in free:
        v = [0] * m
        v[f] = 1 # свободная переменная = 1
        for col in range(m - 1, -1, -1):
            if col_to_row[col] != -1:
                r = col_to_row[col]
                s = 0
                for j in range(col + 1, m):
                    if mat[r][j]:
                        s ^= v[j]
                v[col] = s # подставляем в уравнение
        kernel.append(v)

    best = float('inf')
    for mask in range(1 << len(kernel)): # Перебираем все возможные комбинации свободных переменных (2^|free| ≤ 4096)
        x = x0[:] # берём частное решение
        for i in range(len(kernel)):
            if mask & (1 << i):
                for j in range(m):
                    x[j] ^= kernel[i][j] # добавляем вектор из ядра
        best = min(best, sum(x)) # ищем решение с минимальным числом нажатий
    return best

def min_presses_part2(buttons, target):
    n = len(target) # количество счётчиков
    m = len(buttons) # количество кнопок
    prob = LpProblem("MinPresses", LpMinimize) # Создаём задачу линейного целочисленного программирования
    x = [LpVariable(f"x{j}", lowBound=0, cat='Integer') for j in range(m)] # x[j] — сколько раз нажимаем кнопку j (целое ≥ 0)
    prob += lpSum(x) # Целевая функция: минимизировать общее количество нажатий
    for i in range(n): # Ограничения: каждая кнопка увеличивает свои счётчики ровно на нужное количество
        prob += lpSum(x[j] for j in range(m) if i in buttons[j]) == target[i] # Сумма всех кнопок, которые влияют
        # на счётчик i, должна дать target[i]
    prob.solve(PULP_CBC_CMD(msg=0)) # Решаем задачу (используем встроенный CBC-солвер, без вывода логов)
    if prob.status != 1: # Если решение найдено — возвращаем сумму нажатий
        return -1  # на всякий случай
    return int(value(prob.objective))

def get_solve(list_data_, part=1):
    count_all = 0
    for data in list_data_:
        buttons, pattern, powers = data
        m = len(buttons)
        if part == 1:
            # Часть 1: нужно включить лампочки по шаблону
            target = [1 if c == '#' else 0 for c in pattern]
            A = [[0] * m for _ in range(len(pattern))]
            for col, btn in enumerate(buttons):
                for idx in btn:
                    if idx < len(pattern):
                        A[idx][col] = 1
            count_all += min_presses_part1(A, target)
        else:
            # Часть 2: нужно набрать точные значения на счётчиках
            count_all += min_presses_part2(buttons, powers)
    return count_all

print(f"Решение части 1: {get_solve(list_data, part =1)}")
print(f"Решение части 2: {get_solve(list_data, part =2)}")