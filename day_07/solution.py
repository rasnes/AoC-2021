import numpy as np

test_input = [int(c) for c in "16,1,2,0,4,2,7,1,2,14".split(",")]

with open("input.txt") as f:
    input = [int(c) for c in f.read().split(",")]

# input = test_input   
crab_pos = np.reshape(np.array(input), (-1, 1))
check_pos = np.array(list(range(max(input))))
check_matrix = np.tile(check_pos, (len(input), 1))
diffs = np.abs(check_matrix - crab_pos)
col_sums = np.sum(diffs, axis=0)

print("Part 1: ", np.min(col_sums))

# Part 2
# Slow solution! How can I improve speed here?
@np.vectorize
def step_loss(diff):
    return sum((i+1) for i in range(diff))
col_sums = np.sum(step_loss(diffs), axis=0)
print("Part 2: ", np.min(col_sums))