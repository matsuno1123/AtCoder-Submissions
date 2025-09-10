"""
https://atcoder.jp/contests/abc041/tasks/abc041_b
"""

A, B, C = map(int, input().split())
mod_num = 10**9+7
print((A*B)%mod_num*C%mod_num)