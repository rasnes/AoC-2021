with open("input.txt") as f:
    lines_str = f.read().splitlines()

# Part 1
forwards = [int(l[-1]) for l in lines_str if l.startswith("f")]
ups = [int(l[-1]) for l in lines_str if l.startswith("u")]
downs = [int(l[-1]) for l in lines_str if l.startswith("d")]

horiz_pos = sum(forwards)
depth = sum(downs) - sum(ups)

print(horiz_pos * depth)

# Part 2
splitted = [l.split() for l in lines_str]
tups_int = [(l[0], int(l[1])) for l in splitted]

def get_position(tups_int):
    aim = 0
    depth = 0
    horiz_pos = 0
    
    for action, units in tups_int:
        if action == 'down':
            aim += units
        elif action == 'up':
            aim -= units
        else:
            horiz_pos += units
            depth += aim * units
        
    return horiz_pos, depth

horiz_pos, depth = get_position(tups_int)

print(horiz_pos*depth)
