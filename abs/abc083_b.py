"""
https://atcoder.jp/contests/abs/tasks/abc083_b
"""

N, A, B = map(int, input().split())

result = 0

for i in range(1, N+1):
    sum_i = i%10 + i//10%10 + i//100%10 + i//1000%10 + i//10000
    if A <= sum_i <= B:
        result += i

print(result)