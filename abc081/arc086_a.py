"""
https://atcoder.jp/contests/abc081/tasks/arc086_a
"""

N, K = map(int, input().split())
A = list(map(int, input().split()))

a_dic = {}
for a in A:
    if a in a_dic:
        a_dic[a] += 1
    else:
        a_dic[a] = 1

if len(a_dic) <= K:
    print(0)
else:
    d_num = len(a_dic)-K
    a_list = sorted(list(a_dic.items()), key=lambda x:x[1])
    print(sum(x[1] for x in a_list[0:d_num]))