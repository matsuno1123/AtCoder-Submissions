"""
https://atcoder.jp/contests/abc423/tasks/abc423_b
"""

N = int(input())
L = list(map(int, input().split()))

if 1 not in L:
    print(0)
else:
    start_index = L.index(1)
    L.reverse()
    end_index = len(L)-1 - L.index(1)
    print(end_index-start_index)