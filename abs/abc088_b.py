
https://atcoder.jp/contests/abs/tasks/abc088_b
"""

N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

if N%2 == 1:
    A.append(0)

result = 0
for i in range(0, N, 2):
    result += A[i] - A[i+1]

print(result)