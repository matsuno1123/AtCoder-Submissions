"""
https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b
"""

N, A, B = list(map(int, input().split()))
S = input()

rank = 1
num = 0

border = A+B

for i, s in enumerate(list(S)):
    if s == "a":
       if num < border:
           print("Yes")
           num += 1
       else:
           print("No")
    elif s == "b":
        if num >= border:
            print("No")
        elif rank <= B:
            print("Yes")
            num+=1
            rank+=1
        else:
            print("No")
    else:
        print("No")