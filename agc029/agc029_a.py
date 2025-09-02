"""
https://atcoder.jp/contests/agc029/tasks/agc029_a
"""

S = list(input())
b_count = 0
w_count = 0
before_list = []
for s in S:
    before_list.append(s)
    if s == "B":
        b_count += 1
    else:
        w_count += 1
after_list = ["W" for _ in range(w_count)] + ["B" for _ in range(b_count)]

need_before = []
need_after = []
for i, (before, after) in enumerate(zip(before_list, after_list)):
    if before==after:
        continue
    if before=="W":
        need_before.append(i)
    else:
        need_after.append(i)

result = 0
for before, after in zip(need_before, need_after):
    result += abs(before - after)

print(result)