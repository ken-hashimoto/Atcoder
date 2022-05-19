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

    def same(self, x, y):
        return self.find(x) == self.find(y)

H,W = map(int,input().split())
Q = int(input())
M = [[0 for i in range(W+1)] for j in range(H+1)]
uf = UnionFind((H+1)*(W+1))

def query1(r,c):
  M[r][c] = 1
  for i,j in [(r-1,c),(r,c-1),(r+1,c),(r,c+1)]:
    if i <= 0 or i > H or j <= 0 or j > W:
      continue
    if M[i][j] == 1:
      uf.union(i*W + j, r*W + c)

def query2(ra,ca,rb,cb):
  if uf.same(ra*W+ca,rb*W+cb) and M[ra][ca] == 1 and M[rb][cb] == 1:
    print("Yes")
  else:
    print("No")

for i in range(Q):
  A = list(map(int,input().split()))
  if A[0] == 1:
    r,c = A[1],A[2]
    query1(r,c)
  else:
    ra,ca,rb,cb = A[1:]
    query2(ra,ca,rb,cb)