"""
https://atcoder.jp/contests/arc040/tasks/arc040_a
"""

N = int(input())
count_r, count_b = 0, 0
for _ in range(N):
    S = list(input())
    count_r += S.count("R")
    count_b += S.count("B")

if count_r > count_b:
    print("TAKAHASHI")
elif count_r < count_b:
    print("AOKI")
else:
    print("DRAW")