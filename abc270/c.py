from collections import deque

N,X,Y = map(int,input().split())
X -= 1
Y -= 1
G = [[] for _ in range(N)]
for i in range(N-1):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  G[u].append(v)
  G[v].append(u)
d = deque()
d.append(X)
seen = [False]*N
seen[X] = True
ans = []
par = [-1] * N 
while d:
  v = d.popleft()
  for nv in G[v]:
    if not seen[nv]:
      d.append(nv)
      par[nv] = v
      seen[nv] = True
now = Y
while now != X:
  ans.append(now + 1)
  now = par[now]
ans.append(now + 1)
print(*ans[::-1])