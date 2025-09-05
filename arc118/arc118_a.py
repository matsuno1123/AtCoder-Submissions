"""
https://atcoder.jp/contests/arc118/tasks/arc118_a
"""

t, N = map(int, input().split())
print(((N*100+t-1)//t)*(100+t)//100-1)