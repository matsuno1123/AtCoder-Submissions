"""
https://atcoder.jp/contests/abc061/tasks/abc061_b
"""

N, M = map(int, input().split())
AB = sum([list(map(int, input().split())) for _ in range(M)], [])

for i in range(1, N+1):
    print(AB.count(i))