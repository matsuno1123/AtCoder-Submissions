"""
https://atcoder.jp/contests/abc152/tasks/abc152_c
"""

N = int(input())
P = list(map(int, input().split()))
count = 1
min_p = P[0]
for i, p in enumerate(P[1:N]):
    if p <= min_p:
        count += 1
        min_p = p
print(count)