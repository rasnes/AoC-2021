import numpy as np

with open("input.txt") as f:
    lines_str = f.read().splitlines()

with open("input_test.txt") as f:
    lines_str_test = f.read().splitlines()

# Clean input data
input = lines_str
def tup_split(s, sep=" -> ", straight=True):
    ss = s.split(sep=sep)
    start, stop = sorted([int(c) for c in s.split(",")] for s in ss)
    return start, stop

all_coords = [tup_split(s) for s in input]
straight_check = lambda start, stop: start[0] == stop[0] or start[1] == stop[1]
coords_straight = [t for t in all_coords if straight_check(t[0], t[1])]
coords_diag = [t for t in all_coords if not straight_check(t[0], t[1])]

def create_map(coords, straight=True, size=1000):
    arrs = np.zeros((len(coords), size, size), dtype=np.int8)
    for i, ((x1, y1), (x2, y2)) in enumerate(coords):
        if straight:
            arrs[i, y1:y2+1, x1:x2+1] = 1
            # NOTE TO SELF: don't iterate of over numpy arrays,
            # for some unknown reason the below yields an incorrect result.
            # The updated approach above is both correct and more readable.
            # for i, _ in enumerate(arrs):
            #     arrs[i, coords[i, 0, 1]:coords[i, 1, 1]+1, coords[i, 0, 0]:coords[i, 1, 0]+1] = 1
        else:
            step_x = 1 if x1 < x2 else -1
            step_y = 1 if y1 < y2 else -1
            xs = list(range(x1, x2+step_x, step_x))
            ys = list(range(y1, y2+step_y, step_y))
            diag_coords = list(zip(xs, ys))
            for x, y in diag_coords:
                arrs[i, y, x] = 1
    
    return np.sum(arrs, axis=0)


vent_map_straight = create_map(coords_straight)
vent_map_diag = create_map(coords_diag, straight=False)

def overlaps(vent_map):
    return (vent_map >= 2).sum()

print(overlaps(vent_map_straight))
# 5835 is correct

print(overlaps(vent_map_straight + vent_map_diag))
# 22213 is correct