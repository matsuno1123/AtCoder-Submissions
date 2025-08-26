"""
https://atcoder.jp/contests/abc139/tasks/abc139_b
"""

A, B = list(map(int, input().split()))
d, m = divmod(B-1, A-1)
print(d + (m>0))