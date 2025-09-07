"""
https://atcoder.jp/contests/abc293/tasks/abc293_c
"""

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

def search(x, y, before):
    if A[y][x] in before:
        return 0
    now_set = before.copy()
    now_set.add(A[y][x])
    if x == W-1 and y==H-1:
        return 1
    if x == W-1:
        return search(x, y+1, now_set)
    if y == H-1:
        return search(x+1, y, now_set)
    return search(x+1, y, now_set) + search(x, y+1, now_set)

print(search(0, 0, set()))