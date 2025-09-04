"""
https://atcoder.jp/contests/arc106/tasks/arc106_b
"""

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

uf = UnionFind(N)
for _ in range(M):
    c, d = map(int, input().split())
    uf.union(c-1, d-1)

for members in uf.all_group_members().values():
    a_sum = 0
    b_sum = 0
    for m in members:
        a_sum += A[m]
        b_sum += B[m]
    if a_sum != b_sum:
        print("No")
        break
else:
    print("Yes")