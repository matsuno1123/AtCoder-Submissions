"""
https://atcoder.jp/contests/abc343/tasks/abc343_d
"""

N, T = map(int, input().split())

point_list = [0 for _ in range(N)]
point_list.insert(0, -1)

count_dict  = {0: N}

for _ in range(T):
    A, B = map(int, input().split())
    before_point = point_list[A]
    point_list[A] += B

    count_dict[before_point] -= 1
    if count_dict[before_point] == 0:
        count_dict.pop(before_point)

    if point_list[A] in count_dict:
        count_dict[point_list[A]] += 1
    else:
        count_dict[point_list[A]] = 1

    print(len(count_dict))