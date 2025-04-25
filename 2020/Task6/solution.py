def get_solve(part=1):
    str_all_answer, group = "", 0
    count_all_answer = 0
    for i in open("input.txt"):
        answer = i.strip()
        if answer:
            str_all_answer += answer
            group += 1
        else:
            if part == 1 or group == 1:
                count_all_answer += len(set([i for i in str_all_answer]))
            else:
                count_all_answer += len(set([i for i in str_all_answer if str_all_answer.count(i) == group]))
            str_all_answer, group = "", 0
    if  part == 1 or group == 1:
        count_all_answer += len(set([i for i in str_all_answer]))
    else:
        count_all_answer += len(set([i for i in str_all_answer if str_all_answer.count(i) == group]))
    return count_all_answer

print(f"Решение части 1: {get_solve()}")
print(f"Решение части 2: {get_solve(part=2)}")
