from heapq import heappush,heappop
N,M = map(int,input().split())
G = [[] for _ in range(2*10**5)]
#G[v] = (w,cost,num) ... vからwへは距離costでnum番目の辺をたどっていける
for i in range(M):
    a,b,c = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append((b,c,i+1))
    G[b].append((a,c,i+1))
INF = float('inf')
dist = [INF] * N
que = [(0,0,-1)]
dist[0] = 0
ans = []
while que:
  c,v,edge = heappop(que)
  if dist[v] < c:
    continue
  if edge != -1:
    ans.append(edge)
  for nv,ncost,num in G[v]:
    if dist[nv] > dist[v] + ncost:
      dist[nv] = dist[v] + ncost
      heappush(que,(dist[nv],nv,num))
print(*ans)