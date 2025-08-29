"""
https://atcoder.jp/contests/abc244/tasks/abc244_c
"""

N = int(input())
ans = list(0 for _ in range(2*N+1))
index = 0
for _ in range(N+1):
    for a in ans[index:2*N+1]:
        if a == 0:
            break
        else:
            index += 1
    print(index+1, flush=True)
    index += 1

    e = int(input())
    if e==0:
        break
    ans[e-1] = 1