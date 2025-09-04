"""
https://atcoder.jp/contests/abc177/tasks/abc177_b
"""

S = input()
T = input()

min_count = 1000
for i in range(len(S) - len(T) + 1):
    count = sum(1 for s, t in zip(S[i:i + len(T)], T) if s != t)
    if count < min_count:
        min_count = count

print(min_count)