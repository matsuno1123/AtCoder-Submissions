"""
https://atcoder.jp/contests/arc168/tasks/arc168_a
"""

N = int(input())
S = list(input())

result = 0
count = 0

for i, s in enumerate(S):
    if s == ">":
        count += 1
        result += count
    else:
        count = 0
print(result)