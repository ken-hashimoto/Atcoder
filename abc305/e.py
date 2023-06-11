import heapq
N,M,K = map(int,input().split())
G = [[] for _ in range(N)]
INF=float('inf')
potential = [-INF] * N

pq = []
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
for i in range(K):
    p,h = map(int,input().split())
    p -= 1
    potential[p] = h
    heapq.heappush(pq,(-h,p))
while pq:
    d, v = heapq.heappop(pq)
    d = -d
    if d < potential[v]:
        continue
    for to in G[v]:
        if potential[to] < potential[v] - 1:
            potential[to] = potential[v] - 1
            heapq.heappush(pq, (-potential[to], to))
ans = []
for i in range(N):
    if potential[i] >= 0:
        ans.append(i+1)
print(len(ans))
print(*sorted(ans))