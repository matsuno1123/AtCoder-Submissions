"""
https://atcoder.jp/contests/abc299/tasks/abc299_c
"""

N = int(input())
S = list(input())

result = -1
count = 0
for s in S:
    if s == "o":
        count += 1
    elif count > 0:
        if count > result:
            result = count
        count = 0

if result < count < len(S) and count != 0:
    result = count

print(result)