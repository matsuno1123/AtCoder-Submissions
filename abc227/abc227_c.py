"""
https://atcoder.jp/contests/abc227/tasks/abc227_c
"""

N = int(input())

result = 0
a = 0
while True:
    a += 1
    if a**3 > N:
        break
    n_a = N//a
    b = a-1
    while True:
        b += 1
        if b**2 > n_a:
            break
        result += n_a//b-b+1

print(result)