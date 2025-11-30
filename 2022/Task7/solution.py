#Решения нет
list_data = [i.strip() for i in open("input.txt")]
def get_solve(list_data_, part=1):
    disc, cur_path = {}, []
    for line in list_data_:
        parts = line.split()
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    cur_path.pop()
                elif parts[2] == "/":
                    cur_path = []
                else:
                    cur_path.append(parts[2])
            continue
        if parts[0] == "dir":
            continue
        size = int(parts[0])
        for i in range(len(cur_path) + 1):
            path = "/" + "/".join(cur_path[:i])
            path = "/" if path == "/" else path + "/"
            disc[path] = disc.get(path, 0) + size
    return sum(s for s in disc.values() if s <= 100000) if part == 1 \
        else min([i for i in disc.values() if i>= disc["/"] - 40000000])

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, 2)}")