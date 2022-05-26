import heapq
N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

#ダイクストラ法
graph = [[] for _ in range(N+1)]
Takahashi = []
#Takahashi = [(node,高橋からの距離)]
#graph[i] = (ノードiと繋がっているノード、すなわちi%N +1)
for i in range(1,N+1):
  graph[i].append((S[(i-1)%N],i%N + 1))
  Takahashi.append((T[(i-1)%N],i))
INF = float('inf')
dist = [INF for _ in range(N+1)]
#dist[0]がスタート地点（Takahashi）
dist[0] = 0
queue = [(0,0)]
heapq.heapify(queue)
while queue:
  #候補となっているものから距離が最小のものをとりだす
  start_v,v = heapq.heappop(queue) 
  if start_v > dist[v]: #すでに求まっている最短距離よりも大きい場合はスルー
    continue
  if v == 0: #Vが0,すなわち高橋である場合は別で処理する
    for v_nv,nv in Takahashi:
      if dist[nv] > v_nv:
        dist[nv] = v_nv
        heapq.heappush(queue,(v_nv,nv))
    continue
  for v_nv,nv in graph[v]: #vとつながっているノードに対して
    if dist[nv] > dist[v] + v_nv: 
      #vまでの最短距離とvからnvへの距離の和がnvまでの最短距離よち小さいなら更新する
      dist[nv] = dist[v] + v_nv
      heapq.heappush(queue,(v_nv,nv))
for i in range(1,N+1):
  print(dist[i])
