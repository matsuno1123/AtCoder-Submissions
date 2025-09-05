"""
https://atcoder.jp/contests/code-festival-2016-qualc/tasks/codefestival_2016_qualC_a
"""

s = list(input())
if "C" in s and "F" in s:
    c_index = s.index("C")
    s.reverse()
    f_index = len(s) - s.index("F") -1
    if c_index < f_index:
        print("Yes")
    else:
        print("No")
else:
    print("No")