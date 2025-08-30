"""
https://atcoder.jp/contests/abc376/tasks/abc376_c
"""

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)

i = 0
result = -1
for a in A:
    if i == N-1:
        print(a)
        break
    if a <= B[i]:
        i+=1
        continue
    if result != -1:
        print(-1)
        break
    result=a
else:
    print(result)