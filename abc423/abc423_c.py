"""
https://atcoder.jp/contests/abc423/tasks/abc423_c
"""

N, R = map(int, input().split())
L = list(map(int, input().split()))
left_L = []
right_L = []
if R != 0:
    left_L = L[0:R]
if R != N:
    right_L = L[R:N]
result = 0
if left_L != []:
    open_flg = False
    for l in left_L:
        if open_flg or l == 0:
            open_flg = True
            if l == 0:
                result += 1
            else:
                result += 2
if right_L != []:
    right_L.reverse()
    open_flg = False
    for l in right_L:
        if open_flg or l == 0:
            open_flg = True
            if l == 0:
                result += 1
            else:
                result += 2

print(result)