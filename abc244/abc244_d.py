"""
https://atcoder.jp/contests/abc244/tasks/abc244_d
"""

S = input().split()
T = input().split()
count = 0
for (s, t) in zip(S, T):
    count += not s==t
if count == 2:
    print("No")
else:
    print("Yes")