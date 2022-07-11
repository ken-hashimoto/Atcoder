from collections import deque

N,M = map(int,input().split())
edge = [[] for _ in range(N)]
for i in range(M):
  a,b = map(int,input().split())
  edge[a-1].append(b-1)

ans = 0
for i in range(N):
  #頂点iをスタート地点とするときゴール地点はいくつあるか
  seen = [False]*N
  todo = deque([i])
  while todo:
    v = todo.popleft()
    if seen[v]:
      continue
    seen[v] = True
    for nv in edge[v]:
      if not seen[nv]:
        todo.append(nv)
  ans += sum(seen)
print(ans)
