"""
https://atcoder.jp/contests/abc425/tasks/abc425_a
"""

N = int(input())
result = 0
for i in range(N):
    result += (-1)**(i+1) * (i+1)**3
print(result)