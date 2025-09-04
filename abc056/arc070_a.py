"""
https://atcoder.jp/contests/abc056/tasks/arc070_a
"""

X = int(input())

result = 0
distance = 0
for i in range(1, 10**5):
    distance += i
    result += 1
    if distance >= X:
        break
print(result)