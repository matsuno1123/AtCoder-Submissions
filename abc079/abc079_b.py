"""
https://atcoder.jp/contests/abc079/tasks/abc079_b
"""

N = int(input())

if N == 1:
    print(1)
else:
    l_2 = 2
    l_1 = 1
    for _ in range(N-2):
        l_2, l_1 = l_1, l_2+l_1
    print(l_2+l_1)