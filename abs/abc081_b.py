"""
https://atcoder.jp/contests/abs/tasks/abc081_b
"""

N = int(input())
A = list(map(int, input().split()))

count = 0

flg = False

while True:
    for i, a in enumerate(A):
        if a%2 == 1:
            flg = True
            break
        A[i] = a//2
    if flg:
        break        
    count += 1

print(count)