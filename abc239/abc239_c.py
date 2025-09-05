"""
https://atcoder.jp/contests/abc239/tasks/abc239_c
"""

x1, y1, x2, y2 = map(int, input().split())
points = {(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)}

a_points = {(x+x1, y+y1) for x, y in points}
b_points = {(x+x2, y+y2) for x, y in points}

if len(a_points & b_points) > 0:
    print("Yes")
else:
    print("No")