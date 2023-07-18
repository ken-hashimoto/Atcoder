from heapq import heappush, heappop

N,M = map(int,input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
  A,B,C = map(int,input().split())
  G[A].append((B,C))
  G[B].append((A,C))
#街1から各街までの最短距離を求める
#街Nから各街までの最短距離を求める
INF = float('inf')

def dijkstra(N, G, s):
    dist = [INF] * (N+1)
    que = [(0, s)]
    dist[s] = 0
    while que:
        c, v = heappop(que)
        if dist[v] < c:
            continue
        for t, cost in G[v]:
            if dist[v] + cost < dist[t]:
                dist[t] = dist[v] + cost
                heappush(que, (dist[t], t))
    return dist
dist_from_1 = dijkstra(N,G,1)
dist_from_N = dijkstra(N,G,N)

for i in range(1,N+1):
  print(dist_from_1[i] + dist_from_N[i])
