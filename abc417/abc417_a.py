"""
https://atcoder.jp/contests/abc417/tasks/abc417_a
"""

N, A, B = list(map(int, input().split()))
S = input()
print(S[A:N-B])