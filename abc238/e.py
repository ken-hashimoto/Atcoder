from collections import deque


N,Q = map(int,input().split())
G = [[] for _ in range(N+2)]
for i in range(Q):
  l,r = map(int,input().split())
  r += 1
  G[l].append(r)
  G[r].append(l)
d = deque()
d.append(1)
seen = [False] * (N+2)
seen[0] = True
while d:
  v = d.popleft()
  for nv in G[v]:
    if not seen[nv]:
      seen[nv] = True
      d.append(nv)
if seen[N+1]:
  print("Yes")
else:
  print("No")