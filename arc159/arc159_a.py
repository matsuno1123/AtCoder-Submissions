"""
https://atcoder.jp/contests/arc159/tasks/arc159_a
"""

N, K = map(int, input().split())
A = [list((i, s) for i, s in enumerate(map(int, input().split()))) for _ in range(N)]
cost_list = []

def route_cost(start:int):
    # コスト増加(固定値)
    now_cost = 1
    next_set = set(a[0] for a in A[start] if a[1] == 1)
    while len(next_set) > 0:
        target_set = set()
        for n in next_set:
            # コスト計算済みの場合はスキップ
            if cost_list[n] != -1:
                continue
            cost_list[n] = now_cost
            target_set.update(set(a[0] for a in A[n] if a[1] == 1))
        now_cost += 1
        next_set = target_set

Q = int(input())
for _ in range(Q):
    cost_list = [-1] * N
    s, t = map(int, input().split())
    s, t = (s-1)%N, (t-1)%N
    route_cost(s)
    print(cost_list[t])