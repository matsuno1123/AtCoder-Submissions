"""
https://atcoder.jp/contests/abc425/tasks/abc425_b
"""

N = int(input())
A = list(map(int, input().split()))

stock = [i+1 for i in range(N)]
result = []
for a in A:
    if a == -1:
        result.append(-1)
    elif A.count(a) > 1:
        print("No")
        break
    elif A.count(a) == 1:
        result.append(a)
        stock.remove(a)
else:
    print("Yes")
    for s in stock:
        result[result.index(-1)] = s
    print(*result)