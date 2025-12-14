list_data = [[int(j) for j in i.split(",")] for i in open("input.txt")]
from functions import *
@execution_time
def get_solve(list_data_, part =1):
    n = len(list_data_)
    list_distance = []
    for i in range(n):
        for j in range(i + 1, n):
            dx = list_data_[i][0] - list_data_[j][0]
            dy = list_data_[i][1] - list_data_[j][1]
            dz = list_data_[i][2] - list_data_[j][2]
            dist = dx * dx + dy * dy + dz * dz
            list_distance.append((dist, i, j))
    list_distance.sort()
    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, rank, size, a, b):
        pa = find(parent, a)
        pb = find(parent, b)
        if pa == pb:
            return False
        if rank[pa] < rank[pb]:
            parent[pa] = pb
            size[pb] += size[pa]
        elif rank[pa] > rank[pb]:
            parent[pb] = pa
            size[pa] += size[pb]
        else:
            parent[pb] = pa
            size[pa] += size[pb]
            rank[pa] += 1
        return True

    parent1, rank1, size1 = list(range(n)), [0] * n, [1] * n
    attempts = 10 if n == 20 else 1000

    for i in range(min(attempts, len(list_distance))):
        a, b = list_distance[i][1:3]
        union(parent1, rank1, size1, a, b)

    comp_sizes = sorted([size1[i] for i in range(n) if find(parent1, i) == i], reverse=True)
    result = comp_sizes[0] * comp_sizes[1] * comp_sizes[2]
    if part == 2:
        parent2, rank2, size2 = list(range(n)), [0] * n, [1] * n
        components = n
        last_a, last_b = -1, -1
        for k in range(len(list_distance)):
            a, b = list_distance[k][1:3]
            if union(parent2, rank2, size2, a, b):
                components -= 1
                if components == 1:
                    last_a, last_b = a, b
                    break
        x1 = list_data_[last_a][0]
        x2 = list_data_[last_b][0]
        result = x1 * x2
    return result

print(f"Решение части 1: {get_solve(list_data, part =1)}")
print(f"Решение части 2: {get_solve(list_data, part =2)}")
