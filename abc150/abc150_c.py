"""
https://atcoder.jp/contests/abc150/tasks/abc150_c
"""

import math

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

num_list = [i for i in range(1, N+1)]

p_index = 0
for p in P:
    num_len = len(num_list)
    index = num_list.index(p)
    num_list.pop(index)
    p_index += math.factorial(num_len-1)*index

num_list = [i for i in range(1, N+1)]

q_index = 0
for q in Q:
    num_len = len(num_list)
    index = num_list.index(q)
    num_list.pop(index)
    q_index += math.factorial(num_len-1)*index

print(abs(p_index - q_index))