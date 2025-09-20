"""
https://atcoder.jp/contests/abc424/tasks/abc424_c
"""

import sys
sys.setrecursionlimit(10**6)

N = int(input())
skill_set = set()
target_dict = {}
for i in range(N):
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        skill_set.add(i+1)
    else:
        if A in skill_set or B in skill_set:
            skill_set.add(i+1)
            continue
        if A not in target_dict:
            target_dict[A] = set()
        if B not in target_dict:
            target_dict[B] = set()
        target_dict[A].add(i+1)
        target_dict[B].add(i+1)

next_set = skill_set.copy()

def master_skill(skill: int):
    skill_set.add(skill)
    if skill in target_dict:
        for target in target_dict[skill]:
            if target not in skill_set:
                next_set.add(target)

while len(next_set) > 0:
    now_set=next_set.copy()
    next_set = set()
    for s in now_set:
        master_skill(s)

print(len(skill_set))