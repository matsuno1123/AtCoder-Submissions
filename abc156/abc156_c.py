
https://atcoder.jp/contests/abc156/tasks/abc156_c
"""

N = int(input())
X = list(map(int, input().split()))

result = 10000*10000
for i in range((min(X)),  max(X)+1):
    sum_h = 0
    for x in X:
        sum_h += (x-i)**2
    if sum_h < result:
        result = sum_h

print(result)