#https://adventofcode.com/2024/day/4
list_data = [i.strip("\n") for i in open("input.txt")]

DATA_V1 = [[[1, 0], [2, 0], [3, 0]],[[1, 1], [2, 2], [3, 3]],[[0, 1], [0, 2], [0, 3]],[[-1, 1], [-2, 2], [-3, 3]],
           [[-1, 0], [-2, 0], [-3, 0]],[[-1, -1], [-2, -2], [-3, -3]],[[0, -1], [0, -2], [0, -3]],
           [[1, -1], [2, -2], [3, -3]],]
DATA_V2 = [[[-1, -1], [1, -1], [1, 1], [-1, 1]],[[1, -1], [1, 1], [-1, -1], [-1, 1]],
           [[1, 1], [-1, 1], [-1, -1], [1, -1]],[[-1, 1], [-1, -1], [1, 1], [1, -1]]]

def search(x, y, list_word, matrix, word_find):
    count = 0
    for data in matrix:
        len_search = 0
        for index, delta in enumerate(data):
            x_delta, y_delta = delta
            x_, y_ = x + x_delta, y + y_delta
            if x_ < 0 or y_ < 0:
                break
            try:
                if list_word[y_][x_] != word_find[index]:
                    break
            except IndexError:
                break
            len_search += 1
            if len_search == len(word_find):
                count += 1
    return count

def get_count_word(list_word, part=1):
    matrix, word_find, letter_find = (DATA_V1,'MAS', "X") if part == 1 else (DATA_V2, 'MMSS', "A")
    count_all = 0
    for y, line in enumerate(list_word):
        for x, letter in enumerate(line):
            if list_word[y][x] == letter_find:
                count_all += search(x, y, list_word, matrix, word_find)
    return count_all

print(f"Решение части 1: {get_count_word(list_data, part=1)}")
print(f"Решение части 2: {get_count_word(list_data, part=2)}")







