
https://atcoder.jp/contests/abc420/tasks/abc420_c
"""

N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ROW = []
for i in range(Q):
  ROW.append(input().split())

result = 0
for (a, b) in zip(A, B):
  result += min(a, b)

for i, row in enumerate(ROW):
  index = int(row[1])-1
  value = int(row[2])

  before_min = min(A[index], B[index])

  if row[0] == "A":
      A[index] = value
  else:
      B[index] = value

  after_min = min(A[index], B[index])

  result = result - before_min + after_min

  print(result)