"""
https://atcoder.jp/contests/abc421/tasks/abc421_b
"""

X, Y = map(int, input().split())

a1 = X
a2 = Y
for _ in range(8):
    a12 = a1+a2
    f_a12 = list(str(a12))
    f_a12.reverse()
    f_a12 = int("".join(f_a12))
    a1, a2 = a2, f_a12

print(a2)