"""
https://atcoder.jp/contests/abc226/tasks/abc226_b
"""

N = int(input())
result = set()
for _ in range(N):
    A = input()
    result.add(A)

print(len(result))