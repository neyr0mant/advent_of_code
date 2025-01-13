list_data = [i.strip().split() for i in open("input.txt")]
import itertools
def get_solve(list_data, part=1):
    count = 0
    for password_list in list_data:
        bad_pass = False
        for idx, word in enumerate(password_list):
            if part == 1:
                if password_list.count(word) > 1:
                    bad_pass = True
                    break
            else:
                list_anagram = list(itertools.permutations(word, len(word)))
                list_pass_anagram = ["".join(i) for i in list_anagram]
                if [i for i in password_list[:idx] + password_list[idx + 1:] if i in list_pass_anagram]:
                    bad_pass = True
                    break
        if not bad_pass:
            count += 1
    return count

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data, part=2)}")