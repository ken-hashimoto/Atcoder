N,M = map(int,input().split())
INF = float('inf')
d = [[INF]*N for _ in range(N)]
edges = []
for i in range(M):
  a,b,c = map(int,input().split())
  a -= 1
  b -= 1
  d[a][b] = c
  d[b][a] = c
  edges.append((a,b,c))

#ワーシャルフロイド
for via in range(N):
  for start in range(N):
    for goal in range(N):
      if d[start][goal] > d[start][via] + d[via][goal]:
        d[start][goal] = d[start][via] + d[via][goal]

#考え方
#それぞれの辺についてこの辺を残すかどうかを考える
#頂点a,bをつなぐコストcの辺があったとしてこの辺を残すべきなのは次の2条件を満たすとき
# 1. a,bの最短距離がcである
# 2. この辺を使わずにコストc以下でaからbへ到達することができない
#逆にこの2条件を満たさない辺は削除してよい
ans = 0
for a,b,c in edges:
  #それぞれの辺について
  unused = 0
  for i in range(N):
    #迂回するルートがあるならこの辺はいらない
    if d[a][i] + d[i][b] <= c:
      unused = 1
  ans += unused
print(ans)