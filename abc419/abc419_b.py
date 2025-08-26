
https://atcoder.jp/contests/abc419/tasks/abc419_b
"""

Q = int(input())
QUERY = list(input().split() for _ in range(Q))

balls = []
for query in QUERY:
  if len(query) == 2:
    num = int(query[1])
    balls.append(num)
  else:
    index = balls.index(min(balls))
    print(balls.pop(index))