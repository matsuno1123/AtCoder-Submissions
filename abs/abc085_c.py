
https://atcoder.jp/contests/abs/tasks/abc085_c
"""

N, Y = map(int, input().split())

Y = Y // 1000

xy = [[i*j for i in range(0, N+1)] for j in range(0, N+1)]

result=[-1, -1, -1]

end_flg = False
for x in range(0, N+1):
    for y in range(0, N+1-x):
        z = N-x-y
        if z>=0 and 10*x+5*y+z == Y:
            result = [x, y, z]
            end_flg = True
            break
    if end_flg:
        break

print(result[0], result[1], result[2])