"""
https://atcoder.jp/contests/abc206/tasks/abc206_c
"""

N = int(input())
A = list(map(int, input().split()))

A.sort()

result = 0
diff_len = 0
for i, a in enumerate(A[1:N]):
    if A[i] != a:
        diff_len = i+1
    result += diff_len

print(result)