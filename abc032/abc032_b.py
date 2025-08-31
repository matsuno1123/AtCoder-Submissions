"""
https://atcoder.jp/contests/abc032/tasks/abc032_b
"""

s = input()
k = int(input())
if len(s) == k:
    print(1)
elif len(s) < k:
    print(0)
else:
    passwords = []
    for i in range(len(s)-k+1):
        passwords.append(s[i:i+k])
    print(len(set(passwords)))