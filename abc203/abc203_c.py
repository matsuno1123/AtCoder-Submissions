"""
https://atcoder.jp/contests/abc203/tasks/abc203_c
"""

N, K = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda ab:ab[0])

money = K
for a, b in AB:
    if money < a:
        print(money)
        break
    money += b
else:
    print(money)