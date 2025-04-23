list_str = [i.strip() for i in open("input.txt")]
dict_data = {}
for str_ in list_str:
    list_data = str_.replace(",", "").replace(":", "").split()
    name = list_data[0] + list_data[1]
    data_list = list_data[2:]
    dict_data.update({name: {i:int(data_list[idx+1]) for idx, i in enumerate(data_list) if idx % 2 == 0}})

def get_solve(part = 1):
    st_dict = {'children': 3, 'cats': 7,'samoyeds': 2,'pomeranians': 3,'akitas': 0,'vizslas': 0,
               'goldfish': 5,'trees': 3,'cars': 2,'perfumes': 1}
    for name, data in dict_data.items():
        bad = False
        for key, val in data.items():
            if part == 1:
                if st_dict.get(key) != val:
                    bad = True
                    break
            else:
                if key in ['cats', "trees"]:
                    if st_dict.get(key) > val:
                        bad = True
                        break
                elif key in ['pomeranians', "goldfish"]:
                    if st_dict.get(key) < val:
                        bad = True
                        break
                else:
                    if st_dict.get(key) != val:
                        bad = True
                        break
        if not bad:
            return name.replace("Sue", "")



print(f"Решение части 1: {get_solve()}")
print(f"Решение части 2: {get_solve(part=2)}")

