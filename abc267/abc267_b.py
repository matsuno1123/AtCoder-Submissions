"""
https://atcoder.jp/contests/abc267/tasks/abc267_b
"""

S = list(input())

line = [3, 2, 4, 1, 3, 5, 0, 2, 4, 6]
pin = [0 for _ in range(0, 7)]

for i in range(10):
    if S[i] == "1":
        pin[line[i]] = 1

if S[0] == "1" or not ("1" in S):
    print("No")
else:
    start = pin.index(1)
    pin.reverse()
    end = 6 - pin.index(1)
    pin.reverse()
    if start == end:
        print("No")
    else:
        result = False
        for i in range(start + 1, end):
            if pin[i] == 0:
                result = True
                break
        if result:
            print("Yes")
        else:
            print("No")