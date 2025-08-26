
https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cm
"""

import numpy as np

N = int(input())
A = list(map(int, input().split()))

ave = np.sum(A) // N

for i in range(N):
    print(abs(A[i] - ave))