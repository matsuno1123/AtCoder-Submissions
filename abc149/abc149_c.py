"""
https://atcoder.jp/contests/abc149/tasks/abc149_c
"""

import  math

X = int(input())

for x in range(X, 10000000):
    for j in range(2, math.ceil(math.sqrt(x))):
        if x%j == 0:
            break
    else:
        print(x)
        break