"""
https://atcoder.jp/contests/abc419/tasks/abc419_c
"""

N = int(input())
x_min, y_min, x_max, y_max = 10**9, 10**9, 1, 1
for _ in range(N):
    x, y = map(int, input().split())
    if x < x_min:
        x_min = x
    if x > x_max:
        x_max = x
    if y < y_min:
        y_min = y
    if y > y_max:
        y_max = y
print(max((x_max-x_min+1)//2, (y_max-y_min+1)//2))