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
sx,sy,tx,ty = map(int,input().split())
circles = []
for i in range(N):
  x,y,r = map(int,input().split())
  circles.append((x,y,r))
  if (sx - x)**2 + (sy - y)**2 == r**2:
    start_s = i
  if (tx - x)**2 + (ty - y)**2 == r**2:
    start_t = i
UF = UnionFind(N)
for i in range(N):
  xi,yi,ri = circles[i]
  for j in range(N):
    xj,yj,rj = circles[j]
    d = (xi - xj)**2 + (yi - yj)**2
    if abs(ri - rj)**2 <= d <= (ri + rj)**2:
      UF.union(i,j)
if UF.same(start_s,start_t):
  print("Yes")
else:
  print("No")
