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
        col_hit_sums = np.sum(hits, axis=1)
        row_hit_sums = np.sum(hits, axis=2)
        col_loc_5 = np.where(col_hit_sums == 5)[0]
        row_loc_5 = np.where(row_hit_sums == 5)[0]
        if first: 
            if len(row_loc_5) > 0:
                return boards[row_loc_5], hits[row_loc_5], draw
            if len(col_loc_5) > 0:
                return boards[col_loc_5], hits[col_loc_5], draw
        else:
            completed_boards = set(list(row_loc_5) + list(col_loc_5))
            if len(completed_boards) == len(boards) - 1:
                board_indices = range(len(boards))
                last_set = set(board_indices).difference(completed_boards)
                last, = last_set
            if len(completed_boards) == len(boards):
                return boards[last], hits[last], draw


def calculate_score(board, hits, final_draw):
    misses = board[np.where(hits == 0)]
    sum_misses = sum(misses)
    return sum_misses * final_draw

# Part 1
win_board, win_hits, final_draw = play(draws, boards, first=True)
print(calculate_score(win_board, win_hits, final_draw))
# 44088 is correct.

# Part 2
last_board, last_hits, final_draw = play(draws, boards, first=False)
print(calculate_score(last_board, last_hits, final_draw))
# 23670 is correct