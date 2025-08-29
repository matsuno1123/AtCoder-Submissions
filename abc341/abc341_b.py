"""
https://atcoder.jp/contests/abc341/tasks/abc341_b
"""

N = int(input())
A = list(map(int, input().split()))

result = 0
for a in A[0:N-1]:
    s,t = map(int, input().split())
    result = (result + a)//s*t
print(result+A[N-1])