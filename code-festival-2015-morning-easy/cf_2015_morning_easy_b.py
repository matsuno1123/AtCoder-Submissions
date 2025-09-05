"""
https://atcoder.jp/contests/code-festival-2015-morning-easy/tasks/cf_2015_morning_easy_b
"""

N = int(input())
S = list(input())

if N%2 == 1:
    print(-1)
else:
    A = S[0:N//2]
    B = S[N//2:N]
    print(sum(1 for a,b in zip(A,B) if a!=b))