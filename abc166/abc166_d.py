"""
https://atcoder.jp/contests/abc166/tasks/abc166_d
"""

X = int(input())

range_xy = range(-200, 201)
break_flg = False

for x in range_xy:
    for y in range_xy:
        if x**5-y**5 == X:
            print(x,y)
            break_flg = True
            break
    if break_flg:
        break