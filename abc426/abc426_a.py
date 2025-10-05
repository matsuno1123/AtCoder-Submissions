"""
https://atcoder.jp/contests/abc426/tasks/abc426_a
"""

os = {"Ocelot": 1, "Serval": 2, "Lynx": 3}
X, Y  = input().split()

if os[X] >= os[Y]:
    print("Yes")
else:
    print("No")