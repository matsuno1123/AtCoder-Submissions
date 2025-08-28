"""
https://atcoder.jp/contests/abc133/tasks/abc133_b
"""

N, D = map(int, input().split())
X= [list(map(int, input().split())) for _ in range(N)]

squared = list(num**2 for num in range(1, 130))

count = 0
for i, y in enumerate(X[0:N-1]):
    for z in X[i+1:N]:
        sum = 0
        for k in range(D):
            sum += (y[k]-z[k])**2
        if sum in squared:
            count += 1
print(count)