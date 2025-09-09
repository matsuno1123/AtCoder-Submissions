"""
https://atcoder.jp/contests/abc070/tasks/abc070_c
"""

import math

N = int(input())
T = list(int(input()) for _ in range(N))
print(math.lcm(*T))