"""
https://atcoder.jp/contests/abc422/tasks/abc422_b
"""

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
BLACK = "#"
break_flg = False

for w in range(W):
    for h in range(H):
        if S[h][w] == BLACK:
            count = 0
            if w>0 and S[h][w-1]==BLACK:
                 count += 1
            if w<W-1 and S[h][w+1]==BLACK:
                count += 1
            if h>0 and S[h-1][w]==BLACK:
                count += 1
            if h<H-1 and S[h+1][w]==BLACK:
                count += 1
            if count!=2 and count!=4:
                print("No")
                break_flg = True
                break
    if break_flg:
        break
else:
    print("Yes")