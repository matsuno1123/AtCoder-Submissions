"""
https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_ch
"""

N, S = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# リンゴ・パイナップルをそれぞれ1つずつ購入するとき合計S円になるような買い方が何通りあるか
# ここにプログラムを追記

A.sort()
B.sort()

result = 0

for app in A:
    p = S - app
    for i, pin in enumerate(B):
        if p == pin:
            result += 1
            if i < N-1 and pin != B[i+1]:
                break

print(result)