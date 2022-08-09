from collections import defaultdict, deque

M = int(input())
edge = [[]*10 for _ in range(10)]
for _ in range(M):
  u,v = map(int,input().split())
  edge[u].append(v)
  edge[v].append(u)
P = list(input().split())
start = ''.join(P)
goal = '12345678'
empty = int((set(map(str,range(1,10))) - set(P)).pop())
dist = defaultdict(lambda: 10**9)
dist[start] = 0
d = deque()
seen = set()
d.append((start,empty))
while d:
  v,empty = d.popleft()
  for s in edge[empty]:
    nv = list(v)
    #vのsとかかれたものをemptyに変更する
    nv[list(nv).index(str(s))] = str(empty)
    nv = ''.join(nv)
    if not nv in seen:
      d.append((nv,s))
      dist[nv] = min(dist[nv],dist[v] + 1)
      seen.add(nv)
if goal in set(dist.keys()):
  print(dist[goal])
else:
  print(-1)