
https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cg
"""

N, K = map(int, input().split())
S = input().split()

S = [s for s in S if len(s) >= K]
result = " ".join(S)
print(result)