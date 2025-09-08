"""
https://atcoder.jp/contests/abc374/tasks/abc374_d
"""

import math

def cal_distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def line(xy, distance, points):
    if len(points) == 1:
        p = points[0]
        return distance+min(cal_distance(xy[0], xy[1], p[0], p[1]), cal_distance(xy[0], xy[1], p[2], p[3]))
    result_list = []
    for i, p in enumerate(points):
        target = points.copy()
        target.pop(i)
        d1 = distance+cal_distance(xy[0], xy[1], p[0], p[1])
        d2 = distance+cal_distance(xy[0], xy[1], p[2], p[3])
        xy1 = [p[2], p[3]]
        xy2 = [p[0], p[1]]
        result_list.append(line(xy1, d1, target))
        result_list.append(line(xy2, d2, target))
    return min(result_list)

N, S, T = map(int, input().split())
ABCD = [list(map(int, input().split())) for _ in range(N)]

now = [0,0]
d = line(now, 0.0, ABCD)

print(d/S + sum(cal_distance(p[0], p[1], p[2], p[3]) for p in ABCD)/T)