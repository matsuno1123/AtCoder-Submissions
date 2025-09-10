"""
https://atcoder.jp/contests/abc218/tasks/abc218_e
"""

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

lines = [list(map(int, input().split())) for _ in range(M)]
lines.sort(key=lambda x:x[2])

uf = UnionFind(N)

cost = 0
count = 0
for a, b, c in lines:
        a -= 1
        b -= 1
        if c<0:
            if not uf.same(a, b):
                count += 1
            uf.union(a, b)
            cost += c
        else:
            if count >= N-1:
                break
            if uf.same(a, b):
                continue
            uf.union(a, b)
            cost += c
            count += 1

print(sum(line[2] for line in lines) - cost)