"""
https://atcoder.jp/contests/abc024/tasks/abc024_b
"""

N, T = map(int, input().split())
A = list(int(input()) for _ in range(N))

result = T
for i in range(0, N-1):
    diff_time = A[i+1]-A[i]
    if diff_time > T:
        result+=T
    else:
        result+=diff_time
print(result)