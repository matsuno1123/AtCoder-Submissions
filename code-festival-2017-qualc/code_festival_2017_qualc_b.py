"""
https://atcoder.jp/contests/code-festival-2017-qualc/tasks/code_festival_2017_qualc_b
"""

N = int(input())
A = list(map(int, input().split()))
even_count = len([a for a in A if a==0 or a%2==0])
zero_nine_count = len([a for a in A if a==0 or a==9])

print(3**(N-zero_nine_count)*(2**zero_nine_count) - 2**even_count)