"""
https://atcoder.jp/contests/abc260/tasks/abc260_b
"""

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ABS = []
for i,(a,b) in enumerate(zip(A,B)):
    ABS.append([i+1, a, b, a+b])

result = []

ABS.sort(key=lambda a:a[0])
ABS.sort(key=lambda a:a[1], reverse=True)
for _ in range(X):
    result.append(ABS.pop(0))

ABS.sort(key=lambda a:a[0])
ABS.sort(key=lambda a:a[2], reverse=True)
for _ in range(Y):
    result.append(ABS.pop(0))

ABS.sort(key=lambda a:a[0])
ABS.sort(key=lambda a:a[3], reverse=True)
for _ in range(Z):
    result.append(ABS.pop(0))

result.sort(key=lambda a:a[0])
for r in result:
    print(r[0])