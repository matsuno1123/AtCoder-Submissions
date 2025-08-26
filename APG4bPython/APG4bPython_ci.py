"""
https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_ci
"""

data = list(map(int, input().split()))
data_c = data.copy()
data_c.pop(0)

for d, c in zip(data, data_c):
    if d == c:
        print("YES")
        break
else:
    print("NO")