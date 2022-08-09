import heapq
N,M = map(int,input().split())
G = [[] for _ in range(N)]
deg = [0]*N
for i in range(M):
  a,b = map(int,input().split())
  a -= 1
  b -= 1
  G[a].append(b)
  deg[b] += 1

d = list(v for v in range(N) if deg[v]==0)
heapq.heapify(d)
ans = []

while d:
    v = heapq.heappop(d)
    ans.append(v)
    for nv in G[v]:
      deg[nv] -= 1
      if deg[nv] == 0:
        heapq.heappush(d,nv)
if len(ans) == N:
  ans = list(map(lambda x:x+1,ans))
  print(*ans)
else:
  print(-1)

