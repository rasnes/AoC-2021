# OBS: this solution was obtained from subreddit: https://www.reddit.com/r/adventofcode/comments/r9824c/2021_day_5_solutions/

import re
from collections import Counter

from numpy.lib.twodim_base import _diag_dispatcher

test_data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

with open('input.txt') as f:
    data = f.read()

def solution(data, part=1):
    lines = re.findall('(\d+),(\d+) -> (\d+),(\d+)', data)
    points = Counter()
    for line in lines:
        x1, y1, x2, y2 = map(int, line)
        if part == 1 and x1 != x2 and y1 != y2:  # diagonal line
            continue
        dx, dy = x2 - x1, y2 - y1
        length = max(abs(dx), abs(dy))
        x_step, y_step = dx//length, dy//length
        points.update((x1 + i*x_step, y1 + i*y_step) for i in range(length+1))
    
    return sum(count > 1 for count in points.values())

assert solution(test_data, part=1) == 5
print('Part 1:', solution(data, part=1))

assert solution(test_data, part=2) == 12
print('Part 2:', solution(data, part=2))