with open("input.txt") as f:
    lines_str = f.read().splitlines()

n = len(lines_str)
digits_char = list(zip(*lines_str))


def to_ints(digits_char):
    digits = []
    for l in digits_char:
        digits.append([int(c) for c in l])
    return digits


digits = to_ints(digits_char)

means = [sum(digs)/n for digs in digits]
gamma = "".join([str(int(m*2)) for m in means])
epsilon = "".join([str(1 - int(m*2)) for m in means])
gamma_decimal = int(gamma, 2)
epsilon_decimal = int(epsilon, 2)

print(gamma_decimal * epsilon_decimal)

# Part 2
def get_common(col, most=True):
    mean = sum(col)/len(col)
    if most:
        return 1 if mean >= 0.5 else 0
    else:
        return 0 if mean >= 0.5 else 1


def get_rating(digits, oxygen=True, lines_str=lines_str):
    indices = set(range(len(digits[0])))

    for i, col in enumerate(digits):
        relevant = [col[j] for j in indices]
        common = get_common(relevant, oxygen)
        cur_indices = set(j for j, d in enumerate(col) if d == common)
        indices = indices.intersection(cur_indices)
        if len(indices) == 1:
            binary = lines_str[list(indices)[0]]
            break

    return binary


co2_rating = get_rating(digits, oxygen=False)
oxygen_rating = get_rating(digits, oxygen=True)
print(int(oxygen_rating, 2) * int(co2_rating, 2))
