"""
https://atcoder.jp/contests/abs/tasks/arc089_a
"""

N = int(input())
point = [list(map(int, input().split())) for _ in range(N)]
point.insert(0, [0, 0, 0])

result="No"

for i in range(N):
    now_point = point[i]
    next_point = point[i+1]
    
    t = next_point[0] - now_point[0]
    x = abs(next_point[1] - now_point[1])
    y = abs(next_point[2] - now_point[2])
    if t < x+y:
        break
    if (t-x-y)%2 == 1:
        break
else:
    result="Yes"

print(result)