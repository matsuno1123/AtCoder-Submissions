"""
https://atcoder.jp/contests/abc103/tasks/abc103_b
"""

S = input()
T = input()

for _ in range(len(S)):
    S = S[1:len(S)] + S[0]
    if S == T:
        print("Yes")
        break
else:
    print("No")