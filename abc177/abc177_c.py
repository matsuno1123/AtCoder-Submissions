"""
https://atcoder.jp/contests/abc177/tasks/abc177_c
"""

N=int(input())
A=list(map(int, input().split()))

a_sum = sum(A)

result = 0
for i in range(0, N-1):
    a_sum -= A[i]
    result += a_sum * A[i]
    result %= 10**9+7

print(result)