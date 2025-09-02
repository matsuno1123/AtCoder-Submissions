"""
https://atcoder.jp/contests/abc169/tasks/abc169_d
"""

import math

N = int(input())

prime = {}
temp = N
for i in range(2, math.isqrt(N)+1):
    if temp%i==0:
        count=0
        while temp%i==0:
            count += 1
            temp //= i
        prime[i] = count
if temp!=1:
    prime[temp] = 1

result = 0
for e in prime.values():
    count = 0
    for i in range(1, e+1):
        if i*(i+1)//2 > e:
            break
        count += 1
    result+=count

print(result)