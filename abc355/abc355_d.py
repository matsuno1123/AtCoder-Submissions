"""
https://atcoder.jp/contests/abc355/tasks/abc355_d
"""

N = int(input())
L,R = [0]*N, [0]*N
for i in range(N):
    L[i], R[i]  = map(int, input().split())
L.sort()
R.sort()

r_index = 0
ans = N*(N-1)//2
for l in L:
    while R[r_index] < l:
        r_index += 1
    ans -= r_index

print(ans)