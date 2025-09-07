"""
https://atcoder.jp/contests/abc422/tasks/abc422_a
"""

S = list(map(int, input().split("-")))
if S[1] == 8:
    print(str(S[0]+1)+"-1")
else:
    print(str(S[0])+"-"+str(S[1]+1))