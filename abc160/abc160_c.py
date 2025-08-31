"""
https://atcoder.jp/contests/abc160/tasks/abc160_c
"""

K, N = map(int, input().split())
A = list(map(int, input().split()))

distance = []
sum = 0
for i in range(0, N-1):
    d = A[i+1]-A[i]
    distance.append(d)
    sum += d
distance.append(K-sum)

print(K - max(distance))