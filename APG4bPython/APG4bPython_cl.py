"""
https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cl
"""

S = input()
p = S.count("+")
m = S.count("-")
print(1 + p - m)