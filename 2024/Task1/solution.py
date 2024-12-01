#https://adventofcode.com/2024/day/1
list1, list2 = [], []
f = open('input.txt')
for line in f:
    a, b = line.split()
    list1.append(int(a))
    list2.append(int(b))
list1.sort(reverse=True)
list2.sort(reverse=True)
summ = sum([abs(i-list2[idx]) for idx, i in enumerate(list1)])
print(f"Решение части 1 {summ}")
power = sum([i*list2.count(i) for i in list1])
print(f"Решение части 2 {power}")
