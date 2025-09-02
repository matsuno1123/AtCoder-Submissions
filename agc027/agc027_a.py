"""
https://atcoder.jp/contests/agc027/tasks/agc027_a
"""

N, x = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

sum_a = 0
count = 0
for a in A:
    sum_a += a
    if sum_a > x:
        break
    count += 1
else:
    if sum_a != x:
        count -= 1

print(count)