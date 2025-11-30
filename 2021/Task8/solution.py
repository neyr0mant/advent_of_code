list_data = [i.strip() for i in open("input.txt")]

def get_solve(list_data_, part =1):
    solve = 0
    for data in list_data_:
        left, right = data.split(" | ")
        patterns, out = left.split(), right.split()
        if part == 1:
            solve += sum([1 for i in out if len(i) in [2,3,4,7]])
        else:
            codes = ["".join(sorted(p)) for p in patterns]
            out_ = ["".join(sorted(w)) for w in out]
            digit = {}
            for code in codes:
                if len(code) == 2:
                    one = code
                    digit[code] = 1
                if len(code) == 3:
                    digit[code] = 7
                if len(code) == 4:
                    four = code
                    digit[code] = 4
                if len(code) == 7:
                    digit[code] = 8
            for code in codes:
                if len(code) != 6:
                    continue
                if all(i in code for i in four):
                    digit[code] = 9
                elif sum(i in code for i in one) == 1:
                    six = code
                    digit[code] = 6
                else:
                    digit[code] = 0
            for code in codes:
                if len(code) != 5:
                    continue
                if all(ch in code for ch in one):
                    digit[code] = 3
                elif all(ch in six for ch in code):
                    digit[code] = 5
                else:
                    digit[code] = 2
            num = 0
            for s in out_:
                num = num * 10 + digit[s]
            solve += num
    return solve

print(f"Решение части 1: {get_solve(list_data)}")
print(f"Решение части 2: {get_solve(list_data,part=2)}")