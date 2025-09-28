"""
https://atcoder.jp/contests/abc425/tasks/abc425_c
"""

N, Q = map(int, input().split())
A = list(map(int, input().split()))

sum_list = [0]
sum_result = 0
for a in A:
    sum_result += a
    sum_list.append(sum_result)

now_index = 0
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        now_index += query[1]
        now_index %= N
    else:
        l, r = (query[1]-1+now_index)%N, (query[2]-1+now_index)%N
        l += 1
        r += 1

        if l < r:
            print(sum_list[r]-sum_list[l-1])
        elif l==r:
            print(A[l-1])
        else:
            print(sum_list[r]+sum_list[N]-sum_list[l-1])