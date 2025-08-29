"""
https://atcoder.jp/contests/abc229/tasks/abc229_c
"""

N, W = map(int, input().split())
AB = []
for i in range(N):
    ab = list(map(int, input().split()))
    ab.insert(0, i)
    AB.append(ab)

AB.sort(key=lambda ab:ab[1], reverse=True)

cheese = 0
result = 0

for ab in AB:
    zan = W-cheese
    if ab[2] >= zan:
        result += ab[1]*zan
        break
    else:
        cheese += ab[2]
        result += ab[1] * ab[2]
print(result)