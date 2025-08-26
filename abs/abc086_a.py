"""
https://atcoder.jp/contests/abs/tasks/abc086_a
"""

a, b = map(int, input().split())
if a%2 == 0 or b%2 == 0:
    print("Even")
else:
    print("Odd")