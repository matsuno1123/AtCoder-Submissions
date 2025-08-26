"""
https://atcoder.jp/contests/arc004/tasks/arc004_1
"""

import math

N = int(input())
xy = list(list(map(int, input().split())) for _ in range(N))

max_line = 0

for x1, y1 in xy:
    for x2, y2 in xy:
        now_line = (x2 - x1) ** 2 + (y2 - y1) ** 2
        if max_line < now_line:
          max_line = now_line

print(math.sqrt(max_line))