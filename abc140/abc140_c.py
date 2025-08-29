"""
https://atcoder.jp/contests/abc140/tasks/abc140_c
"""

N = int(input())
B = list(map(int, input().split()))

result = B[0]
for i in range(1, N-1):
    result += min(B[i-1], B[i])

print(result+B[N-2])