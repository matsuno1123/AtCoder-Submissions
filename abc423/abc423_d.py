"""
https://atcoder.jp/contests/abc423/tasks/abc423_d
"""

from sortedcontainers import SortedList

N, K = map(int, input().split())

restaurant = SortedList(key=lambda x:x[0])

now_time = 0
num = 0
for _ in range(N):
    A, B, C = map(int, input().split())
    if num+C <= K:
        num += C
        entry_time = max(A, now_time)
        restaurant.add((entry_time+B, C))
        print(entry_time)
    else:
        while num+C > K or now_time < A:
            if len(restaurant) == 0 or (restaurant[0][0] > A and num+C <= K):
                now_time = A
                break
            now_time, remove_num = restaurant.pop(0)
            num -= remove_num
        num += C
        restaurant.add((now_time+B, C))
        print(now_time)