"""
https://atcoder.jp/contests/abc053/tasks/abc053_b
"""

s = input()
a = s.find("A")
z = s.rfind("Z")
print(z-a+1)