"""
https://atcoder.jp/contests/abc015/tasks/abc015_2
"""

N = int(input())
A = list(map(int, input().split()))
A = list(a for a in A if a!=0)
N = len(A)
print((sum(A)+N-1) // N)