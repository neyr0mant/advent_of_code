#https://adventofcode.com/2024/day/1
list_str = [i.strip("\n ").split() for i in open("input.txt")]
list1, list2 = [int(i[0]) for i in list_str], [int(i[1]) for i in list_str]
[i.sort(reverse=True) for i in [list1, list2]]
print(f"Решение части 1 {sum([abs(i-list2[idx]) for idx, i in enumerate(list1)])}")
print(f"Решение части 2 {sum([i*list2.count(i) for i in list1])}")
