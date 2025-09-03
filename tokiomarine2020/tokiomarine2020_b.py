"""
https://atcoder.jp/contests/tokiomarine2020/tasks/tokiomarine2020_b
"""

A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())
if (V-W)*T >= abs(B-A):
    print("YES")
else:
    print("NO")