"""
https://atcoder.jp/contests/abc066/tasks/abc066_b
"""

S = list(input())
len_S = len(S)

for i in range(1, 100):
    split_index = len_S//2-i
    if S[0:split_index] == S[split_index:len_S-i*2]:
        print(len_S-i*2)
        break