from collections import defaultdict

from numpy import sign

test_input = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

test_data = test_input.split("\n")

with open("input.txt") as f:
    input = f.read().splitlines()

data = input

signals = [s.split(" | ")[0] for s in data]
outputs = [s.split(" | ")[1] for s in data]

def get_1478_count(output):
    output_lens = [len(s) for s in output.split(" ")]
    return len([o for o in output_lens if o in (2,3,4,7)])

print("Part 1:", sum(get_1478_count(o) for o in outputs))


# Part 2
def get_len_dict(signal_list):
    len_dict = defaultdict(list)
    for s in signal_list:
        len_dict[len(s)].append(set(s))
    return dict(len_dict)


signal_lists = [s.split() for s in signals]
output_lists = [s.split() for s in outputs]
signal_dicts = [get_len_dict(l) for l in signal_lists]
output_sets = [[set(s) for s in l] for l in output_lists]


def solver(sd):
    poss = dict()
    nums = dict()
    nums[1], nums[7], nums[4], nums[8] = sd[2][0], sd[3][0], sd[4][0], sd[7][0]
    
    def get_diff(s1, sets, diff_len=1):
        for s in sets:
            diff_set = s.difference(s1)
            if len(diff_set) == diff_len:
                return diff_set
            
    def combine_sets(sets):
        return set().union(*sets)

    # Solve:
    poss['a'] = nums[7].difference(sd[2][0])
    poss['g'] = get_diff(nums[4].union(poss['a']), sd[6])
    nums[9] = nums[4].union(poss['a'], poss['g'])
    poss['e'] = nums[8].difference(nums[9])
    nums[2] = get_diff(combine_sets(poss.values()), sd[5], diff_len=2).union(combine_sets(poss.values()))
    poss['f'] = nums[1].difference(nums[2])
    poss['c'] = nums[1].difference(poss['f'])
    poss['d'] = nums[2].difference(combine_sets(poss.values()))
    poss['b'] = nums[8].difference(combine_sets(poss.values()))
    # Missing: 0, 3, 5, 6
    nums[0] = combine_sets(poss.values()).difference(poss['d'])
    nums[3] = poss['a'].union(poss['c'], poss['d'], poss['f'], poss['g'])
    nums[5] = poss['a'].union(poss['b'], poss['d'], poss['f'], poss['g'])
    nums[6] = nums[5].union(poss['e'])
    return nums


def get_output_value(nums, output_sets):
    digits = ""
    for s in output_sets:
        for k, v in nums.items():
            if v == s:
                digits += str(k)
    return int(digits)


print("Part 2: ", sum(get_output_value(solver(sd), od) for sd, od in zip(signal_dicts, output_sets)))