list_str = [i.strip() for i in open("input.txt")]

test_list_1 = ["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]
test_list_2 = ["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy"]

def get_good_str(str_in, part=1):
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    list_consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's',
                       't', 'v', 'w', 'x', 'y', 'z']
    all_list_letter = list_vowels + list_consonants
    double_list_letter, bad_list_str = [2 * i for i in all_list_letter], ["ab", "cd", "pq", "xy"]
    if part == 1:
        list_condition = [not [i for i in bad_list_str if str_in.count(i) != 0],
                          sum([str_in.count(j) for j in list_vowels]) >= 3,
                          [k for k in double_list_letter if str_in.count(k) != 0]]
    else:
        import itertools
        list_permutations = itertools.permutations(all_list_letter, r=2)
        double_list_letter, str_assert = [f"{i[0]}{i[1]}" for i in list_permutations] + double_list_letter, str_in[:-2]
        list_condition = [[i for i in double_list_letter if str_in.count(i) >= 2],
                          [i for idx, i in enumerate(str_assert) if str_in[idx+2] == i]]
    if all(list_condition):
        return True
    return False


print(f"Решение части 1: {len([i for i in list_str if get_good_str(i)])}")
print(f"Решение части 2: {len([i for i in list_str if get_good_str(i, part=2)])}")