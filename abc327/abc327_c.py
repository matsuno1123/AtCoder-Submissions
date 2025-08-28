"""
https://atcoder.jp/contests/abc327/tasks/abc327_c
"""

def check_num(num_list: list[int]) -> bool:
    for i in range(1, 10):
        if num_list.count(i) != 1:
            return False
    return True

A = [list(map(int, input().split())) for _ in range(9)]
result = "Yes"
for a in A:
    if not check_num(a):
        result = "No"
        break

if result != "No":
    for a in [list(x) for x in zip(*A)]:
        if not check_num(a):
            result = "No"
            break

if result != "No":
    for i in range(9):
        x = 3*(i//3)
        y = i%3
        if not check_num(A[x][3*y:3*y+3]+A[x+1][3*y:3*y+3]+A[x+2][3*y:3*y+3]):
            result = "No"
            break

print(result)