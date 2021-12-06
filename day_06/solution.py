from collections import Counter
from os import stat

with open("input.txt") as f:
    input = [int(c) for c in f.read().split(",")]
    
input_test = [int(c) for c in "3,4,3,1,2".split(",")]


def update_state_naive(state):
    updated_state = []
    born_fish = []
    for t in state:
        if t == 0:
            born_fish.append(8)
            updated_state.append(6)
        else:
            updated_state.append(t-1)
    
    return updated_state + born_fish


def simulate(initial_state, days=18, verbose=False):
    state = initial_state.copy()
    # print("initial: ", state)
    for i in range(days):
        state = update_state_naive(state)
        if verbose:
            print(i+1, " days: ", state)
    return len(state)


print(simulate(input, 80))

# Part 2
# Need a more efficient algorithm..
def get_state_counter(state):
    c = Counter(state)
    empty = set(range(9)).difference(set(c.keys()))
    for x in empty:
        c[x] = 0
    return c


def update_state(state_counter):
    spawns = state_counter[0]
    for k in range(0, len(state_counter)-1):
        state_counter[k] = state_counter[k+1]
    state_counter[8] = spawns
    state_counter[6] += spawns
    return state_counter

    
def simulate_counter(state_counter, days=18):
    stat = state_counter.copy()
    for _ in range(days):
        stat = update_state(stat)
    return sum(v for v in stat.values())


print(simulate_counter(get_state_counter(input), 256))