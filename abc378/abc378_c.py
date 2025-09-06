"""
https://atcoder.jp/contests/abc378/tasks/abc378_c
"""

N = int(input())
A = list(map(int, input().split()))
B = []

a_dic = {}

for i, a in enumerate(A):
    if a in a_dic:
        B.append(a_dic[a])
    else:
        B.append(-1)
    a_dic[a] = i+1

print(*B)