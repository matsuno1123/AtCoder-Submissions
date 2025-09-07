"""
https://atcoder.jp/contests/abc422/tasks/abc422_d
"""

N, K = map(int, input().split())
n_count = 2**N
ave = K//n_count
global B
B = [ave] * n_count

def balance(start, end, num):
    if num == 0:
        return
    elif num == 1:
        B[start] += 1
        return
    else:
        a = (num+2-1)//2
        b = num//2
        balance(start, (start+end)//2, a)
        balance((start+end)//2, end, b)

if K%n_count==0:
    print(0)
else:
    balance(0, n_count, K%n_count)
    print(1)
print(*B)