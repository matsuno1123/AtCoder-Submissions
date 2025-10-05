"""
https://atcoder.jp/contests/abc426/tasks/abc426_b
"""

S = list(str(input()))

s_0 = S[0]
s_1 = ""
flg = False
for s in S[1:len(S)]:
    if s_0 != s:
        s_1 = s
    if s_0 == s:
        flg = True

if flg:
    print(s_1)
else:
    print(s_0)