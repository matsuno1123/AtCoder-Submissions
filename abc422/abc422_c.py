"""
https://atcoder.jp/contests/abc422/tasks/abc422_c
"""

T = int(input())
for _ in range(T):
    a, b, c = map(int, input().split())
    min_ac = min(a, c)
    print(min(min_ac, (a+b+c)//3))