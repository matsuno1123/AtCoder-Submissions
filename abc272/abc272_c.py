"""
https://atcoder.jp/contests/abc272/tasks/abc272_c
"""

N = int(input())
A = list(map(int, input().split()))

A_even = list(a for a in A if a%2 == 0)
A_odd = list(a for a in A if a%2 == 1)

A_even.sort()
A_odd.sort()

even_len = len(A_even)
odd_len = len(A_odd)

if even_len <= 1 and odd_len <= 1:
    print(-1)
elif even_len <= 1:
    print(A_odd[odd_len-1] + A_odd[odd_len-2])
elif odd_len <= 1:
    print(A_even[even_len-1] + A_even[even_len-2])
else:
    print(max(A_even[even_len-1] + A_even[even_len-2], A_odd[odd_len-1] + A_odd[odd_len-2]))