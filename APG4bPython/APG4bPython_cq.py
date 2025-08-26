"""
https://atcoder.jp/contests/APG4bPython/tasks/APG4bPython_cq
"""

A, op, B = input().split()
A = int(A)
B = int(B)

if op == '+':
    print(A + B)
elif op == '-':
    print(A - B)
elif op == '*':
    print(A * B)
elif op == '/':
    if B == 0:
        print("error")
    else:
        print(A // B)
elif op == '?' or op == '=' or op == '!':
    print("error")
