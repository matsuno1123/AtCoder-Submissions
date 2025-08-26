"""
https://atcoder.jp/contests/abc107/tasks/abc107_b
"""

H, W = map(int, input().split())
a = [list(input()) for _ in range(H)]

for i in range(W-1, -1, -1):
    if all(row[i]=='.' for row in a):
        for j in range(H):
            a[j].pop(i)

for row in a:
    if any(d == '#' for d in row):
       print("".join(row))
