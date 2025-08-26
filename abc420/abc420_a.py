
https://atcoder.jp/contests/abc420/tasks/abc420_a
"""

X, Y = map(int, input().split())

X += Y
if X > 12:
    X = X - 12

print(X)