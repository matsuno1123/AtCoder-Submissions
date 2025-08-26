"""
https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cf
"""

N, M = map(int, input().split())
game = [list(map(int, input().split())) for _ in range(M)]

result= [["-" for _ in range(N)] for _ in range(N)]

for a, b in game:
    result[a-1][b-1] = "o"
    result[b-1][a-1] = "x"

for row in result:
    print(" ".join(row))