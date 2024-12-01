#https://adventofcode.com/2024/day/1
list1, list2 = [], []
for line in open('input.txt'):
    a, b = line.split()
    list1.append(int(a))
    list2.append(int(b))
[i.sort(reverse=True) for i in [list1, list2]]
print(f"Решение части 1 {sum([abs(i-list2[idx]) for idx, i in enumerate(list1)])}")
print(f"Решение части 2 {sum([i*list2.count(i) for i in list1])}")
