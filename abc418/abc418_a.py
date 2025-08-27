"""
https://atcoder.jp/contests/abc418/tasks/abc418_a
"""

N = int(input())
S = input()
if S[N-3:N] == "tea":
  print("Yes")
else:
  print("No")