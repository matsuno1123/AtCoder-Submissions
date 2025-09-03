"""
https://atcoder.jp/contests/abc071/tasks/abc071_b
"""

s_set = set(list(input()))
alphabet_list = [chr(ord("a") + i) for i in range(26)]

for target in alphabet_list:
    if not (target in s_set):
        print(target)
        break
else:
    print("None")