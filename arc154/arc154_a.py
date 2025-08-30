"""
https://atcoder.jp/contests/arc154/tasks/arc154_a
"""

import sys
sys.set_int_max_str_digits(1000000)

N = int(input())
A = list(input())
B = list(input())

for i in range(N):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

print(int("".join(A)) * int("".join(B)) % 998244353)