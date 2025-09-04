"""
https://atcoder.jp/contests/abc258/tasks/abc258_c
"""

N, Q = map(int, input().split())
S = input()

now_index = 0

for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        now_index -= x
        if now_index < 0:
            now_index += len(S)
    else:
        print(S[(x+now_index-1)%len(S)])