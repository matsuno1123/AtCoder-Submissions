"""
https://atcoder.jp/contests/arc141/tasks/arc141_a
"""

T = int(input())

for _ in range(T):
    case = input()
    len_case = len(case)
    n = []
    if case in [10**i for i in range(1,19)]:
        print(int(str(9)*(len_case-1)))
    else:
        for i in range(2, len_case+1):
            if len_case%i == 0:
                len_pattern = len_case//i
                num = int("".join(case[0:len_pattern]*i))
                if num > int(case):
                    num = int("".join(str(int(case[0:len_pattern])-1)*i))
                if len(str(num)) == len_case:
                    n.append(num)
        if not n:
            n.append(int(str(9)*(len_case-1)))
        print(max(n))