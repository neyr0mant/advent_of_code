data = [[int(j) for j in i.strip().split()] for i in open("input.txt")][0]
def get_solve(data, part=1):
    summ_meta = 0
    def parse(position):
        nonlocal summ_meta
        child_count, meta_count, position, child_list = data[position], data[position + 1], position+2, []
        for _ in range(child_count):
            val, position = parse(position)
            child_list.append(val)
        meta = data[position:position + meta_count]
        summ_meta += sum(meta)
        position += meta_count
        if child_count == 0:
            value = sum(meta)
        else:
            value = 0
            for i in meta:
                if 1 <= i <= len(child_list):
                    value += child_list[i - 1]
        return value, position
    root_value = parse(0)[0]
    return root_value if part == 2 else summ_meta

print(f"Решение части 1: {get_solve(data)}")
print(f"Решение части 2: {get_solve(data, part=2)}")