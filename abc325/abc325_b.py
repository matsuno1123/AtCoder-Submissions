"""
https://atcoder.jp/contests/abc325/tasks/abc325_b
"""

N = int(input())
WX = [list(map(int, input().split())) for _ in range(0, N)]

result = 0
for time in range(0, 24):
    sum = 0
    start = 9+time
    end = 17+time

    for w, x in WX:
        if start <= x <= end or start <= x+24 <= end:
            sum += w
    if result < sum:
        result = sum
print(result)