
def get_solve(path, part=1):
    game_rule = {"A": {"figure": 1, "W": "C", "L": "B"},
                 "B": {"figure": 2, "W": "A", "L": "C"},
                 "C": {"figure": 3, "W": "B", "L": "A"}}
    convert_dict = {"X": "A", "Y": "B", "Z": "C"}
    all_prize = 0
    for game in open(path):
        game, prize = game.strip().split(), 0
        if part == 1:
            player_1, player_2 = game[0], convert_dict[game[1]]
            prize = game_rule[player_2]["figure"]
            if player_1 == player_2:
                prize += 3
            elif player_1 != game_rule[player_2]["L"]:
                prize += 6
        else:
            player_1, res_game = game
            if res_game == "X":
                player_2 = game_rule[player_1]["W"]
            elif res_game == "Y":
                prize += 3
                player_2 = player_1
            else:
                player_2 = game_rule[player_1]["L"]
                prize += 6
            prize_player = game_rule[player_2]["figure"]
            prize += prize_player
        all_prize += prize
    return all_prize
print(f"Решение части 1: {get_solve('input.txt')}")
print(f"Решение части 2: {get_solve('input.txt', part=2)}")








