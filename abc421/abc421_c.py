"""
https://atcoder.jp/contests/abc421/tasks/abc421_c
"""

N = int(input())
S = list(input())

first = S[0]

f_before = []
a_after = [i for i in range(0,2*N) if i%2 == 0]
b_after = [i for i in range(0,2*N) if i%2 == 1]
for i, s in enumerate(S):
    if s == first:
        f_before.append(i)

a_swap = 0
b_swap = 0
for before, after in zip(f_before, a_after):
    a_swap += abs(before-after)
for before, after in zip(f_before, b_after):
    b_swap += abs(before-after)

print(min(a_swap, b_swap))