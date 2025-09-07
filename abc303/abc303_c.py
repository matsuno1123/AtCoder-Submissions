"""
https://atcoder.jp/contests/abc303/tasks/abc303_c
"""

N, M, H, K = map(int, input().split())
S = list(input())

now_x, now_y = 0, 0
game_set = set()

for _ in range(M):
    x, y = map(int, input().split())
    game_set.add((x,y))

for s in S:
    if s == "R":
        now_x += 1
    elif s == "L":
        now_x -= 1
    elif s == "U":
        now_y += 1
    elif s == "D":
        now_y += -1
    H -= 1
    if H < 0:
        print("No")
        break
    if H < K and (now_x, now_y) in game_set:
        H = K
        game_set.discard((now_x, now_y))
else:
    print("Yes")