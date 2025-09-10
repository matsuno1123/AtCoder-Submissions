"""
https://atcoder.jp/contests/abc406/tasks/abc406_d
"""

H, W, N = map(int, input().split())
x_dict = {i:set() for i in range(1, H+1)}
y_dict = {i:set() for i in range(1, W+1)}

for _ in range(N):
    x, y = map(int, input().split())
    x_dict[x].add(y)
    y_dict[y].add(x)

Q = int(input())
for _ in range(Q):
    t, xy = map(int, input().split())
    if t==1:
        y_dust = x_dict[xy]
        print(len(y_dust))
        x_dict[xy] = set()
        for i in y_dust:
            y_dict[i].remove(xy)
    else:
        x_dust = y_dict[xy]
        print(len(x_dust))
        y_dict[xy] = set()
        for i in x_dust:
            x_dict[i].remove(xy)