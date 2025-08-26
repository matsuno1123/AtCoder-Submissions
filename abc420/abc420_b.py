
https://atcoder.jp/contests/abc420/tasks/abc420_b
"""

N, M = map(int, input().split())
S = [list(map(int, input())) for _ in range(N)]

vote = [-1] * M
result = [0] * N

for i in range(M):
    vote_sum = 0
    for j in range(N):
        vote_sum += S[j][i]
    if vote_sum <= N//2:
        vote[i] = 1
    else:
        vote[i] = 0

for k, row in enumerate(S):
    for (r, v) in zip(row, vote):
        if r == v:
            result[k] += 1

m = max(result)
max_index = [str(i+1) for i, r in enumerate(result) if r == max(result)]

print(" ".join(max_index))