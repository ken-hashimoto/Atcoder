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

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
N = int(input())
uf = UnionFind(N)
X_Y = []
convert = []
for i in range(N):
  x,y = map(int,input().split())
  x += 1000
  y += 1000
  X_Y.append((x,y))
  convert.append(2005*x + y)
S = sorted(list(set(convert)))
ranking = {x:i+1 for i,x in enumerate(S)}
ranking_set = ranking.keys()
for x,y in X_Y:
  convert_x_y = ranking[2005*x+y]
  if 2005*(x-1)+(y-1) in ranking_set:
    uf.union(convert_x_y,ranking[2005*(x-1)+(y-1)])
  if 2005*(x-1)+y in ranking_set:
    uf.union(convert_x_y,ranking[2005*(x-1)+y])
  if 2005*x+(y-1) in ranking_set:
    uf.union(convert_x_y,ranking[2005*x+(y-1)])
  if 2005*x+(y+1) in ranking_set:
    uf.union(convert_x_y,ranking[2005*x+(y+1)])
  if 2005*(x+1)+y in ranking_set:
    uf.union(convert_x_y,ranking[2005*(x+1)+y])
  if 2005*(x+1)+(y+1) in ranking_set:
    uf.union(convert_x_y,ranking[2005*(x+1)+(y+1)])
print(uf.group_count())