"""
https://atcoder.jp/contests/abc030/tasks/abc030_b
"""

n, m = map(int, input().split())

short_angle = 6*m
long_angle = (n%12)*30+0.5*m

angle = abs(short_angle-long_angle)
if angle > 180:
    angle = 360-angle

print(angle)