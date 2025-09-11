"""
https://atcoder.jp/contests/abc318/tasks/abc318_e
"""

N = int(input())
A = list(map(int, input().split()))

a_dict = dict()
for i, a in enumerate(A):
    if a in a_dict:
        a_dict[a].append(i)
    else:
        a_dict[a] = [i]

result = 0
for same_list in a_dict.values():
    count = len(same_list)
    left_num = 1
    right_num = count-1
    for i in range(count-1):
        now_index = same_list[i]
        next_index = same_list[i+1]
        result += left_num*right_num*(next_index-now_index-1)
        left_num+=1
        right_num-=1

print(result)