#https://adventofcode.com/2024/day/1
list1, list2 = [], []
f = open('input.txt')
for line in f:
    a, b = line.split()
    list1.append(int(a))
    list2.append(int(b))
list1.sort(reverse=True)
list2.sort(reverse=True)
summ = 0
for idx, i in enumerate(list1):
    summ += abs(int(i)-list2[idx])
print(summ)
power = 0
for i in list1:
    power += i*list2.count(i)
print(power)
