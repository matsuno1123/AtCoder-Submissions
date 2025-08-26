
https://atcoder.jp/contests/abs/tasks/abc087_b
"""

from selectors import SelectSelector

A = int(input())
B = int(input())
C = int(input())
X = int(input())

print(sum(0 <= (X - 500*k - 100*j) // 50 <= C for j in range(B+1) for k in range(A+1)))