"""
https://atcoder.jp/contests/abc304/tasks/abc304_c
"""

import sys
sys.setrecursionlimit(10000)

N, D = map(int, input().split())
XY = [(["No"] + list(map(int, input().split()))) for _ in range(N)]
D = D**2

def infection(x, y):
    global XY
    for i, (status, target_x, target_y) in enumerate(XY):
        if status == "Yes":
            continue
        if x == target_x and y == target_y:
            continue
        if (x-target_x) ** 2 + (y-target_y) ** 2 <= D:
            XY[i][0] = "Yes"
            infection(target_x, target_y)

XY[0][0] = "Yes"
infection(XY[0][1], XY[0][2])

for xy in XY:
    print(xy[0])