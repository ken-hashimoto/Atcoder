import heapq

# ダイクストラを使いたい。
# でも負の辺が出てくるから使えない。
# そこで「現在の高さ」+ 「楽しさ」という量を状態としてもつことを考える
# この量を各頂点について求めればよい
# 高いところにいくとき　X -> Y
# H[X] + happy_X -> H[Y] + happy_X -2*(H[Y] - H[X]) = H[X] + happy_X + (H[X] - H[Y])
# となり量はH[Y] - H[X]だけ減少する
# 低いところにいくとき X -> Y
# H[X] + happy_X -> H[Y] + happy_X + (H[X] - H[Y]) = H[X] + happy_X
# となり量は変わらない

# 以上のことから
# 標高が高くなる辺(X -> Y)にはコストH[Y] - H[X]を、標高が同じか低い辺にはコスト0をもたした辺をつくったグラフを用意する
# そのグラフでダイクストラをして0からの最短経路問題をとく
#得られた結果（costs）を用いて各頂点の楽しさの最大値を
# (H[0] + 0) - H[i] - costs[i]で求める
N,M = map(int,input().split())
H = list(map(int,input().split()))
G = [[] for _ in range(N)]
for i in range(M):
  u,v = map(int,input().split())
  u -= 1
  v -= 1
  G[u].append(v)
  G[v].append(u)
d = [(0,0)]
INF = float('inf')
# XからY(H[X]<H[Y])に向かってコストH[Y] - H[x]の辺を張る
# XからY(H[X]>=H[Y])のときはコスト0の辺を張る
costs = [INF] * N
costs[0] = 0
while d:
  cost,v = heapq.heappop(d)
  if costs[v] < cost:
    continue
  for nv in G[v]:
    if H[nv] > H[v]:
      c = H[nv] - H[v]
    else:
      c = 0
    if costs[nv] > costs[v] + c:
      costs[nv] = costs[v] + c
      heapq.heappush(d,(costs[nv],nv))
ans = [0] * N
init = H[0]
for i in range(N):
  ans[i] = H[0] - H[i] - costs[i]
print(max(ans))
