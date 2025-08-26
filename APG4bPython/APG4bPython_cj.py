"""
https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cj
"""

def sum_scores(scores):
    return sum(scores)


def output(sum_a, sum_b, sum_c):
    print(sum_a*sum_b*sum_c)


# -------------------
# ここから先は変更しない
# -------------------


def input_list(N):
    """
    N 個の入力を受け取ってリストに入れて返す関数

    引数 N: 入力を受け取る個数
    返り値: 受け取った N 個の整数値からなるリスト
    """
    l = list(map(int, input().split()))
    return l


# 科目の数 N を受け取る
N = int(input())

# それぞれのテストの点数を受け取る
A = input_list(N)
B = input_list(N)
C = input_list(N)

# それぞれの合計点を計算
sum_A = sum_scores(A)
sum_B = sum_scores(B)
sum_C = sum_scores(C)

# プレゼントの予算を出力
output(sum_A, sum_B, sum_C)