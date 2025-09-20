"""
https://atcoder.jp/contests/abc424/tasks/abc424_b
"""

N, M, K = map(int, input().split())

ans = [0]*N
result = []
for _ in range(K):
    A, B = map(int, input().split())
    ans[A-1] += 1
    if ans[A-1] == M:
        result.append(A)

print(*result)