"""
https://atcoder.jp/contests/abc194/tasks/abc194_c
"""

N = int(input())
A = list(map(int, input().split()))

a_dic = dict()
for a in A:
    if a in a_dic:
        a_dic[a] += 1
    else:
        a_dic[a] = 1

result = 0
for k1, v1 in a_dic.items():
    for k2, v2 in a_dic.items():
        result += abs(k1-k2)**2*v1*v2

print(result//2)