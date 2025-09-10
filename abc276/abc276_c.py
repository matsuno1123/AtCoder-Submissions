"""
https://atcoder.jp/contests/abc276/tasks/abc276_c
"""

N = int(input())
P = list(map(int, input().split()))

start_index = None
before_p = P[N-1]
for i in range(N-2, -1, -1):
    if before_p < P[i]:
        start_index = i
        break
    before_p = P[i]

target_index = P.index(max(p for p in P[start_index+1:N] if p<P[start_index]))
P[start_index], P[target_index] = P[target_index], P[start_index]

P = P[0:start_index+1] + sorted(P[start_index+1:N], reverse=True)

print(*P)