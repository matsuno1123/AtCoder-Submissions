"""
https://atcoder.jp/contests/abc424/tasks/abc424_a
"""

a, b, c = map(int, input().split())
if a==b or b==c or a==c:
    print("Yes")
else:
    print("No")