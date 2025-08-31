"""
https://atcoder.jp/contests/abc421/tasks/abc421_a
"""

N = int(input())
S = list(input() for _ in range(N))
X, Y = input().split()

if S[int(X)-1] == Y:
    print("Yes")
else:
    print("No")