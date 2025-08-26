
https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_ce
"""

N = int(input())
p = [-1] + list(map(int, input().split()))

def report(i):
    children = [child for child in range(N) if p[child] == i]

    # 終端条件
    if len(children) == 0:
        return 1

    # 再帰
    result = 1
    for c in children:
        result += report(c)

    return result

for index in range(N):
    print(report(index))
