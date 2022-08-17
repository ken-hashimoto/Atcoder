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

N,M,E = map(int,input().split())
edge = []
for i in range(E):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  edge.append((u,v))
connected = [True]*(E) 
#connected[i] = True はi番目の辺が繋がっていることを示す
Q = int(input())
query = []
for i in range(Q):
  x = int(input())
  x -= 1
  connected[x] = False
  query.append(x)
query = query[::-1]
uf = UnionFind(N+1)
#Nと同じグループに入っている -> 電気が通っている
for i in range(E):
  if connected[i]:
    u,v = edge[i]
    uf.union(min(u,N),min(v,N))
ans = [uf.size(N)-1]
for i in range(Q):
  q = query[i]
  u,v = edge[q]
  uf.union(min(u,N),min(v,N))
  ans.append(uf.size(N)-1)
ans = ans[::-1]
for i in range(1,Q+1):
  print(ans[i])