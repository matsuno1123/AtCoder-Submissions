
https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_ck
"""

N = int(input())  # 生徒の数Nを読み込む
T = list(map(int, input().split()))  # 各生徒のゴールまでの時間を読み込む

min_time = min(T)

for i, v in enumerate(T):
    if v == min_time:
        print(i+1)
        break