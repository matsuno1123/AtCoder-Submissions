"""
https://atcoder.jp/contests/abc175/tasks/abc175_c
"""

X, K, D = map(int, input().split())
X = abs(X)

count = X//D
if count >= K:
    print(X-K*D)
else:
    if (K-count)%2 == 0:
        print(X-D*count)
    else:
        print(D-(X-D*count))