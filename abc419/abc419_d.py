"""
https://atcoder.jp/contests/abc419/tasks/abc419_d
"""

N, M = list(map(int, input().split()))
S = list(input())
T = list(input())

query = list(0 for _ in range(N+1))
result = []

for _ in range(M):
  l,r = map(int, input().split())
  query[l-1] += 1
  query[r] += 1

status = 0
for i in range(N):
  status += query[i]
  if status%2 == 0:
    result.append(S[i])
  else:
    result.append(T[i])

print("".join(result))