#https://adventofcode.com/2023/day/4
list_in = [i.strip() for i in open("input.txt")]
dict_data = {}
for idx, game in enumerate(list_in):
    list_split = game.split(":")
    card = list_split[0]
    win, hand = list_split[1].split("|")
    win, hand = win.split(), hand.split()
    win, hand = [int(i) for i in win], [int(i) for i in hand]
    dict_data.update({idx:{"win": win, "hand": hand, "count":1}})

def get_solve(data_in, part = 1):
    solve, list_card = 0, list(data_in.keys())
    for card, data_card in data_in.items():
        if part == 1:
            list_win = [i for i in data_card["hand"] if i in data_card["win"]]
            solve += int(2**(len(list_win)-1))
        else:
            count = len([i for i in data_card["hand"] if i in data_card["win"]])
            list_win = list_card[card + 1:card + count + 1]
            card_count = data_in[card]["count"]
            for i in list_win:
                data_in[i]["count"] += card_count
            solve = sum([i["count"] for i in data_in.values()])
    return solve


print(f"Решение задания 1:{get_solve(dict_data, part=1)}")
print(f"Решение задания 2:{get_solve(dict_data, part=2)}")