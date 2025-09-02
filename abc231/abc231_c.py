"""
https://atcoder.jp/contests/abc231/tasks/abc231_c
"""

import bisect

N, Q = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

for _ in range(Q):
    x = int(input())
    print(N-bisect.bisect_left(A, x))