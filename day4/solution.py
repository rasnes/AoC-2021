import numpy as np
from itertools import groupby

with open("input.txt") as f:
    lines_str = f.read().splitlines()

with open("input_test.txt") as f:
    lines_str_test = f.read().splitlines()

# Clean data, to numpy arrays
input = lines_str
draws = [int(c) for c in input[0].split(",")]


def input_to_arrays(input):
    group_chars = [list(g) for k, g in groupby(input, lambda x: x != "") if k]
    only_chars = []
    for l in group_chars:
        only_chars.append([s.split() for s in l])
    return np.array(only_chars).astype(int)


boards = input_to_arrays(input[1:])


def play(draws, boards, first=True):
    hits = np.zeros(boards.shape, dtype=np.int8)
    for draw in draws:
        np.place(hits, boards == draw, 1)
        row_hit_sums = np.sum(hits, axis=2)
        col_hit_sums = np.sum(hits, axis=1)
        row_location_5 = np.where(row_hit_sums == 5)
        col_location_5 = np.where(col_hit_sums == 5)
        if first: 
            if len(row_location_5[0]) > 0:
                winner_idx = row_location_5[0]
                return boards[winner_idx], hits[winner_idx], draw
            if len(col_location_5[0]) > 0:
                winner_idx = col_location_5[0]
                return boards[winner_idx], hits[winner_idx], draw
        else:
            completed_boards = set(list(row_location_5[0]) + list(col_location_5[0]))
            if len(completed_boards) == len(boards) - 1:
                last_set = set(range(len(boards))).difference(completed_boards)
                last, = last_set
            if len(completed_boards) == len(boards):
                return boards[last], hits[last], draw


def calculate_score(board, hits, final_draw):
    misses = board[np.where(hits == 0)]
    print(misses)
    sum_misses = sum(misses)
    return sum_misses * final_draw

# Part 1
win_board, win_hits, final_draw = play(draws, boards)
print(calculate_score(win_board, win_hits, final_draw))
# 44088 is correct.

# Part 2
last_board, last_hits, final_draw = play(draws, boards, first=False)
print(calculate_score(last_board, last_hits, final_draw))



