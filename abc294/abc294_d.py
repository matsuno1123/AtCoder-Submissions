"""
https://atcoder.jp/contests/abc294/tasks/abc294_d
"""

from sortedcontainers import *

N, Q = map(int, input().split())
member = SortedList(i for i in range(1, N+1))
called_member = SortedList()

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        called_member.add(member.pop(0))
    elif query[0] == 2:
        called_member.remove(query[1])
    elif query[0] == 3:
        print(called_member[0])